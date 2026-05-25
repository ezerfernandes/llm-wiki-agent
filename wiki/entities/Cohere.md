---
title: "Cohere"
type: entity
tags: [company, ai-lab, model-provider, open-weights]
sources: [hands-on-llm-ch01-introduction-to-llms, ai-engineering-ch03-evaluation-methodology, ai-engineering-ch04-evaluate-ai-systems, hands-on-llm-ch04-text-classification, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

# Cohere

Toronto-based AI company; develops the **Command R** family of LLMs (R, R+, R7B) — among the open-weights models the [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]] cites as examples of openly-published models alongside [[Mistral]], [[microsoft|Microsoft's]] Phi, and [[meta|Meta's]] [[Llama]]. *"Some publicly shared models have a permissive commercial license"* — Command R is an example of weights-shared-with-conditions rather than strictly OSI-open licensing.

Cohere is also [[JayAlammar|Jay Alammar's]] employer (Director and Engineering Fellow) — relevant because Alammar's pedagogical work on *Hands-On LLMs* and the *Illustrated Transformer* series is informed by direct engineering work at a foundation-model lab.

## In *Hands-On LLMs* Ch 1

> "Cohere's Command R, the Mistral models, Microsoft's Phi, and Meta's Llama models are all examples of open models." — Ch 1 (p. 30)

The chapter uses Command R as one of four representative open-weights model families when introducing the open-vs-proprietary axis.

## Connections

- [[JayAlammar]] — employee; author of *Hands-On LLMs*.
- [[Mistral]] / [[meta|Meta]] / [[microsoft|Microsoft]] — peer open-weights model providers cited together in Ch 1.
- [[openai|OpenAI]] / [[anthropic|Anthropic]] — proprietary-model counterparts.
- [[HandsOnLLM]] — the book referencing Cohere.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1 source.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 positions Cohere as one of the **provider + API hybrid** model companies (alongside [[Mistral]]):

> "Cohere and Mistral open source some models and provide APIs for some."

Same incentive structure as Mistral: open-source for community goodwill but keep API services as a primary revenue stream. *"Both Mistral and Cohere have open source models, but they also have APIs. At some point, inference services on top of Mistral and Cohere models become their competitors."*

Cohere is also cited in [[ai-engineering-ch03-evaluation-methodology|Ch 3]]'s [[Embedding|embedding-size]] table — `embed-english-v3.0` 1024 dims, `embed-english-light-v3.0` 384 dims.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 names Cohere alongside [[openai|OpenAI]] as one of the two **production embedding-API alternatives** to running [[SentenceTransformers|sentence-transformers]] locally:

> "We used sentence-transformers to extract our embeddings, which benefits from a GPU to speed up inference. However, we can remove this GPU dependency by using an external API to create the embeddings. **Popular choices for generating embeddings are Cohere's and OpenAI's offerings.** As a result, this would allow the pipeline to run entirely on the CPU." — Ch 4

This positions Cohere — alongside its peer Mistral and the closed labs — as a **first-class member of the embedding-API tier** that GPU-poor practitioners can swap into the sentence-transformers slot of any Ch 4 / Ch 5 / Ch 8 pipeline.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 promotes Cohere from *"first-class embedding-API alternative"* (Ch 4) to **the chapter's primary managed-RAG API path** — Cohere's three endpoints constitute the canonical Ch 8 worked-example backbone:

| Endpoint | Concept page | Role |
|---|---|---|
| `co.embed` | [[CohereEmbed]] | Dense-retrieval substrate; `input_type="search_document" / "search_query"` |
| `co.rerank` | [[CohereRerank]] | Cross-encoder reranking |
| `co.chat(documents=...)` | [[CohereChat]] | Grounded generation + **automatic span-level citations** |

The **`co.chat` citation primitive** is the wiki's first runnable demonstration of span-level [[CitationGeneration|citation generation]]:

```python
response = co.chat(message=query, documents=docs_dict)
# response.citations = [ChatCitation(start=21, end=36, text='worldwide gross', document_ids=['doc_0']), ...]
```

Ch 8 also names **Cohere's Command R+** as a model that *"excels at"* [[AgenticRAG|agentic RAG]] tasks — *"available as an open-weights model as well"* — positioning Cohere uniquely as a frontier-API provider with open-weights flagship models that meet the agent-capability bar.

The Jay Alammar / Cohere connection ([[JayAlammar|Alammar]] is Director and Engineering Fellow at Cohere) is **structurally load-bearing** in Ch 8: the chapter's worked examples align tightly with Cohere's product surface because Cohere is the chapter's pedagogical platform.
