---
name: mochi-utm-campaigns
description: "Build URL-encoded campaign links while preserving ordinary query parameters and refusing obvious embedded credentials."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# UTM Campaign Link Builder

Build URL-encoded campaign links while preserving ordinary query parameters and refusing obvious embedded credentials.

## Agree on campaign naming

Choose consistent source, medium and campaign values before building links. Preserve the destination's existing functional query parameters, such as language or product selection. Use term and content labels only when they answer a defined measurement question.

## Inspect the encoded destinations

Review each generated URL after parameter encoding. Confirm the host and path, ensure required campaign fields are nonempty, and check that spaces and non-ASCII labels survive decoding as intended. Do not place names, email addresses, customer IDs or secrets in public query strings.

The helper neither opens links nor installs an analytics collector. Test the final landing page and attribution behavior with the actual publishing and analytics tools when authorized. Return the link manifest and naming conventions; a generated URL does not prove that a campaign was sent, that tracking exists or that conversions are being recorded.

## Reproducible request

links: url,utm_source,utm_medium,utm_campaign and optional utm_term/utm_content. Required values must be nonempty.

The following is fictional fixture data, not a live service result.

```json
{
  "links": [
    {
      "url": "https://example.com/page?lang=en",
      "utm_source": "newsletter",
      "utm_medium": "email",
      "utm_campaign": "demo launch"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
