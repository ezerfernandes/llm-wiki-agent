---
title: "Similarity Threshold"
type: concept
tags: [retrieval, rag, dense-retrieval, ood, filtering]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Similarity Threshold

**Similarity threshold** is the [[DenseRetrieval|dense-retrieval]] mitigation for **out-of-distribution (OOD) queries** — queries whose answer is not in the corpus. Without a threshold, dense retrieval will always return some nearest neighbor; with a threshold, retrievals below a configured similarity score are filtered as "no relevant result."

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 introduces the similarity threshold in the dense-retrieval caveats section, as a mitigation for the first of three named failure modes:

> *"What happens, for example, if the texts don't contain the answer? We still get results and their distances."* — Ch 8

Worked failure case: querying *"What is the mass of the moon?"* against the *Interstellar* Wikipedia corpus returns the film's worldwide-gross sentence as the nearest neighbor — because the corpus has nothing closer, the system surfaces something **arbitrary** that the user might mistake for an answer.

Ch 8's mitigation:

> *"In cases like this, one possible heuristic is to set a threshold level — a maximum distance for relevance, for example. A lot of search systems present the user with the best info they can get and leave it up to the user to decide if it's relevant or not. Tracking the information of whether the user clicked on a result (and were satisfied by it) can improve future versions of the search system."*

## Two design choices

1. **Hard threshold** — filter at retrieval time; return nothing if no candidate is above threshold. Useful when the application wants to say *"I don't know"* (e.g., grounded-answer chatbots that should refuse to answer when no context is found).

2. **Soft surface + user judgment** — return the best candidate regardless, but signal low confidence (display the similarity score, color-code, add a "low relevance" badge). Useful for traditional search where the user can scan results.

The choice is application-specific. RAG systems lean toward (1) because **the LLM will hallucinate fluently over a bad context** — the threshold prevents bad context from entering the prompt in the first place.

## Choosing the threshold

The threshold is **corpus and embedding-model dependent**:

- Different embedding models produce different similarity distributions; a threshold of 0.7 cosine on `all-mpnet-base-v2` is not the same as 0.7 on `text-embedding-3-large`.
- Different corpora have different baseline similarity distributions (a corpus of similar documents will have higher in-corpus similarities than a diverse corpus).

Practical calibration: sample 100 known positive queries + 100 known irrelevant queries, plot similarity-score distributions, pick a threshold that separates them. This is **the same calibration discipline as a classification threshold** in scikit-learn.

## Connections

- [[DenseRetrieval]] — the retrieval family this mitigation applies to.
- [[rag]] — the application surface.
- [[Hallucination]] — the downstream failure mode prevented by filtering bad context out before the prompt.
- [[CosineSimilarity]] / [[Embedding]] — the substrate.
- [[Precision]] / [[Recall]] — the classification analogy: threshold tunes precision vs recall on relevance.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
