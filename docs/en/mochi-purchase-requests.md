# Purchase Request Evidence Desk

## What it does

Calculate decimal purchase-request totals by currency and flag requests above user-provided approval thresholds.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "requests": [
    {
      "id": "r1",
      "quantity": 3,
      "unitPrice": "0.10",
      "currency": "USD",
      "quoteSource": "Fictional quote"
    }
  ],
  "approvalThresholds": {
    "USD": "0.20"
  }
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This organizes requests; it does not grant approval, compare current market prices or execute payments. Tax and shipping are included only if represented in inputs. Verify quotes and authorized approvers separately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-purchase-requests
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
