# CI Failure Signal Map

## What it does

Locate test, dependency, compilation, permission and timeout signals in a selected CI log without replaying the pipeline.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "file": "samples/ci.log"
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

A pattern match is a diagnostic lead, not confirmed root cause. Read relevant surrounding lines privately and investigate the earliest causal failure. Do not expose tokens from logs or rerun side-effecting jobs automatically.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-ci-failure-map
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
