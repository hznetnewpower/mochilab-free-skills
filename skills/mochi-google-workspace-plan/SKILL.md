---
name: mochi-google-workspace-plan
description: "Plan concrete Gmail, Calendar, Drive, Sheets and Docs actions for an explicitly selected authorized account."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Google Workspace Action Plan

Plan concrete Gmail, Calendar, Drive, Sheets and Docs actions for an explicitly selected authorized account.

## Bind every action to an account

Start with the user's concrete objective and the account that should perform it. For each planned step, record the supported action kind plus its query or resource identifier. A document title is not a stable document ID, and an account shown in one connector is not automatically the account used by another tool.

### Read first, then review changes

Use search or list actions to locate the intended email, calendar, Drive file, spreadsheet or document. Inspect the selected object before drafting a mutating action. For writes, preserve the exact destination and describe what will change; verify the live result with the authorized connector after execution.

This package creates a plan only. It neither implements Google OAuth nor calls Google APIs. If the environment uses a CLI, inspect that installed CLI's help instead of inventing flags. Never ask users to paste refresh tokens into conversation. A successful local report is not evidence that mail was sent, an event was created or a document was updated.

## Reproducible request

actions: kind, account, resource or query. Supports documented planning labels for gmail.search/draft,calendar.list/create,drive.list/upload,sheets.read/update,docs.read/update.

The following is fictional fixture data, not a live service result.

```json
{
  "actions": [
    {
      "kind": "gmail.search",
      "account": "demo@example.com",
      "query": "subject:invoice"
    },
    {
      "kind": "docs.update",
      "account": "demo@example.com",
      "resource": "fictional-document"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
