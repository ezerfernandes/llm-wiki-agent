---
title: "Integration Testing"
type: concept
tags: [testing, software-engineering]
sources: [fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Integration Testing

Exercising multiple components together (model + preprocessor + API + DB) to surface contract bugs that unit tests miss. Anchored by [[ArrangeActAssert]] structure and run in [[CICD]]; for ML, often the right level to catch training/serving skew and [[FeatureStore]] drift.

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] treats a system / integration test as a *source* of unit tests: while an end-to-end execution runs (the chapter's `webbrowser()` downloading a URL), a [[Carver|`CallCarver`]] records every internal function call, and [[TestCarving|carving]] synthesizes each into a fast standalone [[UnitTesting|unit test]]. The win is speed — running an internal function alone (e.g. `urlparse()`) is measured as tens of thousands of times cheaper than re-driving the whole integration scenario — so carved unit tests can replace much of what would otherwise need a full system run.

## Sources
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
