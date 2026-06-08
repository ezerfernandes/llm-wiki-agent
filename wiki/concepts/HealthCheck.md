---
title: "HealthCheck (Hypothesis)"
type: concept
tags: [testing, python, hypothesis, property-based-testing]
sources: [hypothesis-howto-suppress-healthchecks, hypothesis-example-count]
last_updated: 2026-06-05
---

# HealthCheck (Hypothesis)

In [[Hypothesis]], **`HealthCheck`** is an enum of built-in warnings the library raises to signal potential problems with a property-based test — specifically issues with test *effectiveness*, *performance*, or *example-generation quality*. They are diagnostics, not hard failures, and exist to stop subtly broken tests from silently passing.

## Named checks
- **`HealthCheck.filter_too_much`** — too many generated examples are being discarded by `.filter(...)` / assumptions, which weakens the test; the canonical example used in the suppression how-to.
- **`HealthCheck.function_scoped_fixture`** — flags function-scoped [[Pytest]] fixtures used with `@given`, where the fixture is *not* re-run per generated example (a common source of confusing bugs).
- **`HealthCheck.differing_executors`** — detects when the same test is run by different executors across examples.
- **`HealthCheck.data_too_large`** — raised when too many generated examples exceed Hypothesis's internal per-example size limit and are retried (the size limit itself is an undocumented implementation detail) ([[hypothesis-example-count]]).

## Suppressing health checks
Checks are silenced through the [[HypothesisSettings|settings system]] via the `suppress_health_check` setting, which takes a list of `HealthCheck` members:

```python
from hypothesis import HealthCheck, settings

settings.register_profile(
    "my_profile", suppress_health_check=[HealthCheck.filter_too_much]
)
settings.load_profile("my_profile")
```

A per-test `@settings(...)` decorator with an explicit `suppress_health_check` overrides any profile-level value. Suppressing everything with `list(HealthCheck)` is possible but explicitly discouraged: the recommendation is to suppress checks as you encounter them, because some (e.g. `function_scoped_fixture`, `differing_executors`) catch subtle interactions that can save hours of debugging.

## Connections
- [[Hypothesis]] — the library that defines and raises these warnings.
- [[HypothesisSettings]] — the `suppress_health_check` setting lives here.
- [[PropertyBasedTesting]] — health checks protect the quality of generated examples.
- [[Pytest]] — `function_scoped_fixture` specifically concerns pytest fixtures.

## Sources
- [[hypothesis-howto-suppress-healthchecks]] — how-to on globally suppressing a health check.
- [[hypothesis-example-count]] — source for the `data_too_large` size-limit behavior.
