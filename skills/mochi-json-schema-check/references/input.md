# Internal input contract for the assistant

schema and value required. Supports type, properties, required, items, enum, minimum, maximum, additionalProperties=false. Unsupported keywords make the verdict incomplete.

## Operational scope

Use a full standards validator for reference resolution, formats, unions or production schema certification. Boolean schemas and arbitrary schema dialects are not supported.

## Fictional example

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

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
