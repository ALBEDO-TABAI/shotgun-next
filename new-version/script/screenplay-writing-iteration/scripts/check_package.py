#!/usr/bin/env python3
"""Read-only structural check of this standalone Skill. Python 3.9+, stdlib only.
Passing this check does not test model behavior, artistic quality or installation.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            h.update(block)
    return h.hexdigest()

def within(root, path):
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False

def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must begin with YAML front matter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("Unclosed front matter")
    result = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError("Expected single-line front matter key/value")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in result:
            raise ValueError("Duplicate front matter key: " + key)
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                raise ValueError("Invalid quoted metadata: " + str(exc))
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        result[key] = value
    return result

def link_targets(text):
    # Source prose uses ordinary inline links. Ignore examples inside code.
    text = re.sub(r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", text)
    text = re.sub(r"`+[^`\n]*`+", "", text)
    targets = re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", text)
    targets += re.findall(r"(?m)^\s*\[[^\]]+\]:\s*(\S+)", text)
    for target in targets:
        target = target.strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = re.split(r'\s+[\"\']', target, maxsplit=1)[0]
        if not target or target.startswith("#"):
            continue
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            continue
        yield unquote(parts.path)

def check(root):
    root = Path(root).resolve()
    errors, counts = [], {"markdown_files": 0, "local_links": 0, "source_documents": 0}
    if not root.is_dir():
        return {"ok": False, "errors": ["Skill directory does not exist"], "counts": counts}
    try:
        meta = frontmatter((root / "SKILL.md").read_text(encoding="utf-8"))
        name, desc = meta.get("name"), meta.get("description")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append("Invalid skill name")
        elif name != root.name:
            errors.append("Skill name must match directory name")
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
            errors.append("Missing or overlong description")
        interface = (root / "agents/openai.yaml").read_text(encoding="utf-8")
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in interface:
                errors.append("Missing interface field " + field)
        if isinstance(name, str) and "$" + name not in interface:
            errors.append("Default prompt does not explicitly name the skill")
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append("Metadata: " + str(exc))
    for required in ("README.md", "VALIDATION.md", "examples/index.md", "evals/cases.json", "evals/README.md"):
        if not (root / required).is_file():
            errors.append("Missing required support file: " + required)
    skills = list(root.rglob("SKILL.md"))
    if len(skills) != 1:
        errors.append("Expected exactly one SKILL.md")
    for path in sorted(root.rglob("*")):
        if path.name in (".DS_Store", "__MACOSX", "__pycache__") or path.name.startswith("._"):
            errors.append("Unexpected build metadata: " + str(path.relative_to(root)))
        if path.is_symlink():
            errors.append("Symlinks are not packaged: " + str(path.relative_to(root)))
        if not path.is_file() or path.suffix != ".md":
            continue
        counts["markdown_files"] += 1
        try:
            text = path.read_text(encoding="utf-8")
            for target in link_targets(text):
                if not target:
                    continue
                counts["local_links"] += 1
                dest = path.parent / target
                if not within(root, dest) or not dest.exists():
                    errors.append("Unresolved local link: " + str(path.relative_to(root)) + " -> " + target)
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(str(path.relative_to(root)) + ": " + str(exc))
    try:
        manifest = json.loads((root / "references/source-manifest.json").read_text(encoding="utf-8"))
        docs = manifest["documents"]
        counts["source_documents"] = len(docs)
        if len(docs) != manifest["source_document_count"] or len(docs) != 303:
            errors.append("Expected all 303 source documents")
        seen = set()
        for item in docs:
            relative = item["packaged_path"]
            path = root / relative
            if relative in seen:
                errors.append("Duplicate source manifest path: " + relative)
            seen.add(relative)
            if not within(root, path) or not path.is_file():
                errors.append("Missing source document: " + relative)
            elif digest(path) != item["packaged_sha256"]:
                errors.append("Source hash mismatch: " + relative)
        actual = {str(p.relative_to(root)) for p in (root / "references/knowledge").rglob("*.md")}
        if actual != seen:
            errors.append("Knowledge directory does not match source manifest")
        cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        ids = [case["id"] for case in cases["cases"]]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate behavioral evaluation ID")
        counts["behavioral_cases"] = len(ids)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        errors.append("Manifest/evaluations: " + str(exc))
    return {"ok": not errors, "scope": "package structure, local file links (not heading anchors), source hashes; not behavior", "counts": counts, "errors": errors}

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    result = check(args.directory)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    sys.exit(main())
