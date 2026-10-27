---
name: mochi-travel-itinerary
description: "Arrange user-selected itinerary stops, detect time overlaps and keep estimated costs separated by currency."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Timezone Itinerary Organizer

Arrange user-selected itinerary stops, detect time overlaps and keep estimated costs separated by currency.

## Build the day from verified constraints

Collect the traveler’s selected stops, aware start/end times and any supplied costs. Keep costs in their original currencies. Before giving current recommendations, verify opening hours, entry rules, availability and transport information with authoritative live sources.

### Review the sequence as a real journey

Read `itinerary.md` in chronological order and inspect every overlap. Check transfers and buffers independently: the supplied times do not establish feasible travel between locations. Allow for accessibility needs, check-in windows and reservations only when the user has provided or verified them.

Totals are estimates grouped by currency; the helper performs no exchange conversion. It does not reserve accommodation, buy tickets or make payments. Deliver the itinerary with assumptions and unresolved bookings clearly identified. Avoid presenting a fictional sample stop or unverified price as a current recommendation.

## Reproducible request

stops: name,start,end and optional cost,currency. Timestamps need offsets. title optional. Exports itinerary.md.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
