# Pairwise Test Matrix

## What it helps with

Generate a bounded greedy pairwise matrix for discrete configuration factors and report coverage without executing tests.

## Say it like this

After installation, describe the task in chat, paste the material or upload the relevant files.

**“Build a pairwise test matrix for Android and HarmonyOS, English and Chinese, and light and dark themes.”**

## What to provide

List the configuration factors and possible values for each.

No fixed request format is needed. The assistant asks a short follow-up when essential information is missing.

## What you receive

Receive a configuration matrix, pair coverage and high-risk combinations to add.

The assistant explains results in plain language, provides actual output files where applicable and separates unresolved details.

## Scope

Pairwise coverage is not exhaustive behavior coverage and the greedy result is not guaranteed minimal. Include known high-risk combinations and execute the tests separately.


The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-test-matrix
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
