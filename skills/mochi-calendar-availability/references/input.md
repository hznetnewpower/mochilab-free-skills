# Input contract

start,end: aware ISO window. minMinutes: positive duration. people: optional busy list of start/end per person. No live calendar queries.

## Operational scope

Obtain each person's calendar access legitimately. This uses provided availability only; travel buffers, working hours and last-minute changes must be supplied or checked separately before booking.

## Fictional example

```json
{
  "start": "2026-10-27T09:00:00Z",
  "end": "2026-10-27T12:00:00Z",
  "people": [
    {
      "busy": [
        {
          "start": "2026-10-27T10:00:00Z",
          "end": "2026-10-27T11:00:00Z"
        }
      ]
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
