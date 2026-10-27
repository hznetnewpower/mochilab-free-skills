# Shared Availability Finder

## What it helps with

Calculate shared free intervals from explicitly provided busy ranges with timezone-aware timestamps.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Find a shared 30-minute slot on 28 October 2026 between 9am and noon in Asia/Shanghai. Wang is busy 10–11am and Lee is busy 9–9:30am.”**

## What to provide

Provide the date, timezone, required duration and each person’s busy intervals, or authorized calendar exports.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive shared free intervals for a later booking decision.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Obtain each person's calendar access legitimately. This uses provided availability only; travel buffers, working hours and last-minute changes must be supplied or checked separately before booking.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-calendar-availability
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
