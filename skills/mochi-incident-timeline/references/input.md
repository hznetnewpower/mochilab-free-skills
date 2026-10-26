# Input contract

events: unique id,at,summary,source. Exports timeline.md; no source systems are queried.

## Operational scope

Distinguish observation time from event time and preserve uncertain reports. Timeline order is not proof of causation. Do not run remediation, delete logs or notify external parties without the user's task authorization.

## Fictional example

```json
{
  "events": [
    {
      "id": "b",
      "at": "2026-10-27T10:05:00Z",
      "summary": "Recovered",
      "source": "synthetic monitor"
    },
    {
      "id": "a",
      "at": "2026-10-27T10:00:00Z",
      "summary": "Failure observed",
      "source": "synthetic log"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
