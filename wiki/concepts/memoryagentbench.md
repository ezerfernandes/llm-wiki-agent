---
title: "MemoryAgentBench"
type: concept
tags: [concept, benchmark, memory, llm-agents]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# MemoryAgentBench

Memory-heavy benchmark for LLM agents (Hu et al., 2025) evaluating **retention, retrieval, and utilization** of memory information across extended interaction histories. Sub-categories reported in [[2605.12357-delta-mem]]: **AR** (Accurate Retrieval — SH-Doc QA / MH-Doc QA / LongMemEval / EventQA), **TTL** (Test-Time Learning — BANKING77, CLINC150, NLU, TREC Coarse/Fine, Movie Recommendation), **LRU** (Long Range Understanding — ∞Bench-Sum, Detective QA), **SF** (Selective Forgetting — FactConsolidation-SH/MH).

In [[2605.12357-delta-mem]], δ-mem (MSW) lifts the Qwen3-4B-Instruct average from **29.54 → 38.85** (1.31× — the paper's largest memory-heavy gain); TTL subscore nearly doubles (26.14 → 50.50 under TSW). Score is a sample-weighted average across categories with per-dataset metrics (Accuracy / Recall@5 / F1).
