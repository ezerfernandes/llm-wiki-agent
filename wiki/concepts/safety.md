---
title: "Safety"
type: concept
tags: [evaluation, safety, generation, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Safety

**The umbrella term for all types of toxicity and biases** in AI-generated outputs. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], one of the two key [[GenerationCapability|generation-capability]] metrics (alongside [[FactualConsistency|factual consistency]]).

## Six categories of unsafe content

Per Ch 4 — different safety solutions categorize harms differently, but in general:

1. **Inappropriate language** — profanity, explicit content.
2. **Harmful recommendations and tutorials** — *"step-by-step guide to rob a bank"*, encouraging self-harm.
3. **Hate speech** — racist, sexist, homophobic, discriminatory.
4. **Violence** — threats, graphic detail.
5. **Stereotypes** — gendered job stereotypes, etc.
6. **Political / religious bias** — model overrepresents an ideology.

## Documented political-leaning skew

Feng et al. 2023, Motoki et al. 2023, Hartman et al. 2023: model alignment leaves measurable political biases. Per Ch 4:

> "OpenAI's GPT-4 is more left-winged and libertarian-leaning, whereas Meta's Llama is more authoritarian."

## Detection: general-purpose vs specialized

- **General-purpose [[LLMAsAJudge|AI judges]]** — GPT-4 / Claude / Gemini can detect harm if prompted properly. Anthropic publishes a content-moderation tutorial for Claude.
- **Provider moderation tools** — [[OpenAIModeration|OpenAI's content moderation endpoint]], Meta's [[LlamaGuard]].
- **Specialized classifiers** — [[FacebookHateSpeech|Facebook's hate-speech model]], [[SkolkovoToxicityClassifier|Skolkovo's toxicity classifier]], [[PerspectiveAPI|Perspective API]]. *"Specialized models tend to be much smaller, faster, and cheaper than general-purpose AI judges."*
- **Language-specialized** — Danish, Vietnamese, and many other language-specific toxicity classifiers exist.

## Benchmarks

- **[[RealToxicityPrompts]]** (Gehman et al. 2020) — 100K prompts that elicit toxicity.
- **[[BOLD]]** (Dhamala et al. 2021) — bias in open-ended generation.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[GenerationCapability]] — parent eval bucket.
- [[FactualConsistency]] — sibling generation-quality metric.
- [[LlamaGuard]] / [[OpenAIModeration]] / [[PerspectiveAPI]] / [[FacebookHateSpeech]] / [[SkolkovoToxicityClassifier]] — detection tools.
- [[RealToxicityPrompts]] / [[BOLD]] — benchmarks.
- [[Guardrail]] — the defensive infrastructure that operationalizes safety.
- [[Hallucination]] — factual unsafety, technically under safety but treated as separate.
