---
name: mochi-notion-block-planner
description: "Convert simple local headings, bullet lines and paragraphs into reviewable Notion block JSON before uploading."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Notion Block Draft Builder

Convert simple local headings, bullet lines and paragraphs into reviewable Notion block JSON before uploading.

## Choose the Markdown that will become blocks

Select the intended UTF-8 document and inspect its structure before conversion. The supported subset is headings one through three, bullet lines and paragraphs. Decide how tables, links, code and inline formatting should be handled before a real upload; this helper does not implement a full Markdown renderer.

## Review the proposed block payload

Inspect `notion-blocks.json` and compare it with the source in reading order. Rich text is split into chunks of at most 1900 characters. Check that chunk boundaries preserve content and that headings represent the intended page hierarchy.

For actual publishing, select the exact Notion page using an authorized connector and respect its current request limits. Read the destination first to avoid appending duplicate content. Keep a record of created block IDs and verify the visible page afterward. Local block generation alone does not prove that Notion accepted the payload or that all source formatting survived.

## Reproducible request

file: UTF-8 plain Markdown. Supports headings1..3, bullet lines and paragraphs; rich text is chunked to1900 characters. Exports notion-blocks.json.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/note.md"
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
