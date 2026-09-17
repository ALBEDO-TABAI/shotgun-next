# T09 · Built-in Agent Tools

The 29 tools handed to every department lead session, plus the 3 deliberately withheld.

```ts
DEPARTMENT_LEAD_BUILTIN_TOOLS = [
  "Agent","TaskOutput","Bash","Glob","Grep","ExitPlanMode","Read","Edit","Write",
  "WebFetch","TodoWrite","WebSearch","TaskStop","AskUserQuestion","Skill",
  "EnterPlanMode","SendMessage","EnterWorktree","ExitWorktree",
  "TeamCreate","TeamDelete","TaskCreate","TaskGet","TaskUpdate","TaskList",
  "ToolSearch","LSP","Monitor","PowerShell"
]
DAEMON_MANAGED_CRON_BUILTIN_TOOLS = ["CronCreate","CronDelete","CronList"]   // disallowedTools
```

---

## Groups

| Group | Tools |
|---|---|
| **Files** | `Read`, `Write`, `Edit`, `Glob`, `Grep` |
| **Execution** | `Bash`, `PowerShell`, `Monitor`, `LSP` |
| **Delegation** | `Agent`, `TaskOutput`, `TaskStop`, `SendMessage`, `TeamCreate`, `TeamDelete` |
| **Session scratch** | `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`, `TodoWrite` |
| **Planning** | `EnterPlanMode`, `ExitPlanMode` |
| **Isolation** | `EnterWorktree`, `ExitWorktree` |
| **Web** | `WebFetch`, `WebSearch` |
| **Discovery** | `Skill`, `ToolSearch` |
| **User** | `AskUserQuestion` |

---

## `Agent` — the delegation tool

This is where multi-agent collaboration actually happens. Its description carries the full
routing policy.

### Runtime routing (verbatim)

> You are the Lead. `Agent` creates Agents. Each Agent runs on one runtime:
>
> - **Default to Neo, and keep it for the large majority of work.** Omit `runtime` unless you have
>   a concrete reason to reach for a specialist. Neo is the Matrix-native worker runtime and
>   follows the user's configured Matrix model routing — it already reaches strong models for code,
>   design, writing, research, and analysis, and it preserves local context and Matrix-native
>   coordination. Claude Code and Codex are external specialist runtimes: they depend on a locally
>   installed binary, are less stable, and lose Matrix-native context, so they are an **opt-in
>   escalation, not the default for "real work."**
> - Choose only the runtime here; **do not pick or override concrete models.**
> - Before selecting a non-Neo runtime, the test is **not** "what category is this work" — Neo
>   handles coding, design, and research perfectly well. The test is: **would this specific task be
>   meaningfully better on an external specialist, enough to justify its instability and loss of
>   Matrix context?** If you cannot name that concrete benefit, stay on Neo.
> - `runtime: "claude_code"` is a reasonable escalation only when the task leans hard on
>   Claude-family strengths Neo's routing won't cover — e.g. heavy design taste from
>   screenshots/mockups, or large open-ended product/narrative shaping — and the work is
>   self-contained enough to leave Matrix context behind.
> - `runtime: "codex"` is a reasonable escalation only when the task leans hard on GPT-family
>   execution strengths — e.g. a large terminal-heavy refactor or migration that benefits from
>   Codex's autonomous execution loop — and the work is self-contained enough to leave Matrix
>   context behind.
> - For mixed work, prefer keeping the whole job on Neo as the lead's same-runtime worker; split
>   out a specialist runtime only for the one slice that clearly needs it, and keep ownership,
>   threading, and final synthesis on Neo.
> - Explicit runtime mentions (`@neo`, `@codex`, `@claude_code`) are **hard worker-assignment
>   instructions.**
> - If one user request names multiple runtime mentions, create separate `Agent` calls with the
>   matching runtime on each.
> - Do not infer runtime from loose brand wording alone.
> - Codex and Claude Code do not support fork context.

**This is the best-argued routing policy in the app.** Note the move: it refuses category-based
routing ("design → Claude") and demands a named, concrete benefit. Copy that framing.

### Worker context modes

| `context` | Worker receives | Use for |
|---|---|---|
| `"task"` (default) | only the prompt you write | most worker tasks, polling, nudges, media checks, follow-ups |
| `"recent"` | prompt + short excerpt of recent parent conversation | worker needs nearby state, not full context |
| `"fork"` | the parent turn/context — **Neo only** | several parallel workers in one parent turn sharing a hot prefix |

### Background discipline (verbatim)

> **Don't peek.** The tool result includes an `output_file` path — do not Read or tail it unless
> the user explicitly asks for a progress check. You get a completion notification; trust it.
> Reading the transcript mid-flight pulls the fork's tool noise into your context, which defeats
> the point of forking.
>
> **Don't race.** After launching, you know nothing about what the fork found. **Never fabricate or
> predict fork results in any format** — not as prose, summary, or structured output. The
> notification arrives as a user-role message in a later turn; it is never something you write
> yourself. If the user asks a follow-up before the notification lands, tell them the fork is still
> running — give status, not a guess.

### Prompt-writing guidance (verbatim)

> Brief the agent like a smart colleague who just walked into the room — it hasn't seen this
> conversation, doesn't know what you've tried, doesn't understand why this task matters.
> - Explain what you're trying to accomplish and why.
> - Describe what you've already learned or ruled out.

### Result handling

> Treat the agent's outputs as **evidence-carrying drafts**: preserve its evidence, assumptions,
> and unknowns; verify before making user-facing claims when stakes are high or the result drives
> code, product, safety, legal, financial, or external actions.
>
> The result returned by the agent is **not visible to the user** — send a text message with a
> concise summary.

### Parallelism

> If the user specifies that they want you to run agents "in parallel", you MUST send a single
> message with multiple `Agent` tool use content blocks.

### Isolation

`isolation: "worktree"` only when the worker specifically needs isolated edits. *"Matrix
workspaces without Git use a managed copy-on-write overlay."* Never for research, read-only work,
fact-checking, planning, or status checks.

`isolation: "remote"` exists but is gated.

### Built-in agent types

`Explore` and `Plan` are recognised read-only agent types; otherwise `general-purpose`.
`verification` is a special type the runtime *can* render a nudge for:

> "NOTE: You just closed out 3+ tasks and none of them was a verification step. Before writing
> your final summary, spawn the verification agent. **You cannot self-assign PARTIAL by listing
> caveats in your summary — only the verifier issues a verdict.**"

This string is not proof of a forced verifier. `verificationNudgeNeeded` has exactly six occurrences in `neo-intelligence.fmt.js`: two schema declarations, two consumers (`mapToolResultToToolResultBlockParam`), and two producers — TodoWrite (`:337411`, `Y = false`) and TaskUpdate (`:396757`, `U = false`) — both literal `false`. There is no other write site, so the “3+ tasks” rule can never fire in this build **[V]**. A mandatory studio Critic would be new enforcement, not a recovered Matrix invariant.

---

## Session-scratch task tools

The shipped `okr-execution` skill describes these as scratch tools:

> They are "a session-scratch todo list — in-memory, gone when the session ends, with no owner,
> proof, or Check-in. They are fine for organizing your own multi-step thinking inside one turn,
> but they are **not** OKR Tasks."

The physical-storage claim in that quotation is contradicted by runtime code: `TaskCreate/Get/Update/List` read and write `tasks/<listId>/<id>.json` (`neo-intelligence.fmt.js:203232`). `NEO_CODE_TASK_LIST_ID`, team or session identity selects the list. Keep this separate from TodoWrite, and do not claim all built-in task records vanish on process exit. They still lack the harness's OKR/proof contract.

---

## File tools — notable details

`Read`: 2 000-line default; images render visually; PDFs need a `pages` range above 10 pages
(max 20/request); Jupyter notebooks return cells with outputs; a file unchanged since the last
read returns *"File unchanged since last read… refer to that instead of re-reading."*

`Write`: must `Read` an existing file first; *"NEVER create documentation files (*.md) or README
files unless explicitly requested"*; *"Only use emojis if the user explicitly requests it."*

`Edit`: permission rules and a sensitive-path check apply; `/.neo/**` and `~/.neo/**` are also used to construct session allow rules, not blanket deny patterns. It can fail with *"File has been unexpectedly
modified. Read it again before attempting to write it."*

`Grep`: ripgrep-backed. *"ALWAYS use Grep for search tasks. NEVER invoke `grep` or `rg` as a Bash
command. The Grep tool has been optimized for correct permissions and access."* Modes:
`content` / `files_with_matches` (default) / `count`; `multiline: true` for cross-line patterns.
Bundled binary at `Resources/vendor/ripgrep/arm64-darwin/rg`.

---

## Discovery tools

`ToolSearch` — fetches deferred tool schemas by name (`select:Read,Edit`) or keyword. Combined
with `alwaysLoad` + `searchHint` on MCP tools, this is how a large tool surface stays affordable.
A read-only set is exempt from gating: `{Read, Glob, Grep, ToolSearch, LSP, TaskGet, TaskList}`.

`Skill` — loads a full `SKILL.md` on demand. The prompt insists on loading `matrix-browser`
**by name** rather than searching the filesystem for it.

---

## Disallowed

```
CronCreate · CronDelete · CronList
```

Removed so scheduling can only go through `mcp__cron__state`, which enforces Task binding.
**The general pattern: when a built-in is too permissive, disable it and ship a constrained MCP
replacement.** Apply the same treatment in shotgun-next to any built-in that can write
tool-owned state.

---

## shotgun-next tool set

```
Files        Read · Write · Edit · Glob · Grep
Execution    Bash · Monitor
Delegation   Agent (+ TaskOutput · TaskStop · SendMessage)
Scratch      TodoWrite
Planning     EnterPlanMode · ExitPlanMode
Web          WebFetch · WebSearch
Discovery    Skill · ToolSearch
User         AskUserQuestion
Disallowed   CronCreate/Delete/List  (+ any tool that writes tool-owned state)
```

Drop: `PowerShell`, `LSP`, `TeamCreate/Delete`, `EnterWorktree/ExitWorktree` (unless the studio
does code), and the four session-scratch Task tools (keep `TodoWrite` only).

Keep, verbatim in spirit: the Agent routing argument, the three context modes, "don't peek /
don't race", "brief it like a colleague who just walked into the room", and evidence-carrying
drafts. The verification pass is **new enforcement in shotgun-next**, not something inherited:
Matrix ships the verifier prompt text, but the inspected `TodoWrite` / `TaskUpdate` producers
return `verificationNudgeNeeded = false` (see [Built-in agent types](#built-in-agent-types) and ERRATA E16), so
nothing in the bundle proves the pass is forced today. Make the Critic gate structural
([shotgun/09 D6](../shotgun/09-decisions.md)).
