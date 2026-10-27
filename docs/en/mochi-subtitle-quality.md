# Subtitle Timing and Reading Rate

## Check timing text before editing dialogue

Use an authorized UTF-8 SRT or WebVTT file with millisecond cue timestamps. Retain the source and choose a reading-rate threshold appropriate to the audience and language. A threshold is an editorial policy, not an automatic accessibility certificate.

### Investigate flagged cues

Read the timestamps and displayed text around a warning. A fast cue may need shorter wording or a longer display interval, but timing changes must be checked against the real audio and adjacent cues. Do not fix a rate warning by deleting important meaning or attributing speech to the wrong speaker.

The helper does not listen to audio, align speech, validate translation or fully support WebVTT regions and positioning. Use an appropriate subtitle editor for those checks. Return cue references and proposed corrections in a separate output; keep the original file intact and state whether synchronization was actually reviewed.

## Input example

```json
{
  "file": "samples/subtitles.srt",
  "maxCharsPerSecond": 20
}
```

A reading-rate warning is an editorial cue, not an accessibility certification. The helper does not listen to audio, synchronize timing or validate translation accuracy. Complex WebVTT positioning and regions need a full parser.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-subtitle-quality
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
