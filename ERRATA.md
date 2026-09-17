# Errata — Verified Corrections

A second-pass review (prompted by an independent Codex review) found **14 substantive errors** in
the first draft of this dossier. Every item below was re-verified against the extracted code with
the evidence cited. Corrections have been applied to the affected documents. A **third pass**
(E15–E24, at the end of this file) then swept for residue and cross-document consistency.

**Root cause of most errors: I inferred behaviour from identifier names instead of reading the
code that consumes them.** The fix is methodological, not cosmetic — see
[Evidence grading](#evidence-grading) at the end.

---

## E1 · Hot-key semantics were inverted — CRITICAL

**I wrote:** `HOT_PROMPT_CONTEXT_QUERY_OPTION_KEYS` = the five fields whose change **restarts the
runtime**; everything else refreshes freely.

**Reality: exactly backwards.** They are the fields that can be **hot-updated in place, without a
restart**. "HOT" means hot-swappable.

`neo-agent.fmt.js:139947` — the set is used to **skip** keys when computing replacement reasons:

```js
for (const key4 of keys) {
  if (key4 === "env" || HOT_PROMPT_CONTEXT_QUERY_OPTION_KEYS.has(key4)) continue;  // ← skipped
  ...
  if (changed) reasons.push(`query_option:${key4}`);        // reasons ⇒ process replacement
}
```

`refreshPromptContext` (`:139970`) then branches: non-empty `replacementReasons` →
`applyProcessReplacementIntent` → `replaceQueryNow()`. Empty → `applyHotUpdateIntent` →
`await query.applyPromptContext(update)` — a **live, in-place update of the running process**
(`:140381`).

### What actually forces a process replacement

From `promptContextReplacementReasons` (`:139928`):

| Reason | Trigger |
|---|---|
| `env` | `resolveQueryEnv(...)` differs (stable-stringified) |
| `cwd` | `context.dir !== this.dir` |
| `mcp_server_surface` | server **names** or **fingerprints** differ (`mcpServerSpecsAreCompatible`, `:129117`) |
| `query_option:<key>` | any query option **not** in the hot set changed — `tools`, `disallowedTools`, `settings`, `extraArgs`, `includePartialMessages`, `thinking`, `fallbackModel`, `effort`, `serviceTier`, `hooks`… |

`stderr` and `spawnNeoCodeProcess` are special-cased: only **presence/absence** change counts,
not value.

### What survives

The static-prefix / volatile-tail split is still real, but for a **prompt-cache** reason, not a
process-restart reason — and that is the vendor's own stated rationale:

> "Department topology, OKR/task briefs, recent peer directives, and self-trace are live state.
> They are injected near the conversation tail by the runtime state snapshot path rather than
> baked into the cached prompt prefix."
> — `neo-agent-seed/templates/workspace-architecture.md`

So: churning `instructions` costs you the **cached prefix**, not a restart. The design conclusion
holds; my stated mechanism was wrong.

**Fixed in:** `docs/02` §3.3 · `docs/06` §1, §9 · `modules/M07` · `modules/M08` ·
`diagrams/D08` · `shotgun/05`

---

## E2 · The endpoint list mixed three layers and was incomplete

**I wrote:** ~230 endpoints, scraped from string literals.

**Reality:** the authoritative surface is the `Methods` object (`:30035`, **232 entries**),
dispatched by `switch (req.method)` inside the function returned by `createHandler`
(`:99707`+3880). Requests are `{ id, method, params }`.

### Wrong layer — these are not daemon methods

| I listed | What it actually is |
|---|---|
| `cloudflare.accounts.list`, `cloudflare.dns.records.*`, `cloudflare.zones.list`, … | **provider-pack operation ids** in the Cloudflare MCP catalog (`:4864`, `:86360`) |
| `okr.state` | the **MCP tool** `mcp__okr__state` |
| `objective.state_patch`, `key_result.state_patch` | **MCP actions**, not RPC methods (daemon has `objective.create/update/delete`) |
| `department.get` | MCP action; the daemon method is `department.config.get` |

### Whole families I missed

```
wechat.configure · wechat.connect · wechat.status · wechat.sign_out · wechat.stop
userProfile.get · userProfile.update · userProfile.discover · userProfile.discovery.cancel
workspace.fs.importDirectory.begin/chunk/commit/abort
workspace.activationChecklist.get/completeTask/markEmailGreetingSent
workspace.onboardingDraft.create/update/discard/finalize
workspace.blueprint.suggestOptions · workspace.dispatchOnboardingOpening
workspace.runtimeOnboarding.apply · workspace.prepareAcquisitionHandover
department.prepareMarketplaceHandoff
workspace.fs.departmentAssociations(.confirm) · workspace.fs.workerConflicts(.resolve)
workspace.fs.readBinary
wallet.link.get · wallet.link.configure
matrixBrowser.userProfileProcess.open · media.characterAsset.register
trace.list · transcript.explain · wake.history · ping · pool.metrics
```

### Naming

Several families are **camelCase**, which I uniformly wrote as snake_case:
`userProfile.*`, `workspace.fs.importDirectory.*`, `workspace.activationChecklist.completeTask`,
`workspace.onboardingDraft.*`, `department.prepareMarketplaceHandoff`,
`matrixBrowser.userProfileProcess.open`, `media.characterAsset.register`.

### Also undocumented: a real authorization layer

```js
if (SHUTDOWN_GATED_METHODS.has(req.method) && deps.isShuttingDown?.()) → "daemon_shutting_down"
if (WORKSPACE_SCOPED_METHODS.has(req.method) && !workspace)            → "missing workspace"
if (workspaceAuthz) {
  caller = callerFromActorParam(p._actor);
  assertWorkspaceGlobalMethodAction(caller, req.method);
  accessGuard.assertAccess(caller, workspace);
  assertWorkspaceMethodAction(caller, workspace, req.method);
}
```

`EnforcingWorkspaceAccessGuard` vs `defaultWorkspaceAccessGuard`, gated by
`workspaceAuthzEnabled(process.env)`. I omitted this entirely.

**Fixed in:** `docs/05` (rewritten against `Methods`) · `diagrams/D12`

---

## E3 · Media tool schemas were wrong — documented calls would fail

`neo-agent.fmt.js:128662`:

```ts
workRunSchema = z.object({
  id:         z.string().trim().min(1),          // REQUIRED
  title:      z.string().trim().min(1).optional(),
  itemId:     z.string().trim().min(1).optional(),
  totalItems: z.number().int().positive().optional(),
}).optional()

asyncSchema = z.object({
  mode:            z.enum(["async","sync"]).optional()
                    .describe("Default async: create a Matrix hook and return immediately."),
  timeoutSec:      z.number().int().positive().optional(),
  pollIntervalSec: z.number().int().positive().optional(),
}).optional()
```

**I wrote** `workRun?: WorkRun // {taskId, keyResultId?, …}` and treated `async` as a flag. Both
are wrong: `workRun.id` is required and there is no `taskId`/`keyResultId`; `async` is an object
whose `mode` selects behaviour.

Also: `mediaSourceSchema.type` is `"path" | "url" | "asset_uri"` (three values) — I documented
only two for `videoReferenceSchema.source`. `mediaFileSourceSchema` is the two-value one.

**Fixed in:** `tools/T05` · `shotgun/04`

---

## E4 · Cloud sync "field-level merge" was fabricated

**I wrote:** per-domain snapshot modules with field-level merge; append-only structures
"merge without conflict by construction".

**Reality (`:41700`–`41811`):** every `apply*Snapshot` is a whole-file byte comparison.

```js
if (existing === parsed.body) return { status: "applied", reason: "already_current" };
if (existing !== null) {
  await writeSyncConflict(workspaceRoot, op, "<kind>_exists_with_different_content", now, {...});
  return { status: "conflict", reason: "<kind>_exists_with_different_content" };
}
await atomicWrite2(targetPath, parsed.body);
```

There is **no merge anywhere**. Any pre-existing file with different bytes → conflict record.
Conflict reasons are enumerable: `invalid_*_payload`, `*_exists_with_different_content`,
`department_message_parent_missing`. The snapshot modules are **serializers**, not mergers.

I inferred a CRDT-ish design from module names (`apply`/`pull`/`push`/`resolve`/`*_snapshot`).
That was invention.

**Fixed in:** `modules/M26` (rewritten)

---

## E5 · WeChat credentials are **not** encrypted at rest

**I wrote:** "Crypto imports (`createCipheriv`/`createDecipheriv`) indicate credentials are
encrypted at rest."

**Reality:** `saveState()` (`:145067`) writes credentials as plaintext:

```js
await writeStoredState({ credentials: this.credentials, route, shouldReconnect,
                         controlGuidePending, syncBuffer, contextTokens });
// → JSON.stringify(state, null, 2) → ~/.neo/wechat-channel.json
```

Verified on disk: `-rw-r--r--` (**0644**, world-readable), plain JSON.

The AES code is unrelated: `aes128EcbEncrypt/Decrypt` (`:145616`) with `parseAESKey` throwing
*"Invalid WeChat media encryption key"* — it decrypts **WeChat media payloads**, not stored
credentials.

This was inference from an `import` statement. Bad method, wrong conclusion.

**Fixed in:** `modules/M24` · `docs/09`

---

## E6 · `/.neo/**` is an **allow** scope, not a block

**I wrote:** "`/.neo/**` and `~/.neo/**` are explicitly protected from the Edit tool."

**Reality (`neo-intelligence.fmt.js:493128`):** they are allow-rule patterns for the
`neo-folder` / `global-neo-folder` permission scopes — i.e. the "always allow edits in the .neo
folder" affordance:

```js
let V = q.scope === "global-neo-folder" ? v16 : S16,
    H = [{ type:"addRules", rules:[{ toolName: a1 /* Edit */, ruleContent: V }],
           behavior: "allow", destination: "session" }];
```

`:467193` likewise returns `{ behavior: "allow" }` for rules matching those prefixes. The polarity
is the opposite of what I claimed.

**Fixed in:** `docs/09` · `docs/02` §9 · `modules/M16`

---

## E7 · `deniedWrites` does not exist — and the real mechanism is narrower than I first concluded

My shotgun-next plan prescribed `settings.permissions.deniedWrites`. **That key appears zero
times** in either bundle. I invented an API. Codex caught this and replaced it with an enforced
process/storage boundary outside the SDK.

I then tried to "rescue" the prescription with `permissions.deny`. **Re-verification shows that
rescue only partly works, and Codex's stronger conclusion is the correct one.**

### What the settings schema documents **[V]** (`neo-intelligence.fmt.js:541129`)

```json
{ "permissions": {
    "allow": ["Bash(npm:*)", "Edit(.neo)", "Read"],
    "deny":  ["Bash(rm -rf:*)"],
    "ask":   ["Write(/etc/*)"],
    "defaultMode": "default"|"plan"|"acceptEdits"|"dontAsk",
    "additionalDirectories": ["/extra/dir"] } }
```

Rule syntax: exact `Bash(npm run test)`, prefix wildcard `Bash(git:*)`, tool-only `Read`.

### Deny does outrank `bypassPermissions` **[V]**

In `TWK` (`:441309`) the deny check runs first and returns before the mode check that would
otherwise auto-allow:

```js
let J = xT7(Z.toolPermissionContext, A7);
if (J) return { behavior: "deny", ... };                      // ← first
...
if (Q?.behavior === "deny") return Q;                         // tool checkPermissions deny
...
if (mode === "bypassPermissions") return { behavior: "allow", ... };   // ← last
```

### But the matchers ignore patterns **[V]**

`xT7` → `nGA` (deny rules) → matched by `KI0` (`:441147`), which **bails out on any patterned
rule**:

```js
function KI0(A7, q) {
  if (q.ruleValue.ruleContent !== undefined) return false;   // ← patterned rule: no match
  ...  // only tool-level names, incl. mcp__server__* wildcards
}
```

`lFK` (`:433633`, tool-list filtering) does the same: `if (_.ruleContent !== undefined) continue`.

I could find **no consumer that enforces a path-scoped deny pattern for `Write`/`Edit`.**

### Corrected conclusion

| Claim | Status |
|---|---|
| Blanket tool-level deny (`"deny": ["Write"]`) beats `bypassPermissions` | **[V]** enforced |
| Path-scoped deny (`"deny": ["Write(config.json)"]`) protects that file | **[U]** no enforcing consumer found — do not rely on it |
| `deniedWrites` | **does not exist** |

So protecting tool-owned state by path requires either **not granting the write tool to that
session at all**, or **an enforcement boundary outside the SDK** — which is exactly what Codex
prescribed in `shotgun/10-implementation-contracts.md`. My attempted rescue was itself
half-inferred; this entry records the narrower verified result.

**The underlying gap in Matrix is still real:** the daemon passes only
`settings: { permissions: { additionalDirectories: [...] } }` and never populates `deny`, so its
registry, OKR stores and task packets are protected by prompt text alone.

**Fixed in:** `docs/09` · `shotgun/05` §7 · `shotgun/09` · `shotgun/10`

---

## E8 · The destructive-write gate is a heuristic, not a hard boundary

I graded it "hard at tool boundary".

**Reality (`:125084`):** `hasRecentUserConfirmationForDestructiveWorkspaceDataOperation` scans the
last **12** chat messages for user text that `userTextExplicitlyConfirms(...)`, optionally looking
back 3 messages to see whether the assistant had asked. It **returns `false` if
`deps.readDepartmentChat` is absent**, and `DESTRUCTIVE_WORKSPACE_CONFIRMATION_NEXT` is a *prompt
string* instructing the model to ask.

It is a chat-text heuristic on the OKR/department tool paths only — not a filesystem protection,
and not a hard gate.

**Fixed in:** `docs/09` (regraded) · `modules/M04`

---

## E9 · WS authentication was overstated — and the real default is weaker

**I wrote:** "Auth: owner lease (`ownerMode: swift_child`) or `NEO_OWNER_TOKEN` bearer."

**Reality (`:110629`, `:150792`):**

```js
const wsAuthToken = opts.wsAuthToken;              // ← NEO_DAEMON_WS_TOKEN, not NEO_OWNER_TOKEN
if (wsAuthToken) { /* require x-neo-daemon-token header or ?daemon_token= */ }
// when unset: no authentication at all
```

Origin check (`isAllowedOrigin`) returns **`true` for a missing Origin header**, and allows
`matrix:`/`transcript:` schemes plus loopback hosts.

`NEO_DAEMON_WS_TOKEN` does not appear in the app binary's strings, and the daemon contract's env
list does not include it. **Evidence therefore indicates that in the shipped desktop
configuration the WebSocket API is unauthenticated**, protected only by loopback binding — so any
local process can drive the daemon. That is a more significant finding than what I originally
wrote, and it belongs in the security section.

**Fourth pass (R1) closed the remaining [U]:** the client binary also lacks the
`x-neo-daemon-token` header and `daemon_token` query names — the only credential channels the
daemon accepts — and its recovered spawn arguments carry no token. Unauthenticated loopback is
the shipped default, **[V]**.

**Fixed in:** `docs/05` §1 · `docs/09`

---

## E10 · The sidebar is not a fixed 288 pt

I cherry-picked the 288-wide entries from the persisted `NSSplitView` frames. The full
distribution in `com.matrixai.app.plist`:

```
 27 × 280.0     11 × 288.0     1 × 255.0     1 × 238.0
```

It is a **resizable** sidebar; observed widths span ~238–288, with 280 most common.

**Fixed in:** `docs/07` §1 · `diagrams/D10` · `shotgun/06`

---

## E11 · Render pass order and frame rate were unverified

I presented a specific pass order (shadow → opaque → SSAO → TAA → bloom → exposure → reflections
→ composite) and "60 fps". Neither is established by the evidence — I had **shader entry-point
names only** (`default.metallib` strings), which prove the passes *exist*, not their order, and
say nothing about frame rate.

The shader inventory, adaptive-load constants and cache keys stand. The ordering diagram is now
marked as inferred, and the frame-rate claim is removed.

**Fourth pass (R2, R3):** the renderer's stored-property metadata was recovered from the main
binary, which fixes the texture data-flow between passes (so the order is now *constrained*,
not guessed) and shows the frame rate is a runtime variable (`targetFPS`,
`dynamicResolutionScale`) on a **demand-driven render loop** with an explicit idle pause. "60
fps" was not just unverified — it is the wrong model.

**Fixed in:** `docs/08` §2 · `diagrams/D11` · `modules/M29`

---

## E12 · Multiplayer voice capability overstated

I wrote that "multiplayer visitors can join your office over LiveKit and you can hold a voice
conversation with a department."

**What is actually established:** `LiveKitWebRTC.framework` + `RustLiveKitUniFFI.framework` are
bundled and the main binary carries **36 909 LiveKit symbols**; `OfficeLiveVisitorSceneBanner`,
`OfficeVisitorSnapshot`, `RenderableVisitor`, `ProjectedVisitorBadge/Bubble` exist; presence
methods (`focus.broadcast`, `activity.broadcast`) exist.

**What is not established:** that the feature is enabled or reachable in this build.
`MATRIX_ELEVENLABS_AGENT_ID` and `MATRIX_ELEVENLABS_ENVIRONMENT` are **empty strings** in
`Info.plist`. Linked code ≠ shipped feature.

**Fourth pass (R4, R5) narrowed this further.** The transport attribution was also wrong:
LiveKit's only identifiable consumer in the client is the **ElevenLabs Conversational-AI SDK**
(its `WebRTCConnectionManager` declares `LiveKitRoomEventDelegate`), i.e. the one-to-one voice
path. The multiplayer "live workspace" record (`WorkspaceLiveRoom`) carries Supabase Storage
fields and an `inviteURL`, no LiveKit `serverUrl`/`participantToken`; the join path is a
`matrix://live/join/<token>` deep link that requires sign-in, and the client ships the string
*"Live workspaces are unavailable in this build."* behind a remote release gate. See
`docs/08` §7.

**Fixed in:** `docs/08` §7 · `modules/M30`

---

## E13 · "Source" framing was too strong

`neo-agent.fmt.js` is **recovered bundler output**, reformatted — not original source. It retains
module names, function names and full prompt text, which makes it unusually legible, but it is
not the repository. `neo-intelligence.fmt.js` is additionally **minified**: identifiers are
mangled, so any type or function name I attributed there is inferred from strings and call sites.

`_analysis/README.md` labelled it "THE DAEMON SOURCE". Corrected throughout to "recovered bundle".

---

## E14 · Contradictory permission rules in the shotgun-next plan

Two invariants I wrote conflict:

- *"A seat cannot mutate a peer's state"* (`shotgun/04`, inherited from Matrix's
  `resolveTargetRole`)
- *"A maker cannot accept its own work — gate reviews require `authorRoleId == Critic`"*

The Critic must write `item.review` on **items owned by other roles**, which the first rule
forbids. The plan never said who may submit, review, or finally approve.

**Resolution — an explicit rights matrix, now in [`shotgun/02` §9](shotgun/02-role-system.md#9-rights-matrix-resolves-errata-e14)
and mirrored in [`shotgun/10`](shotgun/10-implementation-contracts.md):**

| Action | Owner | Assigned Critic | Director | Human user | Other role |
|---|---|---|---|---|---|
| `item.upsert` (own item, non-terminal status) | ✅ | — | ✅ own seat | — | — |
| set `review_pending` (submit) | ✅ | — | ✅ own seat | — | — |
| `quality` review on a **peer's** assigned item | ❌ | ✅ append-only | ❌ | — | ❌ |
| `quality` review on **own** item | ❌ | n/a | ❌ | — | ❌ |
| `user_acceptance` → final `accepted` / `rejected` | ❌ | ❌ | ❌ | ✅ exact `reviewedRevisionId` | ❌ |
| `control` record → `blocked` / `cancelled` | ✅ own | ❌ | ✅ own | ✅ | ❌ |
| `milestone.state_patch` | ✅ own | ❌ | ✅ own | — | ❌ |
| Brief create / update / state_patch | ❌ | ❌ | ✅ | ✅ meaning changes | ❌ |

Rule: **write access follows ownership; verdict access follows a stable ID (`criticRoleId`),
and final acceptance follows the authenticated human.** Actor identity is derived by the daemon
from the session, never read from an `authorRoleId` argument. A Critic `accept` leaves the item
in `review_pending`; the human's acceptance on the same revision moves it to `accepted`. (An
earlier version of this table let the Critic or Director write final `accepted`; that
contradicted `shotgun/10` and is withdrawn — see E24.)

---

## Third pass (2026-09-17) — consistency and residue

A third pass re-checked every document against the extracted bundle and against each other. It
found no new inverted mechanisms, but **ten residue / consistency errors** (E15–E24), mostly
places where an earlier correction was applied to one file and not its neighbours.

## E15 · Surface count and "60 fps" residue in `docs/07`

`docs/07` opened with "the eight surfaces" while `docs/01`, `M27` and `D10` count seven detail
surfaces (Chat, Work, Dashboard, Files, Terminal, Office, Agent Space) plus the Memory/Skills
catalog and Settings. Its rendering-strategy table still said "60 fps 3D" after E11 removed the
claim elsewhere. Both fixed.

## E16 · "Forced verification pass" retained after being disproved

`T09` §Built-in agent types already recorded that `verificationNudgeNeeded` is `false` in the
inspected `TodoWrite` / `TaskUpdate` producers (`neo-intelligence.fmt.js:337411`, `:396757`), yet
the same file's shotgun-next section told the reader to keep "the forced verification pass" and
called `verification` a type "the runtime can force". Reworded: the Critic gate is **new
enforcement**, not an inherited invariant (`shotgun/09` D6).

## E17 · Managed-skill count and frontmatter table

- `00-EXECUTIVE-SUMMARY` said "11 managed skills"; the seed has **9** `SKILL.md` templates, 2
  companion reference files and 1 legacy template (12 files). Fixed; `T10` now explains the
  split.
- `T10`'s table showed `—` for `seedVersion` / `category` / `symbolName` on `find-skills` (2 /
  development / `sparkle.magnifyingglass`), `media-generation` (13 / automation /
  `photo.on.rectangle.angled`, `allowed-tools: Read + 7 mcp__media__*`) and `skill-creator`
  (3 / development / `hammer.fill`). Filled from the frontmatter.
- `T10` quoted the `okr-execution` description's "vanish when the session ends" without the
  caveat that `TaskCreate/Get/Update/List` persist to `tasks/<listId>/<id>.json`
  (`neo-intelligence.fmt.js:203232`), which `T09` and `M05` already state. Caveat added.

## E18 · Shader entry points: 28 → 32

`strings default.metallib | grep -E '^(office|city|farm)_[a-z_]+$' | sort -u` returns **32**
names. `docs/08` §2.1 listed 28 and omitted `office_fragment_legacy`,
`office_mesh_fragment_legacy`, `office_mesh_vertex_instanced`,
`office_mesh_shadow_vertex_instanced`. Count corrected in `docs/08`, `docs/10`, `M29`,
`shotgun/09` D9.

## E19 · SPM resource bundles: 13 → 10

`ls Contents/Resources | grep '\.bundle$'` lists exactly ten. `docs/10` said 13 in the tree and
then named ten in §1.1. Tree fixed; frameworks (Ghostty, Sparkle, LiveKitWebRTC,
RustLiveKitUniFFI) noted as not being resource bundles.

## E20 · Stale counts in the executive summary and `D01`

After E2 established 232 methods / 41 events and 417 *named initializers*, the executive summary
and `D01` still said "~230 endpoints" and "417 modules". Also "CloakBrowser 237 MB": `du -sh`
of `Matrix Browser.app` is **351 MB**; ~237 MB is the Chromium framework alone. All three fixed.

## E21 · Method / event names that do not exist in the registry

Checked against `_analysis/audit/protocol.json`:

| Written | Reality | Where |
|---|---|---|
| `config.credentials.*` | no such family; credentials go through `config.providers.set` + OAuth routes (`docs/05` already said so) | `M18` |
| `experimental.codex_subscription.status` | not a method; `codex.service.status` is, and `runtime.subscription_prompt` is the event | `M19` |
| `permission.respond` | `task.permission.respond` | `docs/02` §3 state diagram |
| `session.turn_failure` / `session.turn_stream_inactivity` "events" | not top-level events; they are `rawType` values inside `runtime.raw.event` (`neo-agent.fmt.js:139639`, `:139675`) | `docs/02` §3.2, `M07` |

## E22 · Prompt-surface fingerprints abbreviated; off-by-one line reference

`docs/06` §7 wrote `mcp__media__…:always-load@1` and
`mcp__matrix-browser__browser_task_message+browser_script_run:always-load@1`. The actual
`toolSurface` strings are the full forms recorded in `T05` / `T07`
(`mcp__matrix-browser__browser_task_message+mcp__matrix-browser__browser_script_run:always-load@1`);
the provider-pack form `mcp__<key>__search+mcp__<key>__execute:connected@1` was missing. Also
`promptContextReplacementReasons` is at line **139928**, not 139929. Fixed.

## E23 · shotgun-next vocabulary drift between files

- `T02` §9 mapped `learningDecision` to `ignore | proof-only | style-note | skill-update |
  next-item`; the canonical enum in `shotgun/03` §4 (used by `D15` and `shotgun/04`) is
  `ignore | deliverable-only | style-lock | memory-card | skill-update | next-item`, and
  `blockerCategory` also has `budget`. `T02` realigned.
- `T05` §7 typed `FileSource` as `path | url` only, though E3 had established that
  `videoReferenceSchema.source` accepts `path | url | asset_uri`. Comment added.
- `shotgun/04` §6 said mode exclusivity is "stated in prose because the schema can't express it";
  `T05` §4 already notes a replica can encode it with unions/refinements. Reworded.

## E24 · Build-schedule and rights-matrix references out of sync

- `shotgun/08` was rewritten to engineer-days (133–138), but `shotgun/README` and `D15` still
  showed the withdrawn 15-week plan. Both realigned.
- `shotgun/08`'s Gantt used `dateFormat X` with raw integers, which Mermaid renders as epoch
  seconds (an unreadable SVG). Replaced with day durations that match the phase tables.
- E14 said the rights matrix was "now in `shotgun/02` §9" — that section did not exist. Added,
  and E14's own table (which let the Critic/Director write final `accepted`) was brought in line
  with `shotgun/10`: final acceptance belongs to the authenticated human.

---

## Fourth pass (2026-09-17) — resolving [I] and [U]

Not errors: these are claims the dossier had honestly marked *inferred* or *unverifiable* and
which a replica would otherwise have had to re-derive or over-build. Two evidence sources that
the first three passes never used closed most of them:

- **The main binary's string table** (`strings -n 6 Contents/MacOS/Matrix`, 227 874 lines). It
  leaks 255 first-party `Matrix/*.swift` file names via `#fileID`, three absolute build paths,
  every `NEO_*`/`MATRIX_*` key the client reads, every gateway path literal, `os_log` format
  strings (`renderCensus …`, `officeRenderLoop wake reason=…`), and Swift field metadata in
  declaration order — which is how the renderer's texture chain was recovered.
- **The live `~/.neo/daemon/daemon.log`** (6.7 MB + 22 MB rotated): 15 recorded daemon starts
  in the current log, every one with the same ten-phase sequence and `authMode`.

| # | Was | Now | Where |
|---|---|---|---|
| **R1** | WS auth default **[U]** — "whether the launcher sets `NEO_DAEMON_WS_TOKEN` by another path is not determinable" | **[V]** unauthenticated loopback is the shipped default. The client binary contains neither the env key nor the only two credential channels the daemon reads (`x-neo-daemon-token`, `daemon_token`); its recovered spawn line is `daemon run --owner-pid --host=127.0.0.1 --owner-mode=swift_child --owner-lease-path`; 15/15 logged starts say `authMode: "loopback-bind"` | `docs/09` §1 · `docs/02` §1.1 · E9 |
| **R2** | Render pass order **[I]** from convention | **[I, constrained]** — pipeline-state and texture field names recovered in declaration order fix the data-flow shadow → geometry → SSAO → AO blur → composite → TAA → bloom → exposure → MetalFX → present; only bloom/TAA placement and exposure sample point remain open | `docs/08` §2.1 · `D11` |
| **R3** | Frame rate "not measured"; scene-sync NOOP "animation may still draw" | **[V]** demand-driven render loop (`singleFrame` / `continuous(duration)` / `idlePause`), `targetFPS` + `dynamicResolutionScale` are runtime variables, MetalFX `disabled/temporal/spatialFallback`, per-frame feature flags, built-in `office-render-baseline` capture | `docs/08` §2.1, §8 · `D11` · `docs/07` |
| **R4** | Voice provider **[U]** beyond "ElevenLabs intent" | **[V]** two providers selected by `NEO_/MATRIX_VOICE_PROVIDER`: ElevenLabs ConvAI (over its SDK's LiveKit transport, one client tool `call_neo_intelligence`) or OpenAI-style realtime through the gateway (`wss://matrix.agent.space/v1/realtime?model=gpt-realtime-2`) | `docs/08` §7.1 |
| **R5** | Multiplayer "over LiveKit", enablement **[U]** | **[V structure]** live workspaces = host-published scene descriptor + presence + shared whiteboard behind a revocable `matrix://live/join/<token>` deep link; requires sign-in; room record has Supabase Storage fields and no LiveKit token; gated by remote `MatrixReleaseGate`/`PublicConfig` with the shipped string *"Live workspaces are unavailable in this build."* Enablement per account stays **[U]** | `docs/08` §7.2 · E12 |
| **R6** | Cloud sync: "exact Swift conflict UI not established"; transport unstated | **[V]** op-log with Lamport clocks, `baseVersion`, 9 entity types (4 applied), outbox/inbox, `POST /sync/op-log`, `pull-cursor.json`; **master switch `MATRIX_SYNC_OUTBOX` is absent from the client's env keys → sync is off in the shipped app**; UI is `Matrix/WorkspaceCloudSyncPane.swift` + `HubSyncConflict*` DTOs | `M26` |
| **R7** | "Durable sequence-numbered replay not established" | **[V]** none exists: `EventJournal` is an in-memory `Map<streamId, event[]>`; broadcast frames carry no seq; recovery is by re-reading `chat.history`/`session.history` | `M01` |
| **R8** | Import validation coverage **[U]** | **[V]** structural only: path shape, ≤10 000 files/dirs, ≤2 GiB/file, ≤20 GiB total, 6 MiB chunks, duplicate/kind checks; **no** frontmatter, `allowed-tools`, signature or injection check | `M15` · `shotgun/09` D14 |
| **R9** | Persona (`agent_minds`) reaching a model "cannot be established" | **[V]** never: zero references in the daemon bundle, written by `Matrix/AgentMindService.swift` on the client only | `M29` |
| **R10** | Verifier nudge "not established as active" | **[V]** dead code: exactly two producers, both literal `false`, no other write site | `T09` · `shotgun/09` D6 · `shotgun/00` |
| **R11** | Hub DTO generation "unknown" | **[I, strong]** hand-written: no codegen marker, function-local `Ack` Codable structs with `CodingKeys`, custom `HubChannelValue.init(from:)`, single `Matrix/HubService.swift` | `M27` · `shotgun/01` · `shotgun/09` D2 |
| **R12** | Build pipeline, dependency set, account backend, gateway surface — unstated | **[V]** GitHub Actions macOS runner, monorepo `apps/hq/mac`; 16 third-party SwiftPM packages incl. **supabase-swift** (auth/storage/realtime, canonical host `forward.agent.space`) plus two in-house web-view packages; 32 client-only + 19 daemon-only + 13 shared gateway paths | `docs/10` §1.2 · `docs/05` · `_analysis/audit/gateway-surface.md` |

Also settled on the way: the VRM parser reads both 0.x and 1.0 structures and no third-party
glTF/VRM library is linked (`docs/08` §4.1); the daemon's ten startup phases and the fact that
the API socket opens *before* repairs/watchers/state hydration (`docs/02` §1.1); snapshot
publishing to `snapshot.matrix.build` needs `MATRIX_SNAPSHOT_PUBLISH_TOKEN` and is therefore a
developer path, not a user feature.

**Still [U] after this pass, and why:** everything server-side (gateway semantics, release-gate
values, marketplace Edge Function behaviour); whether live workspaces are enabled for a given
account; the exact bloom/TAA order. None of these change what a replica must build.

---

## Evidence grading

To prevent recurrence, every non-obvious claim in this dossier now carries a marker:

| Marker | Meaning |
|---|---|
| **[V]** | Verified — code read, with file:line |
| **[O]** | Observed — live artifact on this machine (file on disk, plist, sqlite) |
| **[I]** | Inferred — reasoned from names/structure; **not** confirmed by reading the consumer |
| **[U]** | Unverifiable from the bundle (e.g. server-side behaviour, whether a feature is enabled) |

The rule that would have prevented E1, E4, E5, E6 and E12:

> **Never describe what an identifier does until you have read the code that consumes it.**

A constant named `HOT_*` was documented as its own opposite; a `createCipheriv` import became
"encrypted at rest"; module names called `apply`/`resolve` became "field-level merge". In all
three cases the consuming code was a few lines away and said otherwise.
