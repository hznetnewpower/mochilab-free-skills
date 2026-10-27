# Internal input contract for the assistant

file: relative XLSX path. Returns formula cells, cached-result presence, literal REF errors and external-link parts.

## Operational scope

Missing caches do not prove formulas are wrong; stale caches can be misleading. Use Excel or a compatible calculation engine for real recalculation, then inspect results. No macros or links are executed.

## Fictional example

```json
{
  "file": "samples/book.xlsx"
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
