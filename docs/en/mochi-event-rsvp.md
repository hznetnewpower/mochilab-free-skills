# Event RSVP Capacity Desk

## What it helps with

Count explicit RSVP statuses, confirmed party sizes and meal choices while flagging capacity overruns.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Reconcile event RSVPs: Wang confirms a party of 3; Lee confirms 1 vegetarian guest; Chen is undecided. Capacity is 10. Summarize confirmed seats, uncertainty and missing meal details.
```

## What to provide

Paste replies or upload a sign-up sheet and provide capacity. Ambiguous party sizes should be clarified.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

For this example: 4 confirmed people, 1 undecided response and no capacity overrun; 1 known vegetarian meal, with meal preferences for Wang’s party of 3 still unknown.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Counts reflect the supplied export, not live attendance. Collect only necessary attendee data and do not expose contact details in public reports. No invitation or reminder is sent.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-event-rsvp
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
