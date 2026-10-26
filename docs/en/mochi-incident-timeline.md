# Incident Evidence Timeline

## What it does

Order sourced incident events by aware timestamps and expose elapsed gaps without inventing a root cause.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "events": [
    {
      "id": "b",
      "at": "2026-10-27T10:05:00Z",
      "summary": "Recovered",
      "source": "synthetic monitor"
    },
    {
      "id": "a",
      "at": "2026-10-27T10:00:00Z",
      "summary": "Failure observed",
      "source": "synthetic log"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Distinguish observation time from event time and preserve uncertain reports. Timeline order is not proof of causation. Do not run remediation, delete logs or notify external parties without the user's task authorization.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-incident-timeline
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
