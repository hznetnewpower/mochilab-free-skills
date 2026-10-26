# Input contract

dates: ISO dates. asOf: ISO cutoff date. windowDays:1..3660 default30. Duplicate dates count once.

## Operational scope

Only use self-recorded completion data. No health diagnosis, behavioral profiling or automatic reminders. A missed day does not establish motivation or health status; keep interpretation descriptive.

## Fictional example

```json
{
  "dates": [
    "2026-10-25",
    "2026-10-26",
    "2026-10-27",
    "2026-10-27"
  ],
  "asOf": "2026-10-27",
  "windowDays": 7
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
