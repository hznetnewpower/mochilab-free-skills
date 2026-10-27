# Dependency Upgrade Delta

## Choose comparable dependency snapshots

Prepare two name-to-version maps from the same dependency scope and package manager. Resolve exact installed or locked versions where possible. Comparing a production map with a development map creates misleading removals; comparing ranges does not establish an actual upgrade.

## Review each kind of change

Added names can introduce new runtime or build requirements. Removed names may still be imported elsewhere. Changed versions need upstream release notes and project-specific checks. Numeric major changes receive a review flag; that flag is not a compatibility prediction, and nonnumeric versions cannot support the same inference.

Report the before and after versions beside each changed name, then identify which migration notes or tests remain necessary. The helper does not install dependencies, query vulnerability databases or certify licenses. Keep a separate decision record for approving the actual upgrade, and retain the lockfile diff as evidence when one exists.

## Input example

```json
{
  "before": {
    "alpha": "1.2.0",
    "old": "1.0.0"
  },
  "after": {
    "alpha": "2.0.0",
    "new": "1.0.0"
  }
}
```

No dependency is installed and no vulnerability database is queried. A major-version flag is a review cue, not a compatibility verdict. Read upstream migration notes and run project checks before upgrading.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-dependency-diff
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
