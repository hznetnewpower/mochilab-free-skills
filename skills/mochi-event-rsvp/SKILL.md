---
name: mochi-event-rsvp
description: "Count explicit RSVP statuses, confirmed party sizes and meal choices while flagging capacity overruns."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Event RSVP Capacity Desk

Count explicit RSVP statuses, confirmed party sizes and meal choices while flagging capacity overruns.

## Reconcile the attendance export

Use a defined cutoff and stable person IDs. Record response status as yes, no, maybe or pending, and use party size for the number of people represented by a positive response. A family or group response must not be counted as a single seat by accident.

## Plan against confirmed attendance

Compare confirmed people with capacity and review meal totals for the relevant accepted parties. Keep uncertain responses separate so that catering and venue decisions can show both committed and possible demand. Resolve duplicate identities in the source rather than silently counting them twice.

Only collect attendee details needed for the event. Public summaries should not expose contact information, dietary identities or the underlying guest list. The helper does not send invitations, chase replies or establish live attendance. Deliver counts with their cutoff and any unresolved source discrepancies before the organizer makes purchasing or capacity decisions.

## Reproducible request

capacity: integer. people: unique id,status(yes/no/maybe/pending), optional positive partySize and meal.

The following is fictional fixture data, not a live service result.

```json
{
  "capacity": 2,
  "people": [
    {
      "id": "a",
      "status": "yes",
      "partySize": 2,
      "meal": "standard"
    },
    {
      "id": "b",
      "status": "yes",
      "meal": "vegetarian"
    },
    {
      "id": "c",
      "status": "maybe"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
