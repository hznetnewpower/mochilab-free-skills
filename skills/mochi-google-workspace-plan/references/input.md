# Internal input contract for the assistant

actions: kind, account, resource or query. Supports documented planning labels for gmail.search/draft,calendar.list/create,drive.list/upload,sheets.read/update,docs.read/update.

## Operational scope

The helper does not implement OAuth or call Google. Use an available authorized connector or inspect the installed gog CLI help before executing. Verify account and resource identifiers; do not request refresh tokens in chat.

## Fictional example

```json
{
  "actions": [
    {
      "kind": "gmail.search",
      "account": "demo@example.com",
      "query": "subject:invoice"
    },
    {
      "kind": "docs.update",
      "account": "demo@example.com",
      "resource": "fictional-document"
    }
  ]
}
```

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
