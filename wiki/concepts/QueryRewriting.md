---
title: "Query Rewriting"
type: concept
tags: [rag, retrieval, llm, optimization]
sources: [ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Query Rewriting

**Query rewriting** (a.k.a. *query reformulation*, *query normalization*, *query expansion*) is the RAG retrieval-optimization tactic of **transforming the user's query into one that retrieves better results** before sending it to the retriever. Named in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as one of four core retrieval-optimization tactics, alongside [[ChunkingStrategy|chunking strategy]], [[ReRanking|reranking]], and [[ContextualRetrieval|contextual retrieval]].

## The canonical conversational case

```
User: When was the last time John Doe bought something from us?
AI: John last bought a Fruity Fedora hat from us two weeks ago, on January 3, 2030.
User: How about Emily Doe?
```

The third query, *"How about Emily Doe?"*, is ambiguous in isolation. Used verbatim, it retrieves irrelevant results. The rewriter, given the conversation history, transforms it into *"When was the last time Emily Doe bought something from us?"* — a self-contained query that the retriever can act on.

## Heuristics vs LM-driven

[[ChipHuyen|Huyen]] notes:

> *"In traditional search engines, query rewriting is often done using heuristics. In AI applications, query rewriting can also be done using other AI models, using a prompt similar to 'Given the following conversation, rewrite the last user input to reflect what the user is actually asking'."*

The LM-driven path is more flexible but introduces a hallucination surface: if the user asks *"How about his wife?"*, the rewriter must first **resolve identity** ("his" → which user → who is their wife) and refuse to hallucinate when the identity isn't in the system of record.

## Position in retrieval optimization

| Tactic | What it modifies |
|---|---|
| [[ChunkingStrategy]] | The corpus, at index time |
| [[ContextualRetrieval]] | The chunks themselves, at index time |
| **Query rewriting** | The query, at runtime |
| [[ReRanking]] | The retrieved set, after retrieval |

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 introduces query rewriting in its **Advanced RAG Techniques** section as the **first step on the delegation continuum** (followed by [[MultiQueryRAG|multi-query]] → [[MultiHopRAG|multi-hop]] → [[QueryRouting|routing]] → [[AgenticRAG|agentic]]):

> *"If the RAG system is a chatbot, the preceding simple RAG implementation would likely struggle with the search step if a question is too verbose, or to refer to context in previous messages in the conversation. This is why it's a good idea to use an LLM to rewrite the query into one that aids the retrieval step in getting the right information."* — Ch 8

**The canonical Ch 8 worked example** — the rambling student-essay question:

> *"User Question: 'We have an essay due tomorrow. We have to write about some animal. I love penguins. I could write about them. But I could also write about dolphins. Are they animals? Maybe. Let's do dolphins. Where do they live for example?'"*
> 
> Should be rewritten into:
> 
> *"Query: 'Where do dolphins live'"*

This is a **different failure mode** from Huyen Ch 6's *"How about Emily Doe?"* (multi-turn referent resolution); Ch 8's failure mode is **conversational verbosity / topic-drift** in single-turn input. The rewrite primitive handles both.

**API path Ch 8 names**: *"Cohere's API, for example, has a dedicated query-rewriting mode for `co.chat`"* — making query rewriting a first-class managed feature alongside [[CohereRerank|`co.rerank`]] and [[CohereChat|`co.chat`]]'s grounded-generation primitive.

## Connections

- [[rag]] — the application family.
- [[ContextualRetrieval]] / [[ChunkingStrategy]] / [[ReRanking]] — sibling optimization tactics.
- [[MultiQueryRAG]] / [[MultiHopRAG]] / [[QueryRouting]] / [[AgenticRAG]] — the next points on Ch 8's Advanced-RAG delegation continuum.
- [[Hallucination]] — the rewriter's failure mode (hallucinating identity resolution).
- [[CohereChat]] — Cohere's managed-API with built-in query-rewriting mode.
- [[ai-engineering-ch06-rag-agents]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — secondary source.
