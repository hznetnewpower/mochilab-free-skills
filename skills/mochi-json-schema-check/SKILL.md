---
name: mochi-json-schema-check
description: "Check JSON values against an explicitly supported schema subset and report unsupported keywords instead of silently accepting them."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# JSON Contract Subset Check

Check JSON values against an explicitly supported schema subset and report unsupported keywords instead of silently accepting them.

## Establish a bounded validation question

Ask which object is being checked and which fields the producer guarantees. Put the schema and candidate value in the same request so that the result can be reproduced. A minimum must be a number rather than a numeric-looking string; `required` names object properties, not their truthiness.

### Interpret three different outcomes

An input error means the request or schema shape cannot be processed. Reported data errors mean the candidate violates the implemented subset. Unsupported schema keywords mean coverage is incomplete, even if all supported checks pass. Keep these outcomes separate in the response.

Supported checks cover types, object properties, required fields, array items, enum membership, numeric bounds and rejection of additional properties. For `$ref`, composition, formats or dialect-specific rules, stop short of a production-valid verdict and recommend the project's maintained standards validator. Preserve the failing property location when explaining a correction; do not silently coerce the user's data.

## Reproducible request

schema and value required. Supports type, properties, required, items, enum, minimum, maximum, additionalProperties=false. Unsupported keywords make the verdict incomplete.

The following is fictional fixture data, not a live service result.

```json
{
  "schema": {
    "type": "object",
    "required": [
      "count"
    ],
    "properties": {
      "count": {
        "type": "integer",
        "minimum": 1
      }
    },
    "additionalProperties": false
  },
  "value": {
    "count": 2
  }
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
