#!/usr/bin/env python3
"""Offline structural checks for Surf Pro records. Never verifies external truth.

Python 3.10+, standard library only. Reads but never modifies input files.
CLI exit codes: 0 no structural errors, 1 validation errors, 2 input/CLI error.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "2.0"
GROUPS = {
    "questions": ("Q", {"id", "question", "tier", "acceptance", "status", "claim_ids", "gap"}),
    "sources": ("S", {"id", "title", "locator", "source_type", "publisher", "published_at", "accessed_at", "access_status", "origin_group", "reading_note", "context"}),
    "claims": ("C", {"id", "statement", "question_ids", "kind", "status", "confidence", "confidence_reason", "evidence", "limitations"}),
    "extensions": ("X", {"id", "question_id", "anchor_question_ids", "why_relevant", "benefit", "status"}),
    "queries": ("R", {"id", "query", "question_ids", "channel", "purpose", "outcome", "source_ids"}),
    "assets": ("A", {"id", "source_id", "local_path", "kind", "inspection", "inspection_note", "sha256", "rights_note"}),
}
TOP = {"schema_version", "research_id", "is_example", "brief", *GROUPS, "completion"}
BRIEF = {"user_request", "objective", "scope", "as_of", "depth", "expansion_policy", "assumptions"}
READABLE = {"full", "partial", "abstract"}


def validate_record(data: Any, root: Path | None = None) -> dict[str, Any]:
    """Validate internal consistency. A caller-supplied root enables asset checks."""
    errors: list[str] = []
    warnings: list[str] = []

    def err(path: str, message: str) -> None:
        errors.append(f"{path}: {message}")

    def obj(value: Any, keys: set[str], path: str) -> dict[str, Any]:
        if not isinstance(value, dict):
            err(path, "must be an object")
            return {}
        for key in sorted(keys - value.keys()):
            err(path, f"missing field {key}")
        for key in sorted(value.keys() - keys, key=str):
            err(path, f"unknown field {key}")
        return value

    def text(value: Any, path: str, empty: bool = False) -> bool:
        ok = isinstance(value, str) and (empty or bool(value.strip()))
        if not ok:
            err(path, "must be a nonempty string" if not empty else "must be a string")
        return ok

    def one_of(value: Any, choices: set[str]) -> bool:
        return isinstance(value, str) and value in choices

    def enum(value: Any, choices: set[str], path: str) -> None:
        if not one_of(value, choices):
            err(path, f"must be one of {', '.join(sorted(choices))}")

    def strings(value: Any, path: str, nonempty: bool = False) -> list[str]:
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            err(path, "must be a list of nonempty strings")
            return []
        if nonempty and not value:
            err(path, "must not be empty")
        if len(value) != len(set(value)):
            err(path, "duplicate entries")
        return value

    def day(value: Any, path: str, nullable: bool = False) -> None:
        if value is None and nullable:
            return
        try:
            if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError
            date.fromisoformat(value)
        except (TypeError, ValueError):
            err(path, "must be an ISO date YYYY-MM-DD" + (" or null" if nullable else ""))

    data = obj(data, TOP, "record")
    if data.get("schema_version") != SCHEMA_VERSION:
        err("schema_version", f"expected {SCHEMA_VERSION}")
    text(data.get("research_id"), "research_id")
    if not isinstance(data.get("is_example"), bool):
        err("is_example", "must be boolean")
    elif data["is_example"]:
        warnings.append("Example/template record: not evidence of a real research run.")
    brief = obj(data.get("brief"), BRIEF, "brief")
    for k in ("user_request", "objective", "scope"):
        text(brief.get(k), f"brief.{k}")
    day(brief.get("as_of"), "brief.as_of")
    enum(brief.get("depth"), {"quick", "standard", "deep"}, "brief.depth")
    enum(brief.get("expansion_policy"), {"off", "adaptive", "wide"}, "brief.expansion_policy")
    strings(brief.get("assumptions"), "brief.assumptions")

    indexes: dict[str, dict[str, dict[str, Any]]] = {}
    for group, (prefix, keys) in GROUPS.items():
        indexes[group] = {}
        rows = data.get(group)
        if not isinstance(rows, list):
            err(group, "must be an array")
            continue
        for i, row in enumerate(rows):
            p = f"{group}[{i}]"
            row = obj(row, keys, p)
            ident = row.get("id")
            if not isinstance(ident, str) or not re.fullmatch(prefix + r"\d{3,}", ident):
                err(p, f"id must match {prefix} followed by at least 3 digits")
            elif ident in indexes[group]:
                err(p, f"duplicate id {ident}")
            else:
                indexes[group][ident] = row

    def refs(value: Any, group: str, path: str, nonempty: bool = False) -> list[str]:
        result = strings(value, path, nonempty)
        for ident in result:
            if ident not in indexes[group]:
                err(path, f"unknown {group} id {ident}")
        return result

    def ref(value: Any, group: str, path: str) -> None:
        if not isinstance(value, str) or value not in indexes[group]:
            err(path, f"unknown {group} id")

    for sid, s in indexes["sources"].items():
        for k in ("title", "locator", "source_type", "publisher", "origin_group", "reading_note", "context"):
            text(s.get(k), f"{sid}.{k}")
        day(s.get("published_at"), f"{sid}.published_at", nullable=True)
        day(s.get("accessed_at"), f"{sid}.accessed_at")
        enum(s.get("access_status"), READABLE | {"snippet", "unavailable"}, f"{sid}.access_status")

    for qid, q in indexes["questions"].items():
        for k in ("question", "acceptance"):
            text(q.get(k), f"{qid}.{k}")
        enum(q.get("tier"), {"core", "prerequisite", "extension"}, f"{qid}.tier")
        enum(q.get("status"), {"answered", "partial", "unanswered"}, f"{qid}.status")
        text(q.get("gap"), f"{qid}.gap", empty=q.get("status") == "answered")
        ids = refs(q.get("claim_ids"), "claims", f"{qid}.claim_ids", nonempty=q.get("status") == "answered")
        for cid in ids:
            c = indexes["claims"].get(cid, {})
            if qid not in strings(c.get("question_ids"), f"{cid}.question_ids"):
                err(qid, f"claim {cid} does not link back to this question")
        if q.get("status") == "answered" and ids and all(indexes["claims"].get(cid, {}).get("status") == "unverified" for cid in ids):
            err(qid, "answered question cannot rely only on unverified claims")

    for cid, c in indexes["claims"].items():
        for k in ("statement", "confidence_reason"):
            text(c.get(k), f"{cid}.{k}")
        enum(c.get("kind"), {"fact", "inference", "recommendation", "hypothesis"}, f"{cid}.kind")
        enum(c.get("status"), {"supported", "qualified", "contested", "unverified"}, f"{cid}.status")
        enum(c.get("confidence"), {"strong", "moderate", "weak", "unknown"}, f"{cid}.confidence")
        text(c.get("limitations"), f"{cid}.limitations", empty=c.get("status") == "supported" and c.get("kind") == "fact")
        qids = refs(c.get("question_ids"), "questions", f"{cid}.question_ids", nonempty=True)
        for qid in qids:
            if cid not in strings(indexes["questions"].get(qid, {}).get("claim_ids"), f"{qid}.claim_ids"):
                err(cid, f"question {qid} does not link back to this claim")
        if c.get("status") == "unverified" and one_of(c.get("confidence"), {"strong", "moderate"}):
            err(cid, "unverified claim must use weak or unknown confidence")
        if c.get("kind") == "hypothesis" and c.get("status") == "supported":
            err(cid, "a supported result should be reclassified rather than remain a hypothesis")
        evidence = c.get("evidence")
        if not isinstance(evidence, list):
            err(f"{cid}.evidence", "must be an array")
            evidence = []
        usable: list[tuple[str, str, str]] = []
        seen: set[tuple[str, str, str]] = set()
        for i, e in enumerate(evidence):
            p = f"{cid}.evidence[{i}]"
            e = obj(e, {"source_id", "relation", "locator", "note", "entailment"}, p)
            sid = e.get("source_id")
            ref(sid, "sources", f"{p}.source_id")
            enum(e.get("relation"), {"supports", "contradicts", "context"}, f"{p}.relation")
            enum(e.get("entailment"), {"direct", "partial", "none"}, f"{p}.entailment")
            for k in ("locator", "note"):
                text(e.get(k), f"{p}.{k}")
            if e.get("relation") == "context" and e.get("entailment") != "none":
                err(p, "context-only reference must use entailment=none")
            if one_of(e.get("relation"), {"supports", "contradicts"}) and e.get("entailment") == "none":
                err(p, "support/contradiction must state direct or partial entailment")
            if all(isinstance(e.get(k), str) for k in ("source_id", "relation", "locator")):
                key = (sid, e["relation"], e["locator"])
                if key in seen:
                    err(p, "duplicate evidence entry")
                seen.add(key)
            s = indexes["sources"].get(sid, {}) if isinstance(sid, str) else {}
            if one_of(s.get("access_status"), READABLE) and one_of(e.get("entailment"), {"direct", "partial"}):
                usable.append((sid, e.get("relation"), e.get("entailment")))
        supports = [x for x in usable if x[1] == "supports"]
        against = [x for x in usable if x[1] == "contradicts"]
        if one_of(c.get("kind"), {"fact", "inference"}):
            if one_of(c.get("status"), {"supported", "qualified", "contested"}) and not supports:
                err(cid, "verified factual/inferential claim needs readable supporting evidence")
            if c.get("status") == "supported" and not any(x[2] == "direct" and one_of(indexes["sources"][x[0]].get("access_status"), {"full", "partial"}) for x in supports):
                err(cid, "supported claim needs direct non-abstract support; otherwise qualify it")
        if c.get("status") == "contested" and not (supports and against):
            err(cid, "contested claim needs readable support and contradiction")
        if against and c.get("status") == "supported":
            err(cid, "unresolved contradictory evidence cannot accompany an unqualified supported claim")
        if supports:
            if all(indexes["sources"][s].get("access_status") == "abstract" for s, _, _ in supports):
                warnings.append(f"{cid}: abstract-only support; methods and full-text limits require human review.")
                if c.get("confidence") == "strong":
                    err(cid, "abstract-only claim must not use strong confidence")
            source_ids = {s for s, _, _ in supports}
            origins = {indexes["sources"][s].get("origin_group") for s in source_ids if isinstance(indexes["sources"][s].get("origin_group"), str)}
            if len(source_ids) > 1 and len(origins) == 1:
                warnings.append(f"{cid}: supporting sources share one declared origin; not independent corroboration.")

    extension_targets: set[str] = set()
    for xid, x in indexes["extensions"].items():
        target = x.get("question_id")
        ref(target, "questions", f"{xid}.question_id")
        if isinstance(target, str):
            if target in extension_targets:
                err(xid, "duplicate routing entry for extension question")
            extension_targets.add(target)
        q = indexes["questions"].get(target, {}) if isinstance(target, str) else {}
        if q.get("tier") != "extension":
            err(xid, "target must be an extension question")
        anchors = refs(x.get("anchor_question_ids"), "questions", f"{xid}.anchor_question_ids", nonempty=True)
        for anchor in anchors:
            if not one_of(indexes["questions"].get(anchor, {}).get("tier"), {"core", "prerequisite"}):
                err(xid, "anchor must directly reference core/prerequisite, not another extension")
        for k in ("why_relevant", "benefit"):
            text(x.get(k), f"{xid}.{k}")
        enum(x.get("status"), {"include", "defer", "reject"}, f"{xid}.status")
        if x.get("status") == "include":
            if brief.get("expansion_policy") == "off":
                err(xid, "included optional extension conflicts with expansion_policy=off")
            if not q.get("claim_ids"):
                err(xid, "included extension needs recorded claims or explicitly labeled suggestions")
    for qid, q in indexes["questions"].items():
        if q.get("tier") == "extension" and qid not in extension_targets:
            err(qid, "extension question lacks an anchored routing entry")

    for rid, r in indexes["queries"].items():
        for k in ("query", "channel", "purpose", "outcome"):
            text(r.get(k), f"{rid}.{k}")
        refs(r.get("question_ids"), "questions", f"{rid}.question_ids", nonempty=True)
        refs(r.get("source_ids"), "sources", f"{rid}.source_ids")

    for aid, a in indexes["assets"].items():
        ref(a.get("source_id"), "sources", f"{aid}.source_id")
        enum(a.get("kind"), {"image", "page_clip", "video_frame", "text"}, f"{aid}.kind")
        enum(a.get("inspection"), {"verified", "unverified"}, f"{aid}.inspection")
        for k in ("local_path", "inspection_note", "rights_note"):
            text(a.get(k), f"{aid}.{k}")
        if a.get("inspection") == "unverified":
            warnings.append(f"{aid}: not visually/content inspected; cannot be treated as inspected evidence.")
        digest = a.get("sha256")
        if digest is not None and (not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            err(aid, "sha256 must be lowercase hexadecimal (64 characters) or null")
        raw = a.get("local_path")
        if isinstance(raw, str):
            if not raw or "\\" in raw or "\x00" in raw or ":" in raw or Path(raw).is_absolute() or ".." in Path(raw).parts:
                err(aid, "local_path must be a safe relative POSIX path")
                continue
            if root is not None:
                try:
                    base = root.resolve()
                    p = (base / raw).resolve()
                    if not p.is_relative_to(base):
                        err(aid, "asset escapes root, including via symlink")
                    elif not p.is_file():
                        err(aid, "asset file does not exist")
                    elif isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest):
                        h = hashlib.sha256()
                        with p.open("rb") as f:
                            for block in iter(lambda: f.read(1024 * 1024), b""):
                                h.update(block)
                        if h.hexdigest() != digest:
                            err(aid, "asset sha256 mismatch")
                except (OSError, RuntimeError, ValueError) as exc:
                    err(aid, f"asset read failure: {exc}")

    completion = obj(data.get("completion"), {"status", "reason"}, "completion")
    enum(completion.get("status"), {"draft", "complete_for_scope", "partial", "blocked"}, "completion.status")
    text(completion.get("reason"), "completion.reason")
    essential = [q for q in indexes["questions"].values() if one_of(q.get("tier"), {"core", "prerequisite"})]
    unanswered = [q["id"] for q in essential if q.get("status") != "answered"]
    if completion.get("status") == "complete_for_scope":
        if not any(q.get("tier") == "core" for q in essential):
            err("completion", "complete record must contain a core question")
        if unanswered:
            err("completion", f"essential questions remain unresolved: {', '.join(unanswered)}")
    return {
        "check": "structure_and_internal_consistency_only",
        "result": "failed" if errors else "passed",
        "errors": errors,
        "warnings": warnings,
        "counts": {k: len(v) for k, v in indexes.items()},
        "unresolved_essential_question_ids": unanswered,
        "asset_filesystem_checks_enabled": root is not None,
        "does_not_verify": ["external truth", "semantic entailment", "real source independence", "actual visual inspection", "copyright permission", "research completeness"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="Path to a research-record.json file")
    parser.add_argument("--root", type=Path, help="Asset root; defaults to the record's parent directory")
    args = parser.parse_args()
    try:
        data = json.loads(args.record.read_text(encoding="utf-8"))
        result = validate_record(data, args.root or args.record.parent)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
