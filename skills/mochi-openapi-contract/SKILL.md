---
name: mochi-openapi-contract
description: "Inspect OpenAPI3 JSON operations for duplicate IDs, missing responses and undeclared required path parameters."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# OpenAPI Operation Review

Inspect OpenAPI3 JSON operations for duplicate IDs, missing responses and undeclared required path parameters.

## Collect the actual contract

Work from the OpenAPI JSON exported by the intended service or checked-in API revision. Record that revision in the review notes. A rendered API documentation page or a response example is not a replacement for the specification. Set `file` to this JSON inside the selected workspace.

## Triage the findings

- Follow each reported HTTP method and path back to its operation object.
- Resolve duplicate operation IDs by deciding which operation owns the identifier; do not rename IDs without checking generated clients.
- For a `{placeholder}`, inspect both path-level and operation-level declarations and confirm the parameter is required.
- A response map needs meaningful status descriptions and payload schemas even when this limited checker reports no missing responses.

Hand off external references, authentication schemes, callback definitions and dialect validation to a full OpenAPI validator. This helper does not dereference remote schemas or contact the API. Return an operation inventory and unresolved review items, tied to the supplied specification revision.

## Reproducible request

file: workspace-relative OpenAPI3 JSON. Checks operationId uniqueness, path parameter declarations and response presence.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/openapi.json"
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
