# DOCX Comments and Revisions Map

## What it does

Map comments, their paragraph anchors and tracked insertions or deletions in a DOCX without accepting changes.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "file": "samples/review.docx"
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This is evidence extraction, not legal review, full Word review-state validation or visual layout QA. It does not accept/reject changes or edit comments. Inspect modern threaded/resolved comments and document appearance in Word separately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-docx-review-map
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
