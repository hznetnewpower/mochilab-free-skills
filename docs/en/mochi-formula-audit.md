# Spreadsheet Formula Evidence Audit

## What it helps with

Inspect XLSX formula cells, cached error values and external-link parts without modifying or recalculating the workbook.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Review formulas in this Excel workbook. Locate error markers, external references and cells needing review without changing the file.
```

## What to provide

Upload the workbook and identify any focus sheet or concern.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive a map of formula cells, error markers and external-reference signals.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Missing caches do not prove formulas are wrong; stale caches can be misleading. Use Excel or a compatible calculation engine for real recalculation, then inspect results. No macros or links are executed.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-formula-audit
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
