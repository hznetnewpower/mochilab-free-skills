# Form Review and Submission Plan

## What it does

Map requested values to an observed form, identify missing required fields and separate review from final submission.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "fields": [
    {
      "name": "email",
      "required": true
    },
    {
      "name": "message",
      "required": true
    }
  ],
  "values": {
    "email": "demo@example.com",
    "message": "Fictional inquiry"
  }
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Use observed browser fields rather than guessed selectors. The helper never fills or submits a form. Apply the host approval rules to the final browser action, especially purchases, agreements and account permissions.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-form-submission-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
