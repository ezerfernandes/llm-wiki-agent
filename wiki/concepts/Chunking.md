---
title: "Chunking"
type: concept
tags: [rag, retrieval, preprocessing, embeddings]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch04-rag-feature-pipeline, leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment, ai-engineering-ch06-rag-agents, hands-on-llm-ch08-semantic-search-and-rag]
last_updated: 2026-05-23
---

## Definition
**Chunking** is the preprocessing step that splits long documents into smaller, semantically coherent passages so they can be individually embedded, indexed in a [[VectorDatabase]], and retrieved as context for [[rag|RAG]] generation. Chunk granularity directly shapes retrieval signal: too small loses context, too large dilutes semantic specificity.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] names chunking as one of the three core feature-pipeline operations (clean → chunk → embed), with category-specific strategies for articles, posts, and code. [[leh-ch04-rag-feature-pipeline]] gives the deep treatment: it describes **sliding-window chunking** with overlap (to preserve boundary context in legal/scientific/medical documents), the **small-to-big** strategy (embed a small high-purity span, store a wider window as metadata for prompt construction), and a concrete two-stage `chunk_text` pipeline using LangChain's `RecursiveCharacterTextSplitter` followed by `SentenceTransformersTokenTextSplitter` to enforce the embedding model's max token length. The article chunker uses a regex sentence splitter (`r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"`) that respects abbreviations like "e.g." and "Dr.", then groups sentences into 1,000–2,000-character chunks. The same regex is reused in [[leh-ch05-supervised-fine-tuning]] (for instruction-pair extraction) and [[leh-ch06-preference-alignment]] (for preference-triple extraction).

## Key details
- Trade-off: chunk size vs. retrieval precision vs. context completeness.
- The chunking strategy and the embedding model must be matched — the chunk's token count must respect the embedding model's `max_input_length`.
- Chunk IDs are typically content hashes (MD5/SHA-256) for automatic deduplication.
- **Sliding-window** (chunks overlap) preserves boundary semantics; **small-to-big** decouples retrieval signal from generation context.
- LangChain's `RecursiveCharacterTextSplitter(separators=["\n\n"], chunk_size=500, chunk_overlap=0)` is a paragraph-aware first stage; `SentenceTransformersTokenTextSplitter` enforces the embedding model's token cap with `chunk_overlap=50`.
- The same regex chunker is reused across SFT, DPO, and RAG feature pipelines — a single chunking abstraction underlies multiple downstream consumers.

## Connections
- [[rag]] — chunking is foundational to retrieval.
- [[Embedding]] — chunks are the unit embedded into the vector DB.
- [[VectorDatabase]] — stores chunk embeddings + metadata.
- [[SlidingWindowChunking]] — chunking with overlap.
- [[SmallToBigRetrieval]] — chunking strategy that embeds small spans and returns wider context.
- [[RecursiveCharacterTextSplitter]] — LangChain primitive used in the book's two-stage chunker.
- [[ChunkingStrategy]] — the broader design space the book treats per data category (article/post/code).
- [[Tokenizer]] — defines the token cap each chunk must respect.

## From [[ai-engineering-ch06-rag-agents|AI Engineering Ch 6]]

[[ChipHuyen|Huyen]] frames chunking as **the load-bearing index-time decision in any RAG pipeline** — *"the chunking strategy you use can significantly impact the performance of your retrieval system."* The Ch 6 contribution to this page's coverage is the **canonical worked failure case** for non-overlapping chunking:

> *"Consider the text 'I left my wife a note'. If it's split into 'I left my wife' and 'a note', neither of these two chunks conveys the key information of the original text. Overlapping ensures that important boundary information is included in at least one chunk. If you set the chunk size to be 2,048 characters, you can perhaps set the overlapping size to be 20 characters."*

The chapter pairs chunking with three other production retrieval-optimization tactics — [[ReRanking]], [[QueryRewriting]], [[ContextualRetrieval]] — covered together in the **retrieval optimization** section. See [[ChunkingStrategy]] for the strategy-design space; this page is the *"what is chunking?"* anchor.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 introduces chunking as **the structural answer to Transformer context limits**:

> *"One limitation of Transformer language models is that they are limited in context sizes, meaning we cannot feed them very long texts that go above the number of words or tokens that the model supports. So how do we embed long texts?"* — Ch 8

The Ch 8 contribution beyond Huyen Ch 6 / LEH Ch 4 is the **top-level one-vector-per-document vs multiple-vectors-per-document axis**:

| Approach | How |
|---|---|
| **One vector per document** | (a) Embed only a representative slice (title / opening) — *"useful to get quickly started with building a demo but it leaves a lot of information unindexed and therefore unsearchable"*; (b) embed all chunks and **average** their vectors — *"results in a highly compressed vector that loses a lot of the information."* |
| **Multiple vectors per document** | Chunk + embed each chunk; *"better because it has full coverage of the text and because the vectors tend to capture individual concepts inside the text. This leads to a more expressive search index."* |

Within the multiple-vectors-per-document family, Ch 8 surveys:

- **Each sentence is a chunk** — too granular; vectors don't capture enough context.
- **Each paragraph is a chunk** — good for short paragraphs; otherwise group every 3–8 sentences.
- **Title-prepended chunks** — inject document-level context into each chunk's text.
- **[[SlidingWindowChunking|Overlapping chunks]]** — *"adding some of the text before and after them to the chunk. This way, the chunks can overlap so they include some surrounding text that also appears in adjacent chunks."*
- **LLM-driven chunking** — *"Expect more chunking strategies to arise as the field develops — some of which may even use LLMs to dynamically split a text into meaningful chunks."*

The Ch 8 framing complements (rather than contradicts) [[ai-engineering-ch06-rag-agents|Huyen Ch 6's]] *"I left my wife a note"* failure-case framing and [[leh-ch04-rag-feature-pipeline|LEH Ch 4's]] regex-and-RecursiveCharacterTextSplitter implementation; the three sources together form **a complete chunking design space** for the wiki:

| Source | Framing |
|---|---|
| [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]] | **One-vs-multiple-vectors top-level axis** |
| [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] | **Fixed / recursive / language-specific / token-based / overlapping strategy menu** |
| [[leh-ch04-rag-feature-pipeline|LEH Ch 4]] | **`RecursiveCharacterTextSplitter` + `SentenceTransformersTokenTextSplitter` two-stage pipeline** |
