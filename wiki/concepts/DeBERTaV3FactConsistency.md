---
title: "DeBERTa-v3-base-mnli-fever-anli"
type: concept
tags: [model, classifier, factuality, nli, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# DeBERTa-v3-base-mnli-fever-anli

A **184-million-parameter [[TextualEntailment|NLI]] classifier** trained on 764,000 annotated (hypothesis, premise) pairs to predict entailment / contradiction / neutral. Cited by [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]] as a canonical example of a specialized [[FactualConsistency|factual-consistency]] scorer that is *"smaller, faster, and cheaper than general-purpose AI judges."*

## What's in the name

- **DeBERTa-v3-base** — Microsoft's *Decoding-enhanced BERT with disentangled attention*, base size (≈184M params).
- **mnli** — trained on Multi-Genre NLI (MNLI).
- **fever** — trained on FEVER (Fact Extraction and VERification).
- **anli** — trained on Adversarial NLI.

The model output is a 3-class prediction over `{entailment, contradiction, neutral}`.

## Use as a factual-consistency scorer

Pass (context, generated_output) as (premise, hypothesis); read the entailment probability as a graded factual-consistency score, or threshold to a binary inconsistent / consistent / undetermined decision.

## Why it's chosen for evaluation

- Much smaller than GPT-4-class judges (184M vs 100B+).
- Deterministic and reproducible (no sampling).
- Cheap enough to run on 100% of outputs at production scale.
- Specialized — trained explicitly on the entailment task rather than instruction-tuned on a wide distribution.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[TextualEntailment]] — the task this model classifies.
- [[FactualConsistency]] / [[LocalFactualConsistency]] — what it scores for.
- [[bert|BERT]] / [[DeBERTa]] — model family lineage.
- [[LLMAsAJudge]] — the alternative paradigm this competes with on cost.
