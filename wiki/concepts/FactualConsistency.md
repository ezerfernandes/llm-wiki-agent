---
title: "Factual Consistency"
type: concept
tags: [evaluation, generation, factuality, hallucination]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Factual Consistency

The **primary generation-quality metric** for detecting [[Hallucination|hallucinations]], per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]. Two settings:

- **[[LocalFactualConsistency|Local factual consistency]]** — output evaluated against a given context (summarization, customer support, business analysis). *"If the model outputs 'the sky is blue' and the given context says that the sky is purple, this output is considered factually inconsistent."*
- **[[GlobalFactualConsistency|Global factual consistency]]** — output evaluated against open knowledge (general chatbots, fact-checking, market research).

> "Factual consistency is much easier to verify against explicit facts. … If no context is given, you'll have to first search for reliable sources, derive facts, and then validate the statement against these facts."

## When models hallucinate more

From Huyen's own projects:

1. **Niche knowledge** — *"more likely to hallucinate when I asked it about the VMO (Vietnamese Mathematical Olympiad) than the IMO."*
2. **Non-existent referents** — *"if I ask the model 'What did X say about Y?' the model is more likely to hallucinate if X has never said anything about Y than if X has."*

Benchmarks should focus on these query types.

## Three evaluation approaches

### 1. AI-as-judge prompt

Liu et al. 2023, Luo et al. 2023: GPT-3.5/GPT-4 outperform prior methods. Sample prompt (Liu et al. 2023, verbatim with typo per Huyen):

```
Factual Consistency: Does the summary untruthful or misleading facts that are not supported by the source text?
Source Text: {{Document}}
Summary: {{Summary}}
Does the summary contain factual inconsistency?
```

### 2. [[SelfCheckGPT|Self-verification]] (SelfCheckGPT, Manakul et al. 2023)

Generate N alternate responses; if they disagree with the original, the original is likely hallucinated. *Expensive* — N model calls per evaluation.

### 3. [[SAFEEvaluator|Knowledge-augmented verification]] (SAFE, DeepMind, Wei et al. 2024)

Four steps: (1) decompose response into individual statements; (2) revise statements to be self-contained; (3) generate fact-checking queries → Google Search API; (4) AI determines statement consistency with search results.

## As a classification task: textual entailment

[[TextualEntailment|Textual entailment]] (aka NLI) frames factual consistency as classification:

| Given premise | Hypothesis | Class | Factual meaning |
|---|---|---|---|
| "Mary likes all fruits" | "Mary likes apples" | Entailment | Consistent |
| "Mary likes all fruits" | "Mary hates oranges" | Contradiction | Inconsistent |
| "Mary likes all fruits" | "Mary likes chickens" | Neutral | Undetermined |

Specialized scorers — like [[DeBERTaV3FactConsistency|`DeBERTa-v3-base-mnli-fever-anli`]] (184M params, 764K labeled pairs) — make this faster and cheaper than general-purpose AI judges.

## Benchmarks

- **[[TruthfulQA]]** (Lin et al. 2022) — 817 questions across 38 categories that humans often answer incorrectly due to false beliefs. Ships with [[GPTJudge]] (90-96% human-agreement).

## In RAG

> "Factual consistency is a crucial evaluation criteria for RAG, retrieval-augmented generation, systems. Given a query, a RAG system retrieves relevant information from external databases to supplement the model's context. The generated response should be factually consistent with the retrieved context."

RAG = a Local-Factual-Consistency-evaluable system by construction.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[LocalFactualConsistency]] / [[GlobalFactualConsistency]] — the two settings.
- [[SelfCheckGPT]] / [[SAFEEvaluator]] — advanced detection methods.
- [[TextualEntailment]] / [[DeBERTaV3FactConsistency]] — classification framing.
- [[TruthfulQA]] / [[GPTJudge]] — benchmark + paired judge.
- [[Hallucination]] / [[factuality|Factuality]] — what this metric is for.
- [[GenerationCapability]] — parent evaluation bucket.
- [[rag|RAG]] — the system class most dependent on this metric.
