# Cron Timezone Preview

## What it does

Preview upcoming five-field cron occurrences with an explicit timezone, including DST transitions.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "expression": "0 9 * * 1-5",
  "timezone": "UTC",
  "after": "2026-10-26T08:59:00Z",
  "count": 2
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This is a preview, not a scheduler. Named months/weekdays, macros and seconds are unsupported. Day-of-month and weekday use POSIX OR semantics when both are restricted. Native schedulers can differ; verify the actual scheduler before activation.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-cron-inspector
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
