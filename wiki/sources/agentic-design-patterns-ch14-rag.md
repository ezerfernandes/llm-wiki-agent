---
title: "Chapter 14 — Knowledge Retrieval / RAG (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, rag, retrieval, embeddings, vector-database, semantic-search, graphrag, agentic-rag, grounding, citations]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 14 of [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] presents the **Knowledge Retrieval (RAG)** pattern: connecting LLMs to external knowledge bases so they "look up" current, private, or specialized information before generating an answer — transforming a closed-book reasoner into an open-book one and grounding outputs in verifiable, citable data. It walks the foundational mechanics ([[Embedding|embeddings]], text/[[SemanticSimilarity|semantic similarity]], [[Chunking|chunking]], [[VectorDatabase|vector databases]], [[SemanticSearch|semantic]] vs [[BM25]]/[[HybridSearch|hybrid]] retrieval), then two advanced variants — **[[GraphRAG]]** (retrieval over a knowledge graph of nodes/edges) and **[[AgenticRAG]]** (a reasoning agent that validates, reconciles, decomposes, and tool-augments retrieval). It closes with three hands-on examples on [[GoogleADK|Google ADK]] ([[google|Google Search]] grounding + [[GoogleCloudVertexAI|Vertex AI]] `VertexAiRagMemoryService`) and a full [[LangChain]]/[[langgraph|LangGraph]] + [[Weaviate]] RAG pipeline. (Agentic Design Patterns, PDF pp 213–230.)

## Key Claims
- RAG addresses the core limitation of LLMs — static, training-bound knowledge — by enabling access to external, current, and context-specific information, improving accuracy, relevance, and factual grounding. For AI agents this is "crucial as it allows them to ground their actions and responses in real-time, verifiable data," transforming agents "from simple conversationalists into effective, data-driven tools capable of executing meaningful work."
- The mechanism: a user query is **not** sent directly to the LLM; the system first runs a **semantic search** (understanding intent/meaning, not keyword match) over an external knowledge base, pulls the most relevant **chunks**, **augments** the prompt with them, and only then sends the enriched prompt to the LLM for a fluent answer "factually grounded in the retrieved data."
- Foundational concepts: **[[Embedding|Embeddings]]** (numerical vectors capturing semantic meaning — "cat" (2,3) near "kitten" (2.1,3.1), far from "car" (8,1); real ones are hundreds–thousands of dimensions); **Text Similarity** (lexical/surface vs deeper meaning); **[[SemanticSimilarity|Semantic Similarity and Distance]]** (meaning-based; high similarity = low distance; "a furry feline companion" ≈ "a domestic cat" despite no shared words).
- **[[Chunking|Chunking]]**: breaking large documents into smaller manageable pieces because a RAG system cannot feed entire large documents to the LLM; chunking strategy (sections/paragraphs/sentences) preserves context and makes retrieval faster and more focused (e.g. a "Troubleshooting" chunk separate from the "Installation Guide").
- Retrieval techniques: **vector search** (embeddings + semantic distance) is primary; **[[BM25]]** is an older but valuable keyword/term-frequency algorithm without semantic understanding; **[[HybridSearch|hybrid search]]** combines BM25's keyword precision with semantic search's contextual understanding for more robust retrieval.
- **[[VectorDatabase|Vector databases]]** store and query embeddings efficiently for semantic search — "while other techniques search for words, vector databases search for meaning." Named implementations: managed [[Pinecone]] and [[Weaviate]]; open-source [[ChromaDB|Chroma DB]], [[Milvus]], [[Qdrant]]; vector-augmented existing DBs [[RedisVectorSearch|Redis]], [[Elasticsearch]], [[PostgreSQL|Postgres (pgvector)]]. Core retrieval engines are often powered by libraries like Meta AI's [[FAISS]] or Google Research's [[ScaNN]]; vector DBs use ANN algorithms like **[[HNSW]]** (Hierarchical Navigable Small World).
- RAG's benefits: up-to-date info, reduced **[[Hallucination|hallucination]]** via grounding in verifiable data, use of specialized internal/wiki knowledge, and — "a vital advantage" — **[[CitationGeneration|citations]]** that pinpoint the exact source, enhancing trustworthiness and verifiability.
- RAG's challenges: information spread across multiple chunks/documents can leave the retriever unable to gather all needed context; effectiveness depends heavily on chunking/retrieval quality (irrelevant chunks add noise); synthesizing **contradictory** sources is hard; the knowledge base must be pre-processed into vector/graph DBs (a considerable undertaking requiring periodic reconciliation); and the process adds latency, cost, and token usage.
- **[[GraphRAG]]**: an advanced RAG that uses a **knowledge graph** instead of a vector DB, answering complex queries by navigating explicit relationships (edges) between data entities (nodes). Its key advantage is synthesizing answers from information fragmented across documents — a common failing of traditional RAG. Use cases: complex financial analysis, connecting companies to market events, scientific research on gene-disease relationships. Drawbacks: significant complexity/cost/expertise to build & maintain the graph, less flexibility, higher latency; effectiveness depends entirely on graph quality/completeness. "It excels where deep, interconnected insights are more critical than the speed and simplicity of standard RAG."
- **[[AgenticRAG]]**: introduces a reasoning/decision-making layer where an "agent" acts as a critical **gatekeeper and refiner** of knowledge rather than passively accepting retrieved data. Four scenarios: (1) **reflection & source validation** — discard an outdated 2020 blog post in favor of the authoritative 2025 policy doc by analyzing metadata; (2) **reconciling knowledge conflicts** — choose the finalized financial report (€65,000) over the initial proposal (€50,000); (3) **multi-step reasoning** — decompose "compare our product to Competitor X's features+pricing" into sub-queries, run distinct searches, synthesize a structured comparative context; (4) **identify knowledge gaps and use external [[ToolUse|tools]]** — when the internal base lacks fresh info, activate a live web-search API. Agentic RAG "picks tools to call" (per Fig.2) vs Naive RAG's fixed query→vectors→chunks→model pipeline.
- Challenges of Agentic RAG: significant increase in complexity and cost (decision logic + tool integrations require engineering effort and compute), increased latency from reflection/tool-use/multi-step cycles, and the agent itself as a new error source (flawed reasoning → useless loops, misinterpreted tasks, improperly discarded info).
- Practical applications: Enterprise Search & Q&A (internal chatbots over HR policies/manuals/specs), Customer Support & Helpdesks (manuals/FAQs/tickets), Personalized Content Recommendation (semantically related vs keyword matching), News & Current-Events Summarization (real-time feeds).
- Rule of thumb: use RAG "when you need an LLM to answer questions or generate content based on specific, up-to-date, or proprietary information that was not part of its original training data" — ideal for Q&A over internal docs, customer-support bots, and citation-bearing fact-based responses.

## Key Quotes
> "Knowledge Retrieval (RAG, or Retrieval Augmented Generation), addresses this limitation. RAG enables LLMs to access and integrate external, current, and context-specific information, thereby enhancing the accuracy, relevance, and factual basis of their outputs." — Pattern intro

> "This search is not a simple keyword match; it's a 'semantic search' that understands the user's intent and the meaning behind their words." — RAG Pattern Overview

> "while other techniques search for words, vector databases search for meaning." — Vector databases

> "A vital advantage of this process is the capability to offer 'citations,' which pinpoint the exact source of information, thereby enhancing the trustworthiness and verifiability of the AI's responses." — RAG benefits

> "Rather than passively accepting the initially retrieved data, this agent actively interrogates its quality, relevance, and completeness." — Agentic RAG

> "This process effectively transforms the LLM from a closed-book reasoner into an open-book one, significantly enhancing its utility and trustworthiness." — At Glance / Why

> "Finetuning is for form, and RAG is for facts." — (the wiki's existing canonical decision rule; consistent with Ch 14's framing of RAG as the fix for static, factual-knowledge limitations)

## Connections
- [[RAG]] — the chapter IS the canonical RAG pattern (#14 of the 21 patterns); this source augments the canonical [[rag]] page.
- [[AgenticDesignPatterns]] / [[AntonioGulli]] — the book and author.
- [[AgenticDesignPattern]] — RAG is the 14th of the book's 21 agentic design patterns.
- [[Embedding]] / [[SemanticSimilarity]] / [[SemanticSearch]] — the foundational vector-meaning concepts the chapter builds on.
- [[Chunking]] — document splitting for retrievable units.
- [[VectorDatabase]] — the storage substrate; [[HNSW]] ANN index; [[FAISS]] / [[ScaNN]] core libraries.
- [[BM25]] / [[HybridSearch]] — keyword and fused retrieval, complementing semantic search.
- [[CitationGeneration]] / [[GroundedGeneration]] / [[Hallucination]] — the trust/verifiability payoff and the failure mode RAG mitigates.
- [[GraphRAG]] — knowledge-graph retrieval variant; [[KnowledgeGraph]].
- [[AgenticRAG]] — the agent-as-gatekeeper evolution; [[ToolUse]] (web-search gap-filling), [[Reflection]] (source validation), [[Planning]] (multi-step decomposition), [[Routing]] (source/tool selection).
- [[ToolUse]] (Ch 5) — RAG-as-tool; [[ModelContextProtocol]] (Ch 10) — tools/data over MCP; [[MemoryManagement]] (Ch 8) — `VertexAiRagMemoryService` is the RAG-backed long-term memory store.
- [[GoogleADK]] — `google_search` grounding tool + `VertexAiRagMemoryService` (`SIMILARITY_TOP_K`, `VECTOR_DISTANCE_THRESHOLD`) hands-on examples.
- [[GoogleCloudVertexAI]] — Vertex AI Search / RAG Engine / RAG Corpus.
- [[LangChain]] / [[langgraph|LangGraph]] — the third hands-on example: `CharacterTextSplitter` → [[openai|OpenAI]] `OpenAIEmbeddings` → [[Weaviate]] vectorstore → `StateGraph` (retrieve → generate) RAG pipeline; [[openai|OpenAI]] `gpt-3.5-turbo` generator.
- [[Lewis2020RAG]] / [[PatrickLewis]] — the foundational 2020 RAG paper (Ref 1: arxiv 2005.11401), cited here too.

## Contradictions
- None found. Ch 14's mechanics, vendor list, and trade-offs are consistent with the wiki's existing multi-source RAG treatment ([[ai-engineering-ch06-rag-agents|Huyen Ch 6]], [[hands-on-llm-ch08-semantic-search-and-rag|Hands-On LLMs Ch 8]], LEH Ch 4). Gulli's account is a concise, agent-centric introduction rather than an engineering deep-dive; it adds the explicit "agent as knowledge gatekeeper" four-scenario framing for [[AgenticRAG]] and the financial-analysis/gene-disease use cases for [[GraphRAG]].
