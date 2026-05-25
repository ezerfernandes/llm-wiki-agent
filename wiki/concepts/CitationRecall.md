---
title: "Citation Recall"
type: concept
tags: [evaluation, rag, metric, verifiability, citations]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Citation Recall

**Citation recall** is one of the four axes of the [[RAGEvaluation|RAG-evaluation taxonomy]] defined by [[NelsonFLiu|Nelson F. Liu]], Tianyi Zhang, and [[PercyLiang|Percy Liang]] in *"Evaluating verifiability in generative search engines"* (arXiv:2304.09848, 2023):

> *"Citation recall: the proportion of generated statements about the external world that are fully supported by their citations."* — Ch 8 quoting the paper

## What it measures

For each **factual claim** in the generated answer, citation recall asks: **does at least one of the cited documents fully support this claim?** The metric is computed over all factual claims and reports the fraction that are fully supported.

The structural difference from accuracy: citation recall does **not** require the claim to be *correct in absolute terms* — only that **the citation supports the claim**. A correctly-cited but factually-wrong claim (when the source itself is wrong) has perfect citation recall and zero accuracy. The two metrics are complementary.

## Position relative to [[CitationPrecision]]

| Metric | What it measures |
|---|---|
| **Citation recall** | *Statement → citation*: of all factual statements, how many have supporting citations? |
| **[[CitationPrecision]]** | *Citation → statement*: of all citations, how many actually support their associated statement? |

The asymmetry: low **citation recall** means the answer contains **unsupported claims** (statements without citations or with citations that don't actually support them). Low **citation precision** means the answer has **junk citations** (citations attached to spans they don't actually support, or citing irrelevant documents).

## The verifiability paper's headline finding

The Liu / Zhang / Liang 2023 paper runs human evaluations on four commercial generative-search systems and reports the **51.5%** number — *"only 51.5% of generated sentences are fully supported by citations on average."* This is the **canonical anchor** for *what real RAG systems achieve on citation recall in 2023*.

## Connections

- [[RAGEvaluation]] — the parent four-axis taxonomy.
- [[CitationPrecision]] — the complementary axis.
- [[Fluency]] / [[PerceivedUtility]] — the two non-citation axes.
- [[CitationGeneration]] — the system primitive that produces the citations citation recall measures.
- [[Faithfulness]] — the closely-related [[RAGAS|Ragas]] metric (faithfulness measures whether the **answer is consistent with the context**; citation recall measures whether **claims have citations that support them** — the citation pointer is the load-bearing difference).
- [[llmasjudge]] — the automation path for scoring citation recall at scale.
- [[NelsonFLiu]] / [[PercyLiang]] — paper authors.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
