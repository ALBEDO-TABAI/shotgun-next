const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const root = path.resolve(__dirname, '../..');
const deps = process.env.AUDIT_NODE_MODULES || '/Users/bai/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const markedModule = {exports:{}};
new Function('exports','module',fs.readFileSync(path.join(deps,'marked/lib/marked.umd.js'),'utf8'))(markedModule.exports,markedModule);
const {marked} = markedModule.exports;
const { chromium } = require(path.join(deps, 'playwright'));
const assets = process.env.AUDIT_MERMAID_ASSETS || '/Users/bai/.cache/uv/archive-v0/wkQ04XjpJIr1PibW/gradio/templates/frontend/assets';
const mermaidEntry = fs.readdirSync(assets).find(n=>/^mermaid\.core-.*\.js$/.test(n));
if (!mermaidEntry) throw new Error('Set AUDIT_MERMAID_ASSETS to a local Mermaid asset directory.');
const files = ['README.md','00-EXECUTIVE-SUMMARY.md',...['docs','modules','tools','diagrams','shotgun'].flatMap(d=>fs.readdirSync(path.join(root,d)).filter(n=>n.endsWith('.md')).map(n=>d+'/'+n)), '_analysis/README.md'];
if(fs.existsSync(path.join(root,'AUDIT-REPORT.md'))) files.push('AUDIT-REPORT.md');
const errors=[], diagrams=[], linkRows=[];
const headings=new Map();
const slug = s => s.toLowerCase().replace(/<[^>]*>/g,'').replace(/[`*_]/g,'').replace(/[^\p{L}\p{N}_\-\s]/gu,'').replace(/ /g,'-');
function headingIds(file) {
  if(headings.has(file))return headings.get(file);
  const counts=new Map(),ids=new Set();
  marked.walkTokens(marked.lexer(fs.readFileSync(file,'utf8')),t=>{
    if(t.type!=='heading')return;
    const base=slug(t.text),n=counts.get(base)||0;
    ids.add(base+(n?'-'+n:''));counts.set(base,n+1);
  });headings.set(file,ids);return ids;
}
for(const file of files) {
  let diagramIndex=0;
  const tokens=marked.lexer(fs.readFileSync(path.join(root,file),'utf8'));
  marked.walkTokens(tokens,t=>{
    if(t.type==='code'&&t.lang==='mermaid')diagrams.push({file,index:++diagramIndex,source:t.text});
    if(!['link','image'].includes(t.type))return;
    const href=t.href;
    if(/^[a-z][a-z0-9+.-]*:/i.test(href))return;
    const [raw,fragment]=href.split('#');
    const target=path.resolve(path.dirname(path.join(root,file)),decodeURIComponent(raw||''));
    const row={file,href,target:path.relative(root,target)};linkRows.push(row);
    if(!fs.existsSync(target))errors.push({...row,error:'missing target'});
    else if(fragment&&target.endsWith('.md')&&!headingIds(target).has(decodeURIComponent(fragment)))errors.push({...row,error:'missing heading anchor'});
    else if(fragment&&/^L\d+$/.test(fragment)) {
      const line=Number(fragment.slice(1));
      if(line>fs.readFileSync(target,'utf8').split('\n').length)errors.push({...row,error:'source line out of range'});
    }
  });
}
const server=http.createServer((req,res)=>{
  if(req.url==='/'){res.setHeader('Content-Type','text/html');res.end('<!doctype html><html><body style="margin:16px;background:white"></body></html>');return;}
  const filename=path.resolve(assets,'.'+decodeURIComponent(req.url.split('?')[0]));
  if(!filename.startsWith(assets+path.sep)||!fs.existsSync(filename)){res.writeHead(404);res.end();return;}
  res.setHeader('Content-Type',filename.endsWith('.css')?'text/css':filename.endsWith('.js')?'text/javascript':'application/octet-stream');
  fs.createReadStream(filename).pipe(res);
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  let browser;
  const renders=[];
  try {
    browser=await chromium.launch({headless:true,channel:'msedge'});
    const page=await browser.newPage({viewport:{width:1600,height:1200}});
    const origin='http://127.0.0.1:'+server.address().port;
    await page.route('**/*',route=>route.request().url().startsWith(origin)?route.continue():route.abort());
    await page.goto(origin);
    const engine=await page.evaluate(async entry=>{
      const exports=await import('/'+entry);
      const found=Object.entries(exports).flatMap(([k,v])=>[[k,v],[k+'.default',v?.default]]).find(([,v])=>v && typeof v.initialize==='function' && typeof v.render==='function' && typeof v.parse==='function');
      if(!found)throw Error('No Mermaid public API in local bundle');
      window.auditMermaid=found[1];window.auditMermaid.initialize({startOnLoad:false,securityLevel:'strict',theme:'default',maxTextSize:100000});
      return {exportName:found[0],version:found[1].version || 'not exposed',entry};
    },mermaidEntry);
    fs.mkdirSync(path.join(__dirname,'rendered'),{recursive:true});
    for(let i=0;i<diagrams.length;i++) {
      const d=diagrams[i];
      try {
        const rendered=await page.evaluate(async ({source,id})=>{
          document.body.innerHTML='';
          await window.auditMermaid.parse(source);
          const result=await window.auditMermaid.render(id,source);
          document.body.innerHTML=result.svg;
          const svg=document.querySelector('svg'),b=svg.getBBox();
          return {svg:result.svg,width:b.width,height:b.height,textNodes:svg.querySelectorAll('text,foreignObject').length};
        },{source:d.source,id:'auditDiagram'+i});
        if(rendered.width<=0||rendered.height<=0)throw Error('Blank SVG bounds');
        const stem=d.file.replace(/\.md$/,'').replaceAll('/','--')+'--'+d.index;
        fs.writeFileSync(path.join(__dirname,'rendered',stem+'.svg'),rendered.svg);
        const row={file:d.file,index:d.index,width:rendered.width,height:rendered.height,textNodes:rendered.textNodes,svg:'rendered/'+stem+'.svg'};
        renders.push(row);
        if((d.file==='diagrams/D01-system-architecture.md'||d.file==='diagrams/D15-shotgun-target.md'||d.file==='diagrams/D11-office-scene-sync.md')&&d.index===1)await page.screenshot({path:path.join(__dirname,'rendered',stem+'.png'),fullPage:true});
      }catch(e){errors.push({file:d.file,index:d.index,error:String(e)});}
    }
    const report={checkedAt:new Date().toISOString(),documents:files.length,documentPaths:files,localLinks:linkRows.length,mermaidBlocks:diagrams.length,rendered:renders.length,engine,errors,renders};
    fs.writeFileSync(path.join(__dirname,'validation.json'),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify({...report,renders:undefined,documentPaths:undefined},null,2));
    process.exitCode=errors.length?1:0;
  }finally{await browser?.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
