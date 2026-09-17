# Raw Extraction

Evidence base for the dossier. Everything here is derived from `/Applications/Matrix.app` and
the live runtime state on this machine.

```
_analysis/
├── app-copy/Matrix.app/          verbatim copy of the installed bundle (894 MB)
├── extracted/
│   ├── neo-agent.bun             raw __BUN Mach-O section (4.8 MB)
│   ├── neo-agent.js              original carving, includes invalid binary trailer; do not execute
│   ├── neo-agent.fmt.js          formatted bundled JavaScript, 153 126 lines
│   ├── neo-intelligence.bun      raw section (17.6 MB)
│   ├── neo-intelligence.js       original carving, includes invalid binary trailer; do not execute
│   ├── neo-intelligence.fmt.js   ← beautified — the agent runtime's recovered bundle (minified identifiers)
│   ├── matrix-browser-server.bun small loader section (16 KB)
│   └── mcp_tools_raw.txt         all 27 MCP tool definitions, extracted
└── swift/
    ├── type_descriptors.txt      4 918 mangled nominal type descriptors
    ├── types_demangled.txt       demangled
    ├── all_types.txt             3 756 distinct top-level Matrix types
    └── types_by_file.txt         private-discriminator groups + PUBLIC bucket; not a file census
```

## Reading the extraction

| Want | Look at |
|---|---|
| the daemon's architecture | `extracted/neo-agent.fmt.js` — **not minified**; module names, function names and full prompt text survive |
| the initializer map | [audit/module-initializers.json](audit/module-initializers.json) → 417 named wrappers, including dependencies; declaration order does not prove execution order |
| prompts | `grep -n 'You are the' neo-agent.fmt.js`; `buildDepartmentPromptContext` at line ~129987 |
| MCP tools | `extracted/mcp_tools_raw.txt`, or `grep -n 'createSdkMcpServer' neo-agent.fmt.js` |
| the agent runtime's tools | `neo-intelligence.fmt.js` — minified identifiers, but **all strings and tool descriptions intact**; grep for prose |
| the UI structure | `swift/types_by_file.txt` — symbol groups; type names suggest responsibilities, not implementation or exact layout |
| seed prompts & skills | `app-copy/.../Resources/neo-agent-seed/` (plain files) |
| the browser stack | `app-copy/.../Resources/matrix-browser/` (plain Node tree) |

## Reproducing

Full command sequence: [`../docs/10-build-and-packaging.md`](../docs/10-build-and-packaging.md#5-reproducing-this-teardown).

## Live runtime state (not copied here)

Read-only references used in the dossier, on this machine only:

```
~/.neo/config.json                                    workspace registry
~/.neo/workspaces/<ws>/{config,okr,dashboard}.json    real company state
~/.neo/workspaces/<ws>/departments/<id>/tasks/*.md    real Task packets
~/.neo/workspaces/<ws>/department-messages/messages.sqlite   the bus
~/.neo/daemon/status.json                             liveness
~/Library/Application Support/Matrix/agent_minds.*.json      persona state
~/Library/Preferences/com.matrixai.app.plist          UI restoration keys
```

## Caveats

- `neo-intelligence` identifiers are mangled; type names in that bundle are inferred from strings
  and call sites, not from symbols.
- Swift private discriminators provide grouping clues; the PUBLIC bucket spans many files. The total source-file count and file names are not recovered.
- Network protocol details beyond the bundled code (the Matrix Gateway's own API) are out of
  scope; only the client side is observable here.

## Audit Outputs

`audit/inventory.json` records hashes of key copied and installed artifacts (all compared key files matched at audit time). This is not a byte-for-byte certification of every bundle file.
Fourth-pass artifacts recovered from `strings -n 6 app-copy/Matrix.app/Contents/MacOS/Matrix`: `audit/swift-source-files.txt` (255 first-party `Matrix/*.swift` names leaked through `#fileID` literals — a lower bound), `audit/client-env-keys.txt` (98 `NEO_*`/`MATRIX_*` keys the client reads), and `audit/gateway-surface.md` (every `/v1/*`, `/api/*` and `/sync/*` path literal in the client and daemon, with hosts). Swift field metadata (`__swift5_fieldmd`) also survives in the string table in declaration order; `docs/08` §2.1 uses it for the renderer.
`audit/verify-extraction.cjs` locates Mach-O sections from their load commands, bounds each JS entry before the NUL-terminated module table, parses it, and compares normalized syntax trees with the formatted files. The clean entries and the comparison report are under `audit/`.
`audit/original-documents.tar.gz` preserves the pre-audit dossier. No live credentials or message records were added to this audit.
