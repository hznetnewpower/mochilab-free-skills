# Commit Release Notes

## Select the release range

Collect commits between the actual previous and proposed releases. Preserve each commit ID and subject, and include bodies when they explain migration work. Avoid counting merge commits as additional shipped features unless they contain distinct changes.

## Turn the draft into release evidence

Review feature and fix groups against the real diff. A breaking marker in a subject should lead to an explicit migration note, not merely a warning badge. Verify that the claimed behavior is covered by tests or other concrete evidence, and retain links to relevant issues when available.

The helper exports `release-notes.md` from supplied messages. It does not inspect code, tag a repository, build artifacts or publish a release. Remove internal-only information before public use. Deliver the draft with the chosen version and commit range, identify unverified claims, and leave final publication to the authorized release workflow.

## Input example

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

This does not inspect code or validate that commit messages are accurate. Check the actual diff and test evidence; publishing a release remains separate. Preserve issue links and avoid claiming untested fixes.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-release-notes
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
