# Event RSVP Capacity Desk

## Reconcile the attendance export

Use a defined cutoff and stable person IDs. Record response status as yes, no, maybe or pending, and use party size for the number of people represented by a positive response. A family or group response must not be counted as a single seat by accident.

## Plan against confirmed attendance

Compare confirmed people with capacity and review meal totals for the relevant accepted parties. Keep uncertain responses separate so that catering and venue decisions can show both committed and possible demand. Resolve duplicate identities in the source rather than silently counting them twice.

Only collect attendee details needed for the event. Public summaries should not expose contact information, dietary identities or the underlying guest list. The helper does not send invitations, chase replies or establish live attendance. Deliver counts with their cutoff and any unresolved source discrepancies before the organizer makes purchasing or capacity decisions.

## Input example

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

Counts reflect the supplied export, not live attendance. Collect only necessary attendee data and do not expose contact details in public reports. No invitation or reminder is sent.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-event-rsvp
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
