---
title: "Death Spiral (Intractable Disagreements)"
type: concept
tags: [failure-mode, agentic-ai, multi-agent, non-termination]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# Death Spiral (Intractable Disagreements / Non-Termination)

Failure mode of iterative reviewer-agent loops documented in [[2605.06651v2-ai-co-mathematician]] §7. When the iterative review process fails to reach consensus, it can **fail to terminate entirely** — becoming locked in an endless cycle of revisions and rejections. Over successive autonomous iterations, this loop often degrades into **increasingly hallucinated reasoning**.

The dual of [[ReviewerPleasingBias]]: where Reviewer-Pleasing Bias is *bad consensus*, the Death Spiral is *no consensus*. The paper attributes the core driver to a structural feature of current language models — they frequently disagree with each other. Mitigations implemented in AI co-mathematician are partial; early users have learned to **recognize when a workstream has entered this state and down-weight their trust in its output**.

## Connections
- [[2605.06651v2-ai-co-mathematician]]
- [[ReviewerPleasingBias]] — dual failure mode.
- [[AICoMathematician]] / [[WorkstreamCoordinator]]
