# Product Launch Evidence Checklist

## What it does

Identify required launch tasks lacking completion or evidence before a human go/no-go decision.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "tasks": [
    {
      "id": "smoke",
      "status": "done",
      "evidence": "Fictional test receipt"
    },
    {
      "id": "rollback",
      "status": "pending"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

A checked box is not a compliance certificate. Verify actual artifacts, support ownership, rollback and known limitations. The helper does not deploy, send announcements or accept agreements.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-launch-checklist
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
