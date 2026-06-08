---
title: "Retraining Economics"
type: concept
tags: [mlops, retraining, drift, cost, optimization]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Retraining Economics

The quantitative framework for deciding **how often to retrain** a deployed model, treating it as an engineering optimization rather than intuition. Model accuracy decays like a radioactive isotope: $A(t) = A_0 e^{-\gamma t}$, with a measurable **half-life** determinable from historical accuracy data. Staleness cost accumulates as queries are served by an increasingly stale model; each retraining incurs fixed compute/validation/deployment/risk cost.

The **optimal retraining interval** minimizes total cost per unit time, yielding the **square-root law**:

$$T^* \approx \sqrt{\frac{2C}{Q \cdot V \cdot A_0 \cdot \gamma}}$$

where $C$ = retraining cost, $Q$ = query volume, $V$ = value per query for a unit accuracy change, $A_0$ = initial accuracy, $\gamma$ = daily decay rate. Worked fraud-detection example ($Q$=1M/day, $V$=$0.50, $A_0$=0.95, $\gamma$=2%/day, $C$=$5,000) → $T^* \approx$ **1 day**. Sensitivity: 4× cost → 2× longer interval; 4× volume or 4× decay → 2× shorter. Decision: `Retrain if ΔAccuracy × Value > Training Cost + Deployment Risk`. Limitations: assumes predictable (gradual) drift, a known value function, independent cycles, and linear cost scaling.

Defined in [[mlsysbook-ch14-ml-operations]] (mlsysbook Vol 1, Ch 14) as the operationalization of the **cost-aware automation** principle.

## Connections
- [[MLOps]] — the cost-aware-automation foundational principle.
- [[SystemEntropy]] / [[SilentDegradation]] — the accuracy decay this models.
- [[DriftDetection]] / [[PopulationStabilityIndex]] — triggers for triggered retraining.
- [[ContinualLearning]] / [[StatelessRetraining]] — retraining strategies.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
