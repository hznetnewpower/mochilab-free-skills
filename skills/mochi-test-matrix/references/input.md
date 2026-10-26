# Input contract

factors:1..8 names mapped to nonempty value lists. Cartesian product must not exceed10000. Returns a greedy covering matrix.

## Operational scope

Pairwise coverage is not exhaustive behavior coverage and the greedy result is not guaranteed minimal. Include known high-risk combinations and execute the tests separately.

## Fictional example

```json
{
  "factors": {
    "os": [
      "linux",
      "windows"
    ],
    "lang": [
      "en",
      "zh"
    ],
    "role": [
      "one",
      "two"
    ]
  }
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
