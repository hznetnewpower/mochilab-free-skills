# PPTX Text Density Review

## Choose a text-density review target

Select a PPTX and state the intended character budget per slide. The budget is an editorial heuristic: a technical appendix, a title slide and a presentation for a large room need different judgment. Keep a source copy so that suggested edits can be compared later.

### Read the slide inventory carefully

The helper counts text stored in slide XML and identifies slides above the supplied budget. Inspect those slides for redundant wording and unclear hierarchy, then propose edits that preserve the speaker's meaning. An image-only slide may intentionally have no XML text, so an empty count is not an error by itself.

Render the actual deck or open it in PowerPoint to check clipping, overlap, chart labels, contrast and visual balance. Those properties cannot be established by character counts. Return slide references and text-density findings, keeping the visual-review status explicitly separate from this static check.

## Input example

```json
{
  "file": "samples/slides.pptx",
  "maxCharsPerSlide": 100
}
```

This cannot confirm clipping, overlap, contrast, chart correctness or appearance. Render the deck or open PowerPoint for visual QA. An image-only slide can intentionally contain no XML text.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-pptx-review
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
