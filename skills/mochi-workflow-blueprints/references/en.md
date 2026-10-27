# Automation Dependency Blueprint

## What it helps with

Validate a workflow dependency graph, detect cycles and separate read-only steps from external mutations.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Design a workflow to collect sales sheets, summarize a weekly report and send it to colleagues. Check dependencies without sending anything.
```

## What to provide

Describe the goal, dependencies and intended deliverable.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive a proposed order, dependency problems and steps that change external systems.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

A validated graph is not a running automation. Map each step to available tools, test with fixtures, and create schedules or external actions only when requested. Define retry limits and idempotency before repeated writes.
