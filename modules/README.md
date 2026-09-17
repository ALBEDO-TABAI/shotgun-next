# Module Specifications

Functional specifications grouped for reading, not a recovered source-module map. Depth varies; not every original page contained a diagram or failure analysis. Full initializer locations are in [the generated inventory](../_analysis/audit/module-initializers.json). Native implementation remains inferred from symbols/resources.

## Daemon-side modules

| # | Module | Owns | Spec |
|---|---|---|---|
| M01 | Harness Daemon Core | process, API server, lifecycle, lease | [M01](M01-harness-daemon-core.md) |
| M02 | Workspace Store | workspace CRUD, config, env, migrations | [M02](M02-workspace-store.md) |
| M03 | Department Registry | org topology, profiles, lifecycle | [M03](M03-department-registry.md) |
| M04 | OKR Engine | Objectives, Key Results, fractal view | [M04](M04-okr-engine.md) |
| M05 | Task Engine | Task packets, criteria, check-ins | [M05](M05-task-engine.md) |
| M06 | Department Messaging | SQLite bus, deliveries, threads | [M06](M06-department-messaging.md) |
| M07 | Session Host | agent process lifecycle, turns | [M07](M07-session-host.md) |
| M08 | Prompt Assembly | context construction, caching | [M08](M08-prompt-assembly.md) |
| M09 | Wake Engine | triggers, coalescing, dispatch | [M09](M09-wake-engine.md) |
| M10 | Autonomy & Nudge | lanes, backoff, next-step refs | [M10](M10-autonomy-nudge.md) |
| M11 | Cron Scheduler | time triggers bound to Tasks | [M11](M11-cron-scheduler.md) |
| M12 | Hooks & WorkRuns | async fact tracking | [M12](M12-hooks-workruns.md) |
| M13 | Maintenance & Crystallize | memory consolidation, compaction | [M13](M13-maintenance-crystallize.md) |
| M14 | Memory System | belief cards, index, user profile | [M14](M14-memory-system.md) |
| M15 | Skills System | catalog, overlay, managed seeds | [M15](M15-skills-system.md) |
| M16 | File Service & Provenance | ledger, revisions, lineage, access | [M16](M16-file-service-provenance.md) |
| M17 | Dashboard Projection | derived views, refresh | [M17](M17-dashboard-projection.md) |
| M18 | Model & Provider Gateway | catalog, routing, credentials | [M18](M18-model-provider-gateway.md) |
| M19 | Runtime Installer | claude-code / codex acquisition | [M19](M19-runtime-installer.md) |
| M20 | Matrix Browser | Playwright + CloakBrowser + Browser Agent | [M20](M20-matrix-browser.md) |
| M21 | Media Generation | image / video / audio / characters | [M21](M21-media-generation.md) |
| M22 | Integrations | Composio + native provider packs | [M22](M22-integrations.md) |
| M23 | Receivable | payment links, payouts, disputes | [M23](M23-receivable.md) |
| M24 | Channels | email, Telegram, WeChat | [M24](M24-channels.md) |
| M25 | Marketplace | publish, acquire, import, handover | [M25](M25-marketplace.md) |
| M26 | Cloud Sync | push/pull/apply/conflicts | [M26](M26-cloud-sync.md) |

## Embedded Runtime

| # | Module | Owns | Spec |
|---|---|---|---|
| M31 | Neo Intelligence Runtime | model/tool loop, built-ins, workers, runtime task files | [M31](M31-neo-intelligence-runtime.md) |

## Client-side modules

| # | Module | Owns | Spec |
|---|---|---|---|
| M27 | Swift App Shell & Hub | window, navigation, WS client, DTOs | [M27](M27-swift-app-shell.md) |
| M28 | Terminal (Ghostty) | PTY, blocks, worker TUI attach | [M28](M28-terminal.md) |
| M29 | Office Renderer | Metal, VRM, scene sync | [M29](M29-office-renderer.md) |
| M30 | Voice & Presence | LiveKit, ElevenLabs, visitors | [M30](M30-voice-presence.md) |
