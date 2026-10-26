# Transcript Chapter Evidence

## What it does

Validate proposed video chapters against supplied transcript segment IDs and export a timestamped chapter list.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "segments": [
    {
      "id": "s1",
      "start": 0,
      "end": 60
    },
    {
      "id": "s2",
      "start": 60,
      "end": 120
    }
  ],
  "chapters": [
    {
      "start": 0,
      "title": "Opening",
      "sourceIds": [
        "s1"
      ]
    },
    {
      "start": 60,
      "title": "Example",
      "sourceIds": [
        "s2"
      ]
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Use an authorized transcript or the user's file. The model writes titles from actual segment evidence; the helper only checks references and timing. It does not fetch videos or prove that a summary is factually accurate.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-transcript-chapters
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
