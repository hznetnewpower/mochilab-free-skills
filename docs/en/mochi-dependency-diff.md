# Dependency Upgrade Delta

## What it does

Compare explicit dependency version maps and highlight additions, removals and major-version changes.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "before": {
    "alpha": "1.2.0",
    "old": "1.0.0"
  },
  "after": {
    "alpha": "2.0.0",
    "new": "1.0.0"
  }
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

No dependency is installed and no vulnerability database is queried. A major-version flag is a review cue, not a compatibility verdict. Read upstream migration notes and run project checks before upgrading.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-dependency-diff
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
