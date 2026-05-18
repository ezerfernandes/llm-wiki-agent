---
title: "IFEval"
type: concept
tags: [concept, benchmark, instruction-following]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# IFEval

**Instruction-Following Evaluation** for LLMs (Zhou et al., 2023). Verifies whether model outputs satisfy verifiable instruction constraints (length, format, keyword inclusion/exclusion, etc.). Metric: **prompt-level strict accuracy**.

In [[2605.12357-delta-mem]], used as a **general-capability preservation check** alongside [[gpqa|GPQA-Diamond]]: Qwen3-4B-Instruct baseline 81.89 → δ-mem (TSW) 82.99, confirming δ-mem largely preserves general instruction-following while adding memory capability. Some textual-memory baselines (BM25 RAG, LLMLingua-2, MemoryBank) collapse on IFEval because their context perturbations break instruction adherence — a hidden cost of TMM approaches that δ-mem avoids by never touching the input context.
