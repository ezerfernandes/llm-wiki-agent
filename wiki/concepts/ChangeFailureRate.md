---
title: "Change Failure Rate (CFR)"
type: concept
tags: [observability, monitoring, devops, metric, deployment]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Change Failure Rate (CFR)

**The percentage of changes or deployments that result in failures requiring fixes or rollbacks.** The third of three DevOps observability metrics [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] adopts for AI applications, alongside [[MTTD]] and [[MTTR]].

> *"CFR (change failure rate): The percentage of changes or deployments that result in failures requiring fixes or rollbacks."* — Ch 10

## Ch 10's strong claim

> *"If you don't know your CFR, it's time to redesign your platform to make it more observable."* — Ch 10

CFR is the metric Huyen flags as **the test of whether a platform is observable at all**. If you can't reliably tell which deployments broke things, you can't measure CFR — and you can't measure CFR exactly when you most need to (when your team is shipping fast).

## The evaluation-monitoring feedback loop

CFR has an unusual property compared to MTTD / MTTR: it can be lowered by upstream investment, not just downstream investment.

> *"Having a high CFR doesn't necessarily indicate a bad monitoring system. However, you should rethink your evaluation pipeline so that bad changes are caught before being deployed. Evaluation and monitoring need to work closely together. Evaluation metrics should translate well to monitoring metrics, meaning that a model that does well during evaluation should also do well during monitoring."* — Ch 10

High CFR is a signal that the **[[ai-engineering-ch04-evaluate-ai-systems|evaluation pipeline]] is failing to catch what the deployment finds**. The fix is upstream: either toughen evaluation, or arrange evaluation metrics to correlate with monitoring metrics so an offline win predicts an online win.

## Why AI applications have unusual CFR pressure

Foundation-model behavior is **not unit-testable in the classical sense**. A prompt-template tweak can silently change behavior across a long tail of inputs. A model-provider's [[SilentModelUpdate|silent update]] is a "change" you didn't deploy but whose CFR contribution falls on you anyway. Both make CFR harder to measure and harder to keep low than in conventional software.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[MTTD]] / [[MTTR]] — paired DevOps observability metrics.
- [[ai-engineering-ch04-evaluate-ai-systems]] — the evaluation pipeline whose quality determines CFR.
- [[Evaluation]] — the upstream investment that lowers CFR.
- [[SilentModelUpdate]] — a class of "change" outside your control that hits CFR.
- [[observability]] / [[Monitoring]] — parent disciplines.
