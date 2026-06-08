---
title: "Hypothesis Docs — Domain and Distribution"
type: source
tags: [testing, property-based-testing, python, tooling]
date: 2026-06-05
source_file: raw/hypothesis/explanation-domain-and-distribution.md
sources: [hypothesis-domain-and-distribution]
last_updated: 2026-06-05
---

## Summary
An explanation page from the [[Hypothesis]] documentation that draws the central distinction in [[PropertyBasedTesting|property-based testing]] between a strategy's **domain** (the set of inputs it *can* generate) and its **distribution** (the probability *with which* each input is generated). Its load-bearing thesis: the user owns the **domain**, the library owns the **distribution**. The user's job is to pick the most general strategy that still satisfies the property; the engine's job — deliberately kept a private implementation detail — is to bias generation toward bug-finding.

## Key Claims
- **Domain vs distribution** are orthogonal: `lists(integers())` has a domain of *all* integer lists; the distribution decides whether small/large lists or positive/negative ints show up more often.
- **Division of responsibility**: "while users may be responsible for selecting the domain, the property-based testing library — not the user — should be responsible for selecting the distribution."
- **Choose the most-general domain** "so that it can in principle generate any edge case for which the test should pass." Over-restricting the domain risks excluding the very values that trigger bugs.
- **Don't shrink the domain for speed prematurely** — only add size limits after observing substantial slowdowns: "Far better to find bugs slowly, than not find them at all." Prefer the `phases` / `max_examples` settings for performance management over narrowing the strategy.
- **Distribution control is intentionally not a public knob** for three reasons: (1) humans over-tune for *known* bugs and under-prepare for *unknown* ones; (2) the optimal distribution depends on both codebase and the specific property; (3) keeping distribution internal lets Hypothesis improve generation without breaking public APIs.
- Users who genuinely need distribution control are pointed to alternative backends — `hypofuzz` and `crosshair`.
- The actual generator is multi-faceted and bug-discovery-optimized (not uniform or "realistic"): static strategy design, dynamic engine features, source-code analysis, and swarm testing.

## Key Quotes
> "while users may be responsible for selecting the domain, the property-based testing library — not the user — should be responsible for selecting the distribution." — the page's governing principle

> "Far better to find bugs slowly, than not find them at all." — argument against premature domain-narrowing for performance

## Connections
- [[PropertyBasedTesting]] — this page is the canonical statement of the domain/distribution split that underpins the method
- [[Hypothesis]] — the library whose design philosophy this page documents
- [[HypothesisSettings]] — `max_examples` / `phases` are the page's recommended performance levers (vs narrowing the domain)
- [[HealthCheck]] — over-restrictive domains/filters are exactly what the health-check system warns about (`filter_too_much`)
- [[Pytest]] — Hypothesis runs as a plugin on top of pytest's test functions
- [[BehavioralTesting]] — property-based tests assert invariants over behavior rather than fixed input→output pairs
- [[UnitTesting]] / [[RegressionTesting]] — PBT generalizes example-based unit tests by generating the examples
- `hypofuzz` / `crosshair` — alternative backends the page names for users who genuinely need distribution control

## Contradictions
- No contradictions with existing wiki content. Complements the prior Hypothesis source [[hypothesis-howto-suppress-healthchecks]] (run-time settings / health checks) by documenting the *design philosophy* behind input generation. The wiki's example-based testing pages ([[Pytest]], [[BehavioralTesting]], [[UnitTesting]], [[RegressionTesting]]) remain consistent — this source adds the *generative* branch without conflict.
