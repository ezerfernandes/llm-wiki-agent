---
title: "Workstream Coordinator"
type: concept
tags: [agent-role, agentic-ai, harness]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# Workstream Coordinator

Per-goal coordinator agent in the [[AICoMathematician|AI co-mathematician]] hierarchy ([[2605.06651v2-ai-co-mathematician]]). Receives a research question + selected Goal + any instructions from the [[ProjectCoordinatorAgent|Project Coordinator]]; performs a **linear sequence of actions** which may include delegating to specialized sub-agents (literature reviewer, coder, prover, reviewer); produces a fully-reviewed LaTeX [[WorkingPaper|report]] as the final artifact.

Each goal can host multiple workstreams. Workstreams may fail to complete; failures are preserved as **first-class durable artifacts** in the shared file system (no silent restart). Each workstream supplies incremental reports the user can monitor without blocking the workstream's execution.

The coordinator must pass an iterative reviewer-agent process before the workstream can be marked finalized. If it cannot, it escalates to the Project Coordinator with a clear "unfinished" status.

## Connections
- [[AICoMathematician]]
- [[ProjectCoordinatorAgent]]
- [[WorkingPaper]]
- [[ReviewerPleasingBias]] — failure mode of the iterative review.
- [[DeathSpiral]] — non-termination failure mode.
- [[2605.06651v2-ai-co-mathematician]]
