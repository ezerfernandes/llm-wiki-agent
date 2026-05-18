---
title: "HotpotQA"
type: concept
tags: [concept, benchmark, qa, multi-hop]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# HotpotQA

Multi-hop QA dataset (Yang et al., EMNLP 2018) requiring reasoning over multiple Wikipedia paragraphs. Two question types: **Bridge** (true multi-hop, where one fact bridges to another) and **Comparison** (compare attributes of two entities). Metrics: Exact Match (EM) and F1.

Used in [[2605.12357-delta-mem]] as a memory-heavy reasoning benchmark and — more revealingly — in the **no-context ablation**: with all explicit context removed, δ-mem's online state alone lifts overall EM from **0.08% → 6.48%** and F1 from **8.27% → 15.20%**; Bridge subset EM from 0.08% → 3.97%. The compact $8 \times 8$ state retains usable multi-hop signal.
