# Release Evidence Gate

## What it helps with

Check a release manifest for valid versions, checksums and recorded passing tests before a human publication decision.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Review the attached release package, version, checksum file and test receipts. List missing evidence without publishing.”**

## What to provide

Provide the release artifacts, versions and existing test evidence.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive missing items, inconsistencies and decisions needed before release.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Manifest fields do not prove a file or test is genuine. Verify files, signatures, installation and public downloads separately. Never equate a submitted marketplace version with public availability.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-release-readiness
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
