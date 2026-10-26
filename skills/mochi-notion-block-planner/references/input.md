# Input contract

file: UTF-8 plain Markdown. Supports headings1..3, bullet lines and paragraphs; rich text is chunked to1900 characters. Exports notion-blocks.json.

## Operational scope

Not a full Markdown renderer; tables, code fences, links and formatting need explicit mapping. No Notion API call occurs. For upload, use the intended page and authorized connector, and respect its current batch limits.

## Fictional example

```json
{
  "file": "samples/note.md"
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
