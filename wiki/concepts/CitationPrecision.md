---
title: "Citation Precision"
type: concept
tags: [evaluation, rag, metric, verifiability, citations]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Citation Precision

**Citation precision** is one of the four axes of the [[RAGEvaluation|RAG-evaluation taxonomy]] defined by [[NelsonFLiu|Nelson F. Liu]], Tianyi Zhang, and [[PercyLiang|Percy Liang]] in *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848, 2023):

> *"Citation precision: the proportion of generated citations that support their associated statements."* — Ch 8 quoting the paper

## What it measures

For each **citation** in the generated answer, citation precision asks: **does this citation actually support the statement it's attached to?** The metric is computed over all citations and reports the fraction that genuinely support their associated span.

The structural difference from [[CitationRecall|citation recall]]: this metric iterates over **citations**, not over statements. Low precision means the answer is **citation-spamming** — attaching citations to spans they don't actually support.

## Position relative to [[CitationRecall]]

| Metric | Iterates over | Penalizes |
|---|---|---|
| **Citation precision** | Citations | Junk / unsupporting citations |
| **[[CitationRecall]]** | Statements | Unsupported claims |

The two are jointly necessary for **trustworthy verifiability**: high precision without recall means the answer is *"selectively careful"* — only citing some claims correctly while leaving others unsupported; high recall without precision means the answer is *"performatively cited"* — every claim has a citation but the citations don't actually back the claims up.

## When citation precision fails

Common failure modes:

1. **Wrong-document citation** — the cited document discusses an adjacent topic but doesn't contain the specific claim.
2. **Hallucinated citations** — the LLM emits a plausible-looking but non-existent reference (most severe failure mode; eliminated by **constraining citations to retrieved documents only**).
3. **Citation-spamming** — every sentence gets a citation regardless of whether retrieval supports it.

## Connections

- [[RAGEvaluation]] — the parent four-axis taxonomy.
- [[CitationRecall]] — the complementary axis.
- [[Fluency]] / [[PerceivedUtility]] — the two non-citation axes.
- [[CitationGeneration]] — the system primitive whose precision this metric measures.
- [[Faithfulness]] — the closely-related [[RAGAS|Ragas]] metric (faithfulness measures answer-context alignment; citation precision measures citation-statement alignment).
- [[llmasjudge]] — the automation path.
- [[NelsonFLiu]] / [[PercyLiang]] — paper authors.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
