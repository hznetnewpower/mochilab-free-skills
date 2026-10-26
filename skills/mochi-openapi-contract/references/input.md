# Input contract

file: workspace-relative OpenAPI3 JSON. Checks operationId uniqueness, path parameter declarations and response presence.

## Operational scope

This is a focused static check, not full OpenAPI validation or an API penetration test. References are not resolved and no endpoints are called. Confirm authentication and payload contracts using the actual service docs.

## Fictional example

```json
{
  "file": "samples/openapi.json"
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
