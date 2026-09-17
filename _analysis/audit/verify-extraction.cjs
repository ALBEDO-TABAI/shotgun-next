const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const base = path.resolve(__dirname, '..');
const acorn = {};
new Function('exports', 'module', process.binding('natives')['internal/deps/acorn/acorn/dist/acorn'])(acorn, {exports: acorn});
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const results=[];
for(const name of ['neo-agent','neo-intelligence']) {
  const binary=fs.readFileSync(path.join(base,'app-copy/Matrix.app/Contents/Resources',name));
  if(binary.readUInt32LE(0)!==0xfeedfacf) throw new Error('Expected thin little-endian Mach-O arm64');
  let offset=32, section;
  for(let i=0;i<binary.readUInt32LE(16);i++) {
    const cmd=binary.readUInt32LE(offset),size=binary.readUInt32LE(offset+4);
    if(cmd===0x19) for(let j=0;j<binary.readUInt32LE(offset+64);j++) {
      const p=offset+72+j*80;
      const sectname=binary.subarray(p,p+16).toString().replace(/\0.*$/s,'');
      const segname=binary.subarray(p+16,p+32).toString().replace(/\0.*$/s,'');
      if(/bun/i.test(sectname+' '+segname)) section={sectname,segname,offset:binary.readUInt32LE(p+48),size:Number(binary.readBigUInt64LE(p+40))};
    }
    offset+=size;
  }
  if(!section) throw new Error('Missing Bun section: '+name);
  const raw=binary.subarray(section.offset,section.offset+section.size);
  const saved=fs.readFileSync(path.join(base,'extracted',name+'.bun'));
  if(!raw.equals(saved)) throw new Error('Bun section differs from saved extraction');
  const start=raw.indexOf(Buffer.from('#!/usr/bin/env bun'));
  const end=raw.indexOf(0,start);
  if(start<0||end<0) throw new Error('Cannot locate bounded JS entry');
  const clean=new TextDecoder('utf8',{fatal:true}).decode(raw.subarray(start,end));
  const cleanTree=acorn.parse(clean,{ecmaVersion:'latest',sourceType:'module'});
  const formatted=fs.readFileSync(path.join(base,'extracted',name+'.fmt.js'),'utf8');
  const formattedTree=acorn.parse(formatted,{ecmaVersion:'latest',sourceType:'module'});
  function normalized(node) {
    if(!node || typeof node!=='object') return typeof node==='bigint'?String(node):node;
    if(node.type==='BlockStatement' && node.body.length===1) return normalized(node.body[0]);
    if(node.type==='TemplateLiteral' && node.expressions.length===0) return {type:'Literal',value:node.quasis[0].value.cooked};
    if(Array.isArray(node)) return node.filter(n=>n?.type!=='EmptyStatement').map(normalized);
    const result={};
    for(const key of Object.keys(node).sort()) {
      if(['start','end','raw'].includes(key)) continue;
      result[key]=normalized(node[key]);
      if(node.type==='ImportDeclaration' && key==='specifiers') result[key].sort((a,b)=>a.local.name.localeCompare(b.local.name));
    }
    return result;
  }
  const cleanAstSha256=sha(JSON.stringify(normalized(cleanTree)));
  const formattedAstSha256=sha(JSON.stringify(normalized(formattedTree)));
  function fingerprint(source) {
    const h=crypto.createHash('sha256'); let count=0;
    for(const token of acorn.tokenizer(source,{ecmaVersion:'latest',sourceType:'module'})) {
      // Formatting may insert semicolons and trailing commas. Compare significant lexical values.
      if([';',','].includes(token.type.label)) continue;
      h.update(JSON.stringify([token.type.label,token.value],(_,v)=>typeof v==='bigint'?String(v):v)+'\n');count++;
    }
    return {sha256:h.digest('hex'),count};
  }
  const originalTokens=fingerprint(clean),formattedTokens=fingerprint(formatted);
  fs.writeFileSync(path.join(__dirname,name+'.clean.js'),clean);
  results.push({name,section,sectionSha256:sha(raw),jsByteRange:[start,end],cleanSha256:sha(Buffer.from(clean)),parse:true,originalTokens,formattedTokens,lexicalEquivalent:originalTokens.sha256===formattedTokens.sha256,cleanAstSha256,formattedAstSha256,normalizedAstEquivalent:cleanAstSha256===formattedAstSha256,limitation:'AST comparison normalizes import-specifier order, single-statement blocks, empty statements and expression-free templates. Formatting integrity only, not runtime behavior proof.'});
}
fs.writeFileSync(path.join(__dirname,'extraction-validation.json'),JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(results,null,2));
