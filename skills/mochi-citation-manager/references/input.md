# Internal input contract for the assistant

records: id,title, optional authors list,year,doi. Exact normalized DOI/title deduplication. Exports references.bib.

## Operational scope

No DOI resolution, scholarly search or truth verification. Preserve distinct editions and corrections when bibliographically meaningful. Check exact publication metadata against the publisher before final citation.

## Fictional example

```json
{
  "records": [
    {
      "id": "demo1",
      "title": "Fictional report",
      "authors": [
        "Example Author"
      ],
      "year": 2026,
      "doi": "https://doi.org/10.0000/demo"
    },
    {
      "id": "demo2",
      "title": "Same record",
      "doi": "10.0000/demo"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
