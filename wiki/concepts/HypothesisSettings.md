---
title: "Hypothesis Settings & Profiles"
type: concept
tags: [testing, python, hypothesis, configuration]
sources: [hypothesis-howto-suppress-healthchecks]
last_updated: 2026-06-05
---

# Hypothesis Settings & Profiles

**Settings** is [[Hypothesis]]'s configuration system for controlling how property-based tests run — number of examples, deadlines, verbosity, and which [[HealthCheck]] warnings are active. It is applied two ways: per-test via the `@settings(...)` decorator, and globally via *named profiles*.

## Profiles
A profile bundles a set of settings under a name. Register one and activate it before tests run:

```python
from hypothesis import HealthCheck, settings

settings.register_profile(
    "my_profile", suppress_health_check=[HealthCheck.filter_too_much]
)
settings.load_profile("my_profile")
```

For [[Pytest]], the conventional place for this code is `conftest.py`, which is imported before the test session begins.

## Precedence
A per-test `@settings(...)` decorator with an explicit value **overrides** the loaded profile for that test. So a profile sets the suite-wide default and individual tests can opt out or override.

## The `suppress_health_check` setting
- Type: a list of [[HealthCheck]] enum members.
- Suppress one: `suppress_health_check=[HealthCheck.filter_too_much]`.
- Suppress all (discouraged): `suppress_health_check=list(HealthCheck)`.

## Connections
- [[Hypothesis]] — the library this configures.
- [[HealthCheck]] — the warnings controlled by `suppress_health_check`.
- [[PropertyBasedTesting]] — the paradigm whose runs these settings tune.
- [[Pytest]] — `conftest.py` loads the profile before tests run.
- [[ExampleDatabase]] — the failing-example store is selected via the `database=` setting.

## Sources
- [[hypothesis-howto-suppress-healthchecks]] — how-to demonstrating `register_profile` / `load_profile` for global suppression.
- [[hypothesis-howto-custom-database]] — how-to using `database=` to plug in a custom `ExampleDatabase`.
