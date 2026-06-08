---
title: "Reproducible System Artifact"
type: concept
tags: [mlops, reproducibility, deployment, mlsysbook]
sources: [mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Reproducible System Artifact

The **true deliverable** of the model-development stage — not trained weights alone, but the complete bundle needed to reproduce and serve the model (Reddi, [[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]):

1. **Model weights** — the learned parameters.
2. **Inference code** — the exact code to run the model, including preprocessing logic.
3. **Environment specification** — the full dependency graph (Docker container, `requirements.txt`, CUDA drivers).
4. **Configuration** — hyperparameters and runtime settings.

A common failure mode is treating weights as the sole output. Without bundling the environment, the "it works on my machine" problem causes catastrophic deployment failures: "A system that achieves 99% accuracy but relies on a specific library version not present in production is a broken system."

## Connections

- [[Reproducibility]] — the broader discipline this artifact enforces.
- [[ExperimentTracking]] / [[DataVersioning]] / [[DataLineage]] — how the bundle's provenance is tracked.
- [[Determinism]] — nondeterministic floating-point is why hardware/env must be pinned.
- [[mlsysbook-ch03-ml-workflow]] — source.
