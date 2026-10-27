# Internal input contract for the assistant

tasks: unique id, optional required(default true),status,evidence. Required tasks need done plus nonempty evidence.

## Operational scope

A checked box is not a compliance certificate. Verify actual artifacts, support ownership, rollback and known limitations. The helper does not deploy, send announcements or accept agreements.

## Fictional example

```json
{
  "tasks": [
    {
      "id": "smoke",
      "status": "done",
      "evidence": "Fictional test receipt"
    },
    {
      "id": "rollback",
      "status": "pending"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
