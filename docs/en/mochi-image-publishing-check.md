# Image Publishing Checklist

## What it does

Check selected image assets for file budgets, declared dimensions and missing nondecorative alt text before publication.

## How to use it

Give the assistant the concrete task and required inputs. This fictional request illustrates the contract; use your selected files and parameters for real work.

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

## Output and verification

Creates a JSON report and, when applicable, CSV, Markdown or document artifacts in the current workspace. Inputs remain intact. Five offline tests cover the example, invalid input, actual CLI output, path boundaries and non-overwrite behavior. Live account, browser and visual results require separate verification.

## Scope

Inspect actual images with an image tool and verify declared dimensions before publishing. The helper does not generate images, evaluate alt-text accuracy, resize files or certify accessibility. Decorative status must be chosen deliberately.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-image-publishing-check
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
