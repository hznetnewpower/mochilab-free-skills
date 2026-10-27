# Transcript Chapter Evidence

## Anchor chapter titles in transcript evidence

Collect authorized transcript segments with unique IDs and start/end times. Read the actual segment text when drafting titles; this helper receives timing and source references and cannot establish what a speaker said. Keep the transcript provenance with the task notes.

## Review the chapter boundary proposals

Each chapter needs a start, a meaningful title and at least one source ID that exists in the segment list. Confirm that proposed boundaries follow the program's actual topic changes rather than dividing duration mechanically. Check timing order against the media before publishing chapter markers.

Inspect `chapters.txt` and compare its final marker with the supplied recording duration. Source-ID validation proves referential consistency only, not summary accuracy. The helper does not fetch videos, obtain transcripts or publish metadata. Deliver the chapter file and evidence mapping, identifying any title or timing that still needs a human listen-through.

## Input example

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

Use an authorized transcript or the user's file. The model writes titles from actual segment evidence; the helper only checks references and timing. It does not fetch videos or prove that a summary is factually accurate.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-transcript-chapters
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
