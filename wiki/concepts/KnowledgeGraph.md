---
title: "Knowledge Graph"
type: concept
tags: [knowledge-graph, retrieval, rag, structured-knowledge, graphrag]
sources: [agentic-design-patterns-ch14-rag]
last_updated: 2026-06-07
---

# Knowledge Graph

A **knowledge graph** is a structured representation of information as a network of **entities (nodes)** connected by **explicit relationships (edges)**. Rather than storing facts as unstructured text or as isolated embedding vectors, a knowledge graph captures *how* entities relate — company → acquired → company, gene → associated-with → disease, document → cites → document — so a system can reason by **traversing** those relationships.

## Why it matters in agentic systems

In the retrieval context, a knowledge graph is the alternative substrate to a flat [[VectorDatabase|vector database]]. Flat vector retrieval finds chunks that are *semantically similar* to a query but is blind to the **connections** between facts spread across many documents — the chief failing of traditional [[rag|RAG]]. A knowledge graph makes those connections first-class, letting a retriever follow edges to assemble a multi-hop, structurally-grounded answer.

This is the foundation of **[[GraphRAG]]**: parse a corpus into a graph of nodes/edges, optionally run **community detection** (e.g. Louvain) to cluster related topics, then retrieve and summarize graph elements instead of independent text chunks. [[AntonioGulli|Gulli's]] [[AgenticDesignPatterns|*Agentic Design Patterns*]] Ch 14 describes GraphRAG as answering complex queries "by navigating the explicit relationships (edges) between data entities (nodes)," excelling at synthesizing answers fragmented across documents — financial analysis, company-to-market-event linkage, and gene–disease relationship discovery. The trade-off: building and maintaining a high-quality graph requires significant complexity, cost, and expertise, and the system's quality is entirely bounded by the graph's completeness.

## Connections
- [[GraphRAG]] — retrieval-augmented generation that retrieves over a knowledge graph instead of a vector DB.
- [[VectorDatabase]] — the flat-similarity substrate a knowledge graph is contrasted with.
- [[rag]] — the parent retrieval paradigm; knowledge graphs power its graph-structured variant.
- [[agentic-design-patterns-ch14-rag]] — source: Gulli's GraphRAG framing.
- [[PageRank]] — a classic graph-centrality algorithm over node/edge structures.
