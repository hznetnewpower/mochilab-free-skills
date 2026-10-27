# Audio Loudness Preparation

## Establish the audio source and target

Obtain ffprobe JSON for the selected media and review its audio streams. Ask which stream should be processed and what loudness and true-peak targets the delivery channel requires. The package does not bundle ffmpeg or ffprobe; verify installed tool help before running media commands.

## Use a measured two-pass workflow

The helper proposes an analysis filter from the supplied probe data and target values. Run that analysis against the intended audio, retain the measured loudnorm fields, and use those measurements to prepare the second pass. The initial report is not a ready-made second-pass result.

Write processed audio to a new file and listen to quiet passages, peaks, transitions and the ending. Confirm duration and channel mapping before delivery. Loudness normalization does not remove background noise, repair clipping or verify intelligibility. Return the plan and measured evidence, distinguishing a proposed filter from audio that was actually processed and auditioned.

## Input example

```json
{
  "probeFile": "samples/probe.json",
  "targetLufs": -16
}
```

Requires ffmpeg/ffprobe for actual media work; these binaries are not bundled. Run analysis first, use measured loudnorm fields for a second pass, save a new output and listen to it. Loudness normalization is not noise removal.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-audio-cleanup-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
