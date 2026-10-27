# Agent-only local helper instructions

The user gives a normal chat request or source files. You, the assistant, read references/input.md, derive the supported fields from those sources and create request.json inside the active workspace. Do not ask the user to construct this internal request or copy fictional test data into a real task.

Use only workspace-relative input paths. Read or capture actual source files with available authorized tools. If an essential source or parameter is missing, ask a short ordinary-language question. Preserve unknowns and stop short of a numeric or completed verdict when the missing information affects it.

```text
python3 "{baseDir}/scripts/run.py" --workspace "CURRENT_WORKSPACE" --input "request.json"
```

Inspect the exit status, ok flag, task result and returned artifacts. New files are created under exports/mochi-…; preserve originals. Explain results in the user's language and provide useful artifacts. Raw request/response objects are developer details unless the user asks for them. This helper uses Python 3.10+ and the standard library; it neither authenticates services nor performs network requests.

The fictional samples are for a separate scratch workspace. They are not real user inputs or live evidence. The packaged check is:

```text
python3 "{baseDir}/tests/smoke.py"
```

Tests cover local behavior, invalid input, actual CLI artifacts, workspace paths and non-overwrite behavior. They do not establish conversational extraction accuracy, live integration, visual appearance or real account authorization.
