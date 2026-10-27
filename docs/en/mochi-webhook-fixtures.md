# Webhook Fixture Builder

## What it helps with

Deduplicate selected webhook events by event ID and export replay fixtures without sending network requests.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Deduplicate these webhook events by event ID and prepare local replay fixtures without sending requests.
```

## What to provide

Supply an event export and identify its event-ID field. Remove secrets and unnecessary personal data before sharing.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive replay fixtures and a list of duplicate IDs.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Fixture deduplication is not a production idempotency store. Remove secrets and personal payloads before sharing fixtures. Real delivery requires a separately authorized destination and replay strategy.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-webhook-fixtures
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
