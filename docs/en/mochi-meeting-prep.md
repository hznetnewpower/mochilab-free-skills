# Decision-Focused Meeting Prep

## Design the meeting around decisions

Clarify the meeting title, total duration and the decision each agenda item should support. Give topics explicit minute budgets where possible. Background facts should come from supplied notes or cited sources; do not invent participant roles or unresolved commitments.

### Resolve an over-budget agenda

Compare allocated minutes with the total. If topics exceed the budget, propose which decisions must stay and which discussion can move to written follow-up. Leave room for an opening, transitions and clear next steps instead of distributing every minute mechanically.

Review the generated `meeting-prep.md` for actionable topic wording, evidence needed and decision ownership. This is a preparation document, not a transcript analysis or an invitation. The helper does not retrieve private attendee records, send calendar events or assert that an absent participant agreed. Deliver the brief and call out decisions that still lack an owner or supporting material.

## Input example

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

This prepares a meeting; it does not extract commitments from a past transcript, send invitations or fetch private attendee records. Cite any background facts used in the real briefing.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-meeting-prep
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
