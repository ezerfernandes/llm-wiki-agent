---
title: "Lewis et al. 2020 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
type: source
tags: [paper, rag, neurips, 2020, dpr, bart, meta]
date: 2020-12-01
source_file: ""
arxiv_id: "2005.11401"
venue: "NeurIPS 2020"
authors: ["Patrick Lewis", "Ethan Perez", "Aleksandra Piktus", "Fabio Petroni", "Vladimir Karpukhin", "Naman Goyal", "Heinrich Küttler", "Mike Lewis", "Wen-tau Yih", "Tim Rocktäschel", "Sebastian Riedel", "Douro Kiela"]
---

# Lewis et al. 2020 — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Summary

**Stub** — full paper not yet ingested. The **foundational [[rag|RAG]] paper** that introduced the architectural pattern and coined the name *retrieval-augmented generation*. Pairs a learned retriever (DPR — Dense Passage Retrieval) with a generative model (BART) to ground generation on a non-parametric memory (Wikipedia). Cited in [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]] as the canonical RAG reference.

Published in NeurIPS 33 (2020): 9459–9474; arXiv:2005.11401.

## Key contribution

The paper's beyond-naming contribution is **end-to-end backpropagation through the retriever** — both the retriever's query encoder and the generator are fine-tuned jointly, with the retrieval distribution differentiable via marginalization over top-k documents. Modern production RAG systems usually do not backprop through the retriever (they use frozen embedding models), but the architectural pattern stuck.

## Connections
- [[rag]] — the technique family this paper founded.
- [[PatrickLewis]] — first author.
- [[meta|Meta]] / Facebook AI Research — affiliation at time of publication.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8 cites this paper.
- [[ai-engineering-ch06-rag-agents]] — Huyen Ch 6 also references the paper indirectly through the broader RAG discussion.
- [[GroundedGeneration]] — the generation step the paper named.
