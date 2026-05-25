---
title: "Faithfulness"
type: concept
tags: [evaluation, rag, metric, ragas, llm-as-judge, hallucination]
sources: [hands-on-llm-ch08-semantic-search-and-rag, 2408.08849-ecg-chat]
last_updated: 2026-05-23
---

# Faithfulness

**Faithfulness** is a [[RAGAS|Ragas]] metric that measures whether the generated answer is **consistent with the retrieved context** — i.e., whether the LLM stuck to what the retrieved documents say or extrapolated beyond them. A central [[llmasjudge|LLM-as-a-judge]] axis for [[rag|RAG]] evaluation.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names faithfulness as one of two Ragas metrics added beyond the [[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]] 2023 four-axis [[RAGEvaluation|RAG-evaluation taxonomy]]:

> *"It also scores some additional useful metrics like: **Faithfulness** — Whether the answer is consistent with the provided context."* — Ch 8

The other Ch 8-named Ragas metric is [[AnswerRelevance]].

## Position vs other RAG metrics

| Metric | Domain | Failure mode it flags |
|---|---|---|
| **Faithfulness** | answer ↔ retrieved context | Answer contradicts or extrapolates beyond context |
| **[[CitationRecall]]** | answer claims ↔ citations | Claims are unsupported by citations |
| **[[CitationPrecision]]** | citations ↔ claims | Citations don't actually back their claims |
| **[[AnswerRelevance]]** | answer ↔ question | Answer talks about something off-topic |

Faithfulness is the **context-side mirror of [[Hallucination|hallucination]]** — a faithful answer has zero hallucinations relative to its context (it might still be wrong if the context itself is wrong, but it didn't add anything beyond the context).

## In [[2408.08849-ecg-chat|ECG-Chat]]

Ch 8 introduces faithfulness as a single metric; [[2408.08849-ecg-chat|ECG-Chat]] uses it as the **primary axis** in the GraphRAG × DSPy ablation. The headline finding: **GraphRAG lifts Faithfulness from 39.87 to 76.60 alone** on the ECG-ExpertQA benchmark; combined with DSPy, the full system crosses 80 on faithfulness.

The two sources agree on faithfulness's definitional content; ECG-Chat is the deployed-system anchor and Ch 8 is the pedagogical introduction.

## How Ragas computes it

Ragas's faithfulness metric uses an LLM judge to:

1. **Extract atomic claims** from the generated answer.
2. **For each claim**, ask the judge whether the claim is verifiable from the provided context (yes/no).
3. **Faithfulness score** = fraction of claims that are verifiable.

This is the structural reason faithfulness can be automated by [[llmasjudge|LLM-as-a-judge]] — the per-claim verification is a closed-context yes/no question, much easier than open-domain factual checking.

## Connections

- [[RAGAS]] — the parent metric framework.
- [[RAGEvaluation]] — the broader multi-axis surface.
- [[AnswerRelevance]] — the sibling Ragas metric Ch 8 also names.
- [[CitationRecall]] / [[CitationPrecision]] — adjacent verifiability metrics.
- [[Hallucination]] — the failure mode faithfulness operationalizes detection of.
- [[GroundedGeneration]] — the generation step faithfulness scores.
- [[llmasjudge]] — the automation mechanism.
- [[2408.08849-ecg-chat]] — deployed clinical-RAG instance using faithfulness as primary axis.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
