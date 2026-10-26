# Automation Dependency Blueprint

## What it does

Validate a workflow dependency graph, detect cycles and separate read-only steps from external mutations.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "steps": [
    {
      "id": "collect"
    },
    {
      "id": "summarize",
      "needs": [
        "collect"
      ]
    },
    {
      "id": "send",
      "needs": [
        "summarize"
      ],
      "mutates": true
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

A validated graph is not a running automation. Map each step to available tools, test with fixtures, and create schedules or external actions only when requested. Define retry limits and idempotency before repeated writes.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-workflow-blueprints
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
