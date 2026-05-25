---
title: "RAG Evaluation"
type: concept
tags: [evaluation, rag, metric, llm-as-judge, verifiability]
sources: [hands-on-llm-ch08-semantic-search-and-rag, 2408.08849-ecg-chat]
last_updated: 2026-05-23
---

# RAG Evaluation

**RAG evaluation** is the multi-axis evaluation surface for [[rag|RAG]] systems. Because RAG outputs **both retrieved context and generated answer** (often with [[CitationGeneration|citations]]), evaluating them requires more axes than either retrieval evaluation alone ([[MAP]] / [[NDCG]] / [[MRR]] / [[Recall]] / [[Precision]]) or generation evaluation alone ([[bleu|BLEU]] / [[ROUGE]] / [[Fluency|fluency]]).

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names two evaluation frameworks that operationalize RAG evaluation differently:

### The Liu / Zhang / Liang 2023 four-axis taxonomy

The paper *"Evaluating verifiability in generative search engines"* ([[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]], arXiv:2304.09848, 2023) defines four axes:

| Axis | Definition |
|---|---|
| **[[Fluency]]** | *"Whether the generated text is fluent and cohesive."* |
| **[[PerceivedUtility|Perceived utility]]** | *"Whether the generated answer is helpful and informative."* |
| **[[CitationRecall|Citation recall]]** | *"The proportion of generated statements about the external world that are fully supported by their citations."* |
| **[[CitationPrecision|Citation precision]]** | *"The proportion of generated citations that support their associated statements."* |

The paper's headline finding: **only 51.5% of generated sentences are fully supported by citations** on average across four commercial generative-search systems (Bing Chat / NeevaAI / Perplexity / YouChat). Citation-based verifiability is the production gap.

### The Ragas LLM-as-a-judge automation

Ch 8: *"there are approaches that attempt to automate these evaluations by having a capable LLM act as a judge (called LLM-as-a-judge) and score the different generations along the different axes. **[[RAGAS|Ragas]] is a software library that does exactly this.**"*

Ragas adds two further metrics beyond Liu et al.'s axes:

- **[[Faithfulness]]** — *"Whether the answer is consistent with the provided context."*
- **[[AnswerRelevance|Answer relevance]]** — *"How relevant the answer is to the question."*

(The full Ragas metric suite — see [[RAGAS]] and [[2408.08849-ecg-chat|ECG-Chat]] for the seven-metric coverage including Context Recall, Context Precision, Context Utilization, Context Entity Recall, Summarization Score — is broader; Ch 8 names just the two simplest.)

## Why RAG needs multi-axis evaluation

A single metric is **structurally insufficient** for RAG because the system can fail in three orthogonal ways:

1. **Retrieval failure** — the right document isn't retrieved. Caught by retrieval-side metrics ([[ContextRecall]] / [[ContextPrecision]] / [[MAP]] / [[NDCG]]).
2. **Generation failure** — the LLM doesn't faithfully use the retrieved context. Caught by [[Faithfulness]] / [[CitationRecall]].
3. **Question-answer mismatch** — the LLM answers an adjacent question or misses the user's intent. Caught by [[AnswerRelevance]] / [[PerceivedUtility]].

A multi-axis taxonomy lets the failure mode be diagnosed; a single score (e.g., end-to-end accuracy) lets the failure happen invisibly.

## Position relative to retrieval-only evaluation

Pure-retrieval evaluation uses [[MAP]] / [[NDCG]] / [[MRR]] — Ch 8 walks the [[PrecisionAtK|precision-at-k]] → [[AveragePrecision|AP]] → [[MAP]] construction step-by-step earlier in the chapter. These metrics are necessary but not sufficient for RAG because they ignore the **generation step**. The Liu et al. 2023 axes are the **generation-side extension** that completes the picture.

## Connections

- [[rag]] — the application family.
- [[Fluency]] / [[PerceivedUtility]] / [[CitationRecall]] / [[CitationPrecision]] — the Liu et al. 2023 four axes.
- [[Faithfulness]] / [[AnswerRelevance]] — Ragas metrics named in Ch 8.
- [[RAGAS]] — the LLM-as-a-judge library.
- [[CitationGeneration]] — the system primitive the citation axes require.
- [[ContextPrecision]] / [[ContextRecall]] — retrieval-side Ragas metrics (named in Huyen Ch 6 + ECG-Chat).
- [[MAP]] / [[NDCG]] / [[MRR]] — retrieval-only evaluation metrics.
- [[llmasjudge]] — the automation mechanism.
- [[NelsonFLiu]] / [[PercyLiang]] — verifiability paper authors.
- [[2408.08849-ecg-chat]] — wiki's deployed-RAG instance with full Ragas coverage.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
