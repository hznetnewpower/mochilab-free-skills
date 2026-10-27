---
name: mochi-incident-timeline
description: "Order sourced incident events by aware timestamps and expose elapsed gaps without inventing a root cause."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Incident Evidence Timeline

Order sourced incident events by aware timestamps and expose elapsed gaps without inventing a root cause.

## Keep event time separate from observation time

Collect uniquely identified events with aware timestamps, concise summaries and traceable sources. Preserve the raw records privately. When a source was observed later than the event it describes, record that distinction in the investigation notes rather than replacing one timestamp with the other.

## Reconcile the ordered narrative

Review `timeline.md` against logs, monitor results and human reports. Flag clock differences, missing periods and contradictory evidence. Mark uncertain reports explicitly; chronological proximity does not prove that one event caused another.

The helper orders supplied evidence only. It does not query monitoring systems, infer a root cause, run remediation, delete logs or notify outside parties. Deliver a sourced chronology and open questions, then validate any proposed cause through separate investigation. Keep restoration claims tied to an actual recovery observation instead of a person's expectation.

## Reproducible request

events: unique id,at,summary,source. Exports timeline.md; no source systems are queried.

The following is fictional fixture data, not a live service result.

```json
{
  "events": [
    {
      "id": "b",
      "at": "2026-10-27T10:05:00Z",
      "summary": "Recovered",
      "source": "synthetic monitor"
    },
    {
      "id": "a",
      "at": "2026-10-27T10:00:00Z",
      "summary": "Failure observed",
      "source": "synthetic log"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
