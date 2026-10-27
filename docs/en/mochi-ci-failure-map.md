# CI Failure Signal Map

## Begin with one failed run

Obtain the log for the exact failing job, including its run identifier and revision. Select a local UTF-8 export; do not combine unrelated retries without labeling them. Keep the original log private because build output can contain credentials and internal addresses.

### Use line numbers as leads

The report groups dependency, compilation, test, permission and timeout signals. Open the cited locations in the original log and read the preceding step header, first exception and final exit status. A later test failure can be a consequence of an earlier failed install. Multiple categories are not multiple confirmed root causes.

Before rerunning, decide whether the job deploys, publishes packages, migrates data or sends notifications. Investigate with read-only project evidence first. The final diagnosis should identify the failing stage, the strongest supporting lines and remaining uncertainty. Do not paste whole log blocks into a public issue or claim a pipeline was rerun by this helper.

## Input example

```json
{
  "file": "samples/ci.log"
}
```

A pattern match is a diagnostic lead, not confirmed root cause. Read relevant surrounding lines privately and investigate the earliest causal failure. Do not expose tokens from logs or rerun side-effecting jobs automatically.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-ci-failure-map
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
