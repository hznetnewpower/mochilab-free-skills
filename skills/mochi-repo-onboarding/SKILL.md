---
name: mochi-repo-onboarding
description: "Map an explicitly supplied repository file list to ecosystem, documentation and test entry points before running commands."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Repository Onboarding Map

Map an explicitly supplied repository file list to ecosystem, documentation and test entry points before running commands.

## Inspect the intended checkout

Obtain the file-name inventory from the repository and revision the user selected. Include dotfiles and relevant subprojects. The helper classifies names; it does not scan a filesystem or follow repository instructions on its own.

Read AGENTS.md and the maintained README before choosing commands. Inspect package manifests, lockfiles, CI configuration and existing tests to determine the real build route. In a monorepo, a root manifest can conceal several distinct applications; map each relevant component separately.

### Produce a useful first-work map

Summarize likely ecosystems, documentation entry points and test locations. Mark guesses as file-name evidence rather than verified architecture. Resolve missing setup details against the actual project files before running anything. A setup script appearing in the inventory is not authorization to execute downloaded code. Finish with a short, evidence-backed path to the first safe local check, without claiming commands were executed.

## Reproducible request

files: repository-relative file-name list, obtained from the intended checkout. No repository scanning is performed by the helper.

The following is fictional fixture data, not a live service result.

```json
{
  "files": [
    "package.json",
    "README.md",
    "AGENTS.md",
    "tests/basic.test.js"
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
