# UTM Campaign Link Builder

## Agree on campaign naming

Choose consistent source, medium and campaign values before building links. Preserve the destination's existing functional query parameters, such as language or product selection. Use term and content labels only when they answer a defined measurement question.

## Inspect the encoded destinations

Review each generated URL after parameter encoding. Confirm the host and path, ensure required campaign fields are nonempty, and check that spaces and non-ASCII labels survive decoding as intended. Do not place names, email addresses, customer IDs or secrets in public query strings.

The helper neither opens links nor installs an analytics collector. Test the final landing page and attribution behavior with the actual publishing and analytics tools when authorized. Return the link manifest and naming conventions; a generated URL does not prove that a campaign was sent, that tracking exists or that conversions are being recorded.

## Input example

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

No analytics collector is installed and no URL is opened. Do not put personal identifiers or secrets into campaign parameters. A link is not evidence that a campaign was published or tracked.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-utm-campaigns
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
