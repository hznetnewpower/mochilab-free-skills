# Input contract

segments: unique id,start,end in seconds. chapters: start,title,nonempty sourceIds. Exports chapters.txt.

## Operational scope

Use an authorized transcript or the user's file. The model writes titles from actual segment evidence; the helper only checks references and timing. It does not fetch videos or prove that a summary is factually accurate.

## Fictional example

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

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
