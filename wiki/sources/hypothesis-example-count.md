---
title: "Hypothesis Docs — How many times will Hypothesis run my test?"
type: source
tags: [testing, python, hypothesis, property-based-testing, explanation]
date: 2026-06-05
source_file: raw/hypothesis/explanation-example-count.md
sources: [hypothesis-example-count]
last_updated: 2026-06-05
---

## Summary
An explanation page from the [[Hypothesis]] documentation answering "how many times will Hypothesis run my test?" The short answer is *exactly `max_examples` times* — but with four documented exceptions that make the real count vary. The page is the canonical reference for the relationship between `max_examples`, retries, search-space exhaustion, and the [[Shrinking|shrink]] / explain phases. Its most-cited concrete fact: a failing test always runs its **minimal failing example one extra time** to check for flakiness, so even a trivial failure executes the offending input *twice*.

## Key Claims
- The default run count is `max_examples`, subject to four exceptions: search-space exhaustion (fewer), retries (more), and finding a failing example (either).
- **Search-space exhaustion** — if there are no more distinct examples to try, Hypothesis stops early. `@given(st.integers(0, 19))` runs exactly **20** times, not the default 100, because only 20 unique integers exist. Search-space tracking is "good, but not perfect" and is treated as a bonus, not a guarantee.
- **`assume()` / `.filter()` retries** — discarded examples are retried and **not** counted toward `max_examples`. `@given(st.integers())` with `assume(n % 2 == 0)` runs **~200** times (half discarded).
- A failing `assume()` retries the *entire* example immediately, whereas `.filter()` is retried several times *within* the same example — making `.filter()` **more efficient** than `assume()` for the same condition.
- Builtin strategies can themselves use `assume()`/`.filter()` and cause retries even if your code does not; Hypothesis tries to satisfy conditions directly rather than by rejection sampling, so this is relatively uncommon.
- **Examples that are too large** — Hypothesis enforces an internal (undocumented) per-example size limit; oversized examples are retried and not counted, and too many of them raise [[HealthCheck|`HealthCheck.data_too_large`]] (unless suppressed via `settings.suppress_health_check`). Most tests never approach this limit.
- **Failing examples** — generation stops early on failure; the test may be called more during `Phase.shrink` and `Phase.explain`. If the initial failure is already minimal, `Phase.shrink` adds **no** executions (but `Phase.explain` still might).
- **Flakiness replay (always-on)** — regardless of shrinking, the minimal failing example is run **one additional time** to confirm the failure isn't flaky. A test using only `Phase.generate` that fails at `n=0` therefore executes with `n=0` *twice*.

## Key Quotes
> "The short answer is 'exactly `max_examples` times'" — with the four documented exceptions that follow.

> "This runs `test_function` 20 times, not 100, since there are only 20 unique integers to try." — search-space exhaustion example.

> "while failing an `assume()` triggers an immediate retry of the entire example, Hypothesis will try several times in the same example to satisfy a `.filter()` condition. This makes expressing the same condition using `.filter()` more efficient than `assume()`." — the assume-vs-filter efficiency rule.

> "it will always run the minimal failing example one additional time to check for flakiness." — the always-on flakiness replay.

## Code Receipt

Search-space exhaustion (runs 20×, not `max_examples`):

```python
from hypothesis import given, strategies as st

calls = 0

@given(st.integers(0, 19))
def test_function(n):
    global calls
    calls += 1

test_function()
assert calls == 20
```

Flakiness replay — `n=0` runs *twice* even with only `Phase.generate`:

```python
from hypothesis import Phase, given, settings, strategies as st

@given(st.integers())
@settings(phases=[Phase.generate])
def test_function(n):
    print(f"called with {n}")
    assert n != 0

test_function()
```

## Connections
- [[Hypothesis]] — the property-based testing library whose run-count behavior this page documents.
- [[Shrinking]] — `Phase.shrink` / `Phase.explain` and the always-on minimal-example flakiness replay are the source of the variable failing-run count.
- [[HealthCheck]] — `HealthCheck.data_too_large` is the warning raised when too many oversized examples are retried.
- [[HypothesisSettings]] — `max_examples`, `phases`, and `suppress_health_check` are the settings that govern the count.
- [[PropertyBasedTesting]] — generation + retry + shrink is the execution model of the paradigm.
- [[Pytest]] — the host framework Hypothesis tests run under.

## Contradictions
- None. This is a procedural explanation page; it complements (does not conflict with) the sibling Hypothesis sources [[hypothesis-domain-and-distribution]] and [[hypothesis-howto-suppress-healthchecks]]. The wiki's other "hypothesis" pages ([[HypothesisTesting]], [[HypothesisClass]]) are the statistical/ML senses — unrelated to this software library.
