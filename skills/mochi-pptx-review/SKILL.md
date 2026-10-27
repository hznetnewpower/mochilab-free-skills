---
name: mochi-pptx-review
description: "Inspect slide XML for empty text and excessive declared character budgets before visual presentation review."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# PPTX Text Density Review

Inspect slide XML for empty text and excessive declared character budgets before visual presentation review.

## Choose a text-density review target

Select a PPTX and state the intended character budget per slide. The budget is an editorial heuristic: a technical appendix, a title slide and a presentation for a large room need different judgment. Keep a source copy so that suggested edits can be compared later.

### Read the slide inventory carefully

The helper counts text stored in slide XML and identifies slides above the supplied budget. Inspect those slides for redundant wording and unclear hierarchy, then propose edits that preserve the speaker's meaning. An image-only slide may intentionally have no XML text, so an empty count is not an error by itself.

Render the actual deck or open it in PowerPoint to check clipping, overlap, chart labels, contrast and visual balance. Those properties cannot be established by character counts. Return slide references and text-density findings, keeping the visual-review status explicitly separate from this static check.

## Reproducible request

file: PPTX. maxCharsPerSlide: optional integer budget, default900. Counts text in slide XML only.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/slides.pptx",
  "maxCharsPerSlide": 100
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
