#!/usr/bin/env python3
"""
okf_tools.py — Open Knowledge Format (OKF v0.1) workspace utilities.

This single CLI is shared (identical copy) by the okf-bundle and okf-library
skills. It does the deterministic, repetitive work so the agent can spend its
judgement on what knowledge to capture and how to organize it.

Subcommands
-----------
  scan      Discover OKF bundles under a root; print a JSON inventory.
  validate  Check one directory/bundle against OKF v0.1 conformance rules.
  index     (Re)generate the workspace master index (母题索引 / OKF-INDEX.md),
            preserving human-authored fields (theme / status / note) across runs.

OKF v0.1 conformance (verbatim intent from the spec, §9)
--------------------------------------------------------
A bundle is conformant if:
  1. Every non-reserved .md file contains a parseable YAML frontmatter block.
  2. Every frontmatter block contains a non-empty `type` field.
  3. Reserved filenames (index.md, log.md) follow their prescribed structure.
Consumers MUST be permissive. The following are NOT conformance failures and are
reported only as warnings: missing optional fields, unknown `type` values,
unknown extra keys, broken cross-links, missing index.md.

Bundle detection
----------------
Primary: a directory is a bundle root if it holds an `index.md` whose frontmatter
declares `okf_version` (the spec permits frontmatter in a bundle-root index.md for
exactly this purpose; the okf-bundle skill always writes this, so it doubles as a
reliable marker). Fallback (for bundles produced by other tools): the top-most
directories under the root that contain any concept file are treated as bundles.
"""

import argparse
import datetime as _dt
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.stderr.write(
        "okf_tools needs PyYAML. Install it with:\n"
        "  pip install pyyaml --break-system-packages\n"
    )
    sys.exit(2)

RESERVED = {"index.md", "log.md"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
DATE_HEADING_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\b")
DATA_BLOCK_RE = re.compile(
    r"<!--\s*OKF-INDEX-DATA\s*(\{.*?\})\s*-->", re.DOTALL
)


# --------------------------------------------------------------------------- #
# IO + frontmatter
# --------------------------------------------------------------------------- #
def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def split_frontmatter(text):
    """Return (data_dict_or_None, body_str, error_str_or_None).

    `data` is None when there is no frontmatter at all OR when it failed to
    parse; `error` distinguishes the two (None => simply absent).
    """
    if not text.startswith("---"):
        return None, text, None
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None, text, None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            raw = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1:])
            if not raw.strip():
                return {}, body, None
            try:
                data = yaml.safe_load(raw)
            except Exception as exc:  # noqa: BLE001
                return None, body, f"YAML parse error: {exc}"
            if data is None:
                return {}, body, None
            if not isinstance(data, dict):
                return None, body, "frontmatter is not a key/value mapping"
            return data, body, None
    return None, text, "unterminated frontmatter (missing closing '---')"


# --------------------------------------------------------------------------- #
# Validation (used by both `validate` and `scan`)
# --------------------------------------------------------------------------- #
def _check_links(body, md_path, bundle_root):
    """Return a list of broken-link warnings (in-bundle .md targets only)."""
    warnings = []
    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0].strip()
        if not clean or not clean.endswith(".md"):
            continue
        if clean.startswith("/"):
            resolved = os.path.normpath(os.path.join(bundle_root, clean.lstrip("/")))
        else:
            resolved = os.path.normpath(os.path.join(os.path.dirname(md_path), clean))
        # only warn about links that point inside the bundle
        if os.path.commonpath([resolved, bundle_root]) != os.path.normpath(bundle_root):
            continue
        if not os.path.isfile(resolved):
            rel = os.path.relpath(md_path, bundle_root)
            warnings.append(f"{rel}: broken link -> {target}")
    return warnings


def validate_bundle(bundle_root):
    """Validate a bundle directory. Returns a dict summary."""
    bundle_root = os.path.abspath(bundle_root)
    errors, warnings = [], []
    concept_count = 0
    types, tags = {}, set()
    latest_ts = None
    has_index = os.path.isfile(os.path.join(bundle_root, "index.md"))
    has_log = os.path.isfile(os.path.join(bundle_root, "log.md"))
    okf_version = None
    title = None

    for dirpath, _dirs, files in os.walk(bundle_root):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, bundle_root)
            text = read_text(fpath)
            data, body, err = split_frontmatter(text)

            if fname == "log.md":
                if not any(DATE_HEADING_RE.match(ln) for ln in body.splitlines()):
                    warnings.append(f"{rel}: log.md has no '## YYYY-MM-DD' date headings")
                continue

            if fname == "index.md":
                is_root = os.path.normpath(dirpath) == bundle_root
                if data is not None and data:  # frontmatter present
                    if not is_root:
                        warnings.append(
                            f"{rel}: non-root index.md should not carry frontmatter"
                        )
                    else:
                        okf_version = str(data.get("okf_version")) if data.get("okf_version") else None
                        extra = [k for k in data if k != "okf_version"]
                        if extra:
                            warnings.append(
                                f"{rel}: root index.md frontmatter should only hold "
                                f"okf_version (found extra: {', '.join(extra)})"
                            )
                continue

            # --- concept document ---
            concept_count += 1
            if data is None:
                errors.append(
                    f"{rel}: {err or 'missing YAML frontmatter'} "
                    "(every concept needs a frontmatter block)"
                )
                continue
            ctype = data.get("type")
            if not (isinstance(ctype, str) and ctype.strip()):
                errors.append(f"{rel}: missing or empty required `type` field")
            else:
                types[ctype] = types.get(ctype, 0) + 1
            t = data.get("tags")
            if isinstance(t, list):
                tags.update(str(x) for x in t)
            elif isinstance(t, str):
                tags.add(t)
            ts = data.get("timestamp")
            if isinstance(ts, (str, _dt.date, _dt.datetime)):
                ts = str(ts)
                if latest_ts is None or ts > latest_ts:
                    latest_ts = ts
            if title is None and os.path.normpath(dirpath) == bundle_root:
                title = data.get("title")
            warnings.extend(_check_links(body, fpath, bundle_root))

    # title fallback: bundle-root index.md is not a concept, so derive from dir
    if not title:
        title = os.path.basename(bundle_root)

    return {
        "path": bundle_root,
        "title": title,
        "okf_version": okf_version,
        "concept_count": concept_count,
        "types": types,
        "tags": sorted(tags),
        "latest_timestamp": latest_ts,
        "has_index": has_index,
        "has_log": has_log,
        "conformant": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #
def _dir_has_okf_marker(dirpath):
    idx = os.path.join(dirpath, "index.md")
    if os.path.isfile(idx):
        data, _b, _e = split_frontmatter(read_text(idx))
        if data and data.get("okf_version") is not None:
            return True
    return False


def _dir_has_concept(dirpath):
    """True if dirpath (recursively) contains at least one concept file."""
    for _dp, _dirs, files in os.walk(dirpath):
        for fname in files:
            if fname.endswith(".md") and fname not in RESERVED:
                data, _b, _e = split_frontmatter(read_text(os.path.join(_dp, fname)))
                if data is not None and str(data.get("type", "")).strip():
                    return True
    return False


def discover_bundles(root):
    """Return absolute paths of bundle roots under `root`."""
    root = os.path.abspath(root)
    marked = []
    for dirpath, dirs, _files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        if _dir_has_okf_marker(dirpath):
            marked.append(os.path.abspath(dirpath))
    if marked:
        return sorted(set(marked))

    # fallback: top-most dirs that contain any concept file
    found = []
    if any(
        f.endswith(".md") and f not in RESERVED
        and (lambda d: d is not None and str(d.get("type", "")).strip())(
            split_frontmatter(read_text(os.path.join(root, f)))[0]
        )
        for f in os.listdir(root)
        if os.path.isfile(os.path.join(root, f))
    ):
        found.append(root)
    else:
        for entry in sorted(os.listdir(root)):
            sub = os.path.join(root, entry)
            if os.path.isdir(sub) and not entry.startswith(".") and _dir_has_concept(sub):
                found.append(os.path.abspath(sub))
    return sorted(set(found))


def _resolve_zone(root_abs, zone):
    """Interpret a zone path relative to the workspace root, not the CWD.

    Users naturally pass ``--canonical knowledge-base`` meaning "the
    knowledge-base folder inside my workspace". Resolving against CWD would
    silently miss every bundle. Absolute paths are honored as-is.
    """
    if not zone:
        return None
    return zone if os.path.isabs(zone) else os.path.normpath(os.path.join(root_abs, zone))


def _zone_of(path, canonical, staging):
    path = os.path.abspath(path)
    for label, base in (("canonical", canonical), ("staging", staging)):
        if base:
            base = os.path.abspath(base)
            try:
                if os.path.commonpath([path, base]) == base:
                    return label
            except ValueError:
                pass
    return "other"


def scan(root, canonical=None, staging=None):
    root_abs = os.path.abspath(root)
    canonical = _resolve_zone(root_abs, canonical)
    staging = _resolve_zone(root_abs, staging)
    bundles = []
    for bdir in discover_bundles(root):
        info = validate_bundle(bdir)
        info["zone"] = _zone_of(bdir, canonical, staging)
        info["rel_path"] = os.path.relpath(bdir, root_abs)
        bundles.append(info)
    return {
        "root": root_abs,
        "scanned_at": _dt.datetime.now(_dt.timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
        "bundle_count": len(bundles),
        "bundles": bundles,
    }


# --------------------------------------------------------------------------- #
# Master index generation
# --------------------------------------------------------------------------- #
def _load_human_fields(index_path):
    """Recover human-authored fields keyed by absolute bundle path."""
    if not index_path or not os.path.isfile(index_path):
        return {}
    m = DATA_BLOCK_RE.search(read_text(index_path))
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except Exception:  # noqa: BLE001
        return {}


def build_index(root, out_path, canonical=None, staging=None, title="母题索引 · OKF Master Index"):
    out_path = os.path.abspath(out_path)
    out_dir = os.path.dirname(out_path)
    root_abs = os.path.abspath(root)
    canonical = _resolve_zone(root_abs, canonical)
    staging = _resolve_zone(root_abs, staging)
    inv = scan(root, canonical=canonical, staging=staging)
    prior = _load_human_fields(out_path)

    rows = {}
    human = {}
    for b in inv["bundles"]:
        key = b["path"]
        prev = prior.get(key, {})
        theme = prev.get("theme") or b["title"]
        status = prev.get("status") or ("draft" if b["zone"] != "canonical" else "canonical")
        note = prev.get("note", "")
        human[key] = {"theme": theme, "status": status, "note": note}
        link = os.path.relpath(b["path"], out_dir)
        rows[key] = {
            "zone": b["zone"],
            "theme": theme,
            "link": link,
            "rel": b["rel_path"],
            "types": ", ".join(f"{k}×{v}" for k, v in sorted(b["types"].items())) or "—",
            "concepts": b["concept_count"],
            "tags": ", ".join(b["tags"][:8]) or "—",
            "status": status,
            "updated": (b["latest_timestamp"] or "—")[:10],
            "conformant": b["conformant"],
            "note": note,
        }

    # carry forward bundles that were indexed before but are now missing on disk
    present = set(rows)
    missing = [k for k in prior if k not in present]

    now = inv["scanned_at"]
    lines = [
        "---",
        'okf_master_index: "1"',
        f"generated: {now}",
        "---",
        "",
        f"# {title}",
        "",
        "> 这是**工作区级**的知识包总目录（母题索引），用于快速定位工作区内的所有 OKF 知识包。",
        "> 它**不是** OKF 规范的一部分（OKF 的 `index.md` 是单包内部的目录），而是一层治理索引。",
        "> 文件名 `OKF-INDEX.md`（大写）刻意区别于 OKF 保留的小写 `index.md`，不会被误认成包内目录。",
        "",
        f"- 扫描根目录：`{inv['root']}`",
        f"- 受控知识库（canonical）：`{canonical}`" if canonical else "- 受控知识库（canonical）：未设置",
        f"- 暂存知识包（staging）：`{staging}`" if staging else "- 暂存知识包（staging）：未设置",
        f"- 知识包总数：**{inv['bundle_count']}**",
        "",
        "字段说明：**母题** 为人工维护的主题名；**状态** 由人工维护（draft/review/canonical/superseded 等）；其余列由扫描自动生成，可随时用 `okf_tools.py index` 重建。",
        "",
    ]

    for zone_key, zone_title in (
        ("canonical", "受控知识库 · Canonical"),
        ("staging", "暂存知识包 · Staging"),
        ("other", "其它位置 · Other"),
    ):
        zrows = [r for r in rows.values() if r["zone"] == zone_key]
        if not zrows:
            continue
        lines.append(f"## {zone_title}")
        lines.append("")
        lines.append("| 母题 / Theme | 知识包 / Bundle | type 词表 | 概念数 | 标签 | 状态 | 更新于 | 合规 |")
        lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for r in sorted(zrows, key=lambda x: x["theme"].lower()):
            ok = "✅" if r["conformant"] else "⚠️"
            note = f"<br><sub>{r['note']}</sub>" if r["note"] else ""
            lines.append(
                f"| {r['theme']}{note} | [{r['rel']}]({r['link']}) | {r['types']} | "
                f"{r['concepts']} | {r['tags']} | {r['status']} | {r['updated']} | {ok} |"
            )
        lines.append("")

    if missing:
        lines.append("## 未找到 / 可能已移动 · Missing")
        lines.append("")
        lines.append("> 这些条目曾被登记，但本次扫描在磁盘上未找到。请确认是否已移动、合并或删除。")
        lines.append("")
        for k in missing:
            human[k] = prior[k]
            lines.append(f"- `{k}` — 母题：{prior[k].get('theme','?')}，状态：{prior[k].get('status','?')}")
        lines.append("")

    lines.append("<!-- OKF-INDEX-DATA")
    lines.append(json.dumps(human, ensure_ascii=False, indent=2, sort_keys=True))
    lines.append("-->")
    lines.append("")

    os.makedirs(out_dir or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return {"out": out_path, "bundle_count": inv["bundle_count"], "missing": len(missing)}


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _print_validate(summary, verbose):
    status = "CONFORMANT" if summary["conformant"] else "NON-CONFORMANT"
    print(f"[{status}] {summary['path']}")
    print(
        f"  concepts={summary['concept_count']} "
        f"types={summary['types']} "
        f"index={'yes' if summary['has_index'] else 'no'} "
        f"log={'yes' if summary['has_log'] else 'no'}"
    )
    for e in summary["errors"]:
        print(f"  ERROR  {e}")
    if verbose:
        for w in summary["warnings"]:
            print(f"  warn   {w}")
    elif summary["warnings"]:
        print(f"  ({len(summary['warnings'])} warning(s) — re-run with --verbose to see them)")


def main(argv=None):
    p = argparse.ArgumentParser(description="OKF v0.1 workspace utilities")
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("scan", help="discover bundles under a root -> JSON")
    ps.add_argument("root")
    ps.add_argument("--canonical", default=None)
    ps.add_argument("--staging", default=None)
    ps.add_argument("--json", default=None, help="also write JSON here")

    pv = sub.add_parser("validate", help="conformance-check one bundle directory")
    pv.add_argument("path")
    pv.add_argument("--verbose", action="store_true")

    pi = sub.add_parser("index", help="(re)generate the master index (OKF-INDEX.md)")
    pi.add_argument("root")
    pi.add_argument("--out", required=True)
    pi.add_argument("--canonical", default=None)
    pi.add_argument("--staging", default=None)

    args = p.parse_args(argv)

    if args.cmd == "scan":
        result = scan(args.root, canonical=args.canonical, staging=args.staging)
        text = json.dumps(result, ensure_ascii=False, indent=2)
        if args.json:
            with open(args.json, "w", encoding="utf-8") as fh:
                fh.write(text)
        print(text)
        return 0

    if args.cmd == "validate":
        summary = validate_bundle(args.path)
        _print_validate(summary, args.verbose)
        return 0 if summary["conformant"] else 1

    if args.cmd == "index":
        res = build_index(
            args.root, args.out, canonical=args.canonical, staging=args.staging
        )
        print(
            f"Wrote {res['out']} ({res['bundle_count']} bundle(s)"
            + (f", {res['missing']} missing" if res["missing"] else "")
            + ")"
        )
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
