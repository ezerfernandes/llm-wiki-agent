---
title: "Determinism"
type: concept
tags: [reproducibility, ml-engineering]
sources: []
last_updated: 2026-05-15
---

# Determinism

The property that a computation produces identical outputs given identical inputs across runs — critical for reproducibility, debugging, and trusted [[ExperimentTracking]]. Requires seeding RNGs, ordering [[DataLoader]] workers, and constraining nondeterministic [[CUDA]] kernels.
