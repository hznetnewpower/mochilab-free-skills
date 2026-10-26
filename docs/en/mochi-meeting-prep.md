# Decision-Focused Meeting Prep

## What it does

Prepare a timed agenda, identify topics without a decision target and compare allocated time with the meeting budget.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "title": "Fictional planning review",
  "minutes": 30,
  "agenda": [
    {
      "topic": "Choose next milestone",
      "minutes": 20,
      "decision": "Select one option"
    },
    {
      "topic": "Open questions",
      "minutes": 15
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This prepares a meeting; it does not extract commitments from a past transcript, send invitations or fetch private attendee records. Cite any background facts used in the real briefing.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-meeting-prep
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
