# Input contract

file: PPTX. maxCharsPerSlide: optional integer budget, default900. Counts text in slide XML only.

## Operational scope

This cannot confirm clipping, overlap, contrast, chart correctness or appearance. Render the deck or open PowerPoint for visual QA. An image-only slide can intentionally contain no XML text.

## Fictional example

```json
{
  "file": "samples/slides.pptx",
  "maxCharsPerSlide": 100
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
