# OpenAPI Operation Review

## What it does

Inspect OpenAPI3 JSON operations for duplicate IDs, missing responses and undeclared required path parameters.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "file": "samples/openapi.json"
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This is a focused static check, not full OpenAPI validation or an API penetration test. References are not resolved and no endpoints are called. Confirm authentication and payload contracts using the actual service docs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-openapi-contract
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
