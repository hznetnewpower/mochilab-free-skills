# Social Draft Batch Review

## What it does

Review draft posts against user-supplied platform character limits and asset lists without scheduling or publishing.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "platformLimits": {
    "demo": 5
  },
  "posts": [
    {
      "id": "p1",
      "platform": "demo",
      "text": "hello"
    },
    {
      "id": "p2",
      "platform": "demo",
      "text": "too long"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Platforms may use weighted characters or URL rules. Confirm current platform limits and use the platform composer before publishing; this count is not a final platform acceptance check. No account login or scheduling occurs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-social-batch-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
