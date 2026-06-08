---
title: "Model Validation"
type: concept
tags: [evaluation, validation, mlops, deployment, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Model Validation

The **gate that determines whether a trained model is safe to deploy** by testing it against the **full constraint surface** of the deployment environment — latency SLOs, fairness thresholds, cost budgets, and robustness under distribution shift (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]).

Distinct from [[ModelEvaluation|model evaluation]]: evaluation measures accuracy on a held-out i.i.d. test set drawn from the training distribution; validation is a **multi-dimensional gate**. A model at 95% test accuracy may still violate a 100 ms p99 latency SLO, exceed a demographic-parity gap of $\varepsilon \le 5\%$, or degrade 10+% under input perturbation $\|\delta\|_\infty \le 0.01$. Each unchecked dimension is a deployment risk that compounds silently. Validation is therefore best understood as a **risk-management discipline**, not "one more test."

Ch 3 organizes it as a progression toward production: offline evaluation → [[ShadowDeployment|shadow mode]] → [[CanaryDeployment|canary]] → [[ABTesting|A/B test]], plus production-condition validation (cross-source, robustness, temporal) and **regulatory validation** (FDA SaMD). The hallmark of trustworthy systems: those that *fail safely* (refer uncertain cases) over those that *fail silently*.

## Connections

- [[ModelEvaluation]] — accuracy measurement vs. the deployment-gate distinction.
- [[ShadowDeployment]] / [[CanaryDeployment]] / [[ABTesting]] — progressive validation stages.
- [[ModelCalibration]] / [[Sensitivity]] / [[Specificity]] / [[AUC]] — the metrics and risks it weighs.
- [[StageInterfaceSpecification]] — validation produces the stage's "validation certificate."
- [[FDA]] — regulatory validation (SaMD) as a first-class requirement.
- [[mlsysbook-ch03-ml-workflow]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 distinguishes production validation (operational readiness, canary, A/B, slice metrics) from research evaluation against a static test set.

