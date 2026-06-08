---
title: "Property-Based Testing"
type: concept
tags: [testing, python, property-based-testing, methodology]
sources: [hypothesis-howto-suppress-healthchecks, hypothesis-domain-and-distribution, hypothesis-example-count, hypothesis-howto-type-strategies, fuzzingbook-02-intro-testing]
last_updated: 2026-06-06
---

# Property-Based Testing

**Property-based testing** is a testing methodology in which, instead of asserting behavior on a handful of hand-picked examples (as in classic example-based [[UnitTesting]]), you state a general *property* that should hold for all valid inputs and let the test framework generate many inputs automatically to try to falsify it. When a counterexample is found, good frameworks **[[Shrinking|shrink]]** it to a minimal reproducing case (and replay that minimal case once to confirm it isn't flaky).

In the [[Python]] ecosystem the dominant implementation is [[Hypothesis]], which exposes input *strategies* (objects of type [[SearchStrategy]]`[T]`) and a `@given` decorator and runs on top of [[Pytest]].

## Why it matters
- Explores a far larger input space than fixed examples, surfacing edge cases (boundary values, empty/huge inputs, unusual encodings) developers rarely enumerate by hand.
- Complements rather than replaces example-based [[UnitTesting]] and [[RegressionTesting]].
- Generation quality is something the framework actively monitors — e.g. Hypothesis emits [[HealthCheck]] warnings (such as `filter_too_much`) when too many generated examples are discarded by filters, which undermines test effectiveness.
- **Run count is not fixed at `max_examples`** — Hypothesis runs *fewer* times if the search space is exhausted, *more* if examples are retried (discarded by `assume()` / `.filter()`, or too large → `HealthCheck.data_too_large`), and a variable count once a failure triggers the [[Shrinking|shrink]] / explain phases plus a flakiness replay ([[hypothesis-example-count]]).

## Domain vs Distribution
A central design distinction (per [[hypothesis-domain-and-distribution]]):

- **Domain** — the complete set of inputs a *strategy* can produce (e.g. `lists(integers())` → all integer lists). **The user owns the domain.**
- **Distribution** — the probability with which each domain element is actually generated (small vs large lists, positive vs negative ints). **The library owns the distribution.**

Guidance that follows from the split:
- **Pick the most-general strategy** that still satisfies the property, so any pass-eligible edge case is in principle reachable. Over-narrowing the domain hides bugs — *"Far better to find bugs slowly, than not find them at all."*
- **Don't shrink the domain for speed prematurely** — use [[HypothesisSettings|settings]] like `max_examples` / `phases` for performance instead of restricting the strategy.
- **Distribution is deliberately not a public knob** — humans over-tune for known bugs, the optimal distribution is codebase- and property-dependent, and keeping it internal lets the engine improve without breaking APIs. Users needing distribution control are steered to other backends (`hypofuzz`, `crosshair`).

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] of *The Fuzzing Book* shows the seed idea of property-based testing without yet naming it: the invariant √x · √x = x is a *property [[TestOracle|oracle]]* that holds for all valid inputs, so it can be checked over thousands of generated values (`for n in range(1, 1000)` and over `random.random()` inputs) without knowing the expected answer for each. The Shellsort exercise generalizes the pattern with two predicates as the oracle — the result must be `is_sorted` *and* an `is_permutation` of the input. This property-over-generated-inputs structure is exactly what [[Hypothesis]] systematizes with `@given` and [[SearchStrategy|strategies]]; the chapter's caveat about [[RandomTesting|random]] generation missing rare special values is the gap that strategy-driven generation and [[Shrinking|shrinking]] address.

## Connections
- [[Hypothesis]] — the leading Python property-based testing library.
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2; the property-oracle seed idea (√x·√x = x) behind property-based testing.
- [[TestOracle]] — property-based testing is built on property (invariant) oracles.
- [[SearchStrategy]] — the typed strategy object that defines the input domain.
- [[Shrinking]] — the minimization (and flakiness-replay) step that makes counterexamples readable.
- [[HealthCheck]] — guards the quality/effectiveness of generated examples.
- [[HypothesisSettings]] — tunes how many examples are generated and how the run behaves.
- [[Pytest]] — common host framework.
- [[UnitTesting]] — the example-based approach this complements.
- [[Fuzzing]] — the complementary coverage-guided input-generation strategy; [[Hypothesis]]'s `fuzz_one_input` lets an external fuzzer drive a property test (see [[hypothesis-howto-external-fuzzers]]).

## Sources
- [[hypothesis-howto-suppress-healthchecks]] — context on health checks that protect generated-example quality.
- [[hypothesis-domain-and-distribution]] — the domain (user-owned) vs distribution (library-owned) design split.
- [[hypothesis-example-count]] — how many times a test actually runs (generation, retries, shrink/explain, flakiness replay).
- [[hypothesis-howto-type-strategies]] — typing strategies as `SearchStrategy[T]`.
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2: the property-oracle (invariant-over-generated-inputs) idea underpinning property-based testing.
