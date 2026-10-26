# Input contract

files: repository-relative file-name list, obtained from the intended checkout. No repository scanning is performed by the helper.

## Operational scope

File-name signals can be incomplete in monorepos. Read AGENTS.md and project documentation, inspect package scripts and verify the maintained checkout. Do not execute downloaded setup scripts merely because they appear in a manifest.

## Fictional example

```json
{
  "files": [
    "package.json",
    "README.md",
    "AGENTS.md",
    "tests/basic.test.js"
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
