# shotgun-next · Implementation Contracts

These proposed requirements resolve contradictions in the original plan. They do not claim a completed app or user-approved platform choice.

## Authority And Review

Use `production.primaryRoleId` and `production.criticRoleId` as stable identities. Actor identity is injected from an authenticated user connection or role session; ignore/reject actor IDs invented in tool arguments.

| Actor | Allowed mutation |
|---|---|
| Maker | own draft/work fields, artifact submission, blocker/control records; no self-acceptance |
| Assigned Critic | append a quality review to the assigned peer item; no general peer editing |
| Director agent | brief/routing/topology within granted authority; cannot impersonate human approval |
| Human user | final acceptance/revision/rejection of the exact reviewed artifact version |
| Daemon | validate, persist, project and emit events; never invent creative approval |

Every review binds `itemId`, artifact/variant revision, criteria revision and brief revision. Changes invalidate acceptance for the changed version. A Critic pass leaves work awaiting the user; user approval requires the matching pass. Revisions return to the maker, and outdated reviews cannot advance a new item version. Instantiate the reviewer before accepting the first gated submission; a missing/retired reviewer leaves a visible queue, not automatic acceptance.

Style-lock creation references an already persisted review, or is included in the same authoritative transaction as that review. For the separate-call route, record the initial review without not-yet-existing learning refs, create the lock with `authoredIn`, then append a learning-link event. Never require a future lock file to exist before the review ID that creates it exists.

## One Authoritative Store

Use daemon-owned transactional records for roles, work, reviews, schedules, operation state and projections. The Markdown/JSON tree elsewhere in the proposal is a readable export contract, not an independent mutable authority. Artifact files remain ordinary versioned files with immutable content hashes referenced by records.

Keep write authority out of agent processes. File-tool checks alone do not contain Bash, external CLIs, plugins, browser downloads, symlink/hard-link aliases, rename or unlink. Select and test an OS-backed isolation strategy per supported platform before claiming managed state is protected. A normal same-user directory and a deny-pattern setting are insufficient.

Commit a domain mutation and its outbound event intent atomically. On restart, repair derived views and pending delivery from that authoritative intent. The UI never decides truth from a stale cached board.

## Asynchronous Operations

Track independent IDs for the durable item, execution attempt, provider job, hook, role message and review. Register an operation before submitting an external job; preserve provider ID, current state and input digest. Distinguish queued/running/succeeded/failed/cancelled/outcome-unknown. If submission times out without a receipt, query by a stable provider-supported idempotency key or report the unknown outcome; do not blindly resubmit a paid or mutating action.

On completion, obtain the actual artifact, verify type/size/content hash and decode media where relevant. A remote “done” status, local download and accepted deliverable are separate milestones. Cancellation does not imply provider cancellation or zero charge.

## Reconnect, Scheduling And Cost

Snapshots include a sequence cursor and daemon epoch; later events are ordered, duplicate-tolerant and gap-detectable. Refresh when continuity is lost. Do not infer durable replay from a transient socket buffer.

Store schedule timezone explicitly. Test DST, midnight active windows, one-shots missed during shutdown and recurring-run overlap. An autonomy pause applies to all roles. An explicitly authorized work submission may request a bounded continuation/review; it must not become an always-on Critic nudge.

Estimate cost before execution, reserve budget atomically across concurrent workers, settle actual usage, and expose unknown cost. A preflight estimate without reservation is not a spend cap. Review retries and regeneration count toward the same approved budget.

## Fidelity And Platform Decisions

The original Tauri/React, one-room office, deferred multiplayer and creative-only roles are options, not requirements supplied by the user. Define a reference-screen/interaction inventory before freezing them. Native symbols do not reveal exact spacing, colors, typography metrics, animation timing, shader source or voice behavior.

A reduced prototype can validate workflow quickly, but passing that test does not claim Matrix exterior parity. A renderer prototype must be compared on terminal textures, text legibility, camera/selection behavior, frame time and idle power. Distinguish feature present in resources, feature reachable in UI and feature demonstrated end to end.

## Acceptance Scenarios

1. Request becomes owned work; cross-role assignment is persisted once; reply outcome is matched to its original request.
2. Maker cannot self-approve or spoof the Critic; the actual Critic can review a peer without gaining general edit rights; a stale review cannot approve a newer artifact.
3. Shell, worker and download attempts cannot alter daemon state; permitted artifact work still succeeds.
4. Crash between submission, provider receipt, download, review and event delivery resumes without duplicate external effects or fabricated completion.
5. Two concurrent generations cannot both spend the same reserved budget; failed/unknown operations remain visible.
6. Reconnection reconstructs the same board, chat and review queue from canonical records; a missing event triggers recovery.
7. Autonomy pause stops unsolicited review/nudge loops; scheduled work obeys the stored timezone and stop conditions.
8. Installed candidate completes the same scenario with real runtime dependencies and reference visuals; source-only or mock tests do not count as installation proof.
