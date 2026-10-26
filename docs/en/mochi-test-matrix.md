# Pairwise Test Matrix

## What it does

Generate a bounded greedy pairwise matrix for discrete configuration factors and report coverage without executing tests.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "factors": {
    "os": [
      "linux",
      "windows"
    ],
    "lang": [
      "en",
      "zh"
    ],
    "role": [
      "one",
      "two"
    ]
  }
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Pairwise coverage is not exhaustive behavior coverage and the greedy result is not guaranteed minimal. Include known high-risk combinations and execute the tests separately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-test-matrix
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
