---
name: mochi-test-matrix
description: "Generate a bounded greedy pairwise matrix for discrete configuration factors and report coverage without executing tests."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Pairwise Test Matrix

Generate a bounded greedy pairwise matrix for discrete configuration factors and report coverage without executing tests.

## Model the factors before generating cases

Use a factor for each independent setting, such as operating system, language or account role. Supply the actual values that the product supports. Exclude invalid combinations only through an explicit review process: this helper accepts discrete independent factors and has no constraint language.

### Coverage means pairs, not all behavior

The greedy matrix covers every two-factor value combination. Verify the returned pair-coverage result and compare the generated case count with the full Cartesian count. A small matrix is useful for breadth but does not guarantee the smallest possible suite or cover three-way interactions.

Add targeted regressions for past incidents and known risky combinations, then assign real assertions to every case. Execute those tests separately and retain their results; generated rows are not passing tests. Keep the Cartesian product within the documented bound and reduce redundant factor values rather than truncating the report silently.

## Reproducible request

factors:1..8 names mapped to nonempty value lists. Cartesian product must not exceed10000. Returns a greedy covering matrix.

The following is fictional fixture data, not a live service result.

```json
{
  "factors": {
    "os": [
      "linux",
      "windows"
    ],
    "lang": [
      "en",
      "zh"
    ],
    "role": [
      "one",
      "two"
    ]
  }
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
