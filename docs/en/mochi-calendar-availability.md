# Shared Availability Finder

## Define the scheduling window

Ask for a start, end, minimum meeting duration and the timezones participants actually use. Supply aware ISO timestamps with offsets. Collect busy intervals only from calendars the user is authorized to access, and record the export cutoff because availability changes.

## Interpret the remaining intervals

The helper removes supplied busy time from the chosen window and returns gaps long enough for the requested duration. Check that every proposed slot sits inside the window and clear of all supplied conflicts. Convert display times for each participant without changing the underlying instant.

Working hours, travel buffers, holidays and tentative holds must be represented in the inputs or reviewed separately. Absence of a busy record does not prove a person is free. Recheck the selected time in the actual calendars before creating an event. Return candidate intervals and the assumptions used; this tool does not book a meeting or send invitations.

## Input example

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

Obtain each person's calendar access legitimately. This uses provided availability only; travel buffers, working hours and last-minute changes must be supplied or checked separately before booking.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-calendar-availability
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
