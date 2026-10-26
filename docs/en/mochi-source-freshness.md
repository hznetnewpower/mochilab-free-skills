# Source Freshness Review

## What it does

Compare explicitly dated sources with a research cutoff and flag stale, undated or future-dated records.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "asOf": "2026-10-27T00:00:00Z",
  "maxAgeDays": 30,
  "sources": [
    {
      "id": "a",
      "url": "https://example.com/a",
      "publishedAt": "2026-08-01T00:00:00Z"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Publication dates and event dates differ. The helper evaluates provided dates, not factual truth or website changes. Browse the original source when a stale claim affects the answer.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-source-freshness
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
