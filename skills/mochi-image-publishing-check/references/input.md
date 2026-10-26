# Input contract

assets: file, optional width,height,alt,decorative. maxBytes: optional file budget. Does not decode dimensions.

## Operational scope

Inspect actual images with an image tool and verify declared dimensions before publishing. The helper does not generate images, evaluate alt-text accuracy, resize files or certify accessibility. Decorative status must be chosen deliberately.

## Fictional example

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

## Results

The helper returns `ok`, a task-specific `result`, a report path and an artifact list with byte counts and SHA-256. `ok=true` means this local transformation completed; use the explicit result fields for remaining work. Source files are not overwritten. Python3.10+ is required; IANA timezone support needs timezone data on the operating system or the Python tzdata package.
