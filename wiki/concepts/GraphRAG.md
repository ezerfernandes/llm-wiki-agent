---
title: "GraphRAG"
type: concept
tags: [rag, knowledge-graph, retrieval, microsoft, hallucination-mitigation]
sources: [2408.08849-ecg-chat, agentic-design-patterns-ch14-rag]
last_updated: 2026-06-07
---

# GraphRAG

**Edge, Trinh, Cheng, Bradley, Chao, Mody, Steven Truitt, Larson (Microsoft Research, 2024) — *"From local to global: A graph RAG approach to query-focused summarization."*** A [[rag|RAG]] variant that parses a corpus into a **graph structure of nodes and edges**, runs **community detection** (Louvain) to group related medical/technical topics, then retrieves and summarizes graph elements rather than flat text chunks. The empirical claim is that graph-level retrieval surfaces relationships standard chunk-level retrieval misses, particularly for *global* query-focused summarization questions that span many documents.

## Adapted to clinical reporting in [[2408.08849-ecg-chat]]

[[2408.08849-ecg-chat|ECG-Chat]] is the wiki's first record of GraphRAG applied to a **clinical specialty corpus**. The graph is built from seven cardiology textbooks — *ECG Workout: Exercises in Arrhythmia Interpretation* (Huff), *Manual of Cardiovascular Medicine* (Griffin), *Medical Student Survival Skills: ECG* (Jevon & Gupta), *Cardiology Subspecialty Consult* (Crawford & Lin), *The ECG Made Easy* (Hampton & Hampton), *The ECG In Practice* (Hampton), and *Arrhythmia Recognition: The Art of Interpretation* (Miller & Garcia) — and queried per-patient to retrieve a *"comprehensive 'global answer'"* on each ECG interpretation problem. Coupled with [[DSPy]] for prompt tuning, GraphRAG lifts **Faithfulness** on [[RAGAS]] from 39.87 (no RAG, no DSPy) to **82.12** (both). Faithfulness and Answer Relevancy benefit most from the graph (GraphRAG-only column: F 76.60, AR 68.29); Context Recall and Summarization Score benefit most from DSPy on top (CR 9.03→39.44, SS 18.94→81.83 with both).

## From [[agentic-design-patterns-ch14-rag|Agentic Design Patterns (Gulli) Ch 14]]

[[AntonioGulli|Gulli]] presents GraphRAG as *"an advanced form of Retrieval-Augmented Generation that utilizes a [[KnowledgeGraph|knowledge graph]] instead of a simple [[VectorDatabase|vector database]]. It answers complex queries by navigating the explicit relationships (edges) between data entities (nodes) within this structured knowledge base."* Its **key advantage** — the structural answer to traditional RAG's chief failing — is *"its ability to synthesize answers from information fragmented across multiple documents."*

Gulli's distinctive **use cases** anchor GraphRAG to interconnected-reasoning domains: complex **financial analysis**, **connecting companies to market events**, and **scientific research discovering relationships between genes and diseases**. The **drawbacks** he names: significant complexity, cost, and expertise to build & maintain a high-quality graph; less flexibility; higher latency than simpler vector search; and effectiveness *"entirely dependent on the quality and completeness of the underlying graph structure."* His summary verdict — *"it excels where deep, interconnected insights are more critical than the speed and simplicity of standard RAG"* — is the same speed-vs-depth trade-off the wiki's [[2408.08849-ecg-chat|ECG-Chat]] instance demonstrates empirically. Gulli cites the *"Retrieval-Augmented Generation with Graphs (GraphRAG)"* survey (arxiv 2501.00309) as the reference.

## Connections
- [[2408.08849-ecg-chat]] — wiki's first clinical-specialty GraphRAG instance; co-deployed with [[DSPy]] prompt tuning.
- [[agentic-design-patterns-ch14-rag]] — [[AntonioGulli|Gulli's]] knowledge-graph-vs-vector-DB framing + financial/gene-disease use cases.
- [[KnowledgeGraph]] — the node/edge structure GraphRAG retrieves over.
- [[VectorDatabase]] — the flat-retrieval substrate GraphRAG replaces with a graph.
- [[rag]] — the parent retrieval paradigm.
- [[DSPy]] — the prompt-tuning module ECG-Chat pairs GraphRAG with.
- [[Hallucination]] — the failure mode GraphRAG mitigates by grounding generation in authoritative graph nodes.
- [[LLMModuloFramework]] — GraphRAG functions as the *knowledge critic* in the Generate-Test-Critique loop.
- [[RAGAS]] — the metric suite ECG-Chat uses to evaluate the GraphRAG × DSPy interaction.
