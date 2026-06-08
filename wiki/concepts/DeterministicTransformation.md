---
title: "Deterministic Transformation"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, reproducibility]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Deterministic Transformation

A transformation that always produces the same output for the same input, with no dependence on external factors like wall-clock time, random numbers, or mutable global state (Reddi, [[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]).

Time-dependent transforms break determinism: computing "days since event" from the current date means reprocessing historical data yields different results. The fix is to capture temporal reference points explicitly — compute "days from event to a fixed, persisted reference date." Random operations should use seeded RNGs whose seed is derived deterministically from the input data.

Determinism enables debugging (recreate exact features for a problematic example), safe reprocessing after bug fixes, and distributed processing where every worker must produce identical features from the same input. It pairs with [[Idempotency|idempotency]] as the two pillars of processing reliability. KWS example: same raw audio → same MFCC features regardless of when/where computed, with FFT window, hop length, and coefficient count versioned alongside the code.

## Connections

- [[Idempotency]] — the complementary retry-safety property.
- [[DataLineage]] / [[Reproducibility]] — what determinism enables.
- [[TrainingServingConsistency]] — determinism supports it.
- [[mlsysbook-ch04-data-engineering]] — source.
