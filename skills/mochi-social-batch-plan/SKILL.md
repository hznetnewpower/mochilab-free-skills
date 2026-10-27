---
name: mochi-social-batch-plan
description: "Review draft posts against user-supplied platform character limits and asset lists without scheduling or publishing."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Social Draft Batch Review

Review draft posts against user-supplied platform character limits and asset lists without scheduling or publishing.

## Prepare an editorial batch

Assign every post a stable ID, intended platform, final text and optional asset references. Supply the current character limit for each platform from an authoritative source. Keep drafts distinct from content already approved or scheduled.

### Resolve length findings in context

The helper counts Unicode code points. Platforms can apply weighted characters, special URL rules or different limits by account type, so validate borderline posts in the real composer. Shorten wording without changing a factual claim, removing necessary attribution or leaving a misleading fragment.

Review referenced assets and the intended publishing account before any live action. This package does not log in, schedule posts or submit content. Deliver the batch with over-limit IDs and the counting assumptions, then obtain any required publication approval and verify the platform's actual response separately.

## Reproducible request

platformLimits: platform-to-positive-integer map. posts: id,platform,text, optional assets. Counts Unicode code points.

The following is fictional fixture data, not a live service result.

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

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
