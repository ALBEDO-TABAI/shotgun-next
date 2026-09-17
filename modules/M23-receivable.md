# M23 · Receivable (Agent Revenue)

**Source modules:** `receivable_mcp`, `billing_actor`, `link_wallet`, `social_accounts`,
`Payout*` / `Receivable*` Swift types

---

## Purpose

Let a workspace take money. Matrix is the **merchant of record**; the user never handles Stripe
keys.

## Tools (12)

| Tool | Purpose |
|---|---|
| `create_link` | create a payment link |
| `update_link` | retrofit `continue_url` on an existing link |
| `delete_link` | remove a link |
| `list_links` | what links exist (status/limit filters) |
| `list_payments` | payments received; `link_id` joins back to the link |
| `get_stats` | totals by currency + link count |
| `get_balance` | withdrawable balance per currency |
| `request_payout` | cash out |
| `list_payouts` | withdrawal history with status semantics |
| `replay_webhook` | re-fire the latest webhook for a link |
| `list_webhook_deliveries` | debug missing notifications |
| `list_disputes` | chargebacks |

Transport: HTTPS to the Matrix gateway with `Authorization: Bearer <token>` and
`Idempotency-Key` on mutating calls.

## What makes these descriptions unusual

They are written as **role instructions**, not API docs:

> "You are the seller's technical interpreter for payment links. The seller is running a
> business; they don't know what a 'webhook' or a 'redirect URL' is and they shouldn't have to.
> Listen for what they are trying to accomplish, decide which arguments to set, and ask plainly
> when something is missing."

> "You are the seller's interpreter for cashing out earnings. They will say things like
> 'withdraw my money', 'pay me out', 'cash out $50', 'where's my revenue' — they will not say
> 'request a payout'. Your job is to recognize the intent, route them through the right surface,
> and translate the system's response."

> "Don't ask which technical action — pick this tool, the system handles the right outcome based
> on whether anyone has paid." (`delete_link`)

And they teach the **domain**, not just the schema:

> "A dispute (chargeback) is a customer telling their bank 'I didn't authorize this' or 'the
> product wasn't delivered'. Flowith holds the disputed money in reserve until the dispute
> resolves."

> "The number that matters is `available_minor` — that's the only money the user can actually
> withdraw right now. The other fields are explainability."

Payout statuses are documented as user-facing answers:

```
requested  — pending in queue; ops hasn't picked it up yet.
processing — ops is wiring the money out-of-band.
…
```

**This is the single best writing in the entire tool surface.** The pattern generalises: a tool
description should say *who the agent is being for the user*, what the user will actually say,
and what each field means in the user's terms.

## Honesty clause

> "Do not invent revenue facts: if a tool returns an empty list or an error, say so plainly."

And the guidance for "was my link paid?": scan `list_payments` for an entry whose `link_id`
matches, or filter `status: "succeeded"`. *"Returns an empty list if no payments match yet — the
customer simply hasn't completed checkout."* The tool pre-empts the hallucination.

## Related surfaces

`link_wallet` (user-approved payment credentials, `HubLinkWallet*`), `social_accounts`,
`PayoutSetup` / `PayoutSetupStatus` / `PayoutWithdrawalEmail` Swift types with draft persistence,
`billing.activity`.

## Reuse in shotgun-next

**Drop the feature** — a creative studio app doesn't need to be a payment processor.

**Keep the writing style.** Rewrite every shotgun-next tool description in this voice:

```
You are the director's interpreter for <X>. They will say things like "<real phrasing>",
not "<API verb>". Recognize the intent, choose the arguments, and ask plainly when something
is missing. The field that matters is <field> — the rest is explainability.
Do not invent <X> facts: if the tool returns nothing, say so plainly.
```
