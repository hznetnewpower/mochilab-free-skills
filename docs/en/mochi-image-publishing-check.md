# Image Publishing Checklist

## Inspect the real assets first

Select images that the user intends to publish and view them with an available image tool. Supply the workspace-relative file path, declared dimensions and either meaningful alt text or a deliberate decorative designation. Do not mark informative diagrams decorative merely to suppress a missing-alt warning.

### Review the manifest findings

Compare byte counts with the publishing budget and verify declared dimensions using an image decoder. This helper does not decode image dimensions, judge visual quality or determine whether alt text describes the picture accurately. Keep any such checks as separately recorded evidence.

For oversized assets, choose a suitable export format and inspect the resulting image before replacement. Do not overwrite the original silently. Finish with an asset list, measured-size issues and unresolved accessibility or visual questions. A clean manifest report does not certify the whole page's accessibility, performance or appearance.

## Input example

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

Inspect actual images with an image tool and verify declared dimensions before publishing. The helper does not generate images, evaluate alt-text accuracy, resize files or certify accessibility. Decorative status must be chosen deliberately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-image-publishing-check
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
