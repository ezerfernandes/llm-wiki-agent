---
title: "DSPy Optimizer Benchmark"
type: concept
tags: [benchmark, dspy, prompt-optimization, evaluation]
sources: [2406.11695-mipro]
last_updated: 2026-05-24
---

# DSPy Optimizer Benchmark

The seven-task benchmark for [[LMProgram|LM-program]] prompt optimizers released by the [[2406.11695-mipro|MIPRO paper (Opsahl-Ong et al. 2024)]]. Each task is a `(dataset, metric, dspy.Module program)` triple — every program is a real multi-stage [[DSPy]] program with code in the paper's Appendix B.1.

## Tasks (Table 1)

| Benchmark | Task Type | Program | Modules | LM Calls | Metric | Set sizes |
|---|---|---|---|---|---|---|
| [[hotpotqa\|HotPotQA]] | Multi-Hop QA | Multi-Hop Retrieval | 2 | 3 | Exact Match | 500/500/2000 |
| [[HotPotQAConditional]] | Multi-Hop QA + conditional rules | Multi-Hop Retrieval | 2 | 3 | Custom | 500/500/2000 |
| [[Iris]] | Classification | [[chainofthought\|Chain of Thought]] | 1 | 1 | Accuracy | 500/500/full |
| [[IrisTypo]] | Classification (misspelled prompt) | [[chainofthought\|Chain of Thought]] | 1 | 1 | Accuracy | 500/500/full |
| [[HeartDisease]] | Classification | Answer Ensemble | 2 | 4 | Accuracy | 500/500/full |
| [[ScoNe]] | NLI (nested negation) | [[chainofthought\|Chain of Thought]] | 1 | 1 | Exact Match | 500/500/full |
| [[HoVer]] | Multi-Hop Claim Verify | Multi-Hop Retrieval | 4 | 4 | Recall@21 | 500/500/2000 |

## Coverage design

The benchmark is deliberately picked to exercise **four orthogonal axes** of variation:

1. **Number of modules** — 1, 2, or 4 modules per program.
2. **Conditional rule complexity** — Iris-vanilla (easily inferable from features) vs Iris-Typo (requires inferring through a typo) vs HotPotQA-Conditional (rules about answer format conditional on entity type).
3. **Task type** — QA / classification / NLI / claim-verification.
4. **Program structure** — multi-hop retrieval / single-CoT / answer-ensemble.

The paper uses this matrix to surface the **Lesson 3** finding: **instruction optimization wins on tasks with conditional rules not expressible via a small number of few-shot examples** (HotPotQA Conditional, Iris-Typo, Heart Disease) while demos-only wins everywhere else.

## Methodology

- **5 runs per (method × task)** with random seed variation.
- **[[WilcoxonSignedRankTest|Wilcoxon signed-rank test]]** between average per-example scores across runs to test significance between MIPRO and the second-best method on each task.
- 20–50 optimizer trials per run, with full evaluation on the trainset (or a dedicated validation split).
- **Proposer LM**: GPT-3.5 at temperature 0.7.
- **Task LM**: [[Llama3_8BInstruct|Llama-3-8B]] (default), with Llama-3-8B teacher for demo bootstrapping; teacher upgraded to GPT-4o for harder tasks ([[ScoNe]] / [[HoVer]]).

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-multihop-search-tutorial]] — `dspy.MIPROv2` over the [[HoVer]] three-hop subset (the benchmark's hardest multi-hop task) with Llama-3.1-8B; the canonical end-to-end receipt of the prompt-space joint optimization the benchmark was designed to evaluate.
- [[dspy-rl-multihop-tutorial]] — experimental `dspy.ArborGRPO` online [[grpo|GRPO]] over the same HoVer 2-hop program; the *"what comes after MIPROv2 saturates"* receipt — relevant to the benchmark as the post-MIPROv2 weight-tuning frontier on the same task.

## Connections

- [[2406.11695-mipro]] — the canonical source.
- [[MIPROv2|MIPRO]] — the optimizer the benchmark was designed to evaluate.
- [[DSPy]] — the programming model the benchmark programs live in.
- Per-task pages: [[hotpotqa]], [[HotPotQAConditional]], [[Iris]], [[IrisTypo]], [[HeartDisease]], [[ScoNe]], [[HoVer]].
- [[2507.19457-gepa|GEPA (2026)]] — the successor work that explicitly outperforms MIPRO on six of these benchmarks.
