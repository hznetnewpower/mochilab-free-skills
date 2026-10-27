---
name: mochi-meeting-prep
description: "Prepare a timed agenda, identify topics without a decision target and compare allocated time with the meeting budget."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Decision-Focused Meeting Prep

Prepare a timed agenda, identify topics without a decision target and compare allocated time with the meeting budget.

## Design the meeting around decisions

Clarify the meeting title, total duration and the decision each agenda item should support. Give topics explicit minute budgets where possible. Background facts should come from supplied notes or cited sources; do not invent participant roles or unresolved commitments.

### Resolve an over-budget agenda

Compare allocated minutes with the total. If topics exceed the budget, propose which decisions must stay and which discussion can move to written follow-up. Leave room for an opening, transitions and clear next steps instead of distributing every minute mechanically.

Review the generated `meeting-prep.md` for actionable topic wording, evidence needed and decision ownership. This is a preparation document, not a transcript analysis or an invitation. The helper does not retrieve private attendee records, send calendar events or assert that an absent participant agreed. Deliver the brief and call out decisions that still lack an owner or supporting material.

## Reproducible request

title,minutes and agenda required. Each topic has topic, optional minutes and decision. Exports meeting-prep.md.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
