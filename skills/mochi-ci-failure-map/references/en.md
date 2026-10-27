# CI Failure Signal Map

## What it helps with

Locate test, dependency, compilation, permission and timeout signals in a selected CI log without replaying the pipeline.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Review this failed CI log. Identify the earliest useful error signals and line numbers without rerunning deployment.
```

## What to provide

Supply the log for the failing run, with its run ID and revision if available.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive categorized error signals, locations and next investigation steps.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

A pattern match is a diagnostic lead, not confirmed root cause. Read relevant surrounding lines privately and investigate the earliest causal failure. Do not expose tokens from logs or rerun side-effecting jobs automatically.
