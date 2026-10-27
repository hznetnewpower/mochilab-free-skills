# OpenAPI Operation Review

## What it helps with

Inspect OpenAPI3 JSON operations for duplicate IDs, missing responses and undeclared required path parameters.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Review this OpenAPI file for duplicate operation IDs, missing path parameters and missing responses. List findings by endpoint.”**

## What to provide

Upload the target OpenAPI specification. The local checker currently reads JSON.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive an endpoint inventory, located findings and checks outside this review.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

This is a focused static check, not full OpenAPI validation or an API penetration test. References are not resolved and no endpoints are called. Confirm authentication and payload contracts using the actual service docs.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-openapi-contract
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
