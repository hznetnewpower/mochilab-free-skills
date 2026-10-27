# Repository Onboarding Map

## What it helps with

Map an explicitly supplied repository file list to ecosystem, documentation and test entry points before running commands.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Map this repository: its stack, documents to read first and test entry points. Do not install dependencies or start services.
```

## What to provide

Provide the intended checkout or file listing and the area you want to understand.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive an onboarding map and a suggested reading order.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

File-name signals can be incomplete in monorepos. Read AGENTS.md and project documentation, inspect package scripts and verify the maintained checkout. Do not execute downloaded setup scripts merely because they appear in a manifest.
