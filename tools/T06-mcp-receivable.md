# T06 · `mcp__receivable__*`

**Server:** `receivable` · **12 tools** · **Surface:** `mcp__receivable@1`

Payment links, balance, payouts, disputes and webhooks. Matrix is the merchant of record.

Not needed in shotgun-next — **but read this page anyway**: these are the best-written tool
descriptions in the app, and the writing style is the thing to copy.

---

## Tools

| Tool | One-line purpose |
|---|---|
| `create_link` | create a payment link |
| `update_link` | retrofit `continue_url` on an existing link |
| `delete_link` | remove a link (system picks the right underlying action) |
| `list_links` | which links exist — `status ∈ {active,inactive,expired}`, `limit ≤ 100` |
| `list_payments` | payments received — `status ∈ {succeeded,refunded,disputed,failed}` |
| `get_stats` | total received + count by currency + link count |
| `get_balance` | withdrawable balance per currency |
| `request_payout` | cash out |
| `list_payouts` | withdrawal history |
| `replay_webhook` | re-fire the latest webhook for a link |
| `list_webhook_deliveries` | attempts, status codes, response snippets, next attempt |
| `list_disputes` | chargebacks |

Transport: `Bearer` token to the Matrix gateway, `Idempotency-Key` on mutations, request timeout
enforced with `AbortSignal.timeout`.

---

## The writing technique, extracted

### a. Cast the agent in a role

> "You are the seller's technical interpreter for payment links. The seller is running a business;
> they don't know what a 'webhook' or a 'redirect URL' is and they shouldn't have to. Listen for
> what they are trying to accomplish, decide which arguments to set, and ask plainly when
> something is missing."

### b. Predict the user's actual words

> "They will say things like 'withdraw my money', 'pay me out', 'cash out $50', 'where's my
> revenue' — **they will not say 'request a payout'**."

### c. Remove a decision from the agent

> "Don't ask which technical action — pick this tool, the system handles the right outcome based
> on whether anyone has paid." (`delete_link`)

### d. Teach the domain, not the schema

> "A dispute (chargeback) is a customer telling their bank 'I didn't authorize this' or 'the
> product wasn't delivered'. Flowith holds the disputed money in reserve until the dispute
> resolves."

### e. Name the one field that matters

> "The number that matters is `available_minor` — that's the only money the user can actually
> withdraw right now. The other fields are explainability."

### f. Turn enums into user-facing answers

```
requested  — pending in queue; ops hasn't picked it up yet.
processing — ops is wiring the money out-of-band.
…
```

### g. Pre-empt the hallucination

> "This is how you find out whether a `create_link` was paid: scan the list for an entry whose
> `link_id` matches the link's `id`, or filter by `status: "succeeded"`. **Returns an empty list
> if no payments match yet — the customer simply hasn't completed checkout.**"

> "Do not invent revenue facts: if a tool returns an empty list or an error, say so plainly."

### h. Say when to use it from the user's side

> "Use when the user reports their server didn't receive the notification (downtime, deploy, bug
> fixed)." (`replay_webhook`)

---

## Template for shotgun-next tool descriptions

```
You are the <user role>'s interpreter for <capability>. They are <what they actually do>;
they don't know what <jargon> is and they shouldn't have to. Listen for what they are trying
to accomplish, decide which arguments to set, and ask plainly when something is missing.

They will say things like "<real phrasing 1>", "<real phrasing 2>" — they will not say
"<API verb>".

<one-paragraph domain explanation in the user's terms>

The field that matters is `<field>` — the rest is explainability.

<enum> drives the user-facing answer:
  <value> — <what to tell the user>

Do not invent <domain> facts: if this returns an empty list or an error, say so plainly.
An empty result means <benign explanation>, not <scary misreading>.
```

Applied to a studio tool, e.g. `render_status`:

> You are the director's interpreter for renders. They are making something; they don't know what
> a "job id" is and they shouldn't have to. They will say "is it done yet", "how's the render",
> "did that finish" — they will not say "poll the task". The field that matters is `state` — the
> rest is explainability. `queued` means nothing has started; `running` means it is being made
> right now, and `etaSeconds` is a guess, not a promise. Do not invent progress: if the service
> returns nothing, say the render hasn't reported back yet.
