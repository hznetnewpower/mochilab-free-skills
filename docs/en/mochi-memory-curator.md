# Provenance Memory Review

## What it does

Identify conflicting and expired user-selected facts before proposing changes to an agent memory file.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "asOf": "2026-10-27T00:00:00Z",
  "facts": [
    {
      "key": "city",
      "value": "A",
      "source": "user note1"
    },
    {
      "key": "city",
      "value": "B",
      "source": "user note2"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Only include facts the user asked to retain. No chat sweeping, hooks or silent memory writes. Contradictory sources stay visible rather than being resolved by recency alone.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-memory-curator
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
