---
title: "IFEval"
type: concept
tags: [concept, benchmark, instruction-following]
sources: [2605.12357-delta-mem, ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# IFEval

**Instruction-Following Evaluation** for LLMs (Zhou et al. 2023, [[google|Google]]). Verifies whether model outputs satisfy verifiable instruction constraints (length, format, keyword inclusion/exclusion, etc.). Metric: **prompt-level strict accuracy** — fraction of instructions followed correctly out of all instructions.

## What it tests (Ch 4 Table 4-2)

**25 automatically-verifiable instruction types**, grouped:

| Group | Examples |
|---|---|
| **Keywords** | Include / exclude / frequency / letter frequency |
| **Language** | Response language (must be in {language}) |
| **Length constraints** | Number of paragraphs / words / sentences; first-word-of-paragraph |
| **Detectable content** | Postscript markers, placeholder counts |
| **Detectable format** | Bullet counts, titles, highlighted sections, multi-section, JSON format |
| **Choose from** | Constrain answer to one of a set |

The point: *"If you ask a model to write a sentence that uses the word 'ephemeral', you can write a program to check if the output contains this word; hence, this instruction is automatically verifiable."*

## Position

Added to HuggingFace's [[OpenLLMLeaderboard|Open LLM Leaderboard]] in the **June 2024 refresh** as one of six benchmarks. Sibling to [[INFOBench]] (Qin et al. 2024) which broadens beyond format constraints to content / linguistic / style criteria.

## In [[2605.12357-delta-mem]]

Used as a **general-capability preservation check** alongside [[gpqa|GPQA-Diamond]]: Qwen3-4B-Instruct baseline 81.89 → δ-mem (TSW) 82.99, confirming δ-mem largely preserves general instruction-following while adding memory capability. Some textual-memory baselines (BM25 RAG, LLMLingua-2, MemoryBank) collapse on IFEval because their context perturbations break instruction adherence — a hidden cost of TMM approaches that δ-mem avoids by never touching the input context.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary Ch 4 source.
- [[2605.12357-delta-mem]] — δ-mem context.
- [[InstructionFollowingCapability]] — parent capability.
- [[INFOBench]] — sibling broader benchmark.
- [[OpenLLMLeaderboard]] — leaderboard adoption.
- [[google|Google]] — author.
