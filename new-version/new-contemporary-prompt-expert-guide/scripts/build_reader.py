#!/usr/bin/env python3
"""Build a self-contained offline reader from the Markdown knowledge bundle.

No network access or generation APIs. Markdown remains the content source.
"""
from __future__ import annotations
import html
import json
import re
from pathlib import Path, PurePosixPath
import sys

try:
    import yaml
    import mistune
    from bs4 import BeautifulSoup
except ImportError as exc:
    raise SystemExit('重建阅读器需安装 requirements.txt 中的依赖。') from exc

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'knowledge' / 'contemporary-prompting'
GROUPS = {
    'foundations': ('基础方法', '00—05'),
    'language': ('通感与表达', '06—11'),
    'craft': ('视听专业', '12—20'),
    'workflows': ('生成与迭代', '21—28'),
    'cases': ('完整案例', '29—36'),
    'practice': ('工具与练习', '37—40'),
    'references': ('来源与理论', '术语表 · 参考'),
}
MD = mistune.create_markdown(escape=True, plugins=['table', 'strikethrough'])

def split_text(raw: str) -> tuple[dict, str]:
    if not raw.startswith('---\n'):
        return {}, raw
    match = re.match(r'\A---\n(.*?)\n---\n', raw, re.S)
    if not match:
        raise ValueError('YAML frontmatter 未闭合')
    return yaml.safe_load(match.group(1)) or {}, raw[match.end():].strip()

def make_html(body: str, rel: str, all_paths: set[str]) -> tuple[str, list[dict]]:
    pieces = re.split(r'\n# Citations\s*\n', body, maxsplit=1)
    rendered = MD(pieces[0])
    if len(pieces) > 1:
        rendered += '<details class="citations"><summary>来源与依据</summary>' + MD(pieces[1]) + '</details>'
    soup = BeautifulSoup(rendered, 'html.parser')
    toc = []
    prefix = re.sub(r'[^a-zA-Z0-9-]+','-',rel.removesuffix('.md'))
    for i, heading in enumerate(soup.find_all(['h2', 'h3'])):
        anchor = prefix+'-section-'+str(i)
        heading['id'] = anchor
        if heading.name == 'h2':
            toc.append({'id':anchor,'title':heading.get_text()})
    for a in soup.find_all('a', href=True):
        href=a['href']
        if href.startswith(('https://','http://')):
            a['target']='_blank';a['rel']='noopener noreferrer'
            continue
        path,sep,anchor=href.partition('#')
        if path.endswith('.md'):
            if path.startswith('/'):
                target=path.lstrip('/')
            else:
                import posixpath
                target=posixpath.normpath(str(PurePosixPath(rel).parent/path))
            if target not in all_paths:
                raise ValueError(f'无效包内链接: {rel} -> {href}')
            a['href']='#/'+target.removesuffix('.md')
            if sep:a['href']+='?section='+anchor
    for table in list(soup.find_all('table')):
        wrapper=soup.new_tag('div',attrs={'class':'table-wrap'})
        table.wrap(wrapper)
    for pre in soup.find_all('pre'):
        pre['tabindex']='0'
        button=soup.new_tag('button',attrs={'class':'copy-btn','type':'button','aria-label':'复制这一段'})
        button.string='复制'
        pre.insert(0,button)
    return str(soup),toc

def build() -> None:
    if not (BUNDLE/'index.md').is_file():
        raise SystemExit(f'未找到知识包: {BUNDLE}')
    all_paths={p.relative_to(BUNDLE).as_posix() for p in BUNDLE.rglob('*.md')}
    paths=[BUNDLE/'index.md']
    for group in GROUPS:
        paths.append(BUNDLE/group/'index.md')
        paths.extend(p for p in sorted((BUNDLE/group).glob('*.md')) if p.name!='index.md')
    paths.append(BUNDLE/'log.md')
    pages=[]
    for p in paths:
        rel=p.relative_to(BUNDLE).as_posix();fm,body=split_text(p.read_text(encoding='utf-8'))
        rendered,toc=make_html(body,rel,all_paths)
        group=rel.split('/')[0] if '/' in rel else 'home'
        title=fm.get('title') or next((x[2:].strip() for x in body.splitlines() if x.startswith('# ')),p.stem)
        pages.append({'id':rel.removesuffix('.md'),'path':rel,'title':title,'description':fm.get('description',''),
            'type':fm.get('type','Index' if p.name=='index.md' else 'Log'), 'group':group,
            'tags':fm.get('tags',[]),'html':rendered,'text':body,'toc':toc})
    concepts=[p for p in pages if p['type'] not in ('Index','Log')]
    data={'pages':pages,'groups':GROUPS,'conceptCount':len(concepts),'date':'2026-09-18'}
    shell=(ROOT/'scripts/reader_template.html').read_text(encoding='utf-8')
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    if shell.count('__DATA__')!=1:raise ValueError('阅读器模板数据槽数量错误')
    target=ROOT/'开始阅读.html';target.write_text(shell.replace('__DATA__',payload),encoding='utf-8')
    print(f'已生成 {target.name}: {len(concepts)} 个知识单元，{len(pages)} 个页面，{target.stat().st_size:,} bytes')

if __name__=='__main__':build()
