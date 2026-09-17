# Matrix Gateway surface — recovered client + daemon call paths

Static recovery of every gateway path literal in the shipped build. **Server-side behaviour remains [U]**; this file only fixes *which* endpoints a replica's backend must provide and *who* calls them.

Sources: `strings -n 6 Matrix.app/Contents/MacOS/Matrix` (client, 45 literals) and `neo-agent.fmt.js` (daemon, string + template literals). Base hosts: gateway `https://matrix.agent.space` (`/v1/*`), Supabase auth/storage proxied at `https://forward.agent.space` (canonical host, `.supabase.co` rewritten to it), cloud edge `https://edge.matrix.build`, snapshots `https://snapshot.matrix.build`, realtime voice `wss://matrix.agent.space/v1/realtime?model=gpt-realtime-2`.


## Called by the Swift client only

| Path | Purpose (from surrounding strings/types) |
|---|---|
| `/api/publish/start` | workspace snapshot publish (requires `MATRIX_SNAPSHOT_PUBLISH_TOKEN`) |
| `/api/workspaces/` | snapshot publish workspace resource |
| `/v1/billing/balance` | credit balance |
| `/v1/billing/pricing` | pricing table |
| `/v1/billing/redeem` | redeem code |
| `/v1/billing/usage` | usage |
| `/v1/debug-reports` | debug report prepare |
| `/v1/debug-reports/` | debug report complete |
| `/v1/email-preferences` | email preferences |
| `/v1/emails/mailbox` | mailbox identity |
| `/v1/integrations/` | integration detail |
| `/v1/integrations/connections/` | connection detail |
| `/v1/integrations/operations/audit` | operation audit |
| `/v1/integrations/operations/confirmations` | write confirmations |
| `/v1/integrations/operations/plans` | operation plans |
| `/v1/integrations/packs/` | pack detail |
| `/v1/invites/email` | invite by email |
| `/v1/invites/redeem` | redeem invite code |
| `/v1/onboarding/blueprint/complete` | blueprint complete |
| `/v1/onboarding/blueprint/generate` | blueprint generate |
| `/v1/onboarding/complete` | onboarding complete |
| `/v1/receivable/links/` | link detail |
| `/v1/receivable/payouts/` | payout detail |
| `/v1/skills/catalog` | skill marketplace catalog |
| `/v1/subscription` | subscription state |
| `/v1/subscription/cancel` | cancel |
| `/v1/subscription/checkout` | checkout |
| `/v1/subscription/entitlement` | entitlement |
| `/v1/subscription/plans` | plans |
| `/v1/subscription/portal` | billing portal |
| `/v1/subscription/topup/checkout` | top-up |
| `/v1/updates/channels` | update channel access |

## Called by both

| Path |
|---|
| `/v1/chat/completions` |
| `/v1/composio/health-recipes` |
| `/v1/emails/inbox` |
| `/v1/images/edits` |
| `/v1/integrations/composio/execute` |
| `/v1/integrations/connections` |
| `/v1/integrations/packs` |
| `/v1/receivable/balance` |
| `/v1/receivable/disputes` |
| `/v1/receivable/links` |
| `/v1/receivable/payments` |
| `/v1/receivable/payouts` |
| `/v1/receivable/stats` |

## Called by the daemon only

| Path | Purpose |
|---|---|
| `/sync/op-log` | cloud sync outbox push (gated by `MATRIX_SYNC_OUTBOX=1`) |
| `/v1/audio/generations` | `mcp__media__audio_generate` |
| `/v1/billing/charges` | billing activity |
| `/v1/byteplus/assets` | character asset upload (BytePlus) |
| `/v1/emails/send` | outbound email |
| `/v1/emails/{id}` | email read by id |
| `/v1/generations/{id}` | generation status poll (`video_status`) |
| `/v1/images/generations` | `image_generate` |
| `/v1/integrations/operations/execute` | provider pack `execute` |
| `/v1/integrations/operations/plan` | provider pack write plan |
| `/v1/integrations/packs/cloudflare/operations` | Cloudflare pack |
| `/v1/integrations/packs/{id}` | pack manifest |
| `/v1/integrations/packs/{id}/operations` | pack operation list |
| `/v1/models` | model list |
| `/v1/models/catalog` | model catalog |
| `/v1/receivable/links/{id}` | link update/delete + `/webhook/replay` |
| `/v1/responses` | OpenAI Responses-style model call |
| `/v1/uploads` | media upload staging |
| `/v1/videos/generations` | `video_create` |

## Not present anywhere

- No `/v1/live*`, `/v1/rooms*` or LiveKit token endpoint in either binary. Live-workspace records carry Supabase Storage fields (`storageBucket`, `storagePath`, `signedImageURL`) and an `inviteURL`, not LiveKit `serverUrl`/`participantToken`.
- No `config.credentials` or `experimental.*` routes.
- Marketplace publish goes through a Supabase Edge Function (`NEO_AGENT_SPACE_MARKETPLACE_FUNCTION_NAME` = `agent-space-marketplace`) and a Storage bucket, not `/v1/*`.

