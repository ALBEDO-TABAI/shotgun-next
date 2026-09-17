# T10 · Managed Skills

Nine skills seeded into every workspace from `neo-agent-seed/templates/`, upgraded by
`seedVersion`. They are where *judgment* lives — the MCP tools carry execution.

The `templates/` directory holds **12 files**: the 9 `SKILL.md` templates below, 2 companion
reference files (`media-generation-reference.md` 181 lines, `department-management-reference.md`
42 lines) that are mounted next to their skill, and 1 legacy template
(`workspace-architecture.md`, 180 lines) that is superseded by `prompts/workspace-schema.md`.
Any "11" or "12 managed skills" figure elsewhere counts those extras; the skill count is nine.

| Skill | Template file | seedVersion | Lines | Category | Symbol | `allowed-tools` |
|---|---|---|---|---|---|---|
| `matrix-browser` | `browser-skill.md` | — | 947 | — | — | — |
| `debug-and-report` | `debug-and-report-skill.md` | — | 380 | — | — | — |
| `find-skills` | `find-skills-skill.md` | 2 | 167 | development | `sparkle.magnifyingglass` | — |
| `okr-execution` | `okr-execution-skill.md` | 39 | 163 | coordination | `checkmark.seal` | — |
| `media-generation` (+ reference 181) | `media-generation-skill.md` | 13 | 155 | automation | `photo.on.rectangle.angled` | `Read` + the 7 `mcp__media__*` tools |
| `skill-creator` | `skill-creator.md` | 3 | 140 | development | `hammer.fill` | — |
| `email` | `email-skill.md` | 1 | 112 | communication | `envelope` | `Bash` |
| `department-management` (+ reference 42) | `department-management-skill.md` | 19 | 95 | coordination | `building.2.crop.circle` | — |
| `workspace-planning` | `workspace-planning-skill.md` | 14 | 53 | workspace | `point.3.connected.trianglepath.dotted` | — |

`matrix-browser` and `debug-and-report` carry only `name` + `description` in frontmatter — no
`seedVersion`, so they are re-seeded by content rather than by version bump. Only two skills
restrict `allowed-tools`; the rest inherit the session's full tool surface.

---

## The description is the router

Skills are discovered by their `description` alone (only `name + scope + description` reach the
prompt). Matrix writes them as **trigger specifications**, not summaries:

### `okr-execution`

> "Use to track and prove work you own: open a Task and set its done-criteria, attach proof and
> check it in, schedule a reminder / deadline / recurring check, or close an OKR loop (an active
> Objective with no first Key Result, or an active Key Result with no movable next Task).
> **Trigger: "I own this and it needs a durable owner, proof, and a next move."** This is the
> persistent OKR Task system via `mcp__okr__state` — **NOT** the session-scratch
> TaskCreate/TaskList/TodoWrite built-in tools, which vanish when the session ends. To hand work to
> another department or reply to one, use `department-management` instead."

Four moves in one description: what it's for, an explicit trigger sentence, what it is **not**,
and where to go instead.

One factual caveat on the quoted text: "vanish when the session ends" is the *skill's* framing,
not runtime behaviour. `TaskCreate/Get/Update/List` persist to `tasks/<listId>/<id>.json`
(`neo-intelligence.fmt.js:203232`; see [T09](T09-builtin-agent-tools.md) and
[M05](../modules/M05-task-engine.md)). What they lack is the OKR owner/proof/check-in contract,
which is the real reason the skill steers agents to `mcp__okr__state`. Keep the steer; do not
repeat the "vanish" claim as fact in shotgun-next prompts.

### `workspace-planning`

> "Use at the start of a broad, vague, or multi-part request, **before any execution**, to decide
> its shape… **Triggers: ongoing-help language (manage / watch / improve / keep track of / take
> care of), a goal with no clear owner yet, or work spanning several owners.** This skill decides
> the plan only — once owners are clear, use `department-management` … and `okr-execution` …"

It names the literal *words* the user will use. That is far more reliable than a semantic
description.

### `department-management`

> "Use for department CRUD and cross-department coordination: create/update/retire/merge/delete
> owners, inspect department ownership, route work to an existing owner, send or reply to
> department messages, or read another department's prior chat context."

---

## Policy vs mechanics

`department-management` states the split explicitly:

> "A decision policy for ownership and cross-department coordination. `mcp__matrix__department`
> carries the execution; **this skill chooses what to call.**"

Content is correspondingly judgment-heavy:

- **First Principles** — a department is an owner; Tasks belong to departments; agents are seats;
  cross-owner work goes through messages; CRUD lives with the primary; *"File structure follows
  ownership."*
- **Decision Ladder** — one question: does the work fall within an existing department's
  responsibility? yes → `message.send`; no → create the smallest set of owners now, *one clear ask
  is enough*; vague ambition → a Task under whichever owner is responsible.
- **After Creating** — write the routing memory card before or immediately after the first
  `message.send`; record a structure-change Task (`org_change`).
- **Taste Rules** — *"One precise tool call beats a long explanation of internals."* /
  *"User-facing output stays in operating language."* / *"Seed a new department only with what the
  user gave you or what the boundary actually needs; placeholder Key Results, memory, or process
  text obscure real ownership."*

`workspace-planning` is similar: Two Layers, a four-step Decision Order (read intent → resolve
ownership → **move first** → close the loop), State Discipline, Human Output, Receipts.

> "If one part of the ask is clear and another part is vague, move the clear part now and ask one
> precise question for the vague part."

> "Continuity language ('manage', 'watch', 'improve', 'keep track of', 'take care of') usually
> signals ongoing ownership, not a one-off answer."

---

## `okr-execution` — the operating loop

Covered in depth in [M05](../modules/M05-task-engine.md). Structure worth mirroring:

```
Two different "tasks" — do not confuse them      ← disambiguation up front
Concept Application                              ← vocabulary
Use                                              ← when to apply, and when NOT to
Rules                                            ← ~25 hard rules
State Shape                                      ← exact field names and enums
Task Packet                                      ← the file format
Proof-Bearing Execution                          ← how proof attaches
Trigger Discipline                               ← manual / time / department_message
Criteria, Verification, Check-in                 ← the 7-step procedure
OKR, Dashboard, Nudge                            ← the 6 ordered wake reasons
```

Note that it embeds the **exact schema** ("Required Key Result fields: …  Status: draft | active |
at_risk | blocked | completed | cancelled") and then says *"Use only the listed field names and
states; malformed records are ignored."* The skill and the tool agree because the skill quotes the
tool.

---

## `email`

Frontmatter declares its constraints:

```yaml
allowed-tools: Bash
shell: bash
```

Ships a **Bash helper function** (`neo_email_cli`) that resolves the app-provided executable and
falls back to `neo` on PATH, failing loudly with both env values. Rules:

> "Use this workflow only for external email. Use department messages for internal coordination."
>
> "If `NEO_EMAIL_ADDRESS` is missing, stop and tell the user workspace email is not configured."
>
> "Do not print auth tokens, inspect token files, or hand-write gateway `curl` calls. Use the CLI
> helper below so authentication stays inside the app."

Pattern: **when a capability must run through Bash, ship the helper in the skill.** Credentials
never enter context.

---

## `matrix-browser`

947 lines — the operating manual for [T07](T07-mcp-matrix-browser.md). Its structure:
when to prefer WebSearch · how to choose between script and visual · working principles ·
environment & lifecycle · `browser.task.message` (input/output/behaviour/fit/anti-fit/shapes) ·
`browser.script.run` (capabilities, absent APIs, bootstrap, troubleshooting, runtime patterns,
first-cell recipes).

The **Bootstrap** section even includes user-facing communication guidance:

> "These setup details are internal. User-facing progress updates should be less technical in
> nature. Never mention JavaScript runtime cells, persistent bindings, or MCP tool internals
> unless a user is asking for that exact information. If setup or recovery is needed, describe it
> naturally as connecting to the browser or retrying the browser connection."

---

## `debug-and-report`

380 lines including an embedded Python script that walks `~/.neo/workspaces`, extracts
`session_id` / `workspace_id` / `department_id` from `prompt-context.md`, `user-prompt.md` and
`report.json`, resolves predicted transcript paths, copies matching artifacts, and emits a
manifest. A self-service support-bundle collector — ship one.

---

## shotgun-next seed set

```
work-execution        ≈ okr-execution        the Work Item / acceptance / review loop
role-management       ≈ department-management ownership and handoff policy
production-planning   ≈ workspace-planning    turn a vague ask into a shaped production
creative-brief        NEW  client ask → Brief + first Milestone + success signal
art-direction         NEW  style locks, references, palette, do/don't
critique-round        NEW  structured review: severity, required fixes, verdict
production-handoff    NEW  what must accompany work passed to another role
asset-generation      ≈ media-generation
publish-package       NEW  export, naming, formats, delivery manifest
studio-browser        ≈ matrix-browser
debug-and-report      as-is
skill-creator         as-is
find-skills           as-is
```

Write every description with: **what it's for · an explicit trigger sentence · what it is NOT ·
where to go instead.**
