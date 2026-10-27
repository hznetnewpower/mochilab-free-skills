# Purchase Request Evidence Desk

## Prepare requests with auditable prices

Give each request a unique ID, positive quantity, decimal unit price and currency. Preserve the quote source and date in the procurement notes. Use decimal strings for prices when exact arithmetic matters, and do not mix tax-inclusive and tax-exclusive quotes without labeling them.

## Route amounts to a real approval process

Inspect line totals and totals grouped by currency. Optional currency-specific thresholds indicate which requests need review; they do not grant approval or identify an authorized approver. Tax, shipping and discounts contribute only when represented in the supplied figures.

Verify quotes against the vendor before a purchasing decision and confirm budget ownership through the user's actual process. The helper does not compare current market prices, place orders or execute payments. Deliver the request ledger, arithmetic and outstanding approval questions without treating a calculated threshold as a spending authorization.

## Input example

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

This organizes requests; it does not grant approval, compare current market prices or execute payments. Tax and shipping are included only if represented in inputs. Verify quotes and authorized approvers separately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-purchase-requests
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
