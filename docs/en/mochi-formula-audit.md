# Spreadsheet Formula Evidence Audit

## Audit a preserved workbook copy

Select the XLSX that belongs to this task and retain the original. This check inspects workbook XML without running macros, following external links or invoking a spreadsheet calculation engine. Password-protected or non-XLSX inputs need another workflow.

### Review formula evidence

- Locate each reported formula cell in the corresponding worksheet.
- Treat a missing cached result as a recalculation question, not proof of a bad formula.
- Treat a present cache as a stored value that may be stale.
- Investigate literal REF errors and external-link parts before sharing the workbook.

Open the file in Excel or a compatible engine when real recalculation is required, then verify affected cells and downstream totals. Return the formula inventory and outstanding checks. Do not describe the workbook as visually verified, recalculated or free of all spreadsheet errors based only on this static report.

## Input example

```json
{
  "file": "samples/book.xlsx"
}
```

Missing caches do not prove formulas are wrong; stale caches can be misleading. Use Excel or a compatible calculation engine for real recalculation, then inspect results. No macros or links are executed.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-formula-audit
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
