"""Tests of deterministic package checks, not of model behavior."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_package", ROOT / "scripts/check_package.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class PackageTests(unittest.TestCase):
    def test_frontmatter_valid(self):
        self.assertEqual(m.frontmatter('---\nname: test-skill\ndescription: "中文说明"\n---\n')['description'], '中文说明')
    def test_missing_frontmatter(self):
        with self.assertRaises(ValueError): m.frontmatter('# No metadata')
    def test_unclosed_frontmatter(self):
        with self.assertRaises(ValueError): m.frontmatter('---\nname: test-skill')
    def test_duplicate_frontmatter(self):
        with self.assertRaises(ValueError): m.frontmatter('---\nname: x\nname: y\n---')
    def test_bad_quoted_value(self):
        with self.assertRaises(ValueError): m.frontmatter('---\nname: "unterminated\n---')
    def test_name_rules(self):
        for good in ('screenplay-writing-iteration', 'test1'): self.assertTrue(m.NAME_RE.fullmatch(good))
        for bad in ('BadName', 'bad_name', '-bad', 'bad--name', '../escape'): self.assertFalse(m.NAME_RE.fullmatch(bad))
    def test_links_skip_code_and_remote(self):
        text = '[x](real.md)\n```text\n[x](not-a-file.md)\n```\n`[y](not-real.md)`\n[x](https://example.com)\n[z](#section)\n'
        self.assertEqual(list(m.link_targets(text)), ['real.md'])
    def test_link_decode(self):
        self.assertEqual(list(m.link_targets('[x](%E4%B8%80.md#x)')), ['一.md'])
    def test_boundary_check(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)/'skill'; root.mkdir()
            self.assertTrue(m.within(root, root/'references/a.md'))
            self.assertFalse(m.within(root, root/'../outside.md'))
    def test_missing_root(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertFalse(m.check(Path(td)/'missing')['ok'])
    def test_actual_package(self):
        result = m.check(ROOT)
        self.assertTrue(result['ok'], result['errors'])
        self.assertEqual(result['counts']['source_documents'], 303)

    def fixture(self, folder):
        root = Path(folder)/'demo-skill'; root.mkdir()
        (root/'agents').mkdir(); (root/'references/knowledge').mkdir(parents=True)
        (root/'examples').mkdir(); (root/'evals').mkdir()
        (root/'SKILL.md').write_text('---\nname: demo-skill\ndescription: "fixture"\n---\n',encoding='utf-8')
        (root/'agents/openai.yaml').write_text('interface:\n  display_name: demo\n  short_description: test\n  default_prompt: $demo-skill\n',encoding='utf-8')
        for name in ('README.md','VALIDATION.md','examples/index.md','evals/README.md'):
            (root/name).write_text('# Fixture\n',encoding='utf-8')
        (root/'evals/cases.json').write_text(json.dumps({'cases':[{'id':'X01'}]}),encoding='utf-8')
        docs=[]
        for i in range(303):
            p=root/f'references/knowledge/doc-{i:03}.md'; p.write_text('# Source\n',encoding='utf-8')
            docs.append({'packaged_path':str(p.relative_to(root)), 'packaged_sha256':m.digest(p)})
        (root/'references/source-manifest.json').write_text(json.dumps({'source_document_count':303,'documents':docs}),encoding='utf-8')
        return root
    def test_hash_tampering(self):
        with tempfile.TemporaryDirectory() as td:
            root=self.fixture(td); self.assertTrue(m.check(root)['ok'])
            (root/'references/knowledge/doc-000.md').write_text('changed',encoding='utf-8')
            self.assertTrue(any('hash mismatch' in e for e in m.check(root)['errors']))
    def test_broken_link(self):
        with tempfile.TemporaryDirectory() as td:
            root=self.fixture(td); (root/'README.md').write_text('[missing](not-there.md)',encoding='utf-8')
            self.assertTrue(any('Unresolved local link' in e for e in m.check(root)['errors']))
    def test_duplicate_eval_id(self):
        with tempfile.TemporaryDirectory() as td:
            root=self.fixture(td); (root/'evals/cases.json').write_text('{"cases":[{"id":"A"},{"id":"A"}]}',encoding='utf-8')
            self.assertTrue(any('Duplicate behavioral' in e for e in m.check(root)['errors']))
    def test_metadata_folder_mismatch(self):
        with tempfile.TemporaryDirectory() as td:
            root=self.fixture(td); (root/'SKILL.md').write_text('---\nname: wrong-name\ndescription: "fixture"\n---',encoding='utf-8')
            self.assertTrue(any('match directory' in e for e in m.check(root)['errors']))

if __name__ == '__main__': unittest.main()
