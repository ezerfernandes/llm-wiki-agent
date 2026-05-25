---
title: "Patrick Lewis"
type: entity
tags: [person, researcher, author, nlp, llm, rag]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Patrick Lewis

**First author of *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"*** (Lewis et al. 2020, NeurIPS 33: 9459–9474) — the foundational [[rag|RAG]] paper. Researcher at Facebook AI Research (now [[meta|Meta AI]]) at the time of publication; subsequently moved to [[Cohere]].

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 cites Lewis et al. 2020 as the canonical reference for [[rag|RAG]]:

> *"The leading method the industry turned to remedy this behavior is RAG, described in the paper 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' (2020)."*

The footnote in Ch 8 reads: *"Patrick Lewis et al. 'Retrieval-augmented generation for knowledge-intensive NLP tasks.' Advances in Neural Information Processing Systems 33 (2020): 9459–9474."*

## Why the paper matters

The 2020 RAG paper introduced **the architectural pattern** of pairing a learned retriever (DPR — Dense Passage Retrieval) with a generative model (BART) to ground generation on a non-parametric memory (Wikipedia). The pattern's name — *retrieval-augmented generation* — was coined by this paper and has since become the industry-standard term for the technique family.

The paper's contribution beyond the name is **end-to-end backpropagation through the retriever**: both the retriever's query encoder and the generator are fine-tuned jointly, with the retrieval distribution differentiable via marginalization over top-k documents. Modern production RAG systems usually do not backprop through the retriever (they use frozen embedding models), but the architectural pattern stuck.

## Connections

- [[rag]] — the technique family Lewis et al. founded.
- [[Lewis2020RAG]] — the paper source stub.
- [[meta|Meta]] / Facebook AI Research — affiliation at the time of the 2020 paper.
- [[Cohere]] — subsequent affiliation (joins [[JayAlammar]] at the same company).
- [[GroundedGeneration]] — the generation step Lewis et al. named.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source for the citation.
