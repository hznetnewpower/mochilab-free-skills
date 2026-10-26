# UTM Campaign Link Builder

## What it does

Build URL-encoded campaign links while preserving ordinary query parameters and refusing obvious embedded credentials.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

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

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

No analytics collector is installed and no URL is opened. Do not put personal identifiers or secrets into campaign parameters. A link is not evidence that a campaign was published or tracked.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-utm-campaigns
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
