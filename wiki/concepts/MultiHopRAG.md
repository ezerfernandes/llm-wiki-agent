---
title: "Multi-Hop RAG"
type: concept
tags: [rag, retrieval, advanced-rag, multi-hop, reasoning]
sources: [hands-on-llm-ch08-semantic-search-and-rag, dspy-rl-multihop-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# Multi-Hop RAG

**Multi-hop RAG** is the advanced-[[rag|RAG]] extension where one user question requires a **sequence of queries, each depending on the previous result**. The system retrieves → reasons → emits a follow-up query → retrieves again → ... until the original question can be answered. Distinct from [[MultiQueryRAG]] (parallel queries) by the sequential dependency.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names multi-hop RAG in the **Advanced RAG Techniques** section:

> *"A more advanced question may require a series of sequential queries."* — Ch 8

The canonical worked example:

> *"User Question: 'Who are the largest car manufacturers in 2023? Do they each make EVs or not?'"*
> 
> **Step 1**, Query 1: *"largest car manufacturers 2023"*
> 
> **Step 2** (after Step 1 returns Toyota, Volkswagen, Hyundai):
> - Query 1: *"Toyota Motor Corporation electric vehicles"*
> - Query 2: *"Volkswagen AG electric vehicles"*
> - Query 3: *"Hyundai Motor Company electric vehicles"*

The sequential structure is load-bearing — the Step 2 queries can't be generated without first running Step 1 and parsing its results.

## When to use multi-hop

Multi-hop is the right technique when the user's question contains a **chained dependency**:

- *"Who founded X, and where did they go to school?"* (X → founder → founder's school)
- *"What are the top-5 grossing movies of 2023, and which won Oscars?"* (year → movies → per-movie award lookup)
- *"What is the population of the capital of Country X?"* (country → capital → population)

The structural signature: the answer to query N+1 depends on the result of query N.

## Position in the Advanced-RAG continuum

Multi-hop is the **sequential-decomposition** point on Ch 8's delegation continuum (vs [[MultiQueryRAG|multi-query RAG]]'s parallel decomposition):

| Technique | Query structure | Sequential dependency? |
|---|---|---|
| [[QueryRewriting]] | One → one | No |
| [[MultiQueryRAG]] | One → N parallel | No |
| **Multi-hop RAG** | **One → N sequential** | **Yes** |
| [[QueryRouting]] | One → routed | No (data-source-level, not query-sequential) |
| [[AgenticRAG]] | One → LLM-as-agent | Yes (more elaborate planning) |

The wiki's prior coverage of **[[MultiHopQA|multi-hop question answering]]** (as a question type) is the **dataset/benchmark concept**; multi-hop RAG is the **system architecture** that solves it. The two concepts are complementary.

## Connections

- [[rag]] — the parent technique family.
- [[MultiQueryRAG]] — the parallel-decomposition complement.
- [[QueryRewriting]] — the upstream primitive.
- [[QueryRouting]] / [[AgenticRAG]] — sibling advanced-RAG techniques.
- [[MultiHopQA]] — the multi-hop QA task type (dataset-level concept).
- [[react|ReAct]] — agent framework that naturally implements multi-hop retrieval as Thought → Action(retrieve) → Observation cycles.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
- [[ResearchHop]] — the [[DSPy]] [[DSPyModules|`dspy.Module`]] implementation of multi-hop RAG used in [[dspy-rl-multihop-tutorial]] (fixed 2-hop generate-query / append-notes / retrieve loop).
- [[Hop]] — the **structural parent of [[ResearchHop]]**: 4-hop / 10-docs-per-hop generate-query / append-notes program from [[dspy-multihop-search-tutorial]]. The MIPROv2 prompt-optimization sibling of the ArborGRPO ResearchHop receipt.
- [[dspy-multihop-search-tutorial]] — the [[MIPROv2]] prompt-optimization receipt over a multi-hop RAG program on [[HoVer]] (31.3 → 59.1 top5_recall via $5 of GPT-4o).
- [[dspy-rl-multihop-tutorial]] — the [[ArborGRPO|GRPO]] training receipt over a multi-hop RAG program on [[HoVer]].
