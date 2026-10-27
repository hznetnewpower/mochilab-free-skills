# Incident Evidence Timeline

## What it helps with

Order sourced incident events by aware timestamps and expose elapsed gaps without inventing a root cause.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Build an incident timeline from these logs and notes, citing each event and calculating gaps. Do not infer a root cause or run repairs.”**

## What to provide

Provide logs or event records and their timezone, distinguishing occurrence from report times.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive a sourced timeline, elapsed gaps and unresolved timestamps.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Distinguish observation time from event time and preserve uncertain reports. Timeline order is not proof of causation. Do not run remediation, delete logs or notify external parties without the user's task authorization.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-incident-timeline
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
