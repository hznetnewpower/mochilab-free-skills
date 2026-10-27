# JSON Contract Subset Check

## What it helps with

Check JSON values against an explicitly supported schema subset and report unsupported keywords instead of silently accepting them.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Check this order data: quantity must be a positive integer, the order ID must be present, and unexpected fields are forbidden. Locate failures.
```

## What to provide

Supply the data and validation rules, or an existing schema file.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive field-level failures and a clear account of supported and unsupported checks.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Use a full standards validator for reference resolution, formats, unions or production schema certification. Boolean schemas and arbitrary schema dialects are not supported.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-json-schema-check
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
