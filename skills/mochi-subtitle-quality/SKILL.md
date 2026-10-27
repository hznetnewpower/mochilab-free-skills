---
name: mochi-subtitle-quality
description: "Check selected SRT or simple WebVTT cues for nonpositive durations, overlaps and configurable reading-rate warnings."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Subtitle Timing and Reading Rate

Check selected SRT or simple WebVTT cues for nonpositive durations, overlaps and configurable reading-rate warnings.

## Check timing text before editing dialogue

Use an authorized UTF-8 SRT or WebVTT file with millisecond cue timestamps. Retain the source and choose a reading-rate threshold appropriate to the audience and language. A threshold is an editorial policy, not an automatic accessibility certificate.

### Investigate flagged cues

Read the timestamps and displayed text around a warning. A fast cue may need shorter wording or a longer display interval, but timing changes must be checked against the real audio and adjacent cues. Do not fix a rate warning by deleting important meaning or attributing speech to the wrong speaker.

The helper does not listen to audio, align speech, validate translation or fully support WebVTT regions and positioning. Use an appropriate subtitle editor for those checks. Return cue references and proposed corrections in a separate output; keep the original file intact and state whether synchronization was actually reviewed.

## Reproducible request

file: UTF-8 SRT or WebVTT. maxCharsPerSecond: optional positive rate. Millisecond timestamp cues are required.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/subtitles.srt",
  "maxCharsPerSecond": 20
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
