# Google Workspace Action Plan

## Bind every action to an account

Start with the user's concrete objective and the account that should perform it. For each planned step, record the supported action kind plus its query or resource identifier. A document title is not a stable document ID, and an account shown in one connector is not automatically the account used by another tool.

### Read first, then review changes

Use search or list actions to locate the intended email, calendar, Drive file, spreadsheet or document. Inspect the selected object before drafting a mutating action. For writes, preserve the exact destination and describe what will change; verify the live result with the authorized connector after execution.

This package creates a plan only. It neither implements Google OAuth nor calls Google APIs. If the environment uses a CLI, inspect that installed CLI's help instead of inventing flags. Never ask users to paste refresh tokens into conversation. A successful local report is not evidence that mail was sent, an event was created or a document was updated.

## Input example

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

The helper does not implement OAuth or call Google. Use an available authorized connector or inspect the installed gog CLI help before executing. Verify account and resource identifiers; do not request refresh tokens in chat.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-google-workspace-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
