---
title: "HoVer"
type: concept
tags: [benchmark, multi-hop, retrieval-augmented, claim-verification]
sources: [2507.19457-gepa, 2406.11695-mipro, dspy-tutorial-rag-as-agent, dspy-rl-multihop-tutorial, dspy-multihop-search-tutorial]
last_updated: 2026-05-24
---

# HoVer

**Ho**p-wise **V**erification (Jiang et al., 2020). Multi-hop claim-verification benchmark — given a claim and a corpus, retrieve and reason over evidence across multiple Wikipedia documents to decide SUPPORTED / NOT_SUPPORTED / NOT_ENOUGH_INFO. Distinct from [[hotpotqa|HotpotQA]] in that the output is a *verification label* with cited evidence, not a free-text answer.

Used by [[2507.19457-gepa|GEPA]] as one of six core benchmarks; one of the four where the full performance-vs-rollouts curve is plotted (Figures 1a, 1b, 14c, 15c).

## GEPA results on HoVer

| Optimizer | Qwen3 8B | GPT-4.1 Mini |
|---|---|---|
| Baseline | 35.33 | 46.33 |
| [[grpo|GRPO]] | 38.67 | — |
| [[MIPROv2]] | 47.33 | 48.33 |
| **GEPA** | **52.33** | 51.67 |
| **GEPA+Merge** | 51.67 | **56.67** |

## In [[2406.11695-mipro|Opsahl-Ong et al. (2024)]] — MIPRO

HoVer is the **deepest-pipeline** task in the [[DSPyOptimizerBenchmark]] — **4 modules, 4 LM calls**, Recall@21 over three retrieval hops. The paper alternates *three times* between query generation and retrieval, using HoVer's gold labels to report Retrieval@21 over the top-10 documents from each of three hops. Demo bootstrapping uses GPT-4o as teacher (not Llama-3-8B) because of the task's difficulty.

| Optimizer | Train | Dev | Test |
|---|---|---|---|
| N/A baseline | 30.2 | 30.8 | 25.3 |
| Module-Level OPRO | 37.1 | 38.6 | 32.5 |
| 0-Shot MIPRO | 37.7 | 38.4 | 33.1 |
| 0-Shot MIPRO++ | 37.1 | 37.3 | 32.6 |
| Bootstrap RS | 42.0 | 42.0 | 37.2 |
| Bayesian Bootstrap | 44.6 | 44.7 | 37.6 |
| **MIPRO** | 44.7 | **46.7** | **39.0** |

MIPRO's joint optimization wins on dev/test by ~2 absolute points over Bayesian Bootstrap and ~6 points over Module-Level OPRO. **0-Shot MIPRO** is competitive with Module-Level OPRO (37.7 vs 37.1 train) — instructions-only joint search ≈ history-based per-module search on this task.

## In [[dspy-tutorial-rag-as-agent|Building RAG as Agent tutorial]] (DSPy, 2026)

The [[DSPy]] **Building RAG as Agent** tutorial uses the **three-hop subset of HoVer** as the optimization target for a [[react|`dspy.ReAct`]] agent with two Wikipedia tools (search + lookup). Key differences from the [[2406.11695-mipro|MIPRO paper's]] HoVer treatment:

| Axis | MIPRO paper | This tutorial |
|---|---|---|
| Pipeline shape | 4 modules, 4 LM calls (3 hops of generate→retrieve) | Single [[react|`dspy.ReAct`]] loop with `max_iters=20` |
| Student LM | [[Llama3_8BInstruct|Llama-3-8B]] | [[Llama|Llama-3.2-3B-Instruct]] |
| Teacher / proposer | GPT-4o (demos only) | GPT-4o (demos + instructions) |
| Metric | Recall@21 | **top5_recall** (gold titles in top-5) |
| Baseline → optimized | 30.2 → 44.7 (1.5×) | **8% → 41.67% (5×)** |
| Optimizer config | (paper-specific) | `auto="medium"`, `max_bootstrapped_demos=3`, `max_labeled_demos=0`, `max_errors=999` |

The 3B student has **more headroom** than the 8B paper student → larger relative lift but lower absolute ceiling. The dataset is filtered to **`num_hops == 3`** with `hpqa_id` deduplication; 100 train / 100 dev / remainder test.

## In [[dspy-rl-multihop-tutorial|`rl_multihop` tutorial]] (DSPy, 2026) — first weight-space RL receipt

The [[DSPy]] **Online RL for Multi-Hop Research** tutorial uses the **three-hop subset of HoVer** as the optimization target for **online [[grpo|GRPO]] training** (`loss_type="dapo"`, LoRA r=8) of a small `Qwen/Qwen2.5-1.5B-Instruct` student via the [[ArborGRPO]] compiler. The student program is [[ResearchHop]] — a 2-hop generate-query / append-notes loop with a [[bm25s|bm25s]] BM25 retriever over the 2017 Wikipedia abstracts. Differs from the prior two HoVer DSPy receipts on multiple axes:

| Axis | [[2406.11695-mipro|MIPRO paper]] | [[dspy-tutorial-rag-as-agent|RAG-as-agent tutorial]] | This tutorial |
|---|---|---|---|
| Pipeline shape | 4 modules, 4 LM calls | Single `dspy.ReAct` loop, `max_iters=20` | **Fixed 2-hop `ResearchHop`** |
| Optimizer | [[MIPROv2]] family | [[MIPROv2]] `auto="medium"` + GPT-4o teacher | **[[ArborGRPO]] (DAPO, LoRA r=8)** |
| Regime | prompt-space | prompt-space | **weight-space (on-policy RL)** |
| Student | Llama-3-8B | Llama-3.2-3B | **Qwen2.5-1.5B-Instruct** |
| Retriever | [[ColBERTv2]] | [[ColBERTv2]] | **[[bm25s|bm25s]] + [[PyStemmer]]** |
| Metric | Recall@21 | top5_recall | per-page title recall (gold ∩ retrieved) / |gold| |
| Split | (paper-specific) | 100 train / 100 dev / remainder | 600 / 300 / 300 |
| Lift | 30.2 → 44.7 (1.5×) | 8 → 41.67 (5×) | 61.8 → 66.2 (1.07×) |
| Compute | — | (cheap MIPROv2 run) | ~18 h on 4 GPUs (3 training + 1 inference) |

HoVer is now the **first wiki benchmark with both a prompt-space and a weight-space DSPy receipt** — the operational form of the [[2507.19457-gepa|GEPA paper's]] central contrast. Tutorial-internal data point: **the prompt-space optimizer's lift dominates the weight-space optimizer's on the same benchmark family** (the rl_multihop tutorial concedes this explicitly).

## In [[dspy-multihop-search-tutorial|Multi-Hop Search tutorial]] (DSPy, 2026) — third HoVer receipt, MIPROv2 + 8B student

The [[DSPy]] **Multi-Hop Search** tutorial at `https://dspy.ai/tutorials/multihop_search/` is the **third HoVer DSPy receipt** — and **the canonical MIPROv2 receipt with a [[Llama|Llama-3.1-8B-Instruct]] student and [[GPT4o|GPT-4o]] as both proposer and teacher**. Uses [[Hop|`Hop(num_docs=10, num_hops=4)`]] — the 4-hop / 10-docs-per-hop structural parent of [[ResearchHop]] — as the student program, with the same `top5_recall` metric as [[dspy-tutorial-rag-as-agent|the RAG-as-agent tutorial]] but a **stricter `recall >= 1.0` bootstrap gate**.

| Axis | [[2406.11695-mipro|MIPRO paper]] | [[dspy-tutorial-rag-as-agent|RAG-as-agent tutorial]] | **this tutorial** | [[dspy-rl-multihop-tutorial|rl_multihop tutorial]] |
|---|---|---|---|---|
| Optimizer | [[MIPROv2]] family | [[MIPROv2]] `auto="medium"` + teacher | **[[MIPROv2]] `auto="medium"` + proposer + teacher** | [[ArborGRPO]] (DAPO, LoRA r=8) |
| Regime | prompt-space | prompt-space | **prompt-space** | weight-space (RL) |
| Program shape | 4 modules, 4 LM calls | Single `dspy.ReAct` loop, `max_iters=20` | **[[Hop|`Hop(num_docs=10, num_hops=4)`]] = 8 LM calls** | Fixed 2-hop [[ResearchHop]] |
| Student | Llama-3-8B | Llama-3.2-3B | **[[Llama|Llama-3.1-8B-Instruct]]** | Qwen2.5-1.5B-Instruct |
| Retriever | [[ColBERTv2]] | [[ColBERTv2]] | **[[bm25s]] + [[PyStemmer]]** (k1=0.9, b=0.4) | [[bm25s]] + [[PyStemmer]] |
| HF source | (paper-specific) | `hover-nlp/hover` | **`vincentkoc/hover-parquet`** | `hover-nlp/hover` |
| Split | (paper-specific) | 100/100/rem | **200/300/rem** (`hover[650:]` test) | 600/300/300 |
| Metric | Recall@21 | top5_recall (gate `>= 0.5`) | **top5_recall (gate `>= 1.0`)** | per-page title recall |
| Demo budget | (paper-specific) | bootstrap=3, labeled=0 | **bootstrap=4, labeled=4** | exclude_demos=True |
| Lift | 30.2 → 44.7 (1.5×) | 8 → 41.67 (5.21×) | **31.3 → 59.1 (1.89×)** | 61.8 → 66.2 (1.07×) |
| Cost | — | (cheap MIPROv2 run) | **~$5 of GPT-4o** | ~18 h on 4 GPUs |

HoVer is now the wiki's **first benchmark with THREE distinct DSPy tutorial receipts** and the first with **two MIPROv2 receipts that differ in program shape** (the ReAct-loop variant and the fixed-depth `Hop` variant). The two MIPROv2 lifts (5.21× and 1.89×) are not directly comparable — different program shapes, different students, different demo budgets — but together they demonstrate that **MIPROv2's lift is highly program-shape-dependent on the same benchmark**.

## Connections
- [[2507.19457-gepa]] — uses HoVer as a core benchmark.
- [[dspy-tutorial-rag-as-agent]] — **first wiki receipt that treats HoVer (three-hop subset) as the optimization target for a single `dspy.ReAct` loop** (not a multi-hop generate-retrieve pipeline). 8% → 41.67% top5_recall (5×) with Llama-3.2-3B student + GPT-4o teacher.
- [[dspy-multihop-search-tutorial]] — **third HoVer receipt and second MIPROv2 receipt**, on a fixed-depth [[Hop|`Hop(num_docs=10, num_hops=4)`]] program with [[Llama|Llama-3.1-8B-Instruct]] student + [[GPT4o|GPT-4o]] proposer+teacher. **31.3% → 59.1% top5_recall (1.89×) on ~$5 of GPT-4o.** Stricter `recall >= 1.0` bootstrap gate; balanced 4/4 demo budget.
- [[Hop]] — **new concept page.** The 4-hop / 10-docs-per-hop structural parent of [[ResearchHop]] introduced by [[dspy-multihop-search-tutorial]].
- [[dspy-rl-multihop-tutorial]] — **first wiki receipt of HoVer as a weight-space RL target** ([[ArborGRPO]] / DAPO / LoRA) on a fixed 2-hop [[ResearchHop]] program with Qwen2.5-1.5B-Instruct. 61.8 → 66.2 recall.
- [[2406.11695-mipro]] — introduces HoVer as one of seven [[DSPyOptimizerBenchmark]] tasks (the deepest pipeline at 4 modules).
- [[DSPyOptimizerBenchmark]] — the MIPRO benchmark this is part of.
- [[ResearchHop]] — the 2-hop program shape introduced for HoVer RL training.
- [[hotpotqa|HotpotQA]] — sibling multi-hop QA benchmark.
- [[rag|RAG]] — retrieval-augmented setting HoVer evaluates.
- [[2604.27707-agentic-memory-is-a-memo]] — multi-hop is the canonical compositional-generalization probe.
