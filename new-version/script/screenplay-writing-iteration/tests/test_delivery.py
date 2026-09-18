"""Synthetic fixtures only. These are not real user approvals or media tests."""
import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_delivery", ROOT/'scripts/check_delivery.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
A = ('# Synthetic standard\n\n## SC001｜门厅\n甲持有钥匙。\n'
     '**对白 D001｜甲**：明早我再答复你。\n'
     '**旁白 V001｜叙述者**：后来，她等到了答复。\n'
     '**屏幕文字 T001｜卡片**：明早 09:00\n'
     '## SC002｜门外\n**对白 D002｜乙**：好。\n')

class DeliveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name); self.project=self.base/'project.json'
        self.a=self.base/'standard.md'; self.b=self.base/'prompts.md'; self.c=self.base/'alignment.md'
        self.a.write_text(A,encoding='utf-8'); h=m.digest(self.a)
        self.header='标准稿版本：v001\n标准稿 SHA-256：'+h+'\n'
        self.b.write_text(self.header+A,encoding='utf-8')
        self.c.write_text(self.header+'# Synthetic alignment, not actual media review\n',encoding='utf-8')
        self.data={
            'schema_version':1,'project_id':'synthetic-test-only',
            'current':{'version':'v001','file':'standard.md','sha256':h},
            'approval':{'version':'v001','sha256':h,'quote':'合成测试确认，不是真实用户授权。','context':'Unit test fixture only'},
            'derived':{'file':'prompts.md','sha256':m.digest(self.b),'source_version':'v001','source_sha256':h,'alignment_file':'alignment.md','alignment_sha256':m.digest(self.c)}
        }
    def run_check(self, final=True):
        self.project.write_text(json.dumps(self.data,ensure_ascii=False),encoding='utf-8')
        return m.validate(self.project,final)
    def change_b(self, text):
        self.b.write_text(text,encoding='utf-8'); self.data['derived']['sha256']=m.digest(self.b)
    def bad(self):
        r=self.run_check(); self.assertFalse(r['ok'],r); return r
    def test_valid_pair(self):
        r=self.run_check(); self.assertTrue(r['ok'],r); self.assertEqual(r['state'],'paired_structural'); self.assertEqual(r['protected_text_count'],4)
    def test_valid_draft(self):
        self.data['approval']=self.data['derived']=None
        r=self.run_check(False); self.assertTrue(r['ok']); self.assertEqual(r['state'],'draft')
    def test_draft_not_final(self):
        self.data['approval']=self.data['derived']=None; self.bad()
    def test_approved_pending(self):
        self.data['derived']=None; r=self.run_check(False)
        self.assertTrue(r['ok']); self.assertEqual(r['state'],'approved_pending_translation')
    def test_pending_not_final(self):
        self.data['derived']=None; self.bad()
    def test_no_approval_derived(self):
        self.data['approval']=None; self.bad()
    def test_stale_approval_version(self):
        self.data['approval']['version']='v000'; self.bad()
    def test_stale_approval_hash(self):
        self.data['approval']['sha256']='0'*64; self.bad()
    def test_stale_source_version(self):
        self.data['derived']['source_version']='v000'; self.bad()
    def test_stale_source_hash(self):
        self.data['derived']['source_sha256']='0'*64; self.bad()
    def test_changed_standard_bytes(self):
        self.a.write_text(A+'changed',encoding='utf-8'); self.bad()
    def test_changed_prompts_bytes(self):
        self.b.write_text(self.header+A+'changed',encoding='utf-8'); self.bad()
    def test_missing_file(self):
        self.a.unlink(); self.bad()
    def test_path_escape(self):
        self.data['current']['file']='../outside.md'; self.bad()
    def test_absolute_path(self):
        self.data['current']['file']=str(self.a); self.bad()
    def test_duplicate_scene(self):
        self.change_b(self.header+A+'\n## SC001｜duplicate\n'); self.bad()
    def test_scene_order(self):
        self.change_b((self.header+A).replace('SC001','SWAP').replace('SC002','SC001').replace('SWAP','SC002')); self.bad()
    def test_missing_scene(self):
        self.change_b((self.header+A).replace('## SC002｜门外','### SH002｜门外')); self.bad()
    def test_duplicate_utterance(self):
        self.change_b(self.header+A+'\n**对白 D002｜乙**：好。\n'); self.bad()
    def test_changed_speaker(self):
        self.change_b((self.header+A).replace('D001｜甲','D001｜乙')); self.bad()
    def test_changed_spoken_text(self):
        self.change_b((self.header+A).replace('明早我再答复你。','明天见。')); self.bad()
    def test_changed_screen_text(self):
        self.change_b((self.header+A).replace('明早 09:00','明早 10:00')); self.bad()
    def test_changed_channel(self):
        self.change_b((self.header+A).replace('对白 D001','旁白 V002')); self.bad()
    def test_changed_parent_scene(self):
        row='**旁白 V001｜叙述者**：后来，她等到了答复。\n'
        self.change_b((self.header+A).replace(row,'').replace('## SC002｜门外\n','## SC002｜门外\n'+row)); self.bad()
    def test_added_utterance(self):
        self.change_b(self.header+A+'\n**对白 D003｜乙**：再见。\n'); self.bad()
    def test_missing_alignment(self):
        self.c.unlink(); self.bad()
    def test_alignment_wrong_header(self):
        self.c.write_text(self.header.replace('v001','v002'),encoding='utf-8')
        self.data['derived']['alignment_sha256']=m.digest(self.c); self.bad()
    def test_prompts_wrong_header(self):
        self.change_b((self.header+A).replace('标准稿版本：v001','标准稿版本：v002')); self.bad()
    def test_blank_confirmation(self):
        self.data['approval']['quote']=' '; self.bad()
    def test_blank_context(self):
        self.data['approval']['context']=''; self.bad()
    def test_extra_state_field(self):
        self.data['is_final']=True; self.bad()
    def test_bad_schema_bool(self):
        self.data['schema_version']=True; self.bad()
    def test_duplicate_json_key(self):
        self.project.write_text('{"schema_version":1,"schema_version":1}',encoding='utf-8')
        self.assertFalse(m.validate(self.project)['ok'])
    def test_fake_hash(self):
        self.data['current']['sha256']='REPLACE_WITH_ACTUAL_SHA256'; self.bad()
    def test_immutable_approval_on_new_current(self):
        self.data['current']['version']='v002'; self.bad()
    def test_unmarked_semantics_are_not_verified(self):
        # Deliberate semantic drift is invisible to a marker/hash checker.
        # A structural pass MUST NOT be reported as semantic/production success.
        self.change_b((self.header+A).replace('甲持有钥匙。','乙抢走钥匙。'))
        r=self.run_check(); self.assertTrue(r['ok']); self.assertTrue(any('semantic' in x for x in r['not_checked']))
    def test_no_marker_format(self):
        self.change_b('# Plain prose without SC markers\n'); self.bad()
    def test_wrong_id_prefix(self):
        self.change_b((self.header+A).replace('对白 D001','对白 V001')); self.bad()
    def test_malformed_line(self):
        self.change_b((self.header+A).replace('D001｜甲**：','D001｜甲** ')); self.bad()
    def test_script_checker_does_not_write(self):
        self.run_check(); before={p.name:p.read_bytes() for p in self.base.iterdir()}
        m.validate(self.project,True); after={p.name:p.read_bytes() for p in self.base.iterdir()}
        self.assertEqual(before,after)
    def test_real_teaching_pair_markers(self):
        p=ROOT/'examples/approved-pair'; a=(p/'standard-v003.md').read_text(encoding='utf-8'); b=(p/'prompts-v003.md').read_text(encoding='utf-8')
        self.assertEqual(m.parse_script(a,'example A'),m.parse_script(b,'example B'))
        m.source_header(b,'v003',m.digest(p/'standard-v003.md'),'example B')
        m.source_header((p/'alignment-v003.md').read_text(encoding='utf-8'),'v003',m.digest(p/'standard-v003.md'),'example alignment')

if __name__ == '__main__': unittest.main()
