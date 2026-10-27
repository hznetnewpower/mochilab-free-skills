# Cron Timezone Preview

## What it helps with

Preview upcoming five-field cron occurrences with an explicit timezone, including DST transitions.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Preview the next five runs for weekdays at 9am in Asia/Shanghai. Do not create a scheduled task.”**

## What to provide

Describe the frequency and timezone, or paste an existing cron expression.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive the next scheduled times and relevant calendar-rule caveats.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

This is a preview, not a scheduler. Named months/weekdays, macros and seconds are unsupported. Day-of-month and weekday use POSIX OR semantics when both are restricted. Native schedulers can differ; verify the actual scheduler before activation.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-cron-inspector
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
