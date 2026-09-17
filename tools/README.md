# Tool Specifications

Human-readable summaries of tool surfaces. These pages abbreviate schemas and descriptions; they are not verbatim or complete validators. The [exact MCP source expressions](../_analysis/audit/mcp-reference.md) contain all 27 literal daemon tool definitions (23 core plus two provider factory pairs), helper schemas and handler locations. Browser definitions are recorded [separately](../_analysis/audit/browser-tool-definitions.json). Built-in runtime tool coverage and its limits are in [M31](../modules/M31-neo-intelligence-runtime.md).

## Tool inventory

### MCP servers mounted per department session

| Server | Tools | Always loaded | Spec |
|---|---|---|---|
| `matrix` | `department` (13 canonical actions) | yes | [T01](T01-mcp-matrix-department.md) |
| `okr` | `state` (9 actions + aliases) | yes | [T02](T02-mcp-okr-state.md) |
| `cron` | `state` (4 actions) | yes | [T03](T03-mcp-cron-state.md) |
| `files` | `provenance` (6 actions) | yes | [T04](T04-mcp-files-provenance.md) |
| `media` | 7 tools | yes | [T05](T05-mcp-media.md) |
| `receivable` | 12 tools | — | [T06](T06-mcp-receivable.md) |
| `matrix-browser` | 2 tools | yes (if plugin enabled) | [T07](T07-mcp-matrix-browser.md) |
| `cloudflare` / `<provider>` packs | `search`, `execute` | per connection | [T08](T08-mcp-provider-packs.md) |

### Built-in agent tools

| Group | Tools | Spec |
|---|---|---|
| Department lead built-ins | 29 tools | [T09](T09-builtin-agent-tools.md) |
| Disallowed (daemon-managed) | `CronCreate`, `CronDelete`, `CronList` | [T09](T09-builtin-agent-tools.md#disallowed) |

### Managed skills (tool-like capabilities)

| Skill | Spec |
|---|---|
| `okr-execution`, `department-management`, `workspace-planning`, `skill-creator`, `find-skills`, `media-generation`, `email`, `debug-and-report`, `matrix-browser` | [T10](T10-managed-skills.md) |

---

## Cross-cutting conventions worth copying

These patterns occur in selected tools. They are not universal guarantees, and no comparative malformed-call rate was measured.

### 1. One tool, many actions

Rather than 13 tools, `mcp__matrix__department` is one tool with an `action` enum. Fewer tools in
context, one schema to learn, and permissions gate the *action list* rather than the tool list.

### 2. Field relevance is declared per action

```ts
ACTION_RELEVANT_ARG_KEYS = {
  "message.send":  ["action","toDepartment","topic","message","attachments","kind","outcome","messageId"],
  "message.reply": ["action","messageId","kind","message","outcome","attachments"],
  "message.queue": ["action","department","limit"],
  …
}
```

`normalizeMatrixWorkspaceArgs()` **deletes every field not relevant to the action** before
handling. Hallucinated extras simply vanish instead of causing a validation error.

### 3. Placeholder rejection

```ts
PLACEHOLDER_STRING_VALUES = { "placeholder","x","n/a","na","none","null","undefined","unknown" }
EMPTY_STRING_IS_ABSENT_KEYS = [department,toDepartment,messageId,includeBodyFor,sessionId,
                               query,topic,name,description,confirmDepartmentId,parentDepartmentId]
```

Empty strings and placeholder values are treated as **absent**, not as data. Every optional field
description ends with: *"Omit this field instead of using an empty string or placeholder."*

### 4. Unknown-field rejection with a teaching message

```ts
validateKnownMatrixWorkspaceArgs(args) →
  "unsupported field(s): foo, bar"  +  next: "Use only the documented fields for <action>."
```

### 5. Department Results Carry A `next` Hint

```ts
ok(action, payload, next)   → { ok:true,  action, …, next }
fail(action, error, next)   → { ok:false, action, error, next }
```

Real examples:

- `message.send` → *"Message persisted. … A business result only exists after `message.reply`
  `kind="reply"` with outcome. For substantial deliverables, write a Markdown file in the shared
  workspace and send a concise summary plus its path in attachments."*
- `message.queue` → *"Queue entries are stored messages, **not proof that work was completed**."*
- `user_profile.get` → *"Use `user_profile.update` with `expectedVersion` only for stable
  cross-workspace preferences; project/workspace facts belong in belief cards or OKR."*
- `user_profile.update` → *"On conflict, read the current profile and retry with a merged version
  **only if the change is still valid**."*

The `next` field provides recovery guidance on this surface. Media, receivable and provider tools return different payloads, commonly wrapped in MCP `content`; clients must not require `next` on every tool result.

### 6. Action aliases

`state|get|read → state.get`, `task.create|task.update → task.upsert`,
`objective.patch → objective.state_patch`. The model's natural guesses are accepted rather than
punished.

### 7. `alwaysLoad` + `searchHint`

```ts
{ alwaysLoad: true,
  searchHint: "okr state objective key result task check in proof learning progress facts" }
```

Core tools stay in context; everything else is discoverable via `ToolSearch` against the hints.

### 8. Tool surface fingerprints

```
mcp__files__provenance:always-load:department-scope:lineage:import-origin:access-rollups@5
```

Each MCP server declares a versioned capability string used for cache invalidation and
diagnostics. Copy it — it makes "why is this agent behaving differently" answerable.
