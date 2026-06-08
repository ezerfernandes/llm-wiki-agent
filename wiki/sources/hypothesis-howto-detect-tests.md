---
title: "Detect Hypothesis tests (Hypothesis how-to)"
type: source
tags: [testing, python, hypothesis, property-based-testing, introspection, pytest, how-to]
date: 2026-06-05
source_file: raw/hypothesis/how-to/hypothesis-howto-detect-tests.md
---

## Summary
A short [[Hypothesis]] how-to guide on **dynamically determining whether a callable is a Hypothesis test** — i.e. introspecting a function (or stateful test) at runtime to decide if it was decorated with `@given` or otherwise built by Hypothesis. The recommended approach is the public `is_hypothesis_test()` predicate, exported from the top-level `hypothesis` namespace, which also recognizes stateful [[PropertyBasedTesting|property-based]] tests. As a [[Pytest]]-specific alternative, the guide notes that the Hypothesis pytest plugin auto-applies a `@pytest.mark.hypothesis` mark to every Hypothesis test, so a plugin can detect one via `node.get_closest_marker("hypothesis")`. This is primarily useful to authors of plugins, pytest integrations, and other tooling that needs to treat Hypothesis tests specially.

## Key Claims
- The most straightforward way to detect a Hypothesis test is the public predicate `is_hypothesis_test()`, importable as `from hypothesis import is_hypothesis_test`.
- `is_hypothesis_test(f)` returns true for a function decorated with `@given(...)` (e.g. `@given(st.integers())`).
- It also works for **stateful tests**: `is_hypothesis_test(MyStateMachine.TestCase().runTest)` is true for a [[Hypothesis|`RuleBasedStateMachine`]] subclass (imported from `hypothesis.stateful`).
- Under [[Pytest]], the Hypothesis pytest plugin automatically adds the `@pytest.mark.hypothesis` mark to **all** Hypothesis tests.
- That mark gives pytest plugins a second detection path: `node.get_closest_marker("hypothesis")` (or similar) reveals whether the test node is a Hypothesis test.

## Key Quotes
> "How to dynamically determine whether a test function has been defined with Hypothesis." — the guide's stated purpose

> "The most straightforward way is to use `is_hypothesis_test()`" — the recommended, library-agnostic approach

> "If you're working with pytest, the Hypothesis pytest plugin automatically adds the `@pytest.mark.hypothesis` mark to all Hypothesis tests. You can use `node.get_closest_marker(\"hypothesis\")` or similar methods to detect the existence of this mark." — the pytest-specific detection path

## Code Receipt

Detecting a `@given`-decorated function with the public predicate:
```python
from hypothesis import is_hypothesis_test

@given(st.integers())
def f(n): ...

assert is_hypothesis_test(f)
```

The same predicate works for stateful tests:
```python
from hypothesis import is_hypothesis_test
from hypothesis.stateful import RuleBasedStateMachine

class MyStateMachine(RuleBasedStateMachine): ...

assert is_hypothesis_test(MyStateMachine.TestCase().runTest)
```

Pytest-specific detection via the auto-applied mark (Hypothesis pytest plugin adds `@pytest.mark.hypothesis` to every Hypothesis test):
```python
node.get_closest_marker("hypothesis")
```

## Connections
- [[Hypothesis]] — the library whose public introspection predicate (`is_hypothesis_test`) this guide documents.
- [[PropertyBasedTesting]] — the paradigm; detection covers both `@given` tests and stateful machines.
- [[Pytest]] — the host framework whose plugin auto-marks Hypothesis tests with `@pytest.mark.hypothesis`, enabling marker-based detection.
- [[Python]] — `is_hypothesis_test` is a runtime predicate over Python callables; stateful tests live in `hypothesis.stateful`.

## Contradictions
- None. This guide is consistent with the rest of the [[Hypothesis]] cluster; it complements (does not conflict with) the type-hints, health-check, example-count, and database how-tos.
