#!/usr/bin/env python3
"""Read-only screenplay pair checker. Python 3.9+, standard library only.
This checks file identity and marked structural invariants, not user identity,
semantic equivalence, unmarked dialogue, artistic quality, or generated media.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

HASH = re.compile(r"^[0-9a-f]{64}$")
SCENE = re.compile(r"^##\s+(SC\d{3,})(?=$|[\s|｜])")
LINE = re.compile(r"^\*\*(对白|旁白|屏幕文字)\s+([DVT]\d{3,})[｜|]([^*]+)\*\*[：:](.*)$")
PREFIX = {"对白": "D", "旁白": "V", "屏幕文字": "T"}
NOT_CHECKED = ["user identity and approval meaning", "unmarked text and semantic equivalence", "aesthetic quality", "actual model settings, generated media and audience effect"]

class ContractError(ValueError):
    pass

def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            h.update(block)
    return h.hexdigest()

def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContractError("Duplicate JSON key: " + key)
        result[key] = value
    return result

def fields(obj, expected, label):
    if not isinstance(obj, dict) or set(obj) != set(expected):
        raise ContractError(label + " must have exactly these fields: " + ", ".join(expected))

def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ContractError(label + " must be a nonempty string")

def hash_value(value, label):
    if not isinstance(value, str) or not HASH.fullmatch(value):
        raise ContractError(label + " must be an actual lowercase SHA-256")

def checked_file(base, name, expected_hash, label):
    nonempty(name, label + ".file")
    hash_value(expected_hash, label + ".sha256")
    relative = Path(name)
    if relative.is_absolute():
        raise ContractError(label + " must use a project-relative path")
    path = (base / relative).resolve()
    try:
        path.relative_to(base.resolve())
    except ValueError:
        raise ContractError(label + " path escapes the project directory")
    if not path.is_file():
        raise ContractError(label + " file is missing: " + name)
    if digest(path) != expected_hash:
        raise ContractError(label + " file hash differs from the recorded snapshot")
    return path

def parse_script(text, label):
    scenes, utterances, seen_scenes, seen_lines = [], [], set(), set()
    current = None
    for line_number, line in enumerate(text.splitlines(), 1):
        match = SCENE.match(line)
        if match:
            current = match.group(1)
            if current in seen_scenes:
                raise ContractError(label + " duplicate scene: " + current)
            seen_scenes.add(current)
            scenes.append(current)
        match = LINE.fullmatch(line)
        if match:
            kind, uid, owner, content = match.groups()
            if current is None:
                raise ContractError(label + " protected text occurs before any scene")
            if uid in seen_lines:
                raise ContractError(label + " duplicate protected text ID: " + uid)
            if not uid.startswith(PREFIX[kind]):
                raise ContractError(label + " wrong ID prefix for " + kind)
            if not owner.strip() or not content.strip():
                raise ContractError(label + " empty owner/content in " + uid)
            seen_lines.add(uid)
            utterances.append((current, kind, uid, owner, content))
        elif re.match(r"^\*\*(对白|旁白|屏幕文字)\s+[DVT]\d", line):
            raise ContractError(label + " malformed protected line at " + str(line_number))
    if not scenes:
        raise ContractError(label + " has no ## SC001-style scene headings; use documented format or manual review")
    return scenes, utterances

def source_header(text, version, sha256, label):
    versions = re.findall(r"(?m)^标准稿版本[：:]\s*(\S+)\s*$", text)
    hashes = re.findall(r"(?m)^标准稿 SHA-256[：:]\s*(\S+)\s*$", text)
    if versions != [version] or hashes != [sha256]:
        raise ContractError(label + " source header does not uniquely match current version/hash")

def validate(project_path, require_final=False):
    result = {"ok": False, "state": "conflict", "structural_pair_valid": False, "errors": [], "not_checked": NOT_CHECKED}
    try:
        project_path = Path(project_path).resolve()
        data = json.loads(project_path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
        fields(data, ("schema_version", "project_id", "current", "approval", "derived"), "project")
        if type(data["schema_version"]) is not int or data["schema_version"] != 1:
            raise ContractError("Unsupported schema_version")
        nonempty(data["project_id"], "project_id")
        current = data["current"]
        fields(current, ("version", "file", "sha256"), "current")
        nonempty(current["version"], "current.version")
        a = checked_file(project_path.parent, current["file"], current["sha256"], "current")
        approval, derived = data["approval"], data["derived"]
        if approval is None:
            if derived is not None:
                raise ContractError("A final derived object cannot exist without matching approval")
            result["state"] = "draft"
        else:
            fields(approval, ("version", "sha256", "quote", "context"), "approval")
            for key in ("quote", "context"):
                nonempty(approval[key], "approval." + key)
            if approval["version"] != current["version"] or approval["sha256"] != current["sha256"]:
                raise ContractError("Approval belongs to a different version/snapshot")
            result["state"] = "approved_pending_translation"
            if derived is not None:
                fields(derived, ("file", "sha256", "source_version", "source_sha256", "alignment_file", "alignment_sha256"), "derived")
                if derived["source_version"] != current["version"] or derived["source_sha256"] != current["sha256"]:
                    raise ContractError("Derived file belongs to a different source version/snapshot")
                b = checked_file(project_path.parent, derived["file"], derived["sha256"], "derived")
                alignment = checked_file(project_path.parent, derived["alignment_file"], derived["alignment_sha256"], "alignment")
                if len({a, b, alignment, project_path}) != 4:
                    raise ContractError("Project, standard, prompts and alignment must be separate files")
                a_text, b_text = a.read_text(encoding="utf-8"), b.read_text(encoding="utf-8")
                a_scenes, a_lines = parse_script(a_text, "standard")
                b_scenes, b_lines = parse_script(b_text, "prompts")
                if a_scenes != b_scenes:
                    raise ContractError("Scene IDs/order differ between standard and prompts")
                if a_lines != b_lines:
                    raise ContractError("Protected dialogue/VO/on-screen text, owner, order or parent scene differs")
                source_header(b_text, current["version"], current["sha256"], "prompts")
                source_header(alignment.read_text(encoding="utf-8"), current["version"], current["sha256"], "alignment")
                result.update(state="paired_structural", structural_pair_valid=True, scene_count=len(a_scenes), protected_text_count=len(a_lines))
        if require_final and not result["structural_pair_valid"]:
            result["errors"].append("--require-final needs matching approval, prompts and alignment; current state: " + result["state"])
        result["ok"] = not result["errors"]
    except (OSError, UnicodeError, ValueError, TypeError, KeyError) as exc:
        result["state"] = "conflict"
        result["errors"].append(str(exc))
    return result

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", type=Path)
    parser.add_argument("--hash", dest="hash_file", type=Path, help="Print the actual SHA-256 of a file; writes nothing")
    parser.add_argument("--require-final", action="store_true", help="Require the paired structural state, not just a valid draft")
    args = parser.parse_args(argv)
    if args.hash_file is not None:
        if args.project is not None or args.require_final:
            parser.error("--hash is a standalone operation")
        try:
            print(digest(args.hash_file))
            return 0
        except OSError as exc:
            print(json.dumps({"ok": False, "errors": [str(exc)]}, ensure_ascii=False))
            return 1
    if args.project is None:
        parser.error("Provide project.json or --hash FILE")
    result = validate(args.project, args.require_final)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    sys.exit(main())
