# Notion Block Draft Builder

## Choose the Markdown that will become blocks

Select the intended UTF-8 document and inspect its structure before conversion. The supported subset is headings one through three, bullet lines and paragraphs. Decide how tables, links, code and inline formatting should be handled before a real upload; this helper does not implement a full Markdown renderer.

## Review the proposed block payload

Inspect `notion-blocks.json` and compare it with the source in reading order. Rich text is split into chunks of at most 1900 characters. Check that chunk boundaries preserve content and that headings represent the intended page hierarchy.

For actual publishing, select the exact Notion page using an authorized connector and respect its current request limits. Read the destination first to avoid appending duplicate content. Keep a record of created block IDs and verify the visible page afterward. Local block generation alone does not prove that Notion accepted the payload or that all source formatting survived.

## Input example

```json
{
  "file": "samples/note.md"
}
```

Not a full Markdown renderer; tables, code fences, links and formatting need explicit mapping. No Notion API call occurs. For upload, use the intended page and authorized connector, and respect its current batch limits.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-notion-block-planner
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
