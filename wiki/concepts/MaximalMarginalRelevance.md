---
title: "Maximal Marginal Relevance (MMR)"
type: concept
tags: [reranking, diversity, keyword-selection, retrieval]
sources: [hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Maximal Marginal Relevance (MMR)

**Maximal Marginal Relevance (MMR)** is a classical reranking algorithm ([[JaimeCarbonell|Carbonell]] & Goldstein 1998) that iteratively selects items maximizing a **diversity-vs-relevance tradeoff**. It is used in [[BERTopic]] as a [[KeyBERTInspired|representation model]] to **diversify topic keywords** by removing near-duplicates while keeping relevance.

## The MMR criterion

At each step, given a set of already-selected items `S` and a candidate set `C`, pick the candidate maximizing:

$$
\text{MMR}(c) = \lambda \cdot \text{Sim}(c, \text{topic}) - (1 - \lambda) \cdot \max_{s \in S} \text{Sim}(c, s)
$$

where:
- `Sim(c, topic)` rewards relevance to the topic centroid.
- `max_{s ∈ S} Sim(c, s)` penalizes similarity to already-chosen items.
- `λ` controls the tradeoff. In BERTopic, **`diversity = 1 - λ`** — higher `diversity` → more spread, lower → more relevance.

## In BERTopic (per *Hands-On LLMs* Ch 5)

[[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]: *"We can use maximal marginal relevance (MMR) to diversify our topic representations. The algorithm attempts to find a set of keywords that are diverse from one another but still relate to the documents they are compared to. It does so by embedding a set of candidate keywords and iteratively calculating the next best keyword to add. Doing so requires setting a diversity parameter, which indicates how diverse keywords need to be."*

BERTopic uses MMR to go from a larger candidate set (e.g., 30 keywords from c-TF-IDF) to a **smaller, more diverse subset** (e.g., 10 keywords). *"It filters out redundant words and only keeps words that contribute something new to the topic representation."*

## Why MMR matters for topic keywords

[[ClassBasedTFIDF|c-TF-IDF]] often produces near-duplicate keywords ranked together — *"summary"*, *"summaries"*, *"summarization"* might all show up for a summarization topic. MMR keeps **one** representative from each near-duplicate group and uses the freed positions for **broader topic coverage**.

## Usage

```python
from bertopic.representation import MaximalMarginalRelevance

representation_model = MaximalMarginalRelevance(diversity=0.2)
topic_model.update_topics(abstracts, representation_model=representation_model)
```

`diversity=0.2` is a mild diversification; `diversity=0.5` is aggressive. Defaults work well for most topic-keyword tasks.

## Example outputs (per Ch 5)

| Topic | c-TF-IDF (original) | MMR (`diversity=0.2`) |
|---|---|---|
| 4 (summarization) | summarization \| summaries \| summary \| abstract... | summarization \| document \| extractive \| rouge \| ... |
| 3 (NMT) | translation \| nmt \| machine \| neural \| bleu | translation \| nmt \| bleu \| parallel \| multilingual \| ... |

Note that unlike [[KeyBERTInspired]], MMR **preserves domain abbreviations** (*"nmt"*, *"bleu"* still appear) — because MMR operates on the c-TF-IDF candidates rather than reranking via embeddings.

## Beyond topic modeling

MMR also applies in:
- **Search result diversification** — show diverse top-K hits.
- **[[rag|RAG]] context selection** — diverse retrieved passages.
- **Summarization** — select diverse sentences for an extractive summary.

In each case, MMR is the **canonical answer** to *"how do I add diversity to a relevance-ranked list?"*

## Connections

- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — primary source.
- [[BERTopic]] — parent framework.
- [[ClassBasedTFIDF]] — the upstream candidate set MMR re-selects from.
- [[KeyBERTInspired]] / [[GenerativeTopicLabeling]] — sibling BERTopic representation models.
- [[ReRanking]] — the parent pattern.
- [[CosineSimilarity]] — the underlying similarity metric.
- [[JaimeCarbonell]] — co-author of the original MMR paper.
