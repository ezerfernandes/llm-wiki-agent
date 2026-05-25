---
title: "pass@k"
type: concept
tags: [evaluation, metric, code-generation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# pass@k

**`pass@k`** is the canonical metric for code-generation benchmarks. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "When evaluating a model, for each problem a number of code samples, denoted as k, are generated. A model solves a problem if any of the k code samples it generated pass all of that problem's test cases. The final score, called pass@k, is the fraction of the solved problems out of all problems."

## Worked example

10 problems, model solves 5 with `k = 3` → `pass@3 = 50%`.

## Monotonicity in k

*"In expectation, pass@1 score should be lower than pass@3, which, in turn, should be lower than pass@10."* The more samples, the more chances a model has to find a solution.

This monotonicity makes `pass@k` a useful sweep — a model's `pass@1` (single-attempt) and `pass@100` (100-attempt) trace its [[TestTimeCompute|test-time compute]] curve on functional-correctness tasks.

## Position in the wiki

Used by [[HumanEval]], [[MBPP]], and the text-to-SQL benchmarks ([[Spider]] / [[BIRDSQL]] / [[WikiSQL]]). The closest sibling for [[SemanticSimilarity|similarity-based]] metrics has no such monotonicity — BLEU/ROUGE/BERTScore don't improve with more samples by construction.

## Caveat

A high `pass@k` for large k doesn't imply the model can *select* the correct solution — it only says the correct solution is *somewhere* in its top-k. Pairing `pass@k` with a [[Verifier|verifier]] or [[RewardModel|reward model]] to select the best candidate is the [[bestofn|best-of-N]] pattern.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[FunctionalCorrectness]] / [[ExecutionAccuracy]] — what pass@k measures.
- [[HumanEval]] / [[MBPP]] / [[Spider]] / [[BIRDSQL]] / [[WikiSQL]] — benchmarks reporting pass@k.
- [[bestofn]] / [[Verifier]] / [[RewardModel]] — the selection layer that consumes pass@k's top-k candidates.
- [[TestTimeCompute]] — broader pattern; pass@k traces the inference-budget curve.
