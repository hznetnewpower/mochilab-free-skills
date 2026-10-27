---
name: mochi-launch-checklist
description: "Identify required launch tasks lacking completion or evidence before a human go/no-go decision."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Product Launch Evidence Checklist

Identify required launch tasks lacking completion or evidence before a human go/no-go decision.

## Turn readiness claims into evidence

Build a checklist for the actual launch scope. Give each item a unique ID, distinguish required from optional work, and record a concrete status and evidence location. A statement that someone tested a feature is weaker than a reproducible test receipt or reviewed artifact.

## Examine unresolved required work

A required task needs both done status and nonempty evidence. Review the evidence itself before approving a launch; a populated string is not proof that a result is valid. Explicitly cover rollback, support ownership, known limitations and the installation or upgrade path relevant to this release.

The report is an input to a human release decision. It does not deploy software, accept agreements, send launch announcements or certify compliance. Deliver a short list of blocking items and their owners, preserving optional work separately so that it does not obscure genuine release requirements.

## Reproducible request

tasks: unique id, optional required(default true),status,evidence. Required tasks need done plus nonempty evidence.

The following is fictional fixture data, not a live service result.

```json
{
  "tasks": [
    {
      "id": "smoke",
      "status": "done",
      "evidence": "Fictional test receipt"
    },
    {
      "id": "rollback",
      "status": "pending"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
