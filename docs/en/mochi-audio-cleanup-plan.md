# Audio Loudness Preparation

## What it helps with

Read a supplied ffprobe JSON and prepare the first loudness-analysis filter without altering audio or inventing measurements.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Help make this podcast’s loudness more consistent. Inspect the audio and prepare a processing plan while preserving the original.”**

## What to provide

Supply the audio and intended publishing use or target loudness; actual processing requires installed media tools.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive audio stream information, a first-pass loudness-analysis plan and remaining processing steps.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Requires ffmpeg/ffprobe for actual media work; these binaries are not bundled. Run analysis first, use measured loudnorm fields for a second pass, save a new output and listen to it. Loudness normalization is not noise removal.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-audio-cleanup-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
