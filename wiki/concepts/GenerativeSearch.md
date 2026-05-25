---
title: "Generative Search"
type: concept
tags: [rag, search, llm, conversational-search, hallucination-mitigation]
sources: [hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Generative Search

**Generative search** is the class of search systems that **answer queries with LLM-generated natural-language text** (with citations back to source documents) rather than with a ranked list of links. Ch 8 of *Hands-On LLMs* names it as **a subset of [[rag|RAG]]**:

> *"Generative search is a subset of a broader type of category of systems better called RAG systems. These are text generation systems that incorporate search capabilities to reduce hallucinations, increase factuality, and/or ground the generation model on a specific dataset."* — Ch 8

The distinction Ch 8 draws is that *generative search* is a **product category** (the user-facing UI: a chat-style answer with citations) while *RAG* is the **technique family** (the architectural pattern: retrieve → augment prompt → generate). All generative search systems are RAG; not all RAG systems are generative search (an internal *"chat with my company docs"* tool is RAG but not generative search).

## Examples Ch 8 names

> *"More search engines are incorporating an LLM to summarize results or answer questions submitted to the search engine. Examples include [[Perplexity]], Microsoft Bing AI, and [[gemini|Google Gemini]]."*

Three categories represented:

| System | Category |
|---|---|
| **[[Perplexity]]** | Standalone generative-search startup. |
| **Microsoft Bing AI** | Traditional search engine + generative layer. |
| **[[gemini|Google Gemini]]** | Traditional search engine + AI-chat product overlay (Search Generative Experience). |

The competitive structure Ch 8 implies: the next generation of search products will all have generative-search components; the differentiation is the quality of retrieval × generation × citation.

## What distinguishes generative search from QA

Generative search differs from plain question-answering on **three axes**:

1. **Citation surface** — generative search answers carry **explicit links to source documents**. The [[NelsonFLiu|Liu / Zhang / Liang 2023]] verifiability paper Ch 8 cites runs human evaluations on commercial generative-search systems (Bing Chat, NeevaAI, Perplexity, YouChat) and reports **51.5% of generated sentences are fully supported** by their citations on average.
2. **Open-corpus retrieval** — generative search retrieves from the open web (or the search engine's full crawl), not from a curated knowledge base.
3. **Conversational follow-up** — generative search products tend to support multi-turn refinement (re-ranking the answer based on user clarifications), not just one-shot answers.

## Position in the RAG hierarchy

Generative search sits at the **most-user-facing end** of the RAG architecture hierarchy:

| Layer | Pattern | Example |
|---|---|---|
| Internal QA | Closed-corpus RAG | "Chat with our company docs" |
| Domain search | Mid-corpus RAG | Legal search, medical search |
| **Generative search** | **Open-web RAG** | **Perplexity, Bing AI, Gemini** |

## Connections

- [[rag]] — the parent technique family.
- [[GroundedGeneration]] — the generation step.
- [[Perplexity]] — canonical standalone generative-search product.
- [[gemini]] — Google's generative search product line.
- [[microsoft|Microsoft]] — Bing AI is generative search built on top of Bing.
- [[google|Google]] — Search Generative Experience / Gemini integration.
- [[CitationGeneration]] — the span-citation primitive that distinguishes generative search from plain QA.
- [[CitationRecall]] / [[CitationPrecision]] — the verifiability axes [[NelsonFLiu|Liu et al. 2023]] measure on commercial generative-search products.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
