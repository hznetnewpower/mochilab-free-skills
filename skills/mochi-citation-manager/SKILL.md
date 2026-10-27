---
name: mochi-citation-manager
description: "Deduplicate user-supplied references by normalized DOI or title and export escaped BibTeX records."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Citation Normalizer

Deduplicate user-supplied references by normalized DOI or title and export escaped BibTeX records.

## Build a traceable reference set

Gather stable record IDs, titles and any supplied authors, year or DOI. Preserve the source of each bibliographic record outside the normalized export so that later corrections remain possible. Verify publication metadata against the publisher before treating a citation as final.

## Resolve duplicates without losing editions

The helper deduplicates exact normalized DOI or title matches and exports `references.bib`. Inspect the retained record and duplicate IDs rather than assuming every title match is the same work. Translations, editions, corrections and retractions may need distinct entries even when wording overlaps.

Check the exported citation keys in the document or reference manager that will consume them. The helper does not resolve DOI URLs, search scholarly services or establish that a paper supports a claim. Deliver the bibliography with unresolved metadata and duplicate decisions recorded; do not invent missing authors or publication years to make the file look complete.

## Reproducible request

records: id,title, optional authors list,year,doi. Exact normalized DOI/title deduplication. Exports references.bib.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
