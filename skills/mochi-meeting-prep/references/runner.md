# Running the local helper

Prepare request.json in the selected agent workspace using the input contract. Use only workspace-relative input files. The helper requires Python3.10+ and the standard library; it never signs in to external services.

```text
python3 "{baseDir}/scripts/run.py" --workspace "CURRENT_WORKSPACE" --input "request.json"
```

Check the exit status, JSON ok flag and task-specific result. Open returned artifacts, which are created in a fresh exports/mochi-… directory with byte counts and SHA-256 receipts. Input files are preserved. A successful run means this local operation completed, not that a live account action or visual check occurred.

Use the fictional samples only in a separate scratch workspace after copying the required samples directory there. For a real task, choose the user's intended inputs instead. A reproducible local check is:

```text
python3 "{baseDir}/tests/smoke.py"
```

Five packaged cases cover the domain example, invalid input, actual CLI artifacts, path boundaries and non-overwrite behavior. Live services and visual appearance require their own evidence.
