---
title: "RAGAS"
type: concept
tags: [evaluation, rag, metrics]
sources: [2408.08849-ecg-chat, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# RAGAS — Retrieval-Augmented Generation Assessment

A reference-free evaluation framework for RAG systems. Used by [[2408.08849-ecg-chat|ECG-Chat]] as the metric suite for its GraphRAG × DSPy ablation on the [[ECGExpertQA]] benchmark.

## Seven metrics (per ECG-Chat Appendix F)

| Metric | What it measures |
|---|---|
| **Faithfulness (F)** | Generated answer is factually grounded in retrieved context. |
| **Answer Relevancy (AR)** | Generated answer addresses the question. |
| **Context Recall (CR)** | Retrieved context covers the ground-truth answer span. |
| **Context Precision (CP)** | Retrieved context is on-topic for the question. |
| **Context Utilization (CU)** | Generated answer uses available context. |
| **Context Entity Recall (CER)** | Retrieved context covers key entities. |
| **Summarization Score (SS)** | Generated answer summarizes context well. |

## Headline finding in [[2408.08849-ecg-chat]]

GraphRAG and DSPy are **largely orthogonal**: GraphRAG carries Faithfulness / AR / CER (retrieval-side); DSPy carries CR / SS (orchestration-side); both together cross 80+ on five of seven metrics.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names Ragas as the canonical **[[llmasjudge|LLM-as-a-judge]] automation library** for [[RAGEvaluation|RAG evaluation]]:

> *"There are approaches that attempt to automate these evaluations by having a capable LLM act as a judge (called LLM-as-a-judge) and score the different generations along the different axes. Ragas is a software library that does exactly this."* — Ch 8

The Ch 8 contribution is naming **two simpler metrics** beyond the ECG-Chat seven-metric coverage:

- **[[Faithfulness]]** — *"Whether the answer is consistent with the provided context."*
- **[[AnswerRelevance|Answer relevance]]** — *"How relevant the answer is to the question."*

These two are the **most-cited Ragas metrics** in practitioner discussions — Ch 8 introduces them as a pedagogical-friendly subset of the full library, while ECG-Chat exercises the full seven-metric surface in a deployed clinical-RAG instance.

The structural relationship: Ragas's metrics complement the **[[NelsonFLiu|Liu]] / Zhang / [[PercyLiang|Liang]] 2023** four-axis taxonomy ([[Fluency]] / [[PerceivedUtility]] / [[CitationRecall]] / [[CitationPrecision]]) that Ch 8 also names — Liu et al. focuses on **verifiability via citations**; Ragas focuses on **context-answer alignment via LLM judgment**. Both are necessary for full RAG evaluation; see [[RAGEvaluation]].

## Connections
- [[2408.08849-ecg-chat]] — deployed-RAG instance using the full seven-metric Ragas surface.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — pedagogical introduction; names the two simplest metrics.
- [[Faithfulness]] / [[AnswerRelevance]] — Ch 8's named metrics.
- [[RAGEvaluation]] — the multi-axis evaluation surface Ragas operationalizes.
- [[CitationRecall]] / [[CitationPrecision]] / [[Fluency]] / [[PerceivedUtility]] — Liu et al. 2023 axes (complement to Ragas metrics).
- [[llmasjudge]] — the mechanism.
- [[GraphRAG]], [[DSPy]] — the two modules being evaluated in ECG-Chat.
- [[ECGExpertQA]] — the ECG-Chat eval benchmark.
- [[rag]] — the parent paradigm.
