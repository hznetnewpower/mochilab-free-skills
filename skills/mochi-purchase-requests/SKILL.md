---
name: mochi-purchase-requests
description: "Calculate decimal purchase-request totals by currency and flag requests above user-provided approval thresholds."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Purchase Request Evidence Desk

Calculate decimal purchase-request totals by currency and flag requests above user-provided approval thresholds.

## Prepare requests with auditable prices

Give each request a unique ID, positive quantity, decimal unit price and currency. Preserve the quote source and date in the procurement notes. Use decimal strings for prices when exact arithmetic matters, and do not mix tax-inclusive and tax-exclusive quotes without labeling them.

## Route amounts to a real approval process

Inspect line totals and totals grouped by currency. Optional currency-specific thresholds indicate which requests need review; they do not grant approval or identify an authorized approver. Tax, shipping and discounts contribute only when represented in the supplied figures.

Verify quotes against the vendor before a purchasing decision and confirm budget ownership through the user's actual process. The helper does not compare current market prices, place orders or execute payments. Deliver the request ledger, arithmetic and outstanding approval questions without treating a calculated threshold as a spending authorization.

## Reproducible request

requests: unique id,quantity,unitPrice,currency, optional quoteSource. approvalThresholds: optional currency-to-threshold map.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
