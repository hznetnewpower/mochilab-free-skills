# Google Workspace Action Plan

## What it helps with

Plan concrete Gmail, Calendar, Drive, Sheets and Docs actions for an explicitly selected authorized account.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Plan how to find this month’s invoices in my Google mail and summarize them in the selected sheet. Review accounts and resources before editing.
```

## What to provide

Describe the task, intended account and files, using existing authorized connections.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive an action plan and any missing account or resource information.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

The helper does not implement OAuth or call Google. Use an available authorized connector or inspect the installed gog CLI help before executing. Verify account and resource identifiers; do not request refresh tokens in chat.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-google-workspace-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
