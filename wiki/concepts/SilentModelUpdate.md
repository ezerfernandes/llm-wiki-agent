---
title: "Silent Model Update"
type: concept
tags: [drift, model-api, observability, production]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Silent Model Update

**A change in a hosted model's behavior behind a stable API endpoint, without the provider announcing the update.** Named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] under the *underlying-model-changes* class of [[DriftDetection|drift]].

> *"When using a model through an API, it's possible that the API remains unchanged while the underlying model is updated. … Model providers might not always disclose these updates, leaving it to you to detect any changes."* — Ch 10

## The canonical incidents

- **Chen, Zaharia & Zou (2023)** — *"How Is ChatGPT's Behavior Changing over Time?"* — observed notable differences in benchmark scores between the **March 2023 and June 2023** versions of GPT-4 and GPT-3.5 accessed through the same endpoint. Some tasks improved; others regressed.
- **[[Voiceflow]]** — a 10% performance drop in their intent-classification task when switching from `gpt-3.5-turbo-0301` to `gpt-3.5-turbo-1106`. (Also discussed in [[ai-engineering-ch04-evaluate-ai-systems|Ch 4]] as a [[CommercialModel|commercial-model versioning]] hazard, paired with [[GoDaddy]]'s improvement on the *same* migration — "the best model overall might not be the best model for your application.")

## Two flavors

1. **Versioned endpoint, behavioral drift** — provider issues a new dated model (`-1106` vs `-0301`) and lets you opt in. Update is announced, but the *delta* in your task's behavior isn't.
2. **Unversioned endpoint, silent swap** — provider updates the model behind `gpt-4` (no date) without changing the endpoint name. Even more dangerous — no opt-in moment.

## Defenses

- **Pin to versioned endpoints** when offered. Treat unversioned endpoints as a known volatility.
- **Continuous offline eval** — a small held-out evaluation set replayed against the live model on a schedule. Drift surfaces as a metric shift.
- **Production-traffic eval** — sample real requests through a [[ShadowDeployment|shadow deployment]] alongside the prior model where feasible.
- **Provider-side monitoring** — track provider release notes and changelogs; many providers publish them only after incidents force them to.

## Why this is uniquely painful in AI engineering

In conventional software, the provider can't change your dependency's behavior without you upgrading. In AI engineering, **the model is a hosted dependency that ships updates whenever the provider decides**, and the surface that exposes the change is *output quality on your specific task* — not a version string, not a 404, not anything an SRE alert would catch by default.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source (drift section).
- [[ai-engineering-ch04-evaluate-ai-systems]] — same incident discussed under [[CommercialModel|commercial-model]] hazards.
- [[Voiceflow]] / [[GoDaddy]] — case studies on opposite sides of the same migration.
- [[DriftDetection]] — parent concept.
- [[CommercialModel]] / [[ModelAPIProvider]] — the dependency class.
- [[Evaluation]] — the defensive instrument.
- [[ChangeFailureRate]] — silent updates contribute to CFR without being your own changes.
