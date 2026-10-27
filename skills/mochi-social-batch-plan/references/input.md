# Internal input contract for the assistant

platformLimits: platform-to-positive-integer map. posts: id,platform,text, optional assets. Counts Unicode code points.

## Operational scope

Platforms may use weighted characters or URL rules. Confirm current platform limits and use the platform composer before publishing; this count is not a final platform acceptance check. No account login or scheduling occurs.

## Fictional example

```json
{
  "platformLimits": {
    "demo": 5
  },
  "posts": [
    {
      "id": "p1",
      "platform": "demo",
      "text": "hello"
    },
    {
      "id": "p2",
      "platform": "demo",
      "text": "too long"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
