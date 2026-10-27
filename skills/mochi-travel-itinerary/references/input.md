# Internal input contract for the assistant

stops: name,start,end and optional cost,currency. Timestamps need offsets. title optional. Exports itinerary.md.

## Operational scope

Current travel recommendations, opening hours, entry rules, fares and availability require live verification. User-supplied times are not verified transit times. No booking, payment or exchange-rate conversion occurs.

## Fictional example

```json
{
  "title": "Fictional day plan",
  "stops": [
    {
      "name": "Museum",
      "start": "2026-11-01T09:00:00+08:00",
      "end": "2026-11-01T10:00:00+08:00",
      "cost": "20",
      "currency": "CNY"
    },
    {
      "name": "Cafe",
      "start": "2026-11-01T10:30:00+08:00",
      "end": "2026-11-01T11:00:00+08:00",
      "cost": "5",
      "currency": "USD"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
