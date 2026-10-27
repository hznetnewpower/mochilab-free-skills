# Transcript Chapter Evidence

## What it helps with

Validate proposed video chapters against supplied transcript segment IDs and export a timestamped chapter list.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Create concise video chapters from this timestamped transcript. Link each chapter to supporting segments and export a timestamp list.
```

## What to provide

Provide a timestamped transcript; missing timing must be supplied or obtained with an available transcription tool.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive chapter titles, start times and transcript evidence.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Use an authorized transcript or the user's file. The model writes titles from actual segment evidence; the helper only checks references and timing. It does not fetch videos or prove that a summary is factually accurate.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-transcript-chapters
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
