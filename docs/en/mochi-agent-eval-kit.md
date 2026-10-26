# Agent Response Regression Kit

## What it does

Evaluate recorded agent replies against explicit required, forbidden and exact text expectations without calling a model.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "cases": [
    {
      "id": "timezone",
      "actual": "09:00 UTC",
      "mustContain": [
        "UTC"
      ],
      "mustNotContain": [
        "API_KEY"
      ]
    },
    {
      "id": "exact",
      "actual": "done",
      "exact": "done"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

These are deterministic assertions on supplied replies, not a semantic intelligence score. Generate realistic cases, keep held-out cases separate, and report model execution separately. Do not automatically rewrite agent instructions.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-agent-eval-kit
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
