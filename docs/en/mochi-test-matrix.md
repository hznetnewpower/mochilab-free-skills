# Pairwise Test Matrix

## Model the factors before generating cases

Use a factor for each independent setting, such as operating system, language or account role. Supply the actual values that the product supports. Exclude invalid combinations only through an explicit review process: this helper accepts discrete independent factors and has no constraint language.

### Coverage means pairs, not all behavior

The greedy matrix covers every two-factor value combination. Verify the returned pair-coverage result and compare the generated case count with the full Cartesian count. A small matrix is useful for breadth but does not guarantee the smallest possible suite or cover three-way interactions.

Add targeted regressions for past incidents and known risky combinations, then assign real assertions to every case. Execute those tests separately and retain their results; generated rows are not passing tests. Keep the Cartesian product within the documented bound and reduce redundant factor values rather than truncating the report silently.

## Input example

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

Pairwise coverage is not exhaustive behavior coverage and the greedy result is not guaranteed minimal. Include known high-risk combinations and execute the tests separately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-test-matrix
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
