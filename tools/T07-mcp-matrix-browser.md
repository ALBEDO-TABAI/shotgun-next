# T07 · `mcp__matrix-browser__*`

**Server:** `matrix-browser` · **2 tools** · **Surface:**
`mcp__matrix-browser__browser_task_message+mcp__matrix-browser__browser_script_run:always-load@1`

Mounted only when the Browser Use plugin is enabled (`MATRIX_BROWSER_USE_ENABLED=1`).
Operating guide: the 947-line `matrix-browser` managed skill, which the agent must load before
use.

---

## 1 · `browser_script_run`

Execute JavaScript in a **persistent per-session VM** with globals `agent`, `display`, `console`.

### Bootstrap (canonical, from the skill)

```js
// cell 1 — acquire, observe only. Never auto-adopt an existing page.
if (!globalThis.browser) { globalThis.browser = await agent.browser }
await browser.tabs.list()
```

```js
// cell 2 — select explicitly
if (typeof tab === "undefined") {
  globalThis.tab = await browser.tabs.get("tab-id-from-list")
}
```

```js
// or create and navigate in the same call
if (typeof tab === "undefined") {
  globalThis.tab = await browser.tabs.new()
  await tab.goto("https://example.com")
}
```

### VM semantics

- Top-level `const` / `let` / `class` **persist across calls** and survive failed calls.
  → temporary variables go in an async IIFE; intentional state goes on `globalThis`.
- The **final expression** is returned as `result`; use `console.log` for log lines.
- **No top-level `return`.**
- Screenshots return byte arrays → `await display(await tab.screenshot(...))` to put them in
  context.
- Short probe scripts (read DOM, count locators, fill a field) should be async IIFEs by default.
- After a runtime reset or lost binding: `browser.tabs.list()` → `browser.tabs.get(id)`.

### Tab semantics

| Call | Scope |
|---|---|
| `browser.tabs.list()` | **all physical pages** — including the human's and other sessions' |
| `browser.tabs.selected()` | only *this* virtual environment's selection (may be empty) |
| `browser.tabs.get(id)` | select an existing physical page |
| `browser.tabs.new()` | create a blank page (navigate immediately if the URL is known) |
| `tab.close()`, `browser.tabs.finalize()` | close **shared physical pages** — affects others |

### Not available in Matrix Browser

```
tab.cua · tab.dom_cua
browser.user.openTabs() → []   · browser.user.claimTab(...) · browser.user.history(...)
visibility.get() → false; set(false) ok; set(true) unsupported
tab.content.export() · tab.content.exportGsuite(...)
tab.playwright.elementInfo(...) · tab.playwright.elementScreenshot(...)
locator.downloadMedia(...) · tab.playwright.waitForEvent("filechooser")
```

Documenting the **absent** APIs is as valuable as documenting the present ones — it stops the
model from retrying a capability that will never work.

---

## 2 · `browser_task_message`

Delegate **one bounded step** to a vision-driven Browser Agent.

```ts
in : { taskId?: string | null,   // null/omitted = new conversation; existing id = continue
       message: string,          // the task description
       timeoutMs?: number }      // default 10 minutes
out: { taskId, ok, actionSummary?, finalResponse?, errorMessage? }
```

Semantics:

- Blocks until **this message** is handled. It is *not* a submit/poll/cancel lifecycle API.
- `taskId` means **conversation continuity only** — not an environment, page, video session or
  concurrency lock.
- The Browser Agent maintains its own current page. `browser_script_run`'s `tab` is **not** an
  implicit input.
- First message should name the URL or the page title/URL explicitly rather than saying
  "the current page".

Example messages, shipped:

```json
{ "message": "打开 https://example.com 并报告标题。" }
{ "message": "打开需要登录的网站并检查当前登录状态。" }
{ "taskId": "existing-task-id",
  "message": "继续刚才的浏览器任务：在当前页面点击搜索框，输入 Matrix Browser，然后报告搜索结果是否出现。" }
```

---

## Choosing between them

| Prefer `script_run` | Prefer `task_message` |
|---|---|
| stable page structure, precise DOM/Playwright expression | unstable DOM, clear visual path |
| repeated checks, local verification | one step needing visual judgment |
| reading structured page state | strict script detection (e.g. Xiaohongshu) |
| scraping / parsing lots of page data | — |

Hard rules from the skill:

> "能用脚本就不用视觉" — if a script can do it, don't use vision.
>
> "不要把整个任务交给 Browser Agent；只委托一个边界清晰的步骤，然后继续由你掌控任务" — delegate
> one bounded step, then keep control.

And the escalation ladder that precedes both (from the department prompt):

```
WebFetch → WebSearch → service API/CLI via Bash → Matrix Browser
```

> "Don't open a browser just to read information a fetch, search, or API call would have returned."

---

## shotgun-next mapping

Keep both tools and the dual-mode philosophy. Studio uses: reference gathering, competitor/mood
research, publishing flows, and client-portal interactions.

Changes:

- **Per-role browser profiles.** A research seat and a publishing seat must not share cookies.
- **Per-site policy** with an explicit "acting as you on `<site>`" confirmation for
  authenticated actions.
- Keep the skill's absent-API list and the platform-specific warnings — they are hard-won and
  they prevent real damage.
