---
title: "Preference Model"
type: concept
tags: [evaluation, llm-as-judge, specialized-judge, alignment]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Preference Model

A **preference model** is a specialized [[LLMAsAJudge|AI judge]] that *"takes in (prompt, response 1, response 2) as input and outputs which of the two responses is better (preferred by users) for the given prompt"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]).

## Two named exemplars (Ch 3)

- **[[PandaLM]]** (Wang et al. 2023) — outputs the winner *and* a written rationale for the choice.
- **[[JudgeLM]]** (Zhu et al. 2023) — sibling open preference model.

## Why preference models matter

Ch 3: *"This is perhaps one of the more exciting directions for specialized judges. Being able to predict human preference opens up many possibilities. As discussed in Chapter 2, preference data is essential for aligning AI models to human preference, and it's challenging and expensive to obtain. Having a good human preference predictor can generally make evaluation easier and models safer to use."*

The bottleneck for [[rlhf|RLHF]] / [[DPO|DPO]] is **comparison-data labor cost** ([[LMSYS]]: 3-5 minutes per comparison with fact-checking; [[ThomasScialom]]: ≈$3.50 per comparison). A reliable preference model could **synthesize comparison data at near-zero marginal cost**, accelerating preference finetuning.

## Position in the specialized-judge taxonomy

Ch 3 enumerates **three kinds of specialized judges**:
1. [[RewardModel|Reward models]] — score (prompt, response) → scalar.
2. [[ReferenceBasedJudge|Reference-based judges]] — score (generated, references).
3. **Preference models** ← *this page* — score (prompt, response 1, response 2) → winner.

## How it differs from reward models

| Property | [[RewardModel\|Reward model]] | Preference model |
|---|---|---|
| Input | (prompt, response) | (prompt, response_1, response_2) |
| Output | Scalar score | Winner (or tie) |
| Used in | RLHF reward step | Comparative evaluation, synthetic comparison data |
| Calibration | Absolute score interpretation matters | Only relative order matters |

A reward model's score is inherently absolute (or at least scale-fixed); a preference model's output is inherently relative. The two are mathematically related (you can derive a preference from two reward scores, and vice versa via Bradley-Terry assumption), but they have different deployment ergonomics.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[PandaLM]] / [[JudgeLM]] — two named exemplars.
- [[RewardModel]] / [[ReferenceBasedJudge]] — sibling specialized-judge types.
- [[LLMAsAJudge]] — parent paradigm.
- [[ComparisonData]] — the data form preference models output (synthetically).
- [[ComparativeEvaluation]] — the methodology preference models can power.
- [[rlhf|RLHF]] / [[DPO|DPO]] / [[PreferenceFinetuning]] — the alignment uses.
- [[BradleyTerry]] — formal bridge between scalar rewards and pairwise preferences.
