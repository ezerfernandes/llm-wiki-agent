---
title: "Moving Sofa Problem"
type: concept
tags: [math, computational-geometry, open-problem]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# Moving Sofa Problem

A classical problem in computational geometry first introduced by Moser (1966): determine upper bounds on the area of a "sofa" that can be moved around both left- and right-handed right-angle corners. [[2605.06651v2-ai-co-mathematician]] §3 uses this problem as the **walkthrough example** for the [[AICoMathematician|AI co-mathematician]]. Baek's recent work proved Gerver's lower bound sharp for the *classic* (one-corner) sofa problem; the upper bounds for the **ambidextrous** (both-handed) and right-handed variants remain open.

In the walkthrough, the [[ProjectCoordinatorAgent|Project Coordinator]] formalizes three goals (Literature Review, Computational Framework, Execute the Search), spawns parallel workstreams, hits a search-space-explosion bottleneck, surfaces an uncertainty alert, and is *unblocked by the user supplying a topological pruning heuristic* via chat. Demonstrates all seven design principles in one trajectory.

[[AlphaEvolve]] had previously been applied to the same problem (Baek's prior work) — the paper takes this as the inspirational base case for the harness's design.

## Connections
- [[AICoMathematician]]
- [[AlphaEvolve]]
- [[2605.06651v2-ai-co-mathematician]]
