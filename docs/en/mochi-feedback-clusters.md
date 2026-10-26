# Customer Feedback Topic Map

## What it does

Apply user-defined keyword topic labels to selected feedback and expose unmatched records without inferring private traits.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "topics": {
    "speed": [
      "slow",
      "latency"
    ],
    "billing": [
      "invoice"
    ]
  },
  "feedback": [
    {
      "id": "f1",
      "text": "slow response"
    },
    {
      "id": "f2",
      "text": "invoice question"
    },
    {
      "id": "f3",
      "text": "thanks"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This is transparent keyword grouping, not sentiment analysis or semantic clustering. Review ambiguous examples and false positives before making product decisions. No customer reply or external upload occurs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-feedback-clusters
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
