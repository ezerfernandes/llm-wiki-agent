---
title: "Model Selection Workflow"
type: concept
tags: [model-selection, methodology, ai-engineering, workflow]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Model Selection Workflow

The **four-step iterative process** for picking a model for your application, per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

1. **Filter** out models whose [[HardModelAttribute|hard attributes]] don't work for you (licenses, training data, model size, your own privacy policy).
2. **Narrow** to promising candidates using publicly available information — [[PublicBenchmark|public benchmarks]], [[Leaderboard|leaderboard]] rankings. Balance multiple objectives (quality, latency, cost).
3. **Experiment** with your own [[EvaluationPipeline|evaluation pipeline]] to find the best model for your application.
4. **Monitor** in production to detect failures and collect feedback.

## Iteration

> "These four steps are iterative — you might want to change the decision from a previous step with newer information from the current step. For example, you might initially want to host open source models. However, after public and private evaluation, you might realize that open source models can't achieve the level of performance you want and have to switch to commercial APIs."

## Per-technique re-application

The workflow runs many times throughout development as adaptation techniques change:

> "For example, prompt engineering might start with the strongest model overall to evaluate feasibility and then work backward to see if smaller models would work. If you decide to do finetuning, you might start with a small model to test your code and move toward the biggest model that fits your hardware constraints (e.g., one GPU)."

## The two sub-questions

Within each iteration:
1. **What's the best achievable performance?** (define the ceiling)
2. **What model gives the best performance per dollar?** (optimize cost-quality)

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[HardModelAttribute]] / [[SoftModelAttribute]] — the attribute typology.
- [[ModelBuildVsBuy]] — the first major filter.
- [[PublicBenchmark]] / [[Leaderboard]] — step 2 narrowing tools.
- [[EvaluationPipeline]] — step 3 mechanism.
- [[ParetoOptimization]] — the methodology for balancing objectives.
- [[Evaluation]] — discipline.
