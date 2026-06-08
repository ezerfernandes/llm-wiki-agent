---
title: "Suppress a health check everywhere (Hypothesis how-to)"
type: source
tags: [testing, python, hypothesis, property-based-testing, how-to]
date: 2026-06-05
source_file: raw/hypothesis/how-to/hypothesis-howto-suppress-healthchecks.md
---

## Summary
A short how-to from the [[Hypothesis]] documentation explaining how to globally suppress a [[HealthCheck]] warning across an entire test suite. The recommended approach is to register and load a [[HypothesisSettings|settings profile]] (via `settings.register_profile()` + `settings.load_profile()`) in a file loaded before tests run, such as pytest's `conftest.py`. The guide shows suppressing a single check (`filter_too_much`) and — with an explicit warning against it — suppressing every check at once via `list(HealthCheck)`.

## Key Claims
- Hypothesis raises `HealthCheck` warnings to flag potential problems with test effectiveness, performance, or the quality of generated examples.
- To suppress a health check globally, use the settings-profile system: call `settings.register_profile(name, suppress_health_check=[...])` then `settings.load_profile(name)`.
- The profile code must live in a file loaded before tests run; for [[Pytest]] this is `conftest.py`.
- `suppress_health_check` takes a list of `HealthCheck` enum members (e.g. `[HealthCheck.filter_too_much]`).
- A per-test `@settings(...)` decorator with an explicit `suppress_health_check` value overrides the profile-level setting (decorator wins over profile).
- All checks can be suppressed at once with `suppress_health_check=list(HealthCheck)`, but this is explicitly discouraged.
- Blanket suppression is risky because some checks (notably `HealthCheck.function_scoped_fixture` and `HealthCheck.differing_executors`) detect subtle interactions that can save hours of debugging.

## Key Quotes
> "Hypothesis raises `HealthCheck` warnings to signal potential issues with test effectiveness, performance, or example generation quality." — opening framing of why health checks exist

> "We strongly recommend that you suppress health checks as you encounter them, rather than using a blanket suppression. Several health checks check for subtle interactions that may save you hours of debugging, such as `HealthCheck.function_scoped_fixture` and `HealthCheck.differing_executors`." — warning admonition against disabling everything

> "Individual test decorators using `@settings` with explicit `suppress_health_check` values will override the profile setting." — precedence rule

## Code Receipt

Suppress a single health check globally (place in `conftest.py`):

```python
from hypothesis import HealthCheck, settings

settings.register_profile(
    "my_profile", suppress_health_check=[HealthCheck.filter_too_much]
)
settings.load_profile("my_profile")
```

Suppress *all* health checks (not recommended):

```python
from hypothesis import HealthCheck, settings

settings.register_profile("my_profile", suppress_health_check=list(HealthCheck))
settings.load_profile("my_profile")
```

## Connections
- [[Hypothesis]] — the property-based testing library this how-to documents.
- [[HealthCheck]] — the warning mechanism being suppressed; `filter_too_much`, `function_scoped_fixture`, and `differing_executors` are specific members named here.
- [[HypothesisSettings]] — the `settings()` / profile system (`register_profile`, `load_profile`, `suppress_health_check`) that is the recommended suppression mechanism.
- [[PropertyBasedTesting]] — the testing paradigm Hypothesis implements; health checks guard the quality of generated examples.
- [[Pytest]] — `conftest.py` is the canonical place to load the profile before tests run.

## Contradictions
- None. This is a narrow procedural how-to with no factual conflict against existing wiki pages (existing "hypothesis" usages in the corpus are statistical/ML hypotheses, an unrelated sense).
