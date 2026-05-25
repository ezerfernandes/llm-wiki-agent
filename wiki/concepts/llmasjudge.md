---
title: "LLM-as-Judge"
type: concept
tags: [ml-method]
sources: [2601.21343-self-improving-pretraining, 2605.03808-agentic-imodels, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# LLM-as-Judge

Pattern in which a (typically stronger) LLM scores or compares the outputs of another model. Self-Improving Pretraining elevates this to the pretraining stage by using a post-trained model to judge rollouts vs original / rewritten suffixes; AGENTIC-IMODELS uses LLM-graded simulatability as the interpretability metric for evolved models.

## In [[rag|RAG]] evaluation

Per [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]: *"There are approaches that attempt to automate these evaluations by having a capable LLM act as a judge (called LLM-as-a-judge) and score the different generations along the different axes. **[[RAGAS|Ragas]]** is a software library that does exactly this."*

Ch 8 names Ragas as the canonical operationalization of LLM-as-a-judge for RAG. The [[RAGAS|Ragas]] metrics that Ch 8 cites — [[Faithfulness]] (answer-context consistency) and [[AnswerRelevance]] (answer-question relevance) — are computed by an LLM judge scoring claims / extracting questions, not by human annotators.

The structural reason LLM-as-a-judge works for RAG evaluation specifically: the per-axis questions ([[Faithfulness|is this claim supported by this context?]], [[CitationRecall|does this citation back this claim?]]) are **closed-context yes/no** questions — much easier than open-domain factual checking.

## Connections
- [[2601.21343-self-improving-pretraining]]
- [[2605.03808-agentic-imodels]]
- [[simulatability|Simulatability]]
- [[RAGAS]] — the canonical RAG-evaluation operationalization of LLM-as-a-judge.
- [[RAGEvaluation]] — the multi-axis evaluation surface LLM-as-a-judge automates.
- [[Faithfulness]] / [[AnswerRelevance]] / [[CitationRecall]] / [[CitationPrecision]] — the RAG-evaluation axes LLM-as-a-judge scores.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — RAG-evaluation source.
- [[LLMAsAJudge]] — sibling concept page on the wider use of LLM judges (different name, related coverage).
