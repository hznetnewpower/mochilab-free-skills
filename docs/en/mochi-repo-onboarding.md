# Repository Onboarding Map

## What it does

Map an explicitly supplied repository file list to ecosystem, documentation and test entry points before running commands.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "files": [
    "package.json",
    "README.md",
    "AGENTS.md",
    "tests/basic.test.js"
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

File-name signals can be incomplete in monorepos. Read AGENTS.md and project documentation, inspect package scripts and verify the maintained checkout. Do not execute downloaded setup scripts merely because they appear in a manifest.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-repo-onboarding
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
