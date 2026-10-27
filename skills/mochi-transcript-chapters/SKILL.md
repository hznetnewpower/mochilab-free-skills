---
name: mochi-transcript-chapters
description: "Validate proposed video chapters against supplied transcript segment IDs and export a timestamped chapter list."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Transcript Chapter Evidence

Validate proposed video chapters against supplied transcript segment IDs and export a timestamped chapter list.

## Anchor chapter titles in transcript evidence

Collect authorized transcript segments with unique IDs and start/end times. Read the actual segment text when drafting titles; this helper receives timing and source references and cannot establish what a speaker said. Keep the transcript provenance with the task notes.

## Review the chapter boundary proposals

Each chapter needs a start, a meaningful title and at least one source ID that exists in the segment list. Confirm that proposed boundaries follow the program's actual topic changes rather than dividing duration mechanically. Check timing order against the media before publishing chapter markers.

Inspect `chapters.txt` and compare its final marker with the supplied recording duration. Source-ID validation proves referential consistency only, not summary accuracy. The helper does not fetch videos, obtain transcripts or publish metadata. Deliver the chapter file and evidence mapping, identifying any title or timing that still needs a human listen-through.

## Reproducible request

segments: unique id,start,end in seconds. chapters: start,title,nonempty sourceIds. Exports chapters.txt.

The following is fictional fixture data, not a live service result.

```json
{
  "segments": [
    {
      "id": "s1",
      "start": 0,
      "end": 60
    },
    {
      "id": "s2",
      "start": 60,
      "end": 120
    }
  ],
  "chapters": [
    {
      "start": 0,
      "title": "Opening",
      "sourceIds": [
        "s1"
      ]
    },
    {
      "start": 60,
      "title": "Example",
      "sourceIds": [
        "s2"
      ]
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
