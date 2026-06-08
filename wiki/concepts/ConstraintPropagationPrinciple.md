---
title: "Constraint Propagation Principle"
type: concept
tags: [ml-systems, mlsysbook, workflow, cost-modeling, foundations]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Constraint Propagation Principle

A constraint discovered at a **late** [[MLSystemLifecycle|lifecycle]] stage propagates *backward* through all earlier stages, and the cost of correction grows **roughly exponentially** with the number of stages traversed (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]):

$$\text{cost multiplier} \approx 2^{N_{\text{stage}}-1}$$

So a constraint caught at **stage 5 (Deployment) costs 16×** and at **stage 6 (Monitoring) costs 32×** what it would have cost at stage 1 (Problem Definition). The model is a deliberately simplified version of Boehm's empirical software-defect cost curve, adapted because late-discovered ML constraints require retraining, data-pipeline changes, and renewed validation — not just a code change.

Propagation is **bidirectional**: a 100 ms latency SLO discovered at deployment constrains model size ($O$, stage 3) → dataset requirements ($D$, stage 2) → what accuracy is even achievable (stage 1). In [[IronLawOfMLSystems|iron-law]] terms, a deployment constraint on $L_{\text{lat}}$ or $R_{\text{peak}}$ redefines the feasible region for $O$, $D_{\text{vol}}$, and $\eta_{hw}$ at every earlier stage. Key implication: **the deployment environment is a day-one constraint, not the last step** — its latency budget, memory capacity, and power envelope bound every upstream decision. The [[StageInterfaceSpecification|stage interface specification]] operationalizes early detection before propagation costs escalate.

## Connections

- [[StageInterfaceSpecification]] — the contracts that catch violations at the cheapest stage.
- [[MLWorkflow]] / [[MLSystemLifecycle]] — the process the principle governs.
- [[IronLawOfMLSystems]] — the performance equation whose feasible region constraints reshape.
- [[MLTechnicalDebt]] / [[DataCascade]] — what compounds when constraints propagate unchecked.
- [[DeploymentSpectrum]] — paradigm selection as the canonical day-one constraint.
- [[mlsysbook-ch03-ml-workflow]] — source.
