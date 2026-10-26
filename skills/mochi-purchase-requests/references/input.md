# Input contract

requests: unique id,quantity,unitPrice,currency, optional quoteSource. approvalThresholds: optional currency-to-threshold map.

## Operational scope

This organizes requests; it does not grant approval, compare current market prices or execute payments. Tax and shipping are included only if represented in inputs. Verify quotes and authorized approvers separately.

## Fictional example

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

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
