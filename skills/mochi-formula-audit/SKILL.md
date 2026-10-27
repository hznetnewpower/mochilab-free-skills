---
name: mochi-formula-audit
description: "Inspect XLSX formula cells, cached error values and external-link parts without modifying or recalculating the workbook."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Spreadsheet Formula Evidence Audit

Inspect XLSX formula cells, cached error values and external-link parts without modifying or recalculating the workbook.

## Audit a preserved workbook copy

Select the XLSX that belongs to this task and retain the original. This check inspects workbook XML without running macros, following external links or invoking a spreadsheet calculation engine. Password-protected or non-XLSX inputs need another workflow.

### Review formula evidence

- Locate each reported formula cell in the corresponding worksheet.
- Treat a missing cached result as a recalculation question, not proof of a bad formula.
- Treat a present cache as a stored value that may be stale.
- Investigate literal REF errors and external-link parts before sharing the workbook.

Open the file in Excel or a compatible engine when real recalculation is required, then verify affected cells and downstream totals. Return the formula inventory and outstanding checks. Do not describe the workbook as visually verified, recalculated or free of all spreadsheet errors based only on this static report.

## Reproducible request

file: relative XLSX path. Returns formula cells, cached-result presence, literal REF errors and external-link parts.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/book.xlsx"
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
