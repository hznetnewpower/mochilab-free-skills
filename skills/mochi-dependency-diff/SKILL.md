---
name: mochi-dependency-diff
description: "Compare explicit dependency version maps and highlight additions, removals and major-version changes."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Dependency Upgrade Delta

Compare explicit dependency version maps and highlight additions, removals and major-version changes.

## Choose comparable dependency snapshots

Prepare two name-to-version maps from the same dependency scope and package manager. Resolve exact installed or locked versions where possible. Comparing a production map with a development map creates misleading removals; comparing ranges does not establish an actual upgrade.

## Review each kind of change

Added names can introduce new runtime or build requirements. Removed names may still be imported elsewhere. Changed versions need upstream release notes and project-specific checks. Numeric major changes receive a review flag; that flag is not a compatibility prediction, and nonnumeric versions cannot support the same inference.

Report the before and after versions beside each changed name, then identify which migration notes or tests remain necessary. The helper does not install dependencies, query vulnerability databases or certify licenses. Keep a separate decision record for approving the actual upgrade, and retain the lockfile diff as evidence when one exists.

## Reproducible request

before and after: package-name to exact-version maps. Major change detection applies only to numeric major prefixes.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
