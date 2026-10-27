# Commit Release Notes

## What it helps with

Group exported conventional commit subjects into draft release notes and flag declared breaking changes.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Draft release notes for 1.1.0 from these commits. Separate features, fixes and declared breaking changes.”**

## What to provide

Provide commit records or an accessible revision range and the release version.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive draft release notes and items requiring verification.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

This does not inspect code or validate that commit messages are accurate. Check the actual diff and test evidence; publishing a release remains separate. Preserve issue links and avoid claiming untested fixes.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-release-notes
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
