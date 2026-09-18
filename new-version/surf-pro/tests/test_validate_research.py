"""Offline tests using synthetic records only; no search quality claims."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_research.py"
spec = importlib.util.spec_from_file_location("validate_research", SCRIPT)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
validate = module.validate_record


def fixture():
    """Entirely fictional source and facts; example.invalid is not fetched."""
    return {
        "schema_version": "2.0", "research_id": "synthetic-unit-test", "is_example": True,
        "brief": {"user_request": "测试：文档规定什么？", "objective": "检查合成文档中的声明。",
                  "scope": "仅测试夹具，不是真实研究。", "as_of": "2026-09-18", "depth": "quick",
                  "expansion_policy": "adaptive", "assumptions": []},
        "questions": [{"id": "Q001", "question": "合成文档规定什么？", "tier": "core",
                       "acceptance": "能定位给定文本。", "status": "answered", "claim_ids": ["C001"], "gap": ""}],
        "sources": [{"id": "S001", "title": "合成文档，不是真实网页", "locator": "https://example.invalid/fixture",
                     "source_type": "synthetic-fixture", "publisher": "虚构主体", "published_at": None,
                     "accessed_at": "2026-09-18", "access_status": "full", "origin_group": "synthetic-origin-1",
                     "reading_note": "仅合成测试记录，没有访问外部网页。", "context": "不支持现实世界结论。"}],
        "claims": [{"id": "C001", "statement": "合成文档写有测试条款。", "question_ids": ["Q001"], "kind": "fact",
                    "status": "supported", "confidence": "moderate", "confidence_reason": "仅模拟直接支持关系。",
                    "evidence": [{"source_id": "S001", "relation": "supports", "locator": "合成第1段",
                                  "note": "模拟文本支持；不是实际检索记录。", "entailment": "direct"}],
                    "limitations": "本记录不能证明外部事实。"}],
        "extensions": [], "queries": [], "assets": [],
        "completion": {"status": "complete_for_scope", "reason": "合成范围已覆盖，不是现实研究完成。"},
    }


def add_extension(d, status="include"):
    d["questions"].append({"id": "Q002", "question": "教学补充建议？", "tier": "extension", "acceptance": "有范围明确的建议。",
                           "status": "answered", "claim_ids": ["C002"], "gap": ""})
    d["claims"].append({"id": "C002", "statement": "建议把限制写清。", "question_ids": ["Q002"], "kind": "recommendation",
                       "status": "qualified", "confidence": "moderate", "confidence_reason": "本次方法建议，并非经验事实。",
                       "evidence": [], "limitations": "需按实际用途取舍。"})
    d["extensions"].append({"id": "X001", "question_id": "Q002", "anchor_question_ids": ["Q001"],
                            "why_relevant": "有助理解核心声明边界。", "benefit": "减少把示例当事实的风险。", "status": status})


def add_asset(d, path="assets/sample.txt", digest=None):
    d["assets"].append({"id": "A001", "source_id": "S001", "local_path": path, "kind": "text", "inspection": "verified",
                         "inspection_note": "合成文本测试。", "sha256": digest, "rights_note": "本测试生成文本。"})


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.d = fixture()

    def assert_bad(self, needle=None):
        result = validate(self.d)
        self.assertEqual(result["result"], "failed")
        if needle:
            self.assertIn(needle, "\n".join(result["errors"]))

    def test_valid_single_source_record(self):
        result = validate(self.d)
        self.assertEqual(result["errors"], [])
        self.assertIn("external truth", result["does_not_verify"])
        self.assertTrue(result["warnings"])

    def test_empty_template_is_valid_draft_not_research(self):
        d = json.loads((ROOT / "templates" / "research-record.json").read_text())
        self.assertEqual(validate(d)["errors"], [])
        self.assertTrue(d["is_example"])
        self.assertEqual(d["completion"]["status"], "draft")

    def test_wrong_schema(self):
        self.d["schema_version"] = "1.0"
        self.assert_bad("expected 2.0")

    def test_unknown_field(self):
        self.d["sources"][0]["grade"] = "A"
        self.assert_bad("unknown field grade")

    def test_missing_field(self):
        del self.d["claims"][0]["confidence_reason"]
        self.assert_bad("missing field confidence_reason")

    def test_bad_date(self):
        self.d["brief"]["as_of"] = "2026-02-30"
        self.assert_bad("ISO date")

    def test_wrong_boolean_type(self):
        self.d["is_example"] = "false"
        self.assert_bad("must be boolean")

    def test_bad_id_format(self):
        self.d["queries"] = [{"id": "R1", "query": "sample", "question_ids": ["Q001"], "channel": "fixture",
                               "purpose": "test", "outcome": "no source", "source_ids": []}]
        self.assert_bad("at least 3 digits")

    def test_duplicate_source_id(self):
        self.d["sources"].append(copy.deepcopy(self.d["sources"][0]))
        self.assert_bad("duplicate id")

    def test_unknown_source_reference(self):
        self.d["claims"][0]["evidence"][0]["source_id"] = "S999"
        self.assert_bad("unknown sources id")

    def test_unknown_question_reference(self):
        self.d["claims"][0]["question_ids"] = ["Q999"]
        self.assert_bad("unknown questions id")

    def test_missing_question_claim_backlink(self):
        self.d["questions"][0]["claim_ids"] = []
        self.assert_bad("does not link back")

    def test_missing_claim_question_backlink(self):
        self.d["claims"][0]["question_ids"] = []
        self.assert_bad("does not link back")

    def test_duplicate_refs(self):
        self.d["claims"][0]["question_ids"] = ["Q001", "Q001"]
        self.assert_bad("duplicate entries")

    def test_snippet_cannot_support_verified_fact(self):
        self.d["sources"][0]["access_status"] = "snippet"
        self.assert_bad("readable supporting evidence")

    def test_unavailable_cannot_support_verified_fact(self):
        self.d["sources"][0]["access_status"] = "unavailable"
        self.assert_bad("readable supporting evidence")

    def test_abstract_requires_qualification(self):
        self.d["sources"][0]["access_status"] = "abstract"
        self.assert_bad("non-abstract support")

    def test_qualified_abstract_allowed_with_warning(self):
        self.d["sources"][0]["access_status"] = "abstract"
        self.d["claims"][0]["status"] = "qualified"
        result = validate(self.d)
        self.assertEqual(result["errors"], [])
        self.assertIn("abstract-only", "\n".join(result["warnings"]))

    def test_abstract_strong_confidence_rejected(self):
        self.d["sources"][0]["access_status"] = "abstract"
        self.d["claims"][0].update(status="qualified", confidence="strong")
        self.assert_bad("must not use strong confidence")

    def test_context_cannot_claim_direct_entailment(self):
        self.d["claims"][0]["evidence"][0]["relation"] = "context"
        self.assert_bad("context-only")

    def test_support_cannot_have_no_entailment(self):
        self.d["claims"][0]["evidence"][0]["entailment"] = "none"
        self.assert_bad("must state direct or partial")

    def test_duplicate_evidence(self):
        self.d["claims"][0]["evidence"] *= 2
        self.assert_bad("duplicate evidence")

    def test_supported_cannot_ignore_counterevidence(self):
        e = copy.deepcopy(self.d["claims"][0]["evidence"][0])
        e.update(relation="contradicts", locator="合成第2段")
        self.d["claims"][0]["evidence"].append(e)
        self.assert_bad("unresolved contradictory")

    def test_contested_requires_both_sides(self):
        self.d["claims"][0]["status"] = "contested"
        self.assert_bad("support and contradiction")

    def test_valid_contested_record(self):
        e = copy.deepcopy(self.d["claims"][0]["evidence"][0])
        e.update(relation="contradicts", locator="合成第2段")
        self.d["claims"][0]["evidence"].append(e)
        self.d["claims"][0]["status"] = "contested"
        self.assertEqual(validate(self.d)["errors"], [])

    def test_same_origin_warning_not_automatic_error(self):
        s = copy.deepcopy(self.d["sources"][0]); s["id"] = "S002"
        self.d["sources"].append(s)
        e = copy.deepcopy(self.d["claims"][0]["evidence"][0]); e["source_id"] = "S002"
        self.d["claims"][0]["evidence"].append(e)
        result = validate(self.d)
        self.assertEqual(result["errors"], [])
        self.assertIn("one declared origin", "\n".join(result["warnings"]))

    def test_unverified_cannot_claim_answered(self):
        self.d["claims"][0].update(status="unverified", confidence="weak")
        self.assert_bad("cannot rely only on unverified")

    def test_partial_with_unverified_and_snippet_is_valid(self):
        self.d["claims"][0].update(status="unverified", confidence="unknown")
        self.d["sources"][0]["access_status"] = "snippet"
        self.d["questions"][0].update(status="partial", gap="未读正文，关键事实未核实。")
        self.d["completion"].update(status="partial", reason="因访问受限停止，已标明缺口。")
        self.assertEqual(validate(self.d)["errors"], [])

    def test_unverified_cannot_have_strong_confidence(self):
        self.d["claims"][0].update(status="unverified", confidence="strong")
        self.assert_bad("weak or unknown")

    def test_hypothesis_cannot_be_supported(self):
        self.d["claims"][0]["kind"] = "hypothesis"
        self.assert_bad("reclassified")

    def test_recommendation_without_external_fact_is_allowed(self):
        self.d["claims"][0].update(kind="recommendation", status="qualified", evidence=[])
        self.assertEqual(validate(self.d)["errors"], [])

    def test_extension_included_valid(self):
        add_extension(self.d)
        self.assertEqual(validate(self.d)["errors"], [])

    def test_extension_off_rejects_include(self):
        add_extension(self.d)
        self.d["brief"]["expansion_policy"] = "off"
        self.assert_bad("expansion_policy=off")

    def test_extension_off_allows_rejected_candidate(self):
        add_extension(self.d, "reject")
        self.d["brief"]["expansion_policy"] = "off"
        self.assertEqual(validate(self.d)["errors"], [])

    def test_extension_cannot_anchor_itself(self):
        add_extension(self.d)
        self.d["extensions"][0]["anchor_question_ids"] = ["Q002"]
        self.assert_bad("not another extension")

    def test_extension_needs_route(self):
        add_extension(self.d)
        self.d["extensions"] = []
        self.assert_bad("lacks an anchored routing")

    def test_duplicate_extension_route(self):
        add_extension(self.d)
        x = copy.deepcopy(self.d["extensions"][0]); x["id"] = "X002"
        self.d["extensions"].append(x)
        self.assert_bad("duplicate routing")

    def test_promoted_prerequisite_cannot_keep_extension_route(self):
        add_extension(self.d)
        self.d["questions"][1]["tier"] = "prerequisite"
        self.assert_bad("target must be an extension")

    def test_unresolved_extension_does_not_block_core_completion(self):
        add_extension(self.d, "defer")
        self.d["claims"].pop()
        self.d["questions"][1].update(status="unanswered", claim_ids=[], gap="可选线索尚未检索。")
        self.assertEqual(validate(self.d)["errors"], [])

    def test_completion_cannot_hide_core_gap(self):
        self.d["questions"][0].update(status="partial", gap="证据缺口。")
        self.assert_bad("essential questions remain unresolved")

    def test_completed_empty_record_rejected(self):
        self.d["claims"] = []; self.d["questions"] = []
        self.assert_bad("must contain a core question")

    def test_actual_query_can_return_no_sources(self):
        self.d["queries"] = [{"id": "R001", "query": "合成查询", "question_ids": ["Q001"], "channel": "fixture",
                               "purpose": "测试空结果记录。", "outcome": "没有结果，仅合成。", "source_ids": []}]
        self.assertEqual(validate(self.d)["errors"], [])

    def test_asset_safe_path_hash_and_no_mutation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "assets").mkdir()
            p = root / "assets/sample.txt"; p.write_bytes(b"synthetic text")
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
            add_asset(self.d, digest=digest)
            before = copy.deepcopy(self.d)
            self.assertEqual(validate(self.d, root)["errors"], [])
            self.assertEqual(self.d, before)
            self.assertEqual(p.read_bytes(), b"synthetic text")

    def test_asset_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / "a.txt").write_text("x")
            add_asset(self.d, "a.txt", "0" * 64)
            self.assertIn("sha256 mismatch", "\n".join(validate(self.d, root)["errors"]))

    def test_asset_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            add_asset(self.d)
            self.assertIn("does not exist", "\n".join(validate(self.d, Path(tmp))["errors"]))

    def test_asset_path_traversal_rejected_without_io(self):
        for raw in ("../secret", "/absolute", "C:/secret", "assets\\file", "a/../b", "\x00", ""):
            with self.subTest(path=repr(raw)):
                self.d = fixture(); add_asset(self.d, raw)
                self.assert_bad("safe relative POSIX")

    def test_asset_symlink_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp); root = parent / "root"; root.mkdir()
            outside = parent / "outside.txt"; outside.write_text("synthetic")
            try:
                (root / "escape.txt").symlink_to(outside)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable on this platform")
            add_asset(self.d, "escape.txt")
            self.assertIn("escapes root", "\n".join(validate(self.d, root)["errors"]))

    def test_uninspected_asset_warning(self):
        add_asset(self.d)
        self.d["assets"][0]["inspection"] = "unverified"
        result = validate(self.d)
        self.assertEqual(result["errors"], [])
        self.assertIn("not visually/content inspected", "\n".join(result["warnings"]))

    def test_bad_hash_type(self):
        add_asset(self.d, digest="not-a-hash")
        self.assert_bad("64 characters")

    def test_malformed_json_values_never_crash(self):
        values = (None, [], {}, True, 123)
        base = fixture(); add_extension(base); add_asset(base)
        for key in base:
            for value in values:
                d = copy.deepcopy(base); d[key] = value
                with self.subTest(top=key, value=value):
                    self.assertIsInstance(validate(d)["errors"], list)
        containers = ("brief", "completion", "questions", "sources", "claims", "extensions", "assets")
        for group in containers:
            original = base[group][0] if isinstance(base[group], list) else base[group]
            for key in original:
                for value in values:
                    d = copy.deepcopy(base)
                    obj = d[group][0] if isinstance(d[group], list) else d[group]
                    obj[key] = value
                    with self.subTest(group=group, field=key, value=value):
                        self.assertIsInstance(validate(d)["errors"], list)
        for key in base["claims"][0]["evidence"][0]:
            for value in values:
                d = copy.deepcopy(base); d["claims"][0]["evidence"][0][key] = value
                with self.subTest(evidence_field=key, value=value):
                    self.assertIsInstance(validate(d)["errors"], list)
        for value in values:
            with self.subTest(root=value):
                self.assertTrue(validate(value)["errors"])


class CLITests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True, timeout=10)

    def test_valid_file_exit_zero(self):
        p = self.run_cli(ROOT / "templates/research-record.json")
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["check"], "structure_and_internal_consistency_only")

    def test_invalid_schema_exit_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"; path.write_text("{}")
            self.assertEqual(self.run_cli(path).returncode, 1)

    def test_invalid_json_exit_two(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"; path.write_text("{broken")
            self.assertEqual(self.run_cli(path).returncode, 2)

    def test_missing_file_exit_two(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.run_cli(Path(tmp) / "missing.json").returncode, 2)

    def test_help(self):
        self.assertEqual(self.run_cli("--help").returncode, 0)


if __name__ == "__main__":
    unittest.main()
