# Built-in Runtime Tool Evidence

Exact getter expressions and nearby binding candidates, statically recovered. Minified names are scoped; dependency candidates are not an evaluated JSON Schema. Configuration, isEnabled checks, platform, subscription and runtime conditions still determine availability.

## PowerShell

[Tool object, line 199340](../extracted/neo-intelligence.fmt.js#L199340)

```js
get inputSchema() {
      return C48();
    }
```

Binding candidate `C48`, [line 199289](../extracted/neo-intelligence.fmt.js#L199289):

```js
mA(() => BJA ? ow1().omit({ run_in_background: true }) : ow1())
```

## Read

[Tool object, line 202506](../extracted/neo-intelligence.fmt.js#L202506)

```js
get inputSchema() {
        return G88();
      }
```

Binding candidate `G88`, [line 202429](../extracted/neo-intelligence.fmt.js#L202429):

```js
mA(() =>
    j.strictObject({
      file_path: j.string().describe(
        "The absolute path, or current-working-directory-relative path, to the file to read",
      ),
      offset: Kz(j.number().int().nonnegative().optional()).describe(
        "The line number to start reading from. Only provide if the file is too large to read at once",
      ),
      limit: Kz(j.number().int().positive().optional()).describe(
        "The number of lines to read. Only provide if the file is too large to read at once.",
      ),
      pages: j.string().optional().describe(
        `Page range for PDF files (e.g., "1-5", "3", "10-20"). Only applicable to PDF files. Maximum ${yo} pages per request.`,
      ),
    })
  )
```

## ToolSearch

[Tool object, line 202891](../extracted/neo-intelligence.fmt.js#L202891)

```js
get inputSchema() {
      return mM1();
    }
```

Binding candidate `mM1`, [line 202855](../extracted/neo-intelligence.fmt.js#L202855):

```js
mA(() =>
    j.object({
      query: j.string().describe(
        'Query to find deferred tools. Use "select:<tool_name>" for direct selection, or keywords to search.',
      ),
      max_results: j.number().optional().default(5).describe(
        "Maximum number of results to return (default: 5)",
      ),
    })
  )
```

## Write

[Tool object, line 335928](../extracted/neo-intelligence.fmt.js#L335928)

```js
get inputSchema() {
        return Gh8();
      }
```

Binding candidate `Gh8`, [line 335906](../extracted/neo-intelligence.fmt.js#L335906):

```js
mA(() =>
    j.strictObject({
      file_path: j.string().describe(
        "The absolute path to the file to write (must be absolute, not relative)",
      ),
      content: j.string().describe("The content to write to the file"),
    })
  )
```

## Grep

[Tool object, line 336436](../extracted/neo-intelligence.fmt.js#L336436)

```js
get inputSchema() {
        return Uh8();
      }
```

Binding candidate `Uh8`, [line 336384](../extracted/neo-intelligence.fmt.js#L336384):

```js
mA(() =>
    j.strictObject({
      pattern: j.string().describe("The regular expression pattern to search for in file contents"),
      path: j.string().optional().describe(
        "File or directory to search in (rg PATH). Defaults to current working directory.",
      ),
      glob: j.string().optional().describe(
        'Glob pattern to filter files (e.g. "*.js", "*.{ts,tsx}") - maps to rg --glob',
      ),
      output_mode: j.enum(["content", "files_with_matches", "count"]).optional().describe(
        'Output mode: "content" shows matching lines (supports -A/-B/-C context, -n line numbers, head_limit), "files_with_matches" shows file paths (supports head_limit), "count" shows occurrence counts per file (rg --count-matches --with-filename; multiple matches on one line are counted separately; supports head_limit). Defaults to "files_with_matches".',
      ),
      "-B": Kz(j.number().optional()).describe(
        'Number of lines to show before each match (rg -B). Requires output_mode: "content", ignored otherwise.',
      ),
      "-A": Kz(j.number().optional()).describe(
        'Number of lines to show after each match (rg -A). Requires output_mode: "content", ignored otherwise.',
      ),
      "-C": Kz(j.number().optional()).describe("Alias for context."),
      context: Kz(j.number().optional()).describe(
        'Number of lines to show before and after each match (rg -C). Requires output_mode: "content", ignored otherwise.',
      ),
      "-n": FQ(j.boolean().optional()).describe(
        'Show line numbers in output (rg -n). Requires output_mode: "content", ignored otherwise. Defaults to true.',
      ),
      "-i": FQ(j.boolean().optional()).describe("Case insensitive search (rg -i)"),
      type: j.string().optional().describe(
        "File type to search (rg --type). Common types: js, py, rust, go, java, etc. More efficient than include for standard file types.",
      ),
      head_limit: Kz(j.number().optional()).describe(
        'Limit output to first N lines/entries, equivalent to "| head -N". Works across all output modes: content (limits output lines), files_with_matches (limits file paths), count (limits count entries). Defaults to 250 when unspecified. Pass 0 for unlimited (use sparingly \u2014 large result sets waste context).',
      ),
      offset: Kz(j.number().optional()).describe(
        'Skip first N lines/entries before applying head_limit, equivalent to "| tail -n +N | head -N". Works across all output modes. Defaults to 0.',
      ),
      multiline: FQ(j.boolean().optional()).describe(
        "Enable multiline mode where . matches newlines and patterns can span lines (rg -U --multiline-dotall). Default: false.",
      ),
    })
  )
```

## Glob

[Tool object, line 336790](../extracted/neo-intelligence.fmt.js#L336790)

```js
get inputSchema() {
        return Eh8();
      }
```

Binding candidate `Eh8`, [line 336774](../extracted/neo-intelligence.fmt.js#L336774):

```js
mA(() =>
    j.strictObject({
      pattern: j.string().describe("The glob pattern to match files against"),
      path: j.string().optional().describe(
        'The directory to search in. If not specified, the current working directory will be used. IMPORTANT: Omit this field to use the default directory. DO NOT enter "undefined" or "null" - simply omit it for the default behavior. Must be a valid directory path if provided.',
      ),
    })
  )
```

## TodoWrite

[Tool object, line 337376](../extracted/neo-intelligence.fmt.js#L337376)

```js
get inputSchema() {
        return Rh8();
      }
```

Binding candidate `Rh8`, [line 337368](../extracted/neo-intelligence.fmt.js#L337368):

```js
mA(() => j.strictObject({ todos: u2A().describe("The updated todo list") }))
```

## Bash

[Tool object, line 339573](../extracted/neo-intelligence.fmt.js#L339573)

```js
get inputSchema() {
      return s17();
    }
```

Binding candidate `s17`, [line 339501](../extracted/neo-intelligence.fmt.js#L339501):

```js
mA(() =>
      $TA
        ? o17().omit({ run_in_background: true, _simulatedSedEdit: true })
        : o17().omit({ _simulatedSedEdit: true })
    )
```

## Edit

[Tool object, line 339978](../extracted/neo-intelligence.fmt.js#L339978)

```js
get inputSchema() {
      return s26();
    }
```

Binding candidate `s26`, [line 331226](../extracted/neo-intelligence.fmt.js#L331226):

```js
mA(() =>
    j.strictObject({
      file_path: j.string().describe("The absolute path to the file to modify"),
      old_string: j.string().describe("The text to replace"),
      new_string: j.string().describe(
        "The text to replace it with (must be different from old_string)",
      ),
      replace_all: FQ(j.boolean().default(false).optional()).describe(
        "Replace all occurrences of old_string (default false)",
      ),
    })
  )
```

## Agent

[Tool object, line 388874](../extracted/neo-intelligence.fmt.js#L388874)

```js
get inputSchema() {
      return uD0();
    }
```

Binding candidate `uD0`, [line 388770](../extracted/neo-intelligence.fmt.js#L388770):

```js
mA(() => {
      let A7 = W7K().omit({ cwd: true });
      return lF6 || IN() ? A7.omit({ run_in_background: true }) : A7;
    })
```

## AskUserQuestion

[Tool object, line 390184](../extracted/neo-intelligence.fmt.js#L390184)

```js
get inputSchema() {
      return M7K();
    }
```

Binding candidate `M7K`, [line 390167](../extracted/neo-intelligence.fmt.js#L390167):

```js
mA(() =>
      j.strictObject({
        questions: j.array(RF7()).min(1).max(4).describe(
          "Questions to ask the user (1-4 questions)",
        ),
        ...w7K(),
      }).refine(jF7.check, { message: jF7.message })
    )
```

## EnterPlanMode

[Tool object, line 392269](../extracted/neo-intelligence.fmt.js#L392269)

```js
get inputSchema() {
        return N4K();
      }
```

Binding candidate `N4K`, [line 392265](../extracted/neo-intelligence.fmt.js#L392265):

```js
mA(() => j.strictObject({}))
```

## EnterWorktree

[Tool object, line 392432](../extracted/neo-intelligence.fmt.js#L392432)

```js
get inputSchema() {
        return w4K();
      }
```

Binding candidate `w4K`, [line 392412](../extracted/neo-intelligence.fmt.js#L392412):

```js
mA(() =>
    j.strictObject({
      name: j.string().superRefine((A7, q) => {
        try {
          SYA(A7);
        } catch (K) {
          q.addIssue({ code: "custom", message: K.message });
        }
      }).optional().describe(
        'Optional name for the worktree. Each "/"-separated segment may contain only letters, digits, dots, underscores, and dashes; max 64 chars total. A random name is generated if not provided.',
      ),
    })
  )
```

## ExitPlanMode

[Tool object, line 392679](../extracted/neo-intelligence.fmt.js#L392679)

```js
get inputSchema() {
        return CV7();
      }
```

Binding candidate `CV7`, [line 392643](../extracted/neo-intelligence.fmt.js#L392643):

```js
mA(() =>
      j.strictObject({
        allowedPrompts: j.array(j4K()).optional().describe(
          "Prompt-based permissions needed to implement the plan. These describe categories of actions rather than specific commands.",
        ),
      }).passthrough()
    )
```

## ExitWorktree

[Tool object, line 393026](../extracted/neo-intelligence.fmt.js#L393026)

```js
get inputSchema() {
      return b4K();
    }
```

Binding candidate `b4K`, [line 393004](../extracted/neo-intelligence.fmt.js#L393004):

```js
mA(() =>
    j.strictObject({
      action: j.enum(["keep", "remove"]).describe(
        '"keep" leaves the worktree and branch on disk; "remove" deletes both.',
      ),
      discard_changes: j.boolean().optional().describe(
        'Required true when action is "remove" and the worktree has uncommitted files or unmerged commits. The tool will refuse and list them otherwise.',
      ),
    })
  )
```

## LSP

[Tool object, line 394067](../extracted/neo-intelligence.fmt.js#L394067)

```js
get inputSchema() {
        return v4K();
      }
```

Binding candidate `v4K`, [line 394024](../extracted/neo-intelligence.fmt.js#L394024):

```js
mA(() =>
    j.strictObject({
      operation: j.enum([
        "goToDefinition",
        "findReferences",
        "hover",
        "documentSymbol",
        "workspaceSymbol",
        "goToImplementation",
        "prepareCallHierarchy",
        "incomingCalls",
        "outgoingCalls",
      ]).describe("The LSP operation to perform"),
      filePath: j.string().describe("The absolute or relative path to the file"),
      line: j.number().int().positive().describe("The line number (1-based, as shown in editors)"),
      character: j.number().int().positive().describe(
        "The character offset (1-based, as shown in editors)",
      ),
    })
  )
```

## Skill

[Tool object, line 395086](../extracted/neo-intelligence.fmt.js#L395086)

```js
get inputSchema() {
        return A9K();
      }
```

Binding candidate `A9K`, [line 395061](../extracted/neo-intelligence.fmt.js#L395061):

```js
mA(() =>
    j.object({
      skill: j.string().describe(
        "The name of a skill from the available-skills list. Do not guess names.",
      ),
      args: j.string().optional().describe("Optional arguments for the skill"),
    })
  )
```

## TaskCreate

[Tool object, line 395423](../extracted/neo-intelligence.fmt.js#L395423)

```js
get inputSchema() {
        return J9K();
      }
```

Binding candidate `J9K`, [line 395410](../extracted/neo-intelligence.fmt.js#L395410):

```js
mA(() =>
    j.strictObject({
      subject: j.string().describe("A brief title for the task"),
      description: j.string().describe("What needs to be done"),
      activeForm: j.string().optional().describe(
        'Present continuous form shown in spinner when in_progress (e.g., "Running tests")',
      ),
      metadata: j.record(j.string(), j.unknown()).optional().describe(
        "Arbitrary metadata to attach to the task",
      ),
    })
  )
```

## TaskGet

[Tool object, line 395539](../extracted/neo-intelligence.fmt.js#L395539)

```js
get inputSchema() {
        return Q9K();
      }
```

Binding candidate `Q9K`, [line 395526](../extracted/neo-intelligence.fmt.js#L395526):

```js
mA(() => j.strictObject({ taskId: j.string().describe("The ID of the task to retrieve") }))
```

## TaskList

[Tool object, line 395685](../extracted/neo-intelligence.fmt.js#L395685)

```js
get inputSchema() {
        return G9K();
      }
```

Binding candidate `G9K`, [line 395671](../extracted/neo-intelligence.fmt.js#L395671):

```js
mA(() => j.strictObject({}))
```

## TaskOutput

[Tool object, line 396089](../extracted/neo-intelligence.fmt.js#L396089)

```js
get inputSchema() {
      return V9K();
    }
```

Binding candidate `V9K`, [line 396082](../extracted/neo-intelligence.fmt.js#L396082):

```js
mA(() =>
    j.strictObject({
      task_id: j.string().describe("The task ID to get output from"),
      block: FQ(j.boolean().default(true)).describe("Whether to wait for completion"),
      timeout: j.number().min(0).max(600000).default(30000).describe("Max wait time in ms"),
    })
  )
```

## TaskStop

[Tool object, line 396392](../extracted/neo-intelligence.fmt.js#L396392)

```js
get inputSchema() {
        return D9K();
      }
```

Binding candidate `D9K`, [line 396378](../extracted/neo-intelligence.fmt.js#L396378):

```js
mA(() =>
    j.strictObject({
      task_id: j.string().optional().describe("The ID of the background task to stop"),
      shell_id: j.string().optional().describe("Deprecated: use task_id instead"),
    })
  )
```

## TaskUpdate

[Tool object, line 396581](../extracted/neo-intelligence.fmt.js#L396581)

```js
get inputSchema() {
        return M9K();
      }
```

Binding candidate `M9K`, [line 396553](../extracted/neo-intelligence.fmt.js#L396553):

```js
mA(() => {
    let A7 = is().or(j.literal("deleted"));
    return j.strictObject({
      taskId: j.string().describe("The ID of the task to update"),
      subject: j.string().optional().describe("New subject for the task"),
      description: j.string().optional().describe("New description for the task"),
      activeForm: j.string().optional().describe(
        'Present continuous form shown in spinner when in_progress (e.g., "Running tests")',
      ),
      status: A7.optional().describe("New status for the task"),
      addBlocks: j.array(j.string()).optional().describe("Task IDs that this task blocks"),
      addBlockedBy: j.array(j.string()).optional().describe("Task IDs that block this task"),
      owner: j.string().optional().describe("New owner for the task"),
      metadata: j.record(j.string(), j.unknown()).optional().describe(
        "Metadata keys to merge into the task. Set a key to null to delete it.",
      ),
    });
  })
```

## WebFetch

[Tool object, line 413926](../extracted/neo-intelligence.fmt.js#L413926)

```js
get inputSchema() {
      return u3K();
    }
```

Binding candidate `u3K`, [line 413910](../extracted/neo-intelligence.fmt.js#L413910):

```js
mA(() =>
    j.strictObject({
      url: j.string().url().describe("The URL to fetch content from"),
      prompt: j.string().describe("The prompt to run on the fetched content"),
    })
  )
```

## WebSearch

[Tool object, line 414405](../extracted/neo-intelligence.fmt.js#L414405)

```js
get inputSchema() {
        return _5K();
      }
```

Binding candidate `_5K`, [line 414347](../extracted/neo-intelligence.fmt.js#L414347):

```js
mA(() =>
    j.strictObject({
      query: j.string().min(2).describe("The search query to use"),
      provider: j.enum(["auto", "exa", "perplexity", "pplx"]).optional().describe(
        "Optional backend provider override for testing",
      ),
      mode: j.enum(["fast", "balanced", "deep"]).optional().describe(
        "Search depth and latency preference",
      ),
      content: j.enum(["snippet", "highlights", "text"]).optional().describe(
        "How much per-result context to retrieve",
      ),
      content_budget: j.enum(["small", "medium", "large"]).optional().describe(
        "Per-result context budget",
      ),
      recency: j.enum(["any", "hour", "day", "week", "month", "year"]).optional().describe(
        "Prefer results published within this time window",
      ),
      source_policy: j.enum(["general", "official_first"]).optional().describe(
        "Prefer official or primary sources when available",
      ),
      country: j.string().min(2).max(2).optional().describe(
        "Two-letter country code for localized search",
      ),
      allowed_domains: j.array(j.string()).optional().describe(
        "Only include search results from these domains",
      ),
      blocked_domains: j.array(j.string()).optional().describe(
        "Never include search results from these domains",
      ),
    })
  )
```

## TeamCreate

[Tool object, line 431318](../extracted/neo-intelligence.fmt.js#L431318)

```js
get inputSchema() {
      return lXK();
    }
```

Binding candidate `lXK`, [line 431309](../extracted/neo-intelligence.fmt.js#L431309):

```js
mA(() =>
    j.strictObject({
      team_name: j.string().describe("Name for the new team to create."),
      description: j.string().optional().describe("Team description/purpose."),
      agent_type: j.string().optional().describe(
        'Type/role of the team lead (e.g., "researcher", "test-runner"). Used for team file and inter-agent coordination.',
      ),
    })
  )
```

## TeamDelete

[Tool object, line 431460](../extracted/neo-intelligence.fmt.js#L431460)

```js
get inputSchema() {
        return nXK();
      }
```

Binding candidate `nXK`, [line 431459](../extracted/neo-intelligence.fmt.js#L431459):

```js
mA(() => j.strictObject({}))
```

## SendMessage

[Tool object, line 432570](../extracted/neo-intelligence.fmt.js#L432570)

```js
get inputSchema() {
      return VFK();
    }
```

Binding candidate `VFK`, [line 432559](../extracted/neo-intelligence.fmt.js#L432559):

```js
mA(() =>
      j.object({
        to: j.string().describe(
          'Recipient: teammate name, "*" for broadcast, or "bridge:<session-id>" for a Remote Control peer',
        ),
        summary: j.string().optional().describe(
          "A 5-10 word summary shown as a preview in the UI (required when message is a string)",
        ),
        message: j.union([j.string().describe("Plain text message content"), FFK()]),
      })
    )
```

## Monitor

[Tool object, line 433486](../extracted/neo-intelligence.fmt.js#L433486)

```js
get inputSchema() {
      return PFK();
    }
```

Binding candidate `PFK`, [line 433458](../extracted/neo-intelligence.fmt.js#L433458):

```js
mA(() =>
      j.strictObject({
        command: j.string().describe(
          "Shell command or script. Each stdout line is an event; exit ends the watch.",
        ),
        description: j.string().describe(
          "Short human-readable description of what you are monitoring (shown in notifications).",
        ),
        timeout_ms: j.number().min(1000).optional().default(ZT0).describe(
          `Kill the monitor after this deadline. Default ${ZT0}ms, max ${KT0}ms. Ignored when persistent is true.`,
        ),
        persistent: j.boolean().optional().default(false).describe(
          "Run for the lifetime of the session (no timeout). Use for session-length watches like PR monitoring or log tails. Stop with TaskStop.",
        ),
      }).refine((A7) => A7.persistent || (A7.timeout_ms ?? ZT0) <= KT0, {
        message: `timeout_ms must be \u2264 ${KT0}`,
        path: ["timeout_ms"],
      })
    )
```


Unresolved configured names: none.
