#!/usr/bin/env python3
"""Read-only checks for content, package links, input snapshots and optional hashes.

Use --report FILE to write a new check report. Without it, no files are changed.
This cannot validate the artistic quality or generation performance of prompts.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,re,sys,zipfile
from pathlib import Path
from urllib.parse import urlsplit,unquote
import yaml
import okf_tools

ROOT=Path(__file__).resolve().parents[1]
BUNDLE=ROOT/'knowledge/contemporary-prompting'

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def run(skip_checksums=False)->dict:
    report={'scope':'file_and_content_structure_not_media_quality','errors':[],'warnings':[]}
    validation=okf_tools.validate_bundle(str(BUNDLE))
    report['okf']=validation
    report['errors'].extend(validation['errors'])
    report['warnings'].extend(validation['warnings'])
    concepts=[];links=[];external=set();text_chars=0;cjk_chars=0;code_blocks=0
    for p in sorted(BUNDLE.rglob('*.md')):
        raw=p.read_text(encoding='utf-8');fm,body,parse_error=okf_tools.split_frontmatter(raw)
        rel=p.relative_to(BUNDLE).as_posix()
        body=body if body is not None else raw
        fences=re.findall(r'^\s*```.*$',body,re.M)
        if len(fences)%2:report['errors'].append(f'未闭合代码围栏: {rel}')
        code_blocks+=len(fences)//2
        if '\ufffd' in raw:report['errors'].append(f'含替换乱码字符: {rel}')
        if p.name not in ('index.md','log.md'):
            concepts.append(rel)
            if '# Citations' not in body:report['errors'].append(f'缺少来源小节: {rel}')
            text_chars+=len(body)
            cjk_chars+=len(re.findall(r'[\u3400-\u9fff]',body))
        for href in re.findall(r'\[[^\]]*\]\(([^)\s]+)',body):
            if href.startswith(('https://','http://')):external.add(href)
            elif urlsplit(href).path.endswith('.md'):
                target=(BUNDLE/unquote(urlsplit(href).path).lstrip('/')) if href.startswith('/') else p.parent/unquote(urlsplit(href).path)
                try:target.resolve().relative_to(BUNDLE.resolve())
                except ValueError:report['errors'].append(f'跨出知识包的Markdown链接: {rel} -> {href}');continue
                if not target.is_file():report['errors'].append(f'链接不存在: {rel} -> {href}')
                links.append((rel,target.relative_to(BUNDLE).as_posix()))
    incoming=collections.Counter(t for _,t in links)
    for c in concepts:
        if not incoming[c]:report['errors'].append(f'知识单元没有入链: {c}')
    reader=ROOT/'开始阅读.html'
    if not reader.is_file():report['errors'].append('缺少离线阅读器')
    else:
        raw=reader.read_text(encoding='utf-8')
        match=re.search(r'<script id="guide-data" type="application/json">(.*?)</script>',raw,re.S)
        if not match:report['errors'].append('阅读器数据缺失')
        else:
            try:
                data=json.loads(match.group(1)); report['reader_pages']=len(data['pages'])
                if data['conceptCount']!=len(concepts):report['errors'].append('阅读器与Markdown概念数量不一致')
                source_paths={p.relative_to(BUNDLE).as_posix() for p in BUNDLE.rglob('*.md')}
                if {p['path'] for p in data['pages']}!=source_paths:report['errors'].append('阅读器缺页或多页')
                for page in data['pages']:
                    _,body,_=okf_tools.split_frontmatter((BUNDLE/page['path']).read_text(encoding='utf-8'))
                    if page['text'].strip()!=body.strip():report['errors'].append('阅读器内容未同步: '+page['path'])
            except (ValueError,KeyError,TypeError) as exc:report['errors'].append('阅读器数据无法验证: '+str(exc))
        if re.search(r'<(?:script|link|img)[^>]+(?:src|href)=["\']https?://',raw):report['errors'].append('阅读器自动加载网络资源')
    manifest=ROOT/'qa/scope_manifest.json'
    if manifest.is_file():
        source=json.loads(manifest.read_text(encoding='utf-8'))
        review_record=next(x for x in source['source_archives'] if x['filename'].startswith('ciwei-'))
        local=ROOT/'sources/tutorial-text-review-source.zip'
        if not local.is_file() or sha(local)!=review_record['sha256']:report['errors'].append('教程文字输入副本摘要不匹配')
        tool_record=next(x for x in source['direct_source_scope'] if x['scope']=='uploaded-okf-skill' and x['path']=='scripts/okf_tools.py')
        if sha(ROOT/'scripts/okf_tools.py')!=tool_record['sha256']:report['errors'].append('上传skill的校验器副本已改变')
    else:report['errors'].append('缺少输入范围清单')
    sumfile=ROOT/'SHA256SUMS.txt'; checked=0
    if sumfile.is_file() and not skip_checksums:
        entries={}
        for line in sumfile.read_text(encoding='utf-8').splitlines():
            if not line.strip():continue
            digest,rel=line.split('  ',1);target=ROOT/rel
            if rel in entries:report['errors'].append('重复哈希清单项: '+rel)
            entries[rel]=digest
            try:target.resolve().relative_to(ROOT.resolve())
            except ValueError:report['errors'].append('非法哈希清单路径: '+rel);continue
            if not target.is_file() or sha(target)!=digest:report['errors'].append('文件摘要不匹配: '+rel)
            checked+=1
        # Python may create local caches when a user re-runs a script; ignore only those.
        actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt' and '__pycache__' not in p.parts and p.suffix!='.pyc'}
        if actual!=set(entries):report['errors'].append('当前文件集合与SHA256SUMS不同；编辑后应重新生成清单。')
    report['metrics']={'concepts':len(concepts),'body_characters_including_markup':text_chars,'body_cjk_characters':cjk_chars,'code_blocks':code_blocks,'internal_markdown_links_including_indexes':len(links),'unique_internal_edges':len(set(links)),'unique_external_source_urls':len(external),'hash_entries_checked':checked}
    report['media_generation_tests']='not_run'
    report['passed']=not report['errors']
    return report

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--report',type=Path);ap.add_argument('--skip-checksums',action='store_true');args=ap.parse_args()
    result=run(args.skip_checksums);out=json.dumps(result,ensure_ascii=False,indent=2)
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(out+'\n',encoding='utf-8')
    print(out)
    return 0 if result['passed'] else 1

if __name__=='__main__':sys.exit(main())
