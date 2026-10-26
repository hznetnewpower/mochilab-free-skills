# Webhook Fixture Builder

## What it does

Deduplicate selected webhook events by event ID and export replay fixtures without sending network requests.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "events": [
    {
      "id": "one",
      "payload": {
        "n": 1
      }
    },
    {
      "id": "one",
      "payload": {
        "n": 1
      }
    },
    {
      "id": "two",
      "payload": {
        "n": 2
      }
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Fixture deduplication is not a production idempotency store. Remove secrets and personal payloads before sharing fixtures. Real delivery requires a separately authorized destination and replay strategy.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-webhook-fixtures
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
