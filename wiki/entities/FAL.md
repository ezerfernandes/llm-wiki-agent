---
title: "FAL"
type: entity
tags: [company, model-serving, image-generation, infrastructure]
sources: [dspy-image-generation-prompting-tutorial]
last_updated: 2026-05-24
---

# FAL

**FAL** ([fal.ai](https://fal.ai/), `fal-ai/...` namespace) is a **model-serving company** that hosts generative-AI inference endpoints — most prominently the [[FluxPro|Flux Pro]] / Flux Dev / Flux Schnell text-to-image models from [[BlackForestLabs|Black Forest Labs]] (`fal-ai/flux-pro/v1.1-ultra` and siblings).

The Python client `fal_client` exposes a **submit-then-poll** API surface:

```python
import fal_client

request_id = fal_client.submit("fal-ai/flux-pro/v1.1-ultra", arguments={"prompt": prompt}).request_id
result = fal_client.result("fal-ai/flux-pro/v1.1-ultra", request_id)
url = result["images"][0]["url"]
```

Returned image URLs are hosted on the `fal.media` CDN; the client returns the URL only (bytes are not delivered inline).

## In the wiki

- **First wiki receipt: [[dspy-image-generation-prompting-tutorial]]** — the dspy.ai *Image Generation Prompt Iteration* tutorial uses `fal-ai/flux-pro/v1.1-ultra` as the image generator inside a [[DSPy]] critic-then-revise loop. The returned URL is wrapped via [[DSPyImage|`dspy.Image.from_url(url)`]] for the next iteration's `current_image` input.

## Connections

- [[FluxPro]] — the text-to-image model FAL hosts that the first wiki receipt uses.
- [[BlackForestLabs]] — the model's maker.
- [[DSPyImage]] — the DSPy primitive wrapping FAL-returned URLs.
- [[dspy-image-generation-prompting-tutorial]] — first wiki receipt.
