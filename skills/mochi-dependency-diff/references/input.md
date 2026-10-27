# Internal input contract for the assistant

before and after: package-name to exact-version maps. Major change detection applies only to numeric major prefixes.

## Operational scope

No dependency is installed and no vulnerability database is queried. A major-version flag is a review cue, not a compatibility verdict. Read upstream migration notes and run project checks before upgrading.

## Fictional example

```json
{
  "before": {
    "alpha": "1.2.0",
    "old": "1.0.0"
  },
  "after": {
    "alpha": "2.0.0",
    "new": "1.0.0"
  }
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
