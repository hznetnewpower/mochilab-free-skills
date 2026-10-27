# Internal input contract for the assistant

title,minutes and agenda required. Each topic has topic, optional minutes and decision. Exports meeting-prep.md.

## Operational scope

This prepares a meeting; it does not extract commitments from a past transcript, send invitations or fetch private attendee records. Cite any background facts used in the real briefing.

## Fictional example

```json
{
  "title": "Fictional planning review",
  "minutes": 30,
  "agenda": [
    {
      "topic": "Choose next milestone",
      "minutes": 20,
      "decision": "Select one option"
    },
    {
      "topic": "Open questions",
      "minutes": 15
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
