# Internal input contract for the assistant

file: UTF-8 log. Returns matched line numbers and category counts without reproducing full log text.

## Operational scope

A pattern match is a diagnostic lead, not confirmed root cause. Read relevant surrounding lines privately and investigate the earliest causal failure. Do not expose tokens from logs or rerun side-effecting jobs automatically.

## Fictional example

```json
{
  "file": "samples/ci.log"
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
