# Input contract

commits: id, subject and optional body. version: optional heading. Exports release-notes.md.

## Operational scope

This does not inspect code or validate that commit messages are accurate. Check the actual diff and test evidence; publishing a release remains separate. Preserve issue links and avoid claiming untested fixes.

## Fictional example

```json
{
  "version": "1.1.0",
  "commits": [
    {
      "id": "abc123",
      "subject": "feat!: change interface"
    },
    {
      "id": "def456",
      "subject": "fix: preserve settings"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
