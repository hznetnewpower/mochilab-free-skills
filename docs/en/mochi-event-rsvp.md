# Event RSVP Capacity Desk

## What it does

Count explicit RSVP statuses, confirmed party sizes and meal choices while flagging capacity overruns.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "capacity": 2,
  "people": [
    {
      "id": "a",
      "status": "yes",
      "partySize": 2,
      "meal": "standard"
    },
    {
      "id": "b",
      "status": "yes",
      "meal": "vegetarian"
    },
    {
      "id": "c",
      "status": "maybe"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Counts reflect the supplied export, not live attendance. Collect only necessary attendee data and do not expose contact details in public reports. No invitation or reminder is sent.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-event-rsvp
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
