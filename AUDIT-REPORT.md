# 审查与修正报告 · Audit & Corrections Report

Consolidated result of four review passes over this dossier: an independent review (Codex), a
second verification pass, a third consistency sweep, and a fourth pass aimed specifically at the
claims still graded **[I]** or **[U]**. The first three worked from the same extracted
artifacts; the fourth added the main binary's string table and the live daemon log.

**Verdict: the first draft was structurally sound but factually unreliable in specific,
consequential places.** 14 substantive errors were found and corrected in pass two; pass three
found no new inverted mechanisms but 10 residue/consistency errors (E15–E24) where a correction
had reached one file and not its neighbours; pass four resolved 12 previously open items
(R1–R12) — most importantly that the shipped daemon socket is unauthenticated, that cloud sync
is switched off in the shipped client, and that "multiplayer over LiveKit" was the wrong
transport. The architecture story survives; several mechanisms described inside it did not.

- Full error list with evidence → **[`ERRATA.md`](ERRATA.md)**
- Machine-checked references → [`_analysis/audit/`](_analysis/audit/)

---

## 1. What was wrong, by severity

### Would have broken an implementation

| # | Error | Reality |
|---|---|---|
| **E1** | `HOT_PROMPT_CONTEXT_QUERY_OPTION_KEYS` described as the fields that **force a restart** | Exactly inverted — they are the fields that **hot-update in place**. Restart is forced by `env`, `cwd`, MCP-surface change, or any *other* query option. |
| **E3** | Media `workRun` / `async` schemas | `workRun.id` is required (no `taskId`/`keyResultId`); `async` is an object `{mode,timeoutSec,pollIntervalSec}`, not a flag. Documented calls would fail. |
| **E2** | Endpoint list scraped from strings | Authoritative surface is the `Methods` enum: **232 methods**, 232 handler cases, plus **41 events**. My list mixed in MCP actions and provider-pack operation ids, and missed whole families (WeChat, user-profile discovery, directory import, onboarding drafts, activation checklist, wallet…). |

### Overstated enforcement — security-relevant

| # | Error | Reality |
|---|---|---|
| **E6** | "`/.neo/**` is blocked from Edit" | It is an **allow**-rule scope for the "always allow in .neo folder" affordance. Polarity inverted. |
| **E7** | Prescribed a `deniedWrites` setting | The key does not exist. A blanket tool-level `deny` *does* outrank `bypassPermissions`, but **path-scoped deny patterns are explicitly skipped by the matchers** — so they cannot be relied on. |
| **E8** | Destructive-write gate graded "hard at tool boundary" | A heuristic scan of the last 12 chat messages, returning `false` when chat is unavailable. |
| **E9** | "Auth: owner lease or `NEO_OWNER_TOKEN` bearer" | `NEO_OWNER_TOKEN` is a lease contract, not API auth. The WS token is `NEO_DAEMON_WS_TOKEN` and is **optional**; evidence indicates the shipped desktop default serves `/ws` **unauthenticated**, with an Origin check that permits a missing `Origin`. |
| **E5** | "WeChat credentials encrypted at rest" | Plaintext JSON; the AES code protects **media payloads**. Inferred from an `import` statement. |

### Fabricated or unverified

| # | Error | Reality |
|---|---|---|
| **E4** | Cloud sync "field-level merge; append-only merges without conflict" | **No merge exists.** Whole-file byte compare → identical / write / conflict. Invented from module names. |
| **E11** | Render pass order + "60 fps" | Shader names prove passes exist, not their order. Frame rate was invented. |
| **E12** | "Multiplayer visitors can join over LiveKit" | LiveKit is linked and visitor types exist; enablement in this build is not verifiable. |
| **E10** | "Sidebar 288 pt fixed" | Resizable; observed 238–288, most commonly 280. I cherry-picked. |
| **E13** | "THE DAEMON SOURCE" | Recovered bundler output, reformatted. `neo-intelligence` is additionally minified. |
| **E14** | Contradictory shotgun-next rules | "A seat cannot mutate a peer's state" vs "the Critic must review others' work". Resolved with an explicit rights matrix + stable `criticRoleId` + session-derived actor identity. |

### Third pass — residue and cross-document consistency

| # | Error | Reality |
|---|---|---|
| **E15** | `docs/07`: "eight surfaces", "60 fps" | Seven detail surfaces + Memory/Skills + Settings, as in `docs/01`/`M27`/`D10`; frame rate unmeasured. |
| **E16** | `T09`: keep "the forced verification pass" | Same file shows `verificationNudgeNeeded=false` in the producers. The Critic gate is new enforcement. |
| **E17** | "11 managed skills"; `T10` table gaps; "vanish" quoted as fact | 9 skills (+2 references, 1 legacy); frontmatter filled; built-in Task tools persist to `tasks/<listId>/<id>.json`. |
| **E18** | 28 shader entry points | 32 (`_legacy` / `_instanced` variants missed). |
| **E19** | 13 SPM resource bundles | 10. |
| **E20** | Exec summary / `D01`: "~230 endpoints", "417 modules", "CloakBrowser 237 MB" | 232 methods · 41 events; 417 named initializers; bundle is 351 MB (framework ≈237 MB). |
| **E21** | Non-existent names: `config.credentials.*`, `experimental.codex_subscription.status`, `permission.respond`; turn-failure "events" | Not in `protocol.json`; real names `config.providers.*`, `codex.service.status`, `task.permission.respond`; failures are `runtime.raw.event` rawTypes. |
| **E22** | Abbreviated tool-surface fingerprints; line 139929 | Full `toolSurface` strings restored; `promptContextReplacementReasons` is at 139928. |
| **E23** | shotgun enum drift (`T02` vs `shotgun/03`), `FileSource` missing `asset_uri`, mode-exclusivity wording | Aligned to `shotgun/03` §4; E3 follow-through in `T05`; `shotgun/04` reworded. |
| **E24** | Withdrawn 15-week plan still in `shotgun/README` and `D15`; unrenderable Gantt; E14 pointed at a missing `shotgun/02` §9 and gave Critic/Director final `accepted` | Engineer-day figures propagated; Gantt uses day durations; §9 written; final acceptance is the human's, as in `shotgun/10`. |

---

## 2. Root cause

Ten of the fourteen share one failure mode:

> **Behaviour was inferred from an identifier's name without reading the code that consumes it.**

- a constant named `HOT_*` was documented as its own opposite
- a `createCipheriv` import became "encrypted at rest"
- modules named `apply` / `resolve` became "field-level merge"
- `/.neo/**` appearing near permission code became "blocked", when it was "allowed"

In every case the consuming code was within a few lines and said otherwise.

---

## 3. What did not change

The corrections are to mechanisms, not to the architecture. These still hold, now with
citations:

- Three-plane separation (topology / knowledge / execution) — from the vendor's own seed docs
- `dispatch | note | reply(+outcome)` with SQLite CHECK constraints making illegal states
  unrepresentable
- Proof-gated completion: only a check-in writes terminal task states; placeholders are blockers
- The static-prefix / volatile-tail prompt split — **still real, but for prompt-cache economics,
  not process lifecycle** (E1 changed the *why*, not the *what*)
- Wake engine: 11 reasons, coalescing window, per-host mutex, lane policy, activity gate
- Host-side provenance capture rather than agent self-reporting
- "Disable the unconstrained built-in, ship a constrained MCP replacement" (cron)
- `next` hints on every tool result as a teaching mechanism

---

## 4. Evidence markers

Claims now carry a grade:

| Marker | Meaning |
|---|---|
| **[V]** | Verified — code read, with file:line |
| **[O]** | Observed — live artifact on this machine |
| **[I]** | Inferred — reasoned from names/structure, consumer **not** read |
| **[U]** | Unverifiable from the bundle |

---

## 5. Machine-checked artifacts

| File | Contents |
|---|---|
| `_analysis/audit/inventory.json` | 232 methods · 232 handler cases · 41 events · 417 initializers · 27 tool definitions |
| `_analysis/audit/protocol.json` | every method with declaration site, handler line range, and params the handler directly reads |
| `_analysis/audit/protocol-reference.md` | rendered protocol reference |
| `_analysis/audit/mcp-reference.md` | exact MCP tool expressions |
| `_analysis/audit/runtime-tools.json` | runtime tool definitions |
| `_analysis/audit/validation.json` | document-level validation run |
| `_analysis/audit/*.cjs` | the extraction and validation scripts, re-runnable |
| `_analysis/audit/swift-source-files.txt` | 255 first-party Swift file names leaked via `#fileID` (lower bound) |
| `_analysis/audit/client-env-keys.txt` | 98 `NEO_*`/`MATRIX_*` keys the client reads — the absence list matters (`NEO_DAEMON_WS_TOKEN`, `MATRIX_SYNC_OUTBOX`) |
| `_analysis/audit/gateway-surface.md` | every gateway path literal in client and daemon, by caller, with hosts |

Both review passes independently arrived at **232 methods**, which is the strongest single
cross-check in the dossier.

---

## 6. Standing limitation

This remains a **static** reverse-engineering dossier of one pinned build
(`Matrix 1.0.6 (148)`, `neo-agent 0.1.60`). It is not recovered buildable source, not a verified
replica, and it says nothing about server-side behaviour behind the Matrix Gateway — the fourth
pass fixed *which* endpoints exist, not what they do. After R1–R12 the remaining **[I]/[U]**
items are: gateway and release-gate semantics, per-account enablement of live workspaces, and
the bloom-vs-TAA placement inside the renderer. None of them changes the replica's scope.

### What pass four adds for the builder

- Two switches the shipped client never sets: `NEO_DAEMON_WS_TOKEN` (WS auth) and
  `MATRIX_SYNC_OUTBOX` (cloud sync). A replica must decide both deliberately.
- The office renderer is a demand-driven loop with an idle pause, dynamic resolution and MetalFX
  upscaling — budget for that model, not a fixed 60 Hz loop.
- Voice is a thin speech front-end with one tool (`call_neo_intelligence`); live workspaces are
  presence + scene descriptor + whiteboard over Supabase, not an SFU.
- Reconnect replay, field-level merge, content-level import validation and an enforced verifier
  are all **absent** in Matrix; anything the plan says about them is new work.
