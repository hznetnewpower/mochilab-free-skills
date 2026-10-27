---
name: mochi-docx-review-map
description: "Map comments, their paragraph anchors and tracked insertions or deletions in a DOCX without accepting changes."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# DOCX Comments and Revisions Map

Map comments, their paragraph anchors and tracked insertions or deletions in a DOCX without accepting changes.

## Map the review evidence in a DOCX

Use the reviewed document itself, not a PDF export, because revisions and comment anchors live in Word XML parts. Preserve a copy before inspection. The helper reads paragraph positions, comment definitions and insertion/deletion records without changing the review state.

## Follow comments back to paragraphs

Match comment identifiers to their definitions and reported paragraph anchors. A missing definition needs investigation in the original document; it is not an empty reviewer comment. Review inserted and deleted text separately so that a quotation does not accidentally present removed wording as current content.

Open Word for modern threaded or resolved-comment semantics and visual inspection. The helper neither accepts nor rejects revisions and does not establish legal meaning or reviewer agreement. Deliver a traceable inventory with paragraph references, explain any missing parts, and leave decisions about applying edits to the authorized document review process.

## Reproducible request

file: DOCX. Reads word/document.xml and optional word/comments.xml. Reports paragraph indexes, comment IDs, text and revision kind.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/review.docx"
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
