# Internal input contract for the assistant

file: UTF-8 SRT or WebVTT. maxCharsPerSecond: optional positive rate. Millisecond timestamp cues are required.

## Operational scope

A reading-rate warning is an editorial cue, not an accessibility certification. The helper does not listen to audio, synchronize timing or validate translation accuracy. Complex WebVTT positioning and regions need a full parser.

## Fictional example

```json
{
  "file": "samples/subtitles.srt",
  "maxCharsPerSecond": 20
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
