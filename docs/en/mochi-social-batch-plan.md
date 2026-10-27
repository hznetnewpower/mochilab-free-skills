# Social Draft Batch Review

## Prepare an editorial batch

Assign every post a stable ID, intended platform, final text and optional asset references. Supply the current character limit for each platform from an authoritative source. Keep drafts distinct from content already approved or scheduled.

### Resolve length findings in context

The helper counts Unicode code points. Platforms can apply weighted characters, special URL rules or different limits by account type, so validate borderline posts in the real composer. Shorten wording without changing a factual claim, removing necessary attribution or leaving a misleading fragment.

Review referenced assets and the intended publishing account before any live action. This package does not log in, schedule posts or submit content. Deliver the batch with over-limit IDs and the counting assumptions, then obtain any required publication approval and verify the platform's actual response separately.

## Input example

```json
{
  "platformLimits": {
    "demo": 5
  },
  "posts": [
    {
      "id": "p1",
      "platform": "demo",
      "text": "hello"
    },
    {
      "id": "p2",
      "platform": "demo",
      "text": "too long"
    }
  ]
}
```

Platforms may use weighted characters or URL rules. Confirm current platform limits and use the platform composer before publishing; this count is not a final platform acceptance check. No account login or scheduling occurs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-social-batch-plan
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
