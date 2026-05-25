---
title: "GraphRAG"
type: concept
tags: [rag, knowledge-graph, retrieval, microsoft, hallucination-mitigation]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# GraphRAG

**Edge, Trinh, Cheng, Bradley, Chao, Mody, Steven Truitt, Larson (Microsoft Research, 2024) — *"From local to global: A graph RAG approach to query-focused summarization."*** A [[rag|RAG]] variant that parses a corpus into a **graph structure of nodes and edges**, runs **community detection** (Louvain) to group related medical/technical topics, then retrieves and summarizes graph elements rather than flat text chunks. The empirical claim is that graph-level retrieval surfaces relationships standard chunk-level retrieval misses, particularly for *global* query-focused summarization questions that span many documents.

## Adapted to clinical reporting in [[2408.08849-ecg-chat]]

[[2408.08849-ecg-chat|ECG-Chat]] is the wiki's first record of GraphRAG applied to a **clinical specialty corpus**. The graph is built from seven cardiology textbooks — *ECG Workout: Exercises in Arrhythmia Interpretation* (Huff), *Manual of Cardiovascular Medicine* (Griffin), *Medical Student Survival Skills: ECG* (Jevon & Gupta), *Cardiology Subspecialty Consult* (Crawford & Lin), *The ECG Made Easy* (Hampton & Hampton), *The ECG In Practice* (Hampton), and *Arrhythmia Recognition: The Art of Interpretation* (Miller & Garcia) — and queried per-patient to retrieve a *"comprehensive 'global answer'"* on each ECG interpretation problem. Coupled with [[DSPy]] for prompt tuning, GraphRAG lifts **Faithfulness** on [[RAGAS]] from 39.87 (no RAG, no DSPy) to **82.12** (both). Faithfulness and Answer Relevancy benefit most from the graph (GraphRAG-only column: F 76.60, AR 68.29); Context Recall and Summarization Score benefit most from DSPy on top (CR 9.03→39.44, SS 18.94→81.83 with both).

## Connections
- [[2408.08849-ecg-chat]] — wiki's first clinical-specialty GraphRAG instance; co-deployed with [[DSPy]] prompt tuning.
- [[rag]] — the parent retrieval paradigm.
- [[DSPy]] — the prompt-tuning module ECG-Chat pairs GraphRAG with.
- [[Hallucination]] — the failure mode GraphRAG mitigates by grounding generation in authoritative graph nodes.
- [[LLMModuloFramework]] — GraphRAG functions as the *knowledge critic* in the Generate-Test-Critique loop.
- [[RAGAS]] — the metric suite ECG-Chat uses to evaluate the GraphRAG × DSPy interaction.
