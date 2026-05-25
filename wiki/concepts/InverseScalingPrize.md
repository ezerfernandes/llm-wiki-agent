---
title: "Inverse Scaling Prize"
type: concept
tags: [scaling, evaluation, contest, nyu]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Inverse Scaling Prize

A 2023 research contest, organized largely by [[NYU|New York University]] researchers, designed to **find tasks where larger language models perform worse** — concrete demonstrations of [[InverseScaling|inverse scaling]].

## Prize structure

| Tier | Award |
|---|---|
| First | **$100,000** (1 prize) |
| Second | **$20,000 each** |
| Third | **$5,000 each** |

## Results

- **99 submissions** total.
- **11 third prizes awarded.**
- **No first or second prize awarded.**

Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "They found that larger language models are sometimes (only sometimes) worse on **tasks that require memorization** and **tasks with strong priors**. However, they didn't award any second or first prizes because even though the submitted tasks show failures for a small test set, none demonstrated failures in the real world."

## What this tells us

1. **Inverse scaling is real but narrow.** It exists, but the failures don't generalize to production tasks.
2. **The natural failure surface is "strong priors + memorization."** Tasks where the prior is misleading or where the model needs to override a memorized pattern are the most likely candidates.
3. **The "$100K is hard to win" outcome itself is data.** If three orders of magnitude of model size had produced real-world inverse-scaling failures, the prize would have been awarded.

## Connections
- [[InverseScaling]] — the phenomenon the prize targets.
- [[NYU]] — the academic home of the organizers.
- [[scalinglaws]] / [[ChinchillaScalingLaw]] — the positive-scaling defaults this contest rebuts.
- [[ai-engineering-ch02-foundation-models]] — primary source.
