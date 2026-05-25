---
title: "Bootstrap Evaluation"
type: concept
tags: [evaluation, statistics, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Bootstrap Evaluation

**Sampling with replacement** to size and validate an evaluation set. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "If you have an evaluation set of 100 examples, you can create multiple bootstraps of these 100 examples and see if they give similar evaluation results. … If you get 90% on one bootstrap but 70% on another bootstrap, your evaluation pipeline isn't that trustworthy."

## The procedure

For an N-example evaluation set:

1. Draw N samples **with replacement** from the original N evaluation examples.
2. Evaluate your model on these N bootstrapped samples.
3. Repeat K times.
4. If results vary wildly across bootstraps → grow N.

## Why bootstrap and not classical statistics

> "In theory, a statistical significance test can be used to compute the sample size needed for a certain level of confidence (e.g., 95% confidence) if you know the score distribution. However, in reality, it's hard to know the true score distribution."

Bootstrap is **distribution-free** — you don't need to know the underlying score distribution to estimate variability.

## In the wider statistics

Bootstrap resampling (Efron 1979) is a classical statistical technique; Ch 4 applies it specifically to evaluation-set sizing. The same machinery is used for confidence intervals and significance tests in many other contexts.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Bootstrap]] — the broader statistical technique.
- [[EvaluationPipeline]] — parent process.
- [[PrivateBenchmark]] — what bootstrap sizes.
- [[DataSlicing]] — bootstrap each slice separately.
