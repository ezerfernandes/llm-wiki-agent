---
title: "Contextual Retrieval"
type: concept
tags: [rag, retrieval, anthropic, optimization]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Contextual Retrieval

**Contextual retrieval** is the retrieval-optimization tactic of **augmenting each chunk with surrounding context before indexing** — making the chunk self-contained enough that the retriever can find it from a query that wouldn't naturally match the raw chunk. [[anthropic|Anthropic]] introduced the LM-generated variant in their 2024 *Introducing Contextual Retrieval* post; [[ChipHuyen|Huyen]] names it in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as one of four core retrieval-optimization tactics.

## Three augmentation families

1. **Metadata, tags, keywords**: ecommerce products augmented with descriptions and reviews; images with titles and captions; documents with entity tags. If your document contains specific error codes like `EADDRNOTAVAIL (99)`, adding them to metadata allows retrieval-by-keyword even after embedding conversion would otherwise obscure them.
2. **Anticipated questions**: customer-support articles augmented with related queries (e.g. the *reset password* article augmented with *"How to reset password?"*, *"I forgot my password"*, *"I can't log in"*, *"Help, I can't find my account"*). *"Some teams have told me that their retrieval systems work best when the data is organized in a question-and-answer format."*
3. **LM-generated chunk context** (the [[anthropic|Anthropic]] 2024 method): use an AI model to generate a short 50–100-token context that *"explains the chunk and its relationship to the original document"*, prepend that context to each chunk, then index the augmented chunk. Anthropic's exact prompt:

```
<document>{{WHOLE_DOCUMENT}}</document>
Here is the chunk we want to situate within the whole document:
<chunk>{{CHUNK_CONTENT}}</chunk>
Please give a short succinct context to situate this chunk within the
overall document for the purposes of improving search retrieval of the
chunk. Answer only with the succinct context and nothing else.
```

## Why it helps

A chunk split out of a long document can lose **what it's about** — the chunk might say *"This results in a 50% improvement"* without identifying *what* improves *over what*. Prepending *"Section discussing the Q3 sales conversion rate, comparing to the previous quarter"* gives the retriever (and the generator) the surface signal needed to find and use the chunk.

## Position in retrieval optimization

Contextual retrieval modifies the **chunks themselves** at index time — distinct from [[ChunkingStrategy]] (which modifies how text is *split*), [[QueryRewriting]] (which modifies queries at runtime), and [[ReRanking]] (which reorders retrieved results).

## Connections

- [[rag]] — the application family.
- [[anthropic]] — popularized the LM-generated variant.
- [[ChunkingStrategy]] — the upstream step contextual retrieval augments.
- [[QueryRewriting]] / [[ReRanking]] — sibling optimization tactics.
- [[Embedding]] — what the augmented chunks become.
- [[ai-engineering-ch06-rag-agents]] — primary source.
