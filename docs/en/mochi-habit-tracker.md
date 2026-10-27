# Personal Habit Completion Review

## Define what one completed day means

Use the user's own completion dates and agree on the cutoff date and observation window. Several records for one date count as one completed day. Clarify the user's local date convention before converting timestamps from another system.

### Interpret the streak conservatively

The streak ending at the cutoff describes consecutive recorded completion dates, not motivation, personal worth or health. Review dates outside the window and future entries as data-quality questions. A missing record may be an unlogged activity rather than a confirmed missed action.

Use the report to describe completion frequency and continuity without creating behavioral profiles or diagnostic claims. This package does not schedule reminders, contact another person or infer sensitive medical information. Return the chosen dates and calculation assumptions with the summary, and preserve corrections to self-recorded data rather than silently rewriting history.

## Input example

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

Only use self-recorded completion data. No health diagnosis, behavioral profiling or automatic reminders. A missed day does not establish motivation or health status; keep interpretation descriptive.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-habit-tracker
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
