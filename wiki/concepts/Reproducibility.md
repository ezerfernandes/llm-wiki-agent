---
title: "Reproducibility"
type: concept
tags: [mlops, science]
sources: [madewithml-mlops, madewithml-reproducibility, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Reproducibility

The ability to re-run an experiment and obtain the same result. In ML, requires pinning data, code, env (via [[PyprojectToml]], [[VirtualEnvironment]]), and seeds; see [[ReproducibilityInML]] for nuances.

## From [[hands-on-llm-ch05-text-clustering-topic-modeling|*Hands-On LLMs* Ch 5]]

Ch 5 surfaces an explicit **reproducibility tradeoff** in [[UMAP]]: *"setting a `random_state` in UMAP will make the results reproducible across sessions but will disable parallelism and therefore slow down training."* This is a recurring tension in ML — deterministic algorithms typically lose the speedups of parallel reduction operations that introduce nondeterministic floating-point summation order. Ch 5 chooses reproducibility (`random_state=42`) so its 156-cluster output on the ArXiv NLP dataset can be reproduced exactly by readers.

## Connections

- [[madewithml-mlops]] / [[madewithml-reproducibility]] — primary sources.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — Ch 5's UMAP reproducibility tradeoff.
- [[UMAP]] — where the `random_state` knob lives.
- [[ReproducibilityInML]] — full treatment.
