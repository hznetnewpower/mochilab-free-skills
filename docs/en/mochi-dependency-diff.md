# Dependency Upgrade Delta

## What it helps with

Compare explicit dependency version maps and highlight additions, removals and major-version changes.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

```text
Compare these before-and-after dependency lists. Show additions, removals and version changes, especially major upgrades.
```

## What to provide

Provide comparable before-and-after dependency lists or locked-version exports.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive a version delta and migration-review items.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

No dependency is installed and no vulnerability database is queried. A major-version flag is a review cue, not a compatibility verdict. Read upstream migration notes and run project checks before upgrading.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-dependency-diff
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
