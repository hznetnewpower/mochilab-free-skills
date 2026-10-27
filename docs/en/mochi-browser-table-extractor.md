# Browser Table Capture

## What it helps with

Turn a selected HTML table from an authorized browser capture into a quoted CSV with source attribution.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Export the price table on this webpage to CSV, preserving its headings, product names and source link.
```

## What to provide

Provide a page link or saved HTML file, and identify the table if several are present.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive a CSV file with the source and a clear statement of what was captured.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Capture the page with an available browser first. This parser handles outer HTML tables, not nested-table fidelity, JavaScript grids or infinite scrolling. Do not claim the whole site was crawled.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-browser-table-extractor
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
