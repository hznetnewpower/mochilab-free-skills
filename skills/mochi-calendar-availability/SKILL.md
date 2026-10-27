---
name: mochi-calendar-availability
description: "Calculate shared free intervals from explicitly provided busy ranges with timezone-aware timestamps."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Shared Availability Finder

Calculate shared free intervals from explicitly provided busy ranges with timezone-aware timestamps.

## Define the scheduling window

Ask for a start, end, minimum meeting duration and the timezones participants actually use. Supply aware ISO timestamps with offsets. Collect busy intervals only from calendars the user is authorized to access, and record the export cutoff because availability changes.

## Interpret the remaining intervals

The helper removes supplied busy time from the chosen window and returns gaps long enough for the requested duration. Check that every proposed slot sits inside the window and clear of all supplied conflicts. Convert display times for each participant without changing the underlying instant.

Working hours, travel buffers, holidays and tentative holds must be represented in the inputs or reviewed separately. Absence of a busy record does not prove a person is free. Recheck the selected time in the actual calendars before creating an event. Return candidate intervals and the assumptions used; this tool does not book a meeting or send invitations.

## Reproducible request

start,end: aware ISO window. minMinutes: positive duration. people: optional busy list of start/end per person. No live calendar queries.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
