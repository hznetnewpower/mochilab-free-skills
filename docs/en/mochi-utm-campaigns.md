# UTM Campaign Link Builder

## What it helps with

Build URL-encoded campaign links while preserving ordinary query parameters and refusing obvious embedded credentials.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Add campaign tags to this link: source newsletter, medium email and campaign autumn-launch. Preserve its language parameter.
```

## What to provide

Provide the original URL, source, medium and campaign name.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive copyable tagged URLs and a description of the added campaign fields.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

No analytics collector is installed and no URL is opened. Do not put personal identifiers or secrets into campaign parameters. A link is not evidence that a campaign was published or tracked.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-utm-campaigns
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
