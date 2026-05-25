---
title: "WildSeek (dataset)"
type: concept
tags: [dataset, evaluation, information-seeking]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# WildSeek

**WildSeek** — a 100-example dataset of **in-the-wild complex information-seeking tasks** introduced in [[2408.15232-co-storm|Co-STORM (Jiang et al., 2024)]]. Each data point is a pair of `(topic, goal)` representing a real user's information-seeking intent.

## Construction

- Collected from the publicly deployed [[STORM]] web application (storm.genie.stanford.edu), where users submit topics + goals to request a Wikipedia-style report.
- **Filtered** by rule-based heuristics + binary classification with [[gpt-4o|gpt-4o-2024-05-13]] to retain only data points that are *well motivated* (clear, non-trivial information need).
- **Downsampled** to **100 data points across 24 domains** with manual review + refinement.
- Domain labels assigned manually.

## Sample data point

| Field | Value |
|---|---|
| **Domain** | Economics |
| **Topic** | Development of a Shared Trading Currency to Facilitate International Trade |
| **Goal** | Investigate how a new shared currency could eliminate transaction costs and boost GDP among member countries. |

## Why it matters

- **First dataset in this wiki to capture user *goals*, not just queries** — most QA / information-seeking datasets ([[hotpotqa|HotPotQA]], [[TriviaQA]], etc.) collect questions, not goals. The goal field encodes *why* the user wants the information, which is the unit at which complex information-seeking actually operates.
- Sourced from a **publicly deployed system's user logs** — real user intent, not synthetic or crowdworker-generated.
- 24 domains gives broad coverage of complex information-seeking applications (academic research, market analysis, decision-making, etc.).

## Use in Co-STORM evaluation

Each (topic, goal) is given to a simulated user (LM = [[gpt-4o|gpt-4o-2024-05-13]] prompted with topic + goal + discourse history) who interacts with the assistance system. Sessions are terminated after **30 search queries** to ensure fair comparison across [[CoSTORM|Co-STORM]], [[RAGChatbot|RAG Chatbot]], and [[STORM]]+QA. Each system's final long-form report is then scored on Relevance / Breadth / Depth / Novelty / [[InformationDiversity]].

## See also
- [[CoSTORM]] · [[InformationDiversity]] · [[Prometheus2]] · [[InformationSeeking]]
