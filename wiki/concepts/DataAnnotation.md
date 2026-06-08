---
title: "Data Annotation"
type: concept
tags: [dataset-engineering, labeling, supervised-learning]
sources: [ai-engineering-ch08-dataset-engineering, mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Data Annotation

**Labeling raw data with the targets a supervised-learning model will be trained against.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], annotation in the foundation-model era covers (instruction, response) pairs for [[SupervisedFinetuning|SFT]], (instruction, winner, loser) triples for [[PreferenceFinetuning|preference]] training, and ((instruction, response), score) tuples for [[RewardModel|reward modeling]].

## Two flavors

1. **Manual annotation** — human labelers write or rate responses.
2. **AI-powered annotation** — an [[LLMAsAJudge|LLM-as-judge]] or other AI model produces labels.

Both flavors need **[[AnnotationGuidelines|annotation guidelines]]** — the rubric that defines what counts as a good response.

## Why annotation is hard in the FM era

> "Acquiring high-quality data annotations is always challenging, but it's even more challenging if you want to teach models complex behaviors such as chain-of-thought (CoT) reasoning and tool use."

CoT example from Ch 8 (Chun et al. 2024): explaining how to solve a math problem step-by-step is much more challenging than simply giving the final answer. As a result, **CoT datasets are less common than other instruction datasets**.

## When AI annotators beat humans (Ch 8)

[[Llama|Llama 3]] team found:

> "Human-generated data is more prone to errors and inconsistencies, particularly for nuanced safety policies. This led them to develop AI-assisted annotation tools to ensure high data quality."

Three more cases:

- **Tool use** — humans demo via web UIs; AI uses APIs more efficiently. Humans miss steps; observation is needed but biased.
- **Complex math** — AI can generate problems beyond average expert difficulty.
- **Preference ratings** — AI consistency exceeds humans (humans are affected by mood, motivation).

## When humans still win

- **Long-form responses** — AI hallucinates more in long outputs.
- **Domain expertise** — clinical, legal, scientific (with verification).
- **Cultural / political nuance** — explicit human judgment required.
- **Adversarial robustness checks** — humans surface attacks AI generators miss.

## Hybrid pattern: AI instructions + human responses (or vice versa)

Per Ch 8: split annotation by which side is easier to do well at scale. Common patterns:

- AI generates instructions + humans write responses ([[ReverseInstruction|reverse-instruction]] variants).
- Humans write instructions + AI generates responses.
- AI does both, humans verify/filter.

## Cost-benchmark anchor

InstructGPT's annotation:

- ≈$10/(prompt, response) pair × 13,000 pairs ≈ $130,000.
- Labelers ~90% college-educated; ≥1/3 with master's degrees.
- 30 min/pair for long-context summarization.

## Connections

- [[AnnotationGuidelines]] — the rubric that drives annotation quality.
- [[DataLabeling]] — the systems-engineering treatment ([[mlsysbook-ch04-data-engineering|mlsysbook Ch 4]]: label types, consensus via [[CohensKappa|Cohen's]]/Fleiss' κ, tiered escalation, [[AIAssistedLabeling|AI-assisted labeling]]).
- [[DemonstrationData]] — (prompt, response) pairs for SFT.
- [[ComparisonData]] — (prompt, winner, loser) preference data.
- [[LLMAsAJudge]] — AI-powered annotation.
- [[DataAcquisition]] — annotation as one of four channels.
- [[ai-engineering-ch08-dataset-engineering]] / [[mlsysbook-ch04-data-engineering]] — sources.
