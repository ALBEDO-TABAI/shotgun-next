#!/usr/bin/env python3
"""Refresh the delivered workspace index, preserving this bundle's human fields.

The original uploaded OKF helper stores keys as absolute paths. This small wrapper
rebases only this known bundle's entry when the delivered directory is moved.
"""
from __future__ import annotations
import json
from pathlib import Path
import sys
import okf_tools

ROOT=Path(__file__).resolve().parents[1]
REL='knowledge/contemporary-prompting'
BUNDLE=ROOT/REL
OUT=ROOT/'OKF-INDEX.md'

def main() -> None:
    if not (BUNDLE/'index.md').is_file():raise SystemExit('未找到本指南知识包，索引未修改。')
    fields={}
    if OUT.is_file():
        match=okf_tools.DATA_BLOCK_RE.search(OUT.read_text(encoding='utf-8'))
        if match:
            fields=json.loads(match.group(1))
            if not isinstance(fields,dict):raise SystemExit('索引人工字段格式无效，未修改。')
    current=str(BUNDLE.resolve())
    candidates=[k for k in fields if k.replace('\\','/').rstrip('/').endswith('/'+REL)]
    if len(candidates)>1 and current not in candidates:
        raise SystemExit('发现多个旧位置的同名知识包，请先核对OKF-INDEX.md；未修改。')
    old=current if current in fields else (candidates[0] if candidates else None)
    human=fields.get(old,{}) if old else {}
    if not isinstance(human,dict):raise SystemExit('索引条目的人工字段无效，未修改。')
    human={
        'theme':human.get('theme') or '当代生成式视听创作：自然语言、通感与生产迭代',
        'status':human.get('status') or 'review',
        'note':human.get('note') or '文本与结构已检查；原创案例未运行生成实验；核心框架待实际项目检验。'
    }
    if old and old!=current:fields.pop(old)
    fields[current]=human
    # Keep arbitrary other bundle entries; the supplied builder handles missing ones.
    OUT.write_text('<!-- OKF-INDEX-DATA\n'+json.dumps(fields,ensure_ascii=False,indent=2)+'\n-->\n',encoding='utf-8')
    res=okf_tools.build_index(str(ROOT),str(OUT),canonical='knowledge-base',staging='knowledge')
    print(f'已刷新本地工作区索引：{res["bundle_count"]} 个知识包。')

if __name__=='__main__':main()
