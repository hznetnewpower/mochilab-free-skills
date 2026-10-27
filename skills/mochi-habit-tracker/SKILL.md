---
name: mochi-habit-tracker
description: "Calculate unique completion days, a streak ending on an explicit date and a bounded-window completion rate."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Personal Habit Completion Review

Calculate unique completion days, a streak ending on an explicit date and a bounded-window completion rate.

## Define what one completed day means

Use the user's own completion dates and agree on the cutoff date and observation window. Several records for one date count as one completed day. Clarify the user's local date convention before converting timestamps from another system.

### Interpret the streak conservatively

The streak ending at the cutoff describes consecutive recorded completion dates, not motivation, personal worth or health. Review dates outside the window and future entries as data-quality questions. A missing record may be an unlogged activity rather than a confirmed missed action.

Use the report to describe completion frequency and continuity without creating behavioral profiles or diagnostic claims. This package does not schedule reminders, contact another person or infer sensitive medical information. Return the chosen dates and calculation assumptions with the summary, and preserve corrections to self-recorded data rather than silently rewriting history.

## Reproducible request

dates: ISO dates. asOf: ISO cutoff date. windowDays:1..3660 default30. Duplicate dates count once.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
