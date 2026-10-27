# Repository Onboarding Map

## Inspect the intended checkout

Obtain the file-name inventory from the repository and revision the user selected. Include dotfiles and relevant subprojects. The helper classifies names; it does not scan a filesystem or follow repository instructions on its own.

Read AGENTS.md and the maintained README before choosing commands. Inspect package manifests, lockfiles, CI configuration and existing tests to determine the real build route. In a monorepo, a root manifest can conceal several distinct applications; map each relevant component separately.

### Produce a useful first-work map

Summarize likely ecosystems, documentation entry points and test locations. Mark guesses as file-name evidence rather than verified architecture. Resolve missing setup details against the actual project files before running anything. A setup script appearing in the inventory is not authorization to execute downloaded code. Finish with a short, evidence-backed path to the first safe local check, without claiming commands were executed.

## Input example

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

File-name signals can be incomplete in monorepos. Read AGENTS.md and project documentation, inspect package scripts and verify the maintained checkout. Do not execute downloaded setup scripts merely because they appear in a manifest.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-repo-onboarding
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
