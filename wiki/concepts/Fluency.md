---
title: "Fluency"
type: concept
tags: [evaluation, rag, metric, verifiability]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Fluency

**Fluency** is the first axis of the four-axis [[RAGEvaluation|RAG-evaluation taxonomy]] defined by [[NelsonFLiu|Nelson F. Liu]], Tianyi Zhang, and [[PercyLiang|Percy Liang]] in *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848, 2023):

> *"Fluency: Whether the generated text is fluent and cohesive."* — Ch 8 quoting the paper

## What it measures

Fluency asks the most surface-level question of the four axes — **is the generated text well-written?** Independent of whether it's correct, helpful, or properly cited. Operationalized as a human judgment (or [[llmasjudge|LLM-as-a-judge]] rating) of:

- **Grammaticality** — is the text grammatically well-formed?
- **Cohesion** — do sentences flow logically into each other?
- **Naturalness** — does it read like text a competent human would write?

Modern LLMs are **near-saturated on fluency** — base-model fluency has been a non-blocker since GPT-3-class scale. The metric is retained in the four-axis taxonomy mostly as a sanity check and to expose the rare cases where a constrained-decoding or low-resource setup produces fluency degradation.

## Position vs other RAG-evaluation axes

| Axis | Saturated on modern LLMs? |
|---|---|
| **Fluency** | Mostly yes |
| **[[PerceivedUtility]]** | Partially — depends on domain |
| **[[CitationRecall]]** | No — *51.5%* on average (per Liu et al. 2023) |
| **[[CitationPrecision]]** | No — measurable gap |

The headline finding of the verifiability paper is that **modern generative search systems excel at fluency and perceived utility but fail at citation-based verifiability** — the two citation axes are where the production gap lives.

## Connections

- [[RAGEvaluation]] — the parent four-axis taxonomy.
- [[PerceivedUtility]] — sibling non-citation axis.
- [[CitationRecall]] / [[CitationPrecision]] — sibling citation axes.
- [[llmasjudge]] — the automation path.
- [[NelsonFLiu]] / [[PercyLiang]] — paper authors.
- [[bleu|BLEU]] / [[ROUGE]] / [[BERTScore]] — adjacent fluency-overlap metrics from machine-translation lineage.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
