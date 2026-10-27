# DOCX Comments and Revisions Map

## Map the review evidence in a DOCX

Use the reviewed document itself, not a PDF export, because revisions and comment anchors live in Word XML parts. Preserve a copy before inspection. The helper reads paragraph positions, comment definitions and insertion/deletion records without changing the review state.

## Follow comments back to paragraphs

Match comment identifiers to their definitions and reported paragraph anchors. A missing definition needs investigation in the original document; it is not an empty reviewer comment. Review inserted and deleted text separately so that a quotation does not accidentally present removed wording as current content.

Open Word for modern threaded or resolved-comment semantics and visual inspection. The helper neither accepts nor rejects revisions and does not establish legal meaning or reviewer agreement. Deliver a traceable inventory with paragraph references, explain any missing parts, and leave decisions about applying edits to the authorized document review process.

## Input example

```json
{
  "file": "samples/review.docx"
}
```

This is evidence extraction, not legal review, full Word review-state validation or visual layout QA. It does not accept/reject changes or edit comments. Inspect modern threaded/resolved comments and document appearance in Word separately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-docx-review-map
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
