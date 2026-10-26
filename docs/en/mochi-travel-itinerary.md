# Timezone Itinerary Organizer

## What it does

Arrange user-selected itinerary stops, detect time overlaps and keep estimated costs separated by currency.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "title": "Fictional day plan",
  "stops": [
    {
      "name": "Museum",
      "start": "2026-11-01T09:00:00+08:00",
      "end": "2026-11-01T10:00:00+08:00",
      "cost": "20",
      "currency": "CNY"
    },
    {
      "name": "Cafe",
      "start": "2026-11-01T10:30:00+08:00",
      "end": "2026-11-01T11:00:00+08:00",
      "cost": "5",
      "currency": "USD"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Current travel recommendations, opening hours, entry rules, fares and availability require live verification. User-supplied times are not verified transit times. No booking, payment or exchange-rate conversion occurs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-travel-itinerary
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
