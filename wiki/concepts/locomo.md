---
title: "LoCoMo"
type: concept
tags: [concept, benchmark, long-context, memory, conversational]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# LoCoMo

**Long Conversational Memory** benchmark (Maharana et al., 2024) for evaluating very-long-term conversational memory in LLM agents. Question categories: **Multi-hop**, **Temporal**, **Open-domain**, **Single-hop**. Adversarial category excluded by [[2605.12357-delta-mem]] following Chhikara et al. 2025.

In [[2605.12357-delta-mem]], MSW δ-mem reaches **49.12 avg** on Qwen3-4B-Instruct (vs frozen baseline 40.79; vs Context2LoRA 48.11). MSW dominates across all three backbones tested, suggesting parallel sub-states are particularly useful for separating the heterogeneous memory needs of long conversations (facts, preferences, task progress, local events).
