# Product Launch Evidence Checklist

## Turn readiness claims into evidence

Build a checklist for the actual launch scope. Give each item a unique ID, distinguish required from optional work, and record a concrete status and evidence location. A statement that someone tested a feature is weaker than a reproducible test receipt or reviewed artifact.

## Examine unresolved required work

A required task needs both done status and nonempty evidence. Review the evidence itself before approving a launch; a populated string is not proof that a result is valid. Explicitly cover rollback, support ownership, known limitations and the installation or upgrade path relevant to this release.

The report is an input to a human release decision. It does not deploy software, accept agreements, send launch announcements or certify compliance. Deliver a short list of blocking items and their owners, preserving optional work separately so that it does not obscure genuine release requirements.

## Input example

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

A checked box is not a compliance certificate. Verify actual artifacts, support ownership, rollback and known limitations. The helper does not deploy, send announcements or accept agreements.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-launch-checklist
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
