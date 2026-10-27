# Subtitle Timing and Reading Rate

## What it helps with

Check selected SRT or simple WebVTT cues for nonpositive durations, overlaps and configurable reading-rate warnings.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Check these subtitles for overlaps, invalid durations and excessive reading speed. List cue numbers and reasons.
```

## What to provide

Upload SRT or simple WebVTT captions and any preferred reading-rate threshold.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive located timing and reading-rate warnings while preserving the original.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

A reading-rate warning is an editorial cue, not an accessibility certification. The helper does not listen to audio, synchronize timing or validate translation accuracy. Complex WebVTT positioning and regions need a full parser.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-subtitle-quality
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
