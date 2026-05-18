---
title: "Made With ML — Testing ML Systems: Code, Data and Models"
type: source
tags: [mlops, made-with-ml, testing, quality]
date: 2026-05-15
source_file: raw/madewithml/mlops-testing.md
---

## Summary
Made With ML lesson on testing ML systems along three axes: code (pytest), data (great_expectations), and models (behavioral testing). Lays out the Arrange-Act-Assert methodology, the test taxonomy (unit, integration, system, acceptance, regression), and pytest features (parametrize, fixtures, markers, coverage). Builds a data validation suite with great_expectations covering schema, label sets, uniqueness, nulls, and types. Implements model behavioral tests (invariance, directional, MFT) using a `predictor` fixture. Ends by contrasting testing (offline, against held-out expectations) with monitoring (online, drift-aware).

## Key Claims
- ML systems must be tested along three axes: code (deterministic logic), data (schemas, ranges, label sets), and models (behavioral expectations) — code-only tests miss the failure modes unique to ML.
- The Arrange-Act-Assert framework structures every test; a fourth Clean step (e.g. via `pytest-randomly`) defends against state leakage.
- Five test categories sit at different points in the dev cycle: unit, integration, system, acceptance, regression — and ML adds behavioral tests as a model-specific genre.
- Atomic functions with single responsibilities are the precondition for testable code; if a function resists testing, it needs to be split.
- 100% coverage means every line is exercised, not that every line is correctly tested — coverage is a floor, not a correctness proof.
- [[GreatExpectations]] declarative expectations like `expect_column_values_to_be_in_set`, `expect_compound_columns_to_be_unique`, `expect_column_values_to_be_of_type` catch schema drift and label noise upstream.
- Behavioral testing from CheckList decomposes into invariance (perturbations should not change output), directional (perturbations should change output predictably), and MFT (simple input/output pairs).
- Testing is the offline twin of [[Monitoring]]: testing validates offline expectations; monitoring validates the same expectations on live data plus drift, anomalies, and indirect performance signals.
- pytest's `@pytest.mark.skipif` and custom markers (e.g. `@pytest.mark.training`) allow gating compute-intensive tests behind hardware availability.
- Data validation should run as far upstream as possible (in [[DataEngineering]] pipelines), not just inside the ML application that consumes the data.

## Key Quotes
> "Coverage only indicates that a piece of code executed in a test, not necessarily that every part of it was tested, let alone thoroughly tested. Therefore, coverage should never be used as a representation of correctness." — on the limits of coverage

> "ML systems can run to completion without throwing any exceptions / errors but can produce incorrect systems." — on why ML needs more than traditional testing

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[Pytest]] — testing framework
- [[GreatExpectations]] — data validation library
- [[CheckList]] — behavioral testing paper
- [[Coverage]] — coverage library
- [[PytestCov]] — pytest integration
- [[Testing]] — primary concept
- [[UnitTesting]] — test category
- [[IntegrationTesting]] — test category
- [[BehavioralTesting]] — model-level genre
- [[RegressionTesting]] — defending against re-introduced bugs
- [[Monitoring]] — online counterpart
- [[DataEngineering]] — where upstream validation belongs
- [[MLOps]] — discipline
- [[CICD]] — natural execution venue
- [[PreCommit]] — local execution venue
- [[ArrangeActAssert]] — test structure
- [[GitHubActions]] — server-side execution

## Contradictions
- None identified.
