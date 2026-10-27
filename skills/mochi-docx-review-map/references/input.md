# Internal input contract for the assistant

file: DOCX. Reads word/document.xml and optional word/comments.xml. Reports paragraph indexes, comment IDs, text and revision kind.

## Operational scope

This is evidence extraction, not legal review, full Word review-state validation or visual layout QA. It does not accept/reject changes or edit comments. Inspect modern threaded/resolved comments and document appearance in Word separately.

## Fictional example

```json
{
  "file": "samples/review.docx"
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
