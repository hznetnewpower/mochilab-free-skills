---
name: mochi-release-notes
description: "Group exported conventional commit subjects into draft release notes and flag declared breaking changes."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Commit Release Notes

Group exported conventional commit subjects into draft release notes and flag declared breaking changes.

## Select the release range

Collect commits between the actual previous and proposed releases. Preserve each commit ID and subject, and include bodies when they explain migration work. Avoid counting merge commits as additional shipped features unless they contain distinct changes.

## Turn the draft into release evidence

Review feature and fix groups against the real diff. A breaking marker in a subject should lead to an explicit migration note, not merely a warning badge. Verify that the claimed behavior is covered by tests or other concrete evidence, and retain links to relevant issues when available.

The helper exports `release-notes.md` from supplied messages. It does not inspect code, tag a repository, build artifacts or publish a release. Remove internal-only information before public use. Deliver the draft with the chosen version and commit range, identify unverified claims, and leave final publication to the authorized release workflow.

## Reproducible request

commits: id, subject and optional body. version: optional heading. Exports release-notes.md.

The following is fictional fixture data, not a live service result.

```json
{
  "version": "1.1.0",
  "commits": [
    {
      "id": "abc123",
      "subject": "feat!: change interface"
    },
    {
      "id": "def456",
      "subject": "fix: preserve settings"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
