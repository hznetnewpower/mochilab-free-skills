# Citation Normalizer

## Build a traceable reference set

Gather stable record IDs, titles and any supplied authors, year or DOI. Preserve the source of each bibliographic record outside the normalized export so that later corrections remain possible. Verify publication metadata against the publisher before treating a citation as final.

## Resolve duplicates without losing editions

The helper deduplicates exact normalized DOI or title matches and exports `references.bib`. Inspect the retained record and duplicate IDs rather than assuming every title match is the same work. Translations, editions, corrections and retractions may need distinct entries even when wording overlaps.

Check the exported citation keys in the document or reference manager that will consume them. The helper does not resolve DOI URLs, search scholarly services or establish that a paper supports a claim. Deliver the bibliography with unresolved metadata and duplicate decisions recorded; do not invent missing authors or publication years to make the file look complete.

## Input example

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

No DOI resolution, scholarly search or truth verification. Preserve distinct editions and corrections when bibliographically meaningful. Check exact publication metadata against the publisher before final citation.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-citation-manager
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
