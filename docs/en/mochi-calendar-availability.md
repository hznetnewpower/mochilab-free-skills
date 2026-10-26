# Shared Availability Finder

## What it does

Calculate shared free intervals from explicitly provided busy ranges with timezone-aware timestamps.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "start": "2026-10-27T09:00:00Z",
  "end": "2026-10-27T12:00:00Z",
  "people": [
    {
      "busy": [
        {
          "start": "2026-10-27T10:00:00Z",
          "end": "2026-10-27T11:00:00Z"
        }
      ]
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Obtain each person's calendar access legitimately. This uses provided availability only; travel buffers, working hours and last-minute changes must be supplied or checked separately before booking.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-calendar-availability
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
