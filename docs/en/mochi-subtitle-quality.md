# Subtitle Timing and Reading Rate

## What it does

Check selected SRT or simple WebVTT cues for nonpositive durations, overlaps and configurable reading-rate warnings.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

```json
{
  "file": "samples/subtitles.srt",
  "maxCharsPerSecond": 20
}
```

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

A reading-rate warning is an editorial cue, not an accessibility certification. The helper does not listen to audio, synchronize timing or validate translation accuracy. Complex WebVTT positioning and regions need a full parser.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-subtitle-quality
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
