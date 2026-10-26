# Input contract

topics: nonempty name-to-keyword-list map. feedback: id,text records. Matching is casefolded substring matching.

## Operational scope

This is transparent keyword grouping, not sentiment analysis or semantic clustering. Review ambiguous examples and false positives before making product decisions. No customer reply or external upload occurs.

## Fictional example

```json
{
  "topics": {
    "speed": [
      "slow",
      "latency"
    ],
    "billing": [
      "invoice"
    ]
  },
  "feedback": [
    {
      "id": "f1",
      "text": "slow response"
    },
    {
      "id": "f2",
      "text": "invoice question"
    },
    {
      "id": "f3",
      "text": "thanks"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
