---
name: mochi-image-publishing-check
description: "Check selected image assets for file budgets, declared dimensions and missing nondecorative alt text before publication."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Image Publishing Checklist

Check selected image assets for file budgets, declared dimensions and missing nondecorative alt text before publication.

## Inspect the real assets first

Select images that the user intends to publish and view them with an available image tool. Supply the workspace-relative file path, declared dimensions and either meaningful alt text or a deliberate decorative designation. Do not mark informative diagrams decorative merely to suppress a missing-alt warning.

### Review the manifest findings

Compare byte counts with the publishing budget and verify declared dimensions using an image decoder. This helper does not decode image dimensions, judge visual quality or determine whether alt text describes the picture accurately. Keep any such checks as separately recorded evidence.

For oversized assets, choose a suitable export format and inspect the resulting image before replacement. Do not overwrite the original silently. Finish with an asset list, measured-size issues and unresolved accessibility or visual questions. A clean manifest report does not certify the whole page's accessibility, performance or appearance.

## Reproducible request

assets: file, optional width,height,alt,decorative. maxBytes: optional file budget. Does not decode dimensions.

The following is fictional fixture data, not a live service result.

```json
{
  "assets": [
    {
      "file": "samples/demo.png",
      "width": 1,
      "height": 1,
      "alt": "Fictional one-pixel sample"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
