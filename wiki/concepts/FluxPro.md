---
title: "Flux Pro (v1.1 Ultra)"
type: concept
tags: [image-generation, text-to-image, diffusion, flux, blackforestlabs, model]
sources: [dspy-image-generation-prompting-tutorial]
last_updated: 2026-05-24
---

# Flux Pro (v1.1 Ultra)

**Flux Pro** is the commercial-tier text-to-image model in the **Flux** family from [[BlackForestLabs|Black Forest Labs]] — the same team that produced the [[StableDiffusion|Stable Diffusion]] line before founding Black Forest Labs. **First wiki receipt: [[dspy-image-generation-prompting-tutorial]]**, which uses the `fal-ai/flux-pro/v1.1-ultra` endpoint hosted by [[FAL]] as the image generator inside a DSPy critic-then-revise prompt-iteration loop.

The Flux family ships in three quality/cost tiers — *Schnell* (fastest, open weights), *Dev* (open weights, non-commercial), *Pro* (highest quality, closed, API-only). The `v1.1-ultra` variant the [[dspy-image-generation-prompting-tutorial|tutorial]] selects is the highest-tier endpoint at the time of the wiki ingest; the tutorial does not exercise a Schnell/Dev/Pro ablation.

## Invocation (via [[FAL]])

```python
import fal_client

request_id = fal_client.submit(
    "fal-ai/flux-pro/v1.1-ultra",
    arguments={"prompt": prompt},
).request_id
result = fal_client.result("fal-ai/flux-pro/v1.1-ultra", request_id)
url = result["images"][0]["url"]
```

The model returns one (or more) **hosted image URL**(s) on `fal.media/files/...`. The URL is the only artifact returned; bytes are not delivered inline.

## Position vs siblings

- [[StableDiffusion|Stable Diffusion]] — the open-weight progenitor lineage; Flux is the next-gen architecture from the same core team. Stable Diffusion is the wiki's existing reference for diffusion-based text-to-image.
- [[DallE|DALL-E 3]] — [[OpenAI]]'s proprietary text-to-image model; the closest commercial sibling. Not exercised in the first wiki receipt.
- [[MidJourney]] — proprietary aesthetic-tuned text-to-image; not exercised.
- [[DiffusionModel]] — the architectural family Flux belongs to.

## Connections

- [[BlackForestLabs]] — the model's maker.
- [[FAL]] — the serving infrastructure that hosts the `fal-ai/flux-pro/v1.1-ultra` endpoint used in [[dspy-image-generation-prompting-tutorial]].
- [[DSPyImage]] — the DSPy primitive that wraps Flux Pro's returned URLs via `dspy.Image.from_url(url)`.
- [[DiffusionModel]] — architectural family.
- [[dspy-image-generation-prompting-tutorial]] — first wiki receipt.
