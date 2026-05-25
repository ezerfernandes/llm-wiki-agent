---
title: "DSPy Assertions"
type: concept
tags: [concept, dspy, assertions, alias]
sources: [2312.13382-dspy-assertions]
last_updated: 2026-05-24
---

# DSPy Assertions

**`dspy.Assertions`** is the historical / collective name for the assertion-construct family DSPy exposes. The canonical anchor page is **[[LMAssertions]]** — the paper-anchored umbrella concept covering both:

- **[[DSPyAssert|`dspy.Assert`]]** — hard constraint, halts on persistent failure.
- **[[DSPySuggest|`dspy.Suggest`]]** — soft constraint, warns + continues.

Plus the three optimizations the assertion machinery enables:

- **[[AssertionDrivenBacktracking]]** — inference-time retry-with-feedback.
- **[[AssertionDrivenExampleBootstrapping]]** — compile-time teacher backtracking for cleaner few-shot demos.
- **[[CounterexampleBootstrapping]]** — compile-time capture of failure-then-fix traces as negative demonstrations.

This page exists to resolve the long-standing `[[DSPyAssertions]]` forward reference carried in [[DSPyOptimization]] / [[dspy-optimization-overview]] since the DSPy *Learn* corpus closed at 13/13 on 2026-05-17. Read [[LMAssertions]] for the substance.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-customer-service-agent]] — gap-shaped receipt: the seven-tool airline [[react|ReAct]] agent over a [[Pydantic]] domain has **no** assertion gates; the source page names `dspy.Assert` (and the broader `LMAssertions` umbrella) as the natural defense against silently-invalid bookings (e.g. `flight.origin != flight.destination`, `flight.date_time > now()`).
- [[dspy-email-extraction-tutorial]] — gap-shaped receipt: the four-Signature classify-extract-summarize-action pipeline has no assertion gates; the source's Scope-Limit Gaps section explicitly cites `dspy.Assertions` as the natural defense against **prompt-injection emails** and spam-with-injected-instructions that the [[Pydantic]] typed-OutputField layer alone cannot stop.

## Tracked source

- **[[2312.13382-dspy-assertions]]** (Singhvi, Shetty, Tan, Potts, Sen, Zaharia, Khattab 2024) — the introducing paper.
