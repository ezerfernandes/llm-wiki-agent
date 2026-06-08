---
title: "Shrinking"
type: concept
tags: [testing, property-based-testing]
sources: [hypothesis-example-count]
last_updated: 2026-06-05
---

# Shrinking

**Shrinking** is the [[PropertyBasedTesting|property-based testing]] step that, once a generated input falsifies a property, searches for the *smallest / simplest* input that still reproduces the failure — so the reported counterexample is human-readable (e.g. `n=0` rather than a large random integer). In [[Hypothesis]] this is the `Phase.shrink` phase.

Key behaviors documented in [[hypothesis-example-count]]:

- When a failing example is found, generation stops early and the test may be called additional times during the `Phase.shrink` and `Phase.explain` phases.
- If the initial failing example is already as simple as possible, `Phase.shrink` produces **no** additional executions (but `Phase.explain` still might).
- **Flakiness replay**: regardless of whether shrinking ran, Hypothesis always runs the minimal failing example *one extra time* to confirm the failure is not flaky. So even a trivial test that finds `n=0` will execute with `n=0` twice — once to discover the failure, once to replay it.

This replay-once behavior is why the total number of test executions in a failing run is not simply `max_examples`.

## Connections
- [[PropertyBasedTesting]] — the paradigm shrinking belongs to.
- [[Hypothesis]] — implements shrinking via `Phase.shrink` / `Phase.explain`.
- [[ExampleDatabase]] — persists the *minimal* counterexample produced by shrinking so it replays on the next run.
- [[hypothesis-example-count]] — the source documenting shrink/explain/flakiness-replay execution counts.
