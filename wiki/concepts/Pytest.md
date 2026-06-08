---
title: "Pytest"
type: concept
tags: [testing, python, tooling]
sources: [madewithml-testing, hypothesis-howto-suppress-healthchecks, hypothesis-howto-detect-tests]
last_updated: 2026-06-05
---

# Pytest

The dominant [[Python]] testing framework with fixtures, parametrization, and a rich plugin ecosystem including [[PytestCov]]. Core to [[UnitTesting]] and [[RegressionTesting]] in [[MLOps]] codebases.

It also hosts [[PropertyBasedTesting|property-based testing]] via [[Hypothesis]], whose `@given` tests run as ordinary pytest tests; `conftest.py` is the usual place to configure Hypothesis (e.g. loading a [[HypothesisSettings|settings profile]] to suppress a [[HealthCheck]]). Note `HealthCheck.function_scoped_fixture` specifically warns when a function-scoped pytest fixture is combined with `@given`. See [[hypothesis-howto-suppress-healthchecks]]. The Hypothesis pytest plugin auto-applies a `@pytest.mark.hypothesis` mark to every Hypothesis test, so plugins can detect such tests via `node.get_closest_marker("hypothesis")` (or the library-agnostic `is_hypothesis_test()` predicate); see [[hypothesis-howto-detect-tests]].
