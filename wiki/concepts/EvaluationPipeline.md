---
title: "Evaluation Pipeline"
type: concept
tags: [evaluation, methodology, ai-engineering, pipeline]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Evaluation Pipeline

The **production-grade evaluation infrastructure** for an AI application. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "The success of an AI application often hinges on the ability to differentiate good outcomes from bad outcomes. To be able to do this, you need an evaluation pipeline that you can rely upon."

## The six-step design

1. **[[PerComponentEvaluation|Evaluate all components]]** — each pipeline component independently + end-to-end.
2. **Define [[EvaluationGuideline|evaluation guidelines]]** — unambiguous rubrics with examples; the backbone of reliable evaluation.
3. **Define [[ScoringRubric|scoring rubrics]]** with worked examples and validate with humans.
4. **Tie evaluation to [[BusinessMetric|business metrics]]** — map quality scores to dollars/engagement.
5. **Select evaluation methods** — mix-and-match: cheap classifiers on 100% + AI judges on 1%; use [[Logprobs|logprobs]] when available; keep human evaluation in production.
6. **Annotate data, [[DataSlicing|slice it]], and size with [[BootstrapEvaluation|bootstrap]]** — multiple evaluation sets per slice (representative, frequent-mistake, user-typo, [[OutOfScopeEvaluation|out-of-scope]], etc.).

## Per-task, per-turn, per-component

Three evaluation granularities that should all be in the pipeline:

- **Per-component** — each step in a pipeline (PDF → text, then text → extracted-employer).
- **[[TurnBasedEvaluation|Per-turn]]** — quality of each conversation turn.
- **[[TaskBasedEvaluation|Per-task]]** — did the system help the user accomplish their task? (More important but harder to delineate.)

## Production vs experimentation

> "During experimentation, you might have reference data to compare your application's outputs to, whereas, in production, reference data might not be immediately available. However, in production, you have actual users."

Production adds user feedback signals; experiments add reference data signals. A robust pipeline supports both.

## Human evaluation is the north star

Per Ch 4 even with the best automatic metrics, fall back to humans for sanity checks. **LinkedIn manually evaluates up to 500 daily conversations** as a production-time quality sense.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[EvaluationDrivenDevelopment]] — the pre-design principle.
- [[EvaluationGuideline]] / [[ScoringRubric]] / [[BusinessMetric]] / [[DataSlicing]] / [[BootstrapEvaluation]] — ingredients.
- [[PerComponentEvaluation]] / [[TurnBasedEvaluation]] / [[TaskBasedEvaluation]] — granularities.
- [[OutOfScopeEvaluation]] — must-have evaluation set.
- [[ModelSelectionWorkflow]] — step 3 (private experiments) of the workflow uses this pipeline.
- [[Evaluation]] — discipline.
