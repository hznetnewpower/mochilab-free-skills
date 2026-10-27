# OpenAPI Operation Review

## Collect the actual contract

Work from the OpenAPI JSON exported by the intended service or checked-in API revision. Record that revision in the review notes. A rendered API documentation page or a response example is not a replacement for the specification. Set `file` to this JSON inside the selected workspace.

## Triage the findings

- Follow each reported HTTP method and path back to its operation object.
- Resolve duplicate operation IDs by deciding which operation owns the identifier; do not rename IDs without checking generated clients.
- For a `{placeholder}`, inspect both path-level and operation-level declarations and confirm the parameter is required.
- A response map needs meaningful status descriptions and payload schemas even when this limited checker reports no missing responses.

Hand off external references, authentication schemes, callback definitions and dialect validation to a full OpenAPI validator. This helper does not dereference remote schemas or contact the API. Return an operation inventory and unresolved review items, tied to the supplied specification revision.

## Input example

```json
{
  "file": "samples/openapi.json"
}
```

This is a focused static check, not full OpenAPI validation or an API penetration test. References are not resolved and no endpoints are called. Confirm authentication and payload contracts using the actual service docs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-openapi-contract
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
