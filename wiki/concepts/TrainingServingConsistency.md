---
title: "Training-Serving Consistency"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, mlops, reliability]
sources: [mlsysbook-ch04-data-engineering, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Training-Serving Consistency

The **consistency imperative** of Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]): transformation logic must be immutable across training and serving environments. Violating it produces silent accuracy degradation proportional to the [[KullbackLeiblerDivergence|KL divergence]] $\mathcal{D}_{\text{KL}}(p_{g_{\text{serve}}} \lVert p_{g_{\text{train}}})$ between the feature distributions induced by the serving and training transforms.

The crucial nuance: consistency is **not** "fixed by sharing code" — it is a **state-synchronization problem**. Parameters computed on training data (normalization means/std-devs, categorical vocabularies, encoding dictionaries) must be persisted alongside the model artifact and reused at serving. Unknown categories at serving need an explicit "unknown" token. The failure mode is [[TrainingServingSkew|training-serving skew]] (the inverse), which causes 10–15% accuracy drops with no error messages.

The only reliable fix is an **architectural guarantee — shared code, not copied code** — which is why production systems implement transforms in shared libraries and adopt [[FeatureStore|feature stores]].

## Connections

- [[TrainingServingSkew]] — the failure mode this imperative prevents.
- [[FeatureStore]] — the architectural mechanism that enforces consistency.
- [[Idempotency]] / [[DeterministicTransformation]] — reliability properties that support it.
- [[FeatureEngineering]] — every engineered feature must be computed identically.
- [[KullbackLeiblerDivergence]] — the metric that quantifies degradation.
- [[mlsysbook-ch04-data-engineering]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 makes training-serving consistency the "consistency imperative" principle, enforced by feature stores computing features once for both paths.

