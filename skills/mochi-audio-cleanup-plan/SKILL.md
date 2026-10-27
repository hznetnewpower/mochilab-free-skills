---
name: mochi-audio-cleanup-plan
description: "Read a supplied ffprobe JSON and prepare the first loudness-analysis filter without altering audio or inventing measurements."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Audio Loudness Preparation

Read a supplied ffprobe JSON and prepare the first loudness-analysis filter without altering audio or inventing measurements.

## Establish the audio source and target

Obtain ffprobe JSON for the selected media and review its audio streams. Ask which stream should be processed and what loudness and true-peak targets the delivery channel requires. The package does not bundle ffmpeg or ffprobe; verify installed tool help before running media commands.

## Use a measured two-pass workflow

The helper proposes an analysis filter from the supplied probe data and target values. Run that analysis against the intended audio, retain the measured loudnorm fields, and use those measurements to prepare the second pass. The initial report is not a ready-made second-pass result.

Write processed audio to a new file and listen to quiet passages, peaks, transitions and the ending. Confirm duration and channel mapping before delivery. Loudness normalization does not remove background noise, repair clipping or verify intelligibility. Return the plan and measured evidence, distinguishing a proposed filter from audio that was actually processed and auditioned.

## Reproducible request

probeFile: ffprobe JSON. targetLufs:-30..-5 default-16. targetTruePeak:-9..0 default-1. Returns an analysis filter.

The following is fictional fixture data, not a live service result.

```json
{
  "probeFile": "samples/probe.json",
  "targetLufs": -16
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
