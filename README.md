# Matrix — Evidence-Based Teardown & Reconstruction Spec

**2026-09-16 audit:** Start with [审查与修正报告](AUDIT-REPORT.md). This is a static reverse-engineering dossier, not recovered buildable source or a verified replica. Each page now distinguishes extracted code, symbol-based inference and proposed shotgun-next behavior. The [evidence inventory](_analysis/audit/inventory.json) pins the inspected artifacts; [protocol reference](_analysis/audit/protocol-reference.md) and [exact MCP expressions](_analysis/audit/mcp-reference.md) replace approximate inventories.

Reverse-engineering dossier for **Matrix.app 1.0.6 (build 148)** — a macOS "Agent Company"
desktop application — produced as the technical foundation for **shotgun-next**, a
multi-agent collaboration studio where agents work together in professional roles.

Source of truth: `/Applications/Matrix.app`, copied verbatim to `_analysis/app-copy/`,
plus historical observations of runtime state at `~/.neo` and `~/Library/Application Support/Matrix`. Those observations were not preserved as reproducible snapshots and are not current-state verification.

---

## What Matrix actually is

A **native Swift/SwiftUI macOS app** that acts as the cockpit for a **local agent company**.
The company itself runs as a **local Bun-compiled TypeScript daemon** (`neo-agent`, aka the
*harness*) which owns a filesystem-backed workspace and manages persistent department identities with agent processes started, retired and resumed as needed. Department leads use `neo-intelligence`; the Agent tool can launch Neo workers or external `claude_code` / `codex` specialists. Strings and tool behavior suggest Claude Code lineage, but the extracted bundle does not establish its exact upstream version or complete derivation. Departments coordinate through a SQLite message bus, share an
OKR state machine, own memory and skills, and are woken by a multi-lane autonomy scheduler.

Matrix renders all of this three ways: a conventional chat/sidebar app, a Kanban "Work" board,
and a **real-time 3D office** (Metal renderer, VRM avatars, San Francisco city environment)
in which each department is a room and each worker is an animated character at a desk.

```
You ──► Matrix.app (SwiftUI + Metal)
          │  WebSocket 127.0.0.1:7319/ws
          ▼
        neo-agent  ── the harness daemon (Bun/TS)
          │
          ├── department lead sessions ──► neo-intelligence
          │      └── workers ──► Neo | installed claude | installed codex
          ├── MCP servers (matrix, okr, cron, files, media, receivable, browser, packs)
          ├── matrix-browser (Playwright + patched Chromium "CloakBrowser")
          └── ~/.neo/workspaces/<ws>/…  ── the company on disk
```

---

## Accuracy status

This dossier was **reviewed three times**. An independent review (Codex) plus a second
verification pass found **14 substantive errors** in the first draft — including one inverted
core claim, one fabricated subsystem behaviour, and several cases of enforcement being
overstated. A third pass (2026-09-17) found **10 residue and consistency errors** (E15–E24):
stale counts that survived earlier corrections, four RPC/event names that do not exist in the
registry, enum drift between the shotgun-next files, and a rights matrix that was referenced but
never written. A fourth pass (same day) went after the remaining **[I]/[U]** claims with new
evidence sources — the main binary's embedded `#fileID` literals and Swift field metadata, and
the live `daemon.log` — and **resolved twelve of them** (R1–R12 in `ERRATA.md`): WS auth default,
render-loop model, voice/live-workspace transport, cloud-sync gating and op-log, event-replay
durability, import validation, persona isolation, the verifier nudge, Hub DTO provenance, the
build pipeline, and the full gateway endpoint surface.

**Read [`ERRATA.md`](ERRATA.md) before relying on any specific claim.** It lists every
correction with file:line evidence, and explains the root cause: inferring behaviour from
identifier names without reading the consuming code.

Claims now carry evidence markers — **[V]** verified in code · **[O]** observed on disk ·
**[I]** inferred · **[U]** unverifiable from the bundle.

---

## How to read this dossier

| Path | Contents |
|---|---|
| [`00-EXECUTIVE-SUMMARY.md`](00-EXECUTIVE-SUMMARY.md) | The 10-minute version + the single big architecture diagram |
| [`docs/`](docs/) | Cross-cutting specifications: runtime, process topology, data model, protocol, prompts, autonomy, UI, 3D, security, packaging |
| [`modules/`](modules/) | Functional module specifications; these are editorial groupings, not recovered source-file boundaries |
| [`tools/`](tools/) | One specification per tool surface — every MCP tool, every built-in agent tool, every managed skill |
| [`diagrams/`](diagrams/) | Standalone Mermaid diagrams, indexed and reusable |
| [`shotgun/`](shotgun/) | **The build plan** — how to recreate this as a multi-agent studio |
| [`_analysis/`](_analysis/) | Raw extraction: app copy, unpacked Bun bundles, demangled Swift type graph |

Start at `00-EXECUTIVE-SUMMARY.md`, then `docs/02-runtime-architecture.md`,
then `shotgun/00-brief.md`.

---

## Evidence base

Claims come from extracted code, shipped prompts/resources, Swift symbols, historical local observations and explicit design proposals. These evidence classes have different limits; see the audit report.

| Artifact | How it was obtained | Yield |
|---|---|---|
| `Contents/MacOS/Matrix` (166 MB, Mach-O arm64) | `nm` + `swift-demangle` | **3 756 top-level type names**, plus private-discriminator groups; no recovered Swift bodies, complete call graph or proven source-file count |
| `Resources/neo-agent` (65 MB) | Bun `__BUN,__bun` section extracted, formatted | **153 126 lines of bundled JavaScript**, including dependencies; 417 named `__esm` initializers, not 417 independent product modules |
| `Resources/neo-intelligence` (78 MB) | same | **615 762 lines** — the agent runtime (minified identifiers, intact strings/prompts) |
| `Resources/matrix-browser/` | plain Node/Playwright tree + Rust supervisor | Browser automation stack + Chromium 145 fork |
| `Resources/neo-agent-seed/` | plain files | 9 named skill templates, 2 supporting references, 1 legacy architecture template, plus prompts and integration packs |
| `~/.neo/` (live) | filesystem | Real workspaces, departments, task packets, SQLite message bus, traces |
| `en.lproj/Localizable.strings` | `plutil` | 5 768 UI strings incl. the vendor's own architecture tutorial |

Extraction commands are reproduced in [`docs/10-build-and-packaging.md`](docs/10-build-and-packaging.md#5-reproducing-this-teardown).

---

## Version pinned

```
Matrix            1.0.6 (148)   built 2026-08-20T13:35:56Z   macOS 14.6+, arm64
neo-agent         0.1.60        sha 76894dbbb
neo-intelligence  0.1.60        sha 76894dbbb
matrix-browser    0.1.0         Chromium 145.0.7632.109
download manifest claude-code 2.1.126 · codex 0.144.4 (not proof of installed external versions)
bundle id         com.matrixai.app      URL scheme  matrix://
```
