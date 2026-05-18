---
title: "Negative Transfer"
type: concept
tags: [stub, multi-task-learning]
sources: []
last_updated: 2026-05-15
---

# Negative Transfer

*Stub — referenced by other wiki pages but not yet ingested as a primary source.*

In multi-task learning, **negative transfer** occurs when joint training on two tasks degrades performance relative to training each alone. The classical mechanism is gradient conflict: when the task-A gradient and task-B gradient form an angle $>90°$ in parameter space, a step that decreases the loss on A increases it on B. Cited by [[2605.12966-agentic-ai-to-agi]] (Remark B.2) as the per-step manifestation of the [[AverageTrap]] — and the reason mitigations like Gradient Surgery (Yu et al. 2020), Conflict-Averse Gradient Descent (Liu et al. 2021), and sparse training (Zhang et al. 2024) cannot eliminate the $\epsilon$ penalty, only reduce it.

## Connections
- [[2605.12966-agentic-ai-to-agi]]
- [[AverageTrap]]
