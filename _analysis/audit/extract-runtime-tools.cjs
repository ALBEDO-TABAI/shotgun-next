// Recover tool object locations and their exact schema expressions without executing runtime code.
const fs=require('node:fs'),path=require('node:path');
const base=path.resolve(__dirname,'..'),a={};
new Function('exports','module',process.binding('natives')['internal/deps/acorn/acorn/dist/acorn'])(a,{exports:a});
const source=fs.readFileSync(path.join(base,'extracted/neo-intelligence.fmt.js'),'utf8');
const ast=a.parse(source,{ecmaVersion:'latest',sourceType:'module',locations:true});
const wanted=new Set(['Agent','TaskOutput','Bash','Glob','Grep','ExitPlanMode','Read','Edit','Write','WebFetch','TodoWrite','WebSearch','TaskStop','AskUserQuestion','Skill','EnterPlanMode','SendMessage','EnterWorktree','ExitWorktree','TeamCreate','TeamDelete','TaskCreate','TaskGet','TaskUpdate','TaskList','ToolSearch','LSP','Monitor','PowerShell']);
const literals=new Map(),bindings=new Map(),objects=[];
function walk(n){
  if(!n||typeof n!=='object'||!n.type)return;
  let key,value;
  if(n.type==='VariableDeclarator'){key=n.id.name;value=n.init;}
  if(n.type==='AssignmentExpression'){key=n.left.name;value=n.right;}
  if(n.type==='FunctionDeclaration'){key=n.id.name;value=n;}
  if(key&&value){if(!bindings.has(key))bindings.set(key,[]);bindings.get(key).push(value);if(value.type==='Literal'&&wanted.has(value.value))literals.set(key,value.value);}
  if(n.type==='ObjectExpression')objects.push(n);
  for(const[k,v]of Object.entries(n)){if(k==='loc')continue;if(Array.isArray(v))v.forEach(walk);else if(v&&typeof v==='object')walk(v);}
}
walk(ast);
const prop=(n,key)=>n.properties.find(p=>p.type==='Property'&&(p.key.name||p.key.value)===key);
const snippet=n=>({start:n.loc.start.line,end:n.loc.end.line,expression:source.slice(n.start,n.end)});
const rows=[];
for(const n of objects){
  const p=prop(n,'name'),schema=prop(n,'inputSchema');
  if(!p||!schema)continue;
  const name=p.value.type==='Literal'?p.value.value:literals.get(p.value.name);
  if(!wanted.has(name))continue;
  const expression=source.slice(schema.start,schema.end),dependencies=[];
  for(const key of new Set(expression.match(/\b[A-Za-z_$][\w$]*\b/g)||[])){
    const candidates=bindings.get(key)||[];
    for(const candidate of candidates)if(candidate.end-candidate.start<16000)dependencies.push({name:key,...snippet(candidate)});
  }
  rows.push({name,objectStart:n.loc.start.line,objectEnd:n.loc.end.line,inputSchema:snippet(schema),outputSchema:prop(n,'outputSchema')?snippet(prop(n,'outputSchema')):null,isEnabled:prop(n,'isEnabled')?snippet(prop(n,'isEnabled')):null,dependencies});
}
const result={source:'_analysis/extracted/neo-intelligence.fmt.js',configuredNames:[...wanted],foundNames:[...new Set(rows.map(x=>x.name))],missing:[...wanted].filter(n=>!rows.some(r=>r.name===n)),tools:rows};
fs.writeFileSync(path.join(__dirname,'runtime-tools.json'),JSON.stringify(result,null,2)+'\n');
let md='# Built-in Runtime Tool Evidence\n\nExact getter expressions and nearby binding candidates, statically recovered. Minified names are scoped; dependency candidates are not an evaluated JSON Schema. Configuration, isEnabled checks, platform, subscription and runtime conditions still determine availability.\n\n';
for(const r of rows){md+=`## ${r.name}\n\n[Tool object, line ${r.objectStart}](../extracted/neo-intelligence.fmt.js#L${r.objectStart})\n\n\`\`\`js\n${r.inputSchema.expression}\n\`\`\`\n\n`;for(const d of r.dependencies)md+=`Binding candidate \`${d.name}\`, [line ${d.start}](../extracted/neo-intelligence.fmt.js#L${d.start}):\n\n\`\`\`js\n${d.expression}\n\`\`\`\n\n`;}
md+='\nUnresolved configured names: '+(result.missing.join(', ')||'none')+'.\n';
fs.writeFileSync(path.join(__dirname,'runtime-tools-reference.md'),md);
console.log(JSON.stringify({found:result.foundNames.length,objects:rows.length,missing:result.missing},null,2));
