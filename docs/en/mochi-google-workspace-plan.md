# Google Workspace Action Plan

## What it does

Plan concrete Gmail, Calendar, Drive, Sheets and Docs actions for an explicitly selected authorized account.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

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

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

The helper does not implement OAuth or call Google. Use an available authorized connector or inspect the installed gog CLI help before executing. Verify account and resource identifiers; do not request refresh tokens in chat.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-google-workspace-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
