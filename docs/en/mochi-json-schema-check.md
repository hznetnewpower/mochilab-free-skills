# JSON Contract Subset Check

## Establish a bounded validation question

Ask which object is being checked and which fields the producer guarantees. Put the schema and candidate value in the same request so that the result can be reproduced. A minimum must be a number rather than a numeric-looking string; `required` names object properties, not their truthiness.

### Interpret three different outcomes

An input error means the request or schema shape cannot be processed. Reported data errors mean the candidate violates the implemented subset. Unsupported schema keywords mean coverage is incomplete, even if all supported checks pass. Keep these outcomes separate in the response.

Supported checks cover types, object properties, required fields, array items, enum membership, numeric bounds and rejection of additional properties. For `$ref`, composition, formats or dialect-specific rules, stop short of a production-valid verdict and recommend the project's maintained standards validator. Preserve the failing property location when explaining a correction; do not silently coerce the user's data.

## Input example

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

Use a full standards validator for reference resolution, formats, unions or production schema certification. Boolean schemas and arbitrary schema dialects are not supported.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-json-schema-check
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
