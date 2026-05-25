---
title: "Information Diversity (metric)"
type: concept
tags: [metric, evaluation, embeddings]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Information Diversity

**Information Diversity** — the average pairwise *dissimilarity* over retrieved information embeddings. Introduced in [[2408.15232-co-storm|Co-STORM §5.2]] as a complement to LM-rubric-graded report-quality metrics.

## Formula

For a retrieved-information set $\mathcal{I}$ with embeddings $\mathbf{i}, \mathbf{j}$:

$$\text{InfoDiv}(\mathcal{I}) = 1 - \frac{\sum_{i, j \in \mathcal{I}, i \neq j} \cos(\mathbf{i}, \mathbf{j})}{|\mathcal{I}|(|\mathcal{I}| - 1)}$$

— 1 minus the average pairwise cosine similarity. Higher = more diverse retrieval. Co-STORM uses `text-embedding-3-small` embeddings.

## What it captures (and doesn't)

**Captures**: did the system *retrieve* across different parts of the information space, or did it keep pulling near-duplicate sources?

**Does not capture**: did the final *report* cite that diverse set, or did it ignore most of it? InfoDiv is a **process-quality proxy**, not an outcome proxy. A system can retrieve diverse sources but write a shallow report.

This is consistent with the Co-STORM results: Co-STORM's InfoDiv edge over baselines (0.602 vs ~0.59) is much smaller than its Novelty/Depth edges scored by [[Prometheus2]] — InfoDiv is one signal among several, not a one-size metric.

## Co-STORM evaluation

| System | Information Diversity |
|---|---|
| [[RAGChatbot]] | 0.595 |
| [[STORM]] + QA | 0.592 |
| **[[CoSTORM]]** | **0.602** |
| Co-STORM w/o Multi-Expert | 0.589 |
| Co-STORM w/o Moderator | 0.577 |

The moderator ablation has the largest InfoDiv drop — consistent with the moderator's design role of pulling in **on-topic but unexplored** sources.

## See also
- [[CoSTORM]] · [[Prometheus2]] · [[WildSeek]]
