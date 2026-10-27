---
name: mochi-ci-failure-map
description: "Locate test, dependency, compilation, permission and timeout signals in a selected CI log without replaying the pipeline."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# CI Failure Signal Map

Locate test, dependency, compilation, permission and timeout signals in a selected CI log without replaying the pipeline.

## Begin with one failed run

Obtain the log for the exact failing job, including its run identifier and revision. Select a local UTF-8 export; do not combine unrelated retries without labeling them. Keep the original log private because build output can contain credentials and internal addresses.

### Use line numbers as leads

The report groups dependency, compilation, test, permission and timeout signals. Open the cited locations in the original log and read the preceding step header, first exception and final exit status. A later test failure can be a consequence of an earlier failed install. Multiple categories are not multiple confirmed root causes.

Before rerunning, decide whether the job deploys, publishes packages, migrates data or sends notifications. Investigate with read-only project evidence first. The final diagnosis should identify the failing stage, the strongest supporting lines and remaining uncertainty. Do not paste whole log blocks into a public issue or claim a pipeline was rerun by this helper.

## Reproducible request

file: UTF-8 log. Returns matched line numbers and category counts without reproducing full log text.

The following is fictional fixture data, not a live service result.

```json
{
  "file": "samples/ci.log"
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
