---
title: "Private Benchmark"
type: concept
tags: [benchmark, evaluation, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Private Benchmark

An evaluation dataset **you build and hold internally** for your application. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], private benchmarks are the third step of the [[ModelSelectionWorkflow|model-selection workflow]]:

> "After using public benchmarks to narrow them to a set of promising models, you'll need to run your own evaluation pipeline to find the best one for your application."

## Why private over public

- **Application-specific.** Public benchmarks measure general capabilities; yours measures *your* use case.
- **Contamination-resistant.** Your data wasn't in any model's training set (probably).
- **Aligned with business value.** Tied to your [[BusinessMetric|business metric]] thresholds.
- **Curated for your distribution.** Real user prompts, typos, edge cases, [[OutOfScopeEvaluation|out-of-scope]] inputs.

## What it should contain

From the [[EvaluationPipeline|evaluation-pipeline]] discussion in Ch 4:

- **Representative distribution set** — for overall performance estimation.
- **[[DataSlicing|Sliced sets]]** — tiers (paying vs free), traffic sources, usage patterns.
- **Frequent-mistake set** — where the system tends to fail.
- **User-mistake set** — typos, malformed queries.
- **[[OutOfScopeEvaluation|Out-of-scope set]]** — inputs your app shouldn't engage with.
- **Per-component sets** — for [[PerComponentEvaluation|component-level evaluation]].

## Sizing

Use [[BootstrapEvaluation|bootstrap resampling]] to confirm reliability. *"If the evaluation results vary wildly for different bootstraps, this means that you'll need a bigger evaluation set."*

## Reuse for training

Per Ch 4: *"The data curated and annotated for evaluation can then later be used to synthesize more data for training, as discussed in Chapter 8."*

The annotation guideline is doubly valuable — it powers both evaluation and supervised finetuning.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[PublicBenchmark]] — the complement.
- [[ModelSelectionWorkflow]] — where this lives.
- [[EvaluationPipeline]] / [[EvaluationGuideline]] / [[DataSlicing]] / [[BootstrapEvaluation]] — design ingredients.
- [[BusinessMetric]] — what private benchmarks tie back to.
