# Internal input contract for the assistant

links: url,utm_source,utm_medium,utm_campaign and optional utm_term/utm_content. Required values must be nonempty.

## Operational scope

No analytics collector is installed and no URL is opened. Do not put personal identifiers or secrets into campaign parameters. A link is not evidence that a campaign was published or tracked.

## Fictional example

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

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
