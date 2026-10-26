# Audio Loudness Preparation

## What it does

Read a supplied ffprobe JSON and prepare the first loudness-analysis filter without altering audio or inventing measurements.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "probeFile": "samples/probe.json",
  "targetLufs": -16
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Requires ffmpeg/ffprobe for actual media work; these binaries are not bundled. Run analysis first, use measured loudnorm fields for a second pass, save a new output and listen to it. Loudness normalization is not noise removal.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-audio-cleanup-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
