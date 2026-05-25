---
title: "Copyright Regurgitation"
type: concept
tags: [llm, copyright, privacy, training-data, evaluation]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Copyright Regurgitation

**When an LLM emits, verbatim or near-verbatim, copyrighted material from its training data.** Can occur both as a [[InformationExtraction|prompt-attack]] outcome and as a **benign-prompt failure** — the model produces copyrighted content without anyone trying to extract it. Discussed in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

## Two failure modes

1. **Adversarial extraction.** An attacker engineers a prompt that elicits copyrighted material — e.g., the [[DivergenceAttack|divergence attack]] used by [[NasrEtAl2023|Nasr et al. 2023]] to surface verbatim training-data chunks.
2. **Spontaneous regurgitation.** A model generates copyrighted text for an ordinary user query, with no adversarial intent. Stanford's HELM 2022 study measured this by feeding the model the first paragraph of a book and prompting for the second; if the output matches the book, the model regurgitated.

## The HELM 2022 finding

Stanford's *"Holistic Evaluation of Language Models"* concluded:

> "The likelihood of direct regurgitation of long copyrighted sequences is somewhat uncommon, but it does become noticeable when looking at popular books." — paraphrased in Ch 5

So: **rare in expectation, common conditional on the source being popular**. This is the worst configuration for applications — your typical prompt is safe, but high-traffic prompts about famous works are unsafe.

## The non-verbatim problem

Ch 5's worked example: if a model outputs a story about *"the gray-bearded wizard Randalf on a quest to destroy the evil dark lord's powerful bracelet by throwing it into Vordor,"* the HELM study would not flag this as regurgitation — even though it is essentially a [[Lord of the Rings paraphrase]].

> "Determining whether something constitutes copyright infringement can take IP lawyers and subject matter experts months, if not years. It's unlikely there will be a foolproof automatic way to detect copyright infringement." — Ch 5

This is the fundamental reason copyright regurgitation is an *open problem* — verbatim regurgitation is rare and detectable, but non-verbatim regurgitation is common and undetectable.

## Beyond text

[[CarliniEtAl2023|Carlini et al. 2023]] extracted >1,000 near-duplicate images from [[StableDiffusion|Stable Diffusion]] — many containing trademarked company logos. The same problem applies to image and audio generation.

## Practical risk

> "Unknowingly using the regurgitated copyrighted materials can get you sued." — Ch 5

This affects three parties:

| Party | Risk |
|---|---|
| **Model developer** | Lawsuits from copyright holders (NYT v. OpenAI, etc.) |
| **Application developer** | Lawsuits from copyright holders if generated content is used commercially |
| **End user** | If they republish the regurgitated content |

## Defenses

The full defense menu, ranked by completeness:

1. **Don't train on copyrighted material.** Ch 5: *"The best solution... but if you don't train the model yourself, you don't have any control over it."*
2. **License the copyrighted training data.** Commercial deals.
3. **Train-time deduplication** to reduce per-document memorization.
4. **Output filters** that catch verbatim matches. Defeats verbatim regurgitation only.
5. **Indemnification by the model provider** — some providers (Microsoft, Google) offer customer-side legal protection for outputs.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[InformationExtraction]] — parent attack family (when adversarial).
- [[TrainingDataExtraction]] / [[DivergenceAttack]] — attack mechanisms that trigger regurgitation.
- [[NasrEtAl2023]] / [[CarliniEtAl2023]] — researchers.
- [[StableDiffusion]] — diffusion-model regurgitation example.
- [[Hallucination]] — sibling failure mode of generative models.
