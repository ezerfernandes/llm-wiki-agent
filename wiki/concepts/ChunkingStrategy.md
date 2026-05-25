---
title: "Chunking Strategy"
type: concept
tags: [llm-engineering]
sources: [leh-ch04-rag-feature-pipeline, ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

## Definition
The choice of how to split source documents into chunks for embedding and retrieval.

## In LLM Engineer's Handbook
Chunking strategies in [[leh-ch04-rag-feature-pipeline]] include: regex sentence chunking with min/max bounds for articles; [[RecursiveCharacterTextSplitter]] (paragraph-aware) + [[SentenceTransformersTokenTextSplitter]] (token-aware) for general text; broader chunks for code; narrower for prose. Chunk IDs are MD5 hashes of content for free deduplication. Chunk size must respect the embedding model's max input length.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] names chunking strategy as one of four production retrieval-optimization tactics (with [[ReRanking]], [[QueryRewriting]], [[ContextualRetrieval]]). Strategy survey:

- **Fixed-length by unit** — characters / words / sentences / paragraphs. *"You can split each document into chunks of 2,048 characters or 512 words"* or *"each chunk can contain a fixed number of sentences (such as 20)."*
- **Recursive** — start by splitting into sections; if a section is too long, split into paragraphs; if still too long, into sentences. *"This reduces the chance of related texts being arbitrarily broken off."*
- **Language-specific** — programming languages have dedicated splitters; Q&A documents split by question-answer pair; Chinese vs English need different rules.
- **Token-based** — chunk by the *generative model's* tokenizer so chunks align with downstream consumption. Downside: switching models requires reindexing.
- **Overlapping** — without overlap, *"I left my wife a note"* split into *"I left my wife"* and *"a note"* loses meaning. A typical overlap is 20 characters on a 2,048-character chunk.

**The trade-off** Huyen names:

| Smaller chunks | Larger chunks |
|---|---|
| More diversity per query | More continuity per chunk |
| More chunks → larger search space | Fewer chunks → faster search |
| Higher embedding-storage cost | Risk of losing context |
| Loss of important context | Loss of diversity |

> *"There is no universal best chunk size or overlap size. You have to experiment to find what works best for you."*

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 adds the **one-vector-per-document vs multiple-vectors-per-document top-level axis** that Huyen Ch 6 doesn't make explicit. See [[Chunking#from-hands-on-llms-ch-8]] for the full treatment; the headline is:

- **One vector per document** — embed slice (loses uncaptured text) or average chunks (loses precision).
- **Multiple vectors per document** — chunk + embed (full coverage, more vectors). Sub-strategies: sentence / paragraph / title-prepended / overlapping / LLM-driven.

Ch 8 explicitly forward-references LLM-driven chunking: *"Expect more chunking strategies to arise as the field develops — some of which may even use LLMs to dynamically split a text into meaningful chunks."*
