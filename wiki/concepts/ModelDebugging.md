---
title: "Model Debugging"
type: concept
tags: [mlops, debugging, diagnosis, operations]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Model Debugging

Root-cause diagnosis for degraded ML models. Differs from traditional software debugging because failures are **probabilistic, not deterministic** — a model producing wrong predictions throws no exceptions or stack traces. [[mlsysbook-ch14-ml-operations]] gives a **data-first decision tree**:

1. **Is it the data?** Pipeline failures, schema changes, missing values, distribution shifts — **60–80% of production ML issues originate here**.
2. **Is it [[TrainingServingSkew|training-serving skew]]?** Compare feature distributions (KS / [[PopulationStabilityIndex|PSI]]).
3. **Is it a subpopulation?** [[SliceAnalysis|Slice analysis]] across geography, device, segment.
4. **Is it temporal?** Sudden drop → deployment/data issue; gradual decline → concept drift.
5. **Is it the model?** Only after eliminating data — via prediction analysis and feature attribution.

Toolkit: decision trees, [[SliceAnalysis|slice analysis]], [[SHAP]] feature attribution, counterfactual analysis ("if `session_duration` were 45s not 12s, the model would predict 'engaged'"). A six-phase methodology (observe, isolate, hypothesize, test, confirm, generalize) converts each resolved incident into a monitoring rule. Watch for "zombie features" — features deprecated in code but still flowing through feature stores/contracts.

## Connections
- [[IncidentResponse]] — debugging is its diagnosis step.
- [[SliceAnalysis]] / [[SHAP]] — debugging techniques.
- [[TrainingServingSkew]] / [[DataDrift]] / [[ConceptDrift]] — common root causes.
- [[DAMTaxonomy]] — symptom-to-(Data/Algorithm/Machine) mapping.
- [[MLOps]] — production-operations practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
