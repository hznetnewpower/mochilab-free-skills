# Input contract

probeFile: ffprobe JSON. targetLufs:-30..-5 default-16. targetTruePeak:-9..0 default-1. Returns an analysis filter.

## Operational scope

Requires ffmpeg/ffprobe for actual media work; these binaries are not bundled. Run analysis first, use measured loudnorm fields for a second pass, save a new output and listen to it. Loudness normalization is not noise removal.

## Fictional example

```json
{
  "probeFile": "samples/probe.json",
  "targetLufs": -16
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
