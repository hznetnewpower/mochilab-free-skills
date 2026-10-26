# Citation Normalizer

## What it does

Deduplicate user-supplied references by normalized DOI or title and export escaped BibTeX records.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "records": [
    {
      "id": "demo1",
      "title": "Fictional report",
      "authors": [
        "Example Author"
      ],
      "year": 2026,
      "doi": "https://doi.org/10.0000/demo"
    },
    {
      "id": "demo2",
      "title": "Same record",
      "doi": "10.0000/demo"
    }
  ]
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

No DOI resolution, scholarly search or truth verification. Preserve distinct editions and corrections when bibliographically meaningful. Check exact publication metadata against the publisher before final citation.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-citation-manager
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
