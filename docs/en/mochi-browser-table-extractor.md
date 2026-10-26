# Browser Table Capture

## What it does

Turn a selected HTML table from an authorized browser capture into a quoted CSV with source attribution.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "file": "samples/table.html",
  "table": 0,
  "sourceUrl": "https://example.com/demo"
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Capture the page with an available browser first. This parser handles outer HTML tables, not nested-table fidelity, JavaScript grids or infinite scrolling. Do not claim the whole site was crawled.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-browser-table-extractor
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
