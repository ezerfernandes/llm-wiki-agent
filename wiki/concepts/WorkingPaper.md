---
title: "Working Paper (artifact)"
type: concept
tags: [artifact, latex, agentic-ai, mathematics]
sources: [2605.06651v2-ai-co-mathematician]
last_updated: 2026-05-15
---

# Working Paper

The primary stateful output of a [[WorkstreamCoordinator]] in the [[AICoMathematician|AI co-mathematician]] ([[2605.06651v2-ai-co-mathematician]]). Not a transient chat log: a compiled, reviewed **LaTeX manuscript** with four required properties:

1. **Exposition** — must explain the *research process* that led to the outcome, not only the final result.
2. **Margin annotations** — explicitly link claims back to the workspace, e.g. `[Pruning heuristic derived from user suggestion; baseline bound of 2.2195 sourced from paper at arxiv.org/abs/…]`.
3. **Internal linking** — provenance links to internal documents created by the agents, giving the user direct entry points to audit the shared filesystem.
4. **Review process** — must pass an iterative reviewer-agent process (persistent reviewers across rounds) before being marked finalized.

The "working paper" framing is the paper's response to LLMs producing **flawless LaTeX with weak rigor**: making the document explicitly a *working document with marginalia* (rather than a polished manuscript) reduces the visual mismatch between typeset quality and verification status.

## Connections
- [[AICoMathematician]]
- [[WorkstreamCoordinator]]
- [[2605.06651v2-ai-co-mathematician]]
