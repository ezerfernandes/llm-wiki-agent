---
title: "RAG Chatbot (baseline)"
type: concept
tags: [system, baseline, llm-application, rag]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# RAG Chatbot

**RAG Chatbot** — the [[rag|retrieval-augmented generation]] conversational baseline used in [[2408.15232-co-storm|Co-STORM]]'s evaluation. A canonical *one-question-one-answer* information-seeking system: the user asks a question, the system retrieves passages via a search engine, the LM composes a cited answer; repeat.

## Why it's the baseline

The RAG Chatbot pattern is the dominant deployed paradigm in 2024 — every major *generative search* product ([[BingChat]], Google AI Overviews, You.com Chat, Perplexity) follows this template. It is the **realistic alternative** Co-STORM is being measured against.

## Limits the paper draws out

1. **Single-source initiative**. The user must formulate every question. This fails for [[UnknownUnknowns|unknown unknowns]] — users with limited prior knowledge cannot ask what they don't know to ask ([[Kuhlthau1991]]; [[Belkin1982]]).
2. **Echo-chamber risk** ([[ShermanEtAl2024|Sharma et al. 2024]]). Generative search chatbots tend to surface views consistent with user-stated framings, narrowing the information space rather than broadening it.
3. **No durable artifact**. Each conversation is ephemeral; there is no curated long-form takeaway.

## Result

In Co-STORM's evaluation, the RAG Chatbot baseline loses on all four report-quality dimensions, and is preferred only 22% of the time (vs Co-STORM's 78%) for overall information-seeking experience. Co-STORM also cites ~2× as many unique URLs per turn (6.04 vs 2.94), indicating broader retrieval *within* turns.

| Metric | RAG Chatbot | [[CoSTORM]] |
|---|---|---|
| Relevance | 3.57 | 3.78 |
| Breadth | 3.50 | 3.79 |
| Depth | 3.26 | 3.77 |
| Novelty | 2.44 | 3.05 |
| # Unique URLs / turn | 2.94 | 6.04 |

## See also
- [[rag]] · [[CoSTORM]] · [[ConversationalQA]] · [[GoogleSearch]] · [[QASystem]]
