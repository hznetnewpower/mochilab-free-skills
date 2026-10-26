# PPTX Text Density Review

## What it does

Inspect slide XML for empty text and excessive declared character budgets before visual presentation review.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "file": "samples/slides.pptx",
  "maxCharsPerSlide": 100
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

This cannot confirm clipping, overlap, contrast, chart correctness or appearance. Render the deck or open PowerPoint for visual QA. An image-only slide can intentionally contain no XML text.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-pptx-review
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
