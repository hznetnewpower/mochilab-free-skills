# Incident Evidence Timeline

## Keep event time separate from observation time

Collect uniquely identified events with aware timestamps, concise summaries and traceable sources. Preserve the raw records privately. When a source was observed later than the event it describes, record that distinction in the investigation notes rather than replacing one timestamp with the other.

## Reconcile the ordered narrative

Review `timeline.md` against logs, monitor results and human reports. Flag clock differences, missing periods and contradictory evidence. Mark uncertain reports explicitly; chronological proximity does not prove that one event caused another.

The helper orders supplied evidence only. It does not query monitoring systems, infer a root cause, run remediation, delete logs or notify outside parties. Deliver a sourced chronology and open questions, then validate any proposed cause through separate investigation. Keep restoration claims tied to an actual recovery observation instead of a person's expectation.

## Input example

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

Distinguish observation time from event time and preserve uncertain reports. Timeline order is not proof of causation. Do not run remediation, delete logs or notify external parties without the user's task authorization.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-incident-timeline
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
