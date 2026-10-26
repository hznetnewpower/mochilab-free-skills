# Personal Habit Completion Review

## What it does

Calculate unique completion days, a streak ending on an explicit date and a bounded-window completion rate.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "dates": [
    "2026-10-25",
    "2026-10-26",
    "2026-10-27",
    "2026-10-27"
  ],
  "asOf": "2026-10-27",
  "windowDays": 7
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Only use self-recorded completion data. No health diagnosis, behavioral profiling or automatic reminders. A missed day does not establish motivation or health status; keep interpretation descriptive.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-habit-tracker
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
