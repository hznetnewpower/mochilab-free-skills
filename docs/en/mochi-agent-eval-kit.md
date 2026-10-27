# Agent Response Regression Kit

## What it helps with

Evaluate recorded agent replies against explicit required, forbidden and exact text expectations without calling a model.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Check these recorded assistant replies. Each must state a timezone and none may contain an API key. Flag failures.”**

## What to provide

Provide recorded replies and explicit required, forbidden or exact-text expectations.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive per-reply pass/fail results and the failed conditions.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

These are deterministic assertions on supplied replies, not a semantic intelligence score. Generate realistic cases, keep held-out cases separate, and report model execution separately. Do not automatically rewrite agent instructions.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-agent-eval-kit
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
