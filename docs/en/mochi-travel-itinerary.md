# Timezone Itinerary Organizer

## Build the day from verified constraints

Collect the traveler’s selected stops, aware start/end times and any supplied costs. Keep costs in their original currencies. Before giving current recommendations, verify opening hours, entry rules, availability and transport information with authoritative live sources.

### Review the sequence as a real journey

Read `itinerary.md` in chronological order and inspect every overlap. Check transfers and buffers independently: the supplied times do not establish feasible travel between locations. Allow for accessibility needs, check-in windows and reservations only when the user has provided or verified them.

Totals are estimates grouped by currency; the helper performs no exchange conversion. It does not reserve accommodation, buy tickets or make payments. Deliver the itinerary with assumptions and unresolved bookings clearly identified. Avoid presenting a fictional sample stop or unverified price as a current recommendation.

## Input example

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

Current travel recommendations, opening hours, entry rules, fares and availability require live verification. User-supplied times are not verified transit times. No booking, payment or exchange-rate conversion occurs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-travel-itinerary
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
