---
title: "Run-Time Verification"
type: concept
tags: [testing, fuzzing, quality, verification, software-engineering]
sources: [fuzzingbook-02-intro-testing, fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Run-Time Verification

**Run-time verification** moves the [[TestOracle|test oracle]] *inside* the implementation, so that correctness is checked on *every* invocation during normal execution rather than only in a separate test suite. Each call self-validates via embedded [[Assertion|assertions]] (typically [[Postcondition|postconditions]] on the result), making it a runtime form of [[DesignByContract|design-by-contract]].

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] introduces run-time verification by wrapping the running example:

```python
def my_sqrt_checked(x):
    root = my_sqrt(x)
    assertEquals(root * root, x)
    return root
```

Now "*each and every* invocation of `my_sqrt()` will be automatically checked." The chapter states two assumptions and one hard limitation:

- **Formulability** — you must be able to express the check; concrete value comparisons are always possible, but abstract properties (possibly spanning much of the program state) can be hard to formulate.
- **Affordability** — the check must be cheap enough; verifying a large data structure after every small operation can be prohibitively expensive, which is why run-time checks "will typically be disabled during production, trading reliability for efficiency."
- **Limitation** — run-time checks guarantee correctness *only if there is a result* to check; they do **not** guarantee that a result will ever be produced. This is the key gap versus *symbolic verification techniques* and *program proofs*, which can also guarantee termination/existence of a result — at much higher, often manual, effort.

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] supplies the *checks* that run-time verification enforces — and supplies them automatically. Its `@precondition`/`@postcondition` decorators wrap a function so each call self-validates via embedded [[Assertion|assertions]] (the canonical run-time-verification mechanism), and its [[SpecificationMining|specification miner]] *infers* those checks from observed runs as [[DynamicInvariant|dynamic invariants]] rather than requiring them to be hand-written. The chapter's regression demo is run-time verification in action: an annotated `my_sqrt` rejects a negative argument (whose property was never observed) on every call, and a code change that violates a mined postcondition is caught immediately. The Ch 2 caveats still apply — mined run-time checks must be formulable and affordable, and are typically disabled in production.

## Connections
- [[TestOracle]] — run-time verification is an oracle embedded in production code paths.
- [[Assertion]] — the mechanism that encodes the embedded check.
- [[Postcondition]] / [[DesignByContract]] — run-time verification is essentially always-on postcondition checking.
- [[Precondition]] — embedded precondition checks reject illegal inputs early (e.g. `assert 0 <= x`).
- [[InvarianceTesting]] — runtime invariant checks are a related always-on verification style.
- [[Fuzzing]] — runtime checks act as oracles that turn silent corruption into observable failures during fuzzing.
- [[DynamicInvariant]] / [[SpecificationMining]] — Ch 22 *mines* the runtime checks (pre-/postconditions) from observed executions.
- [[fuzzingbook-22-dynamic-invariants]] — Ch 22, which builds the `@precondition`/`@postcondition` decorators and mines their checks.

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications" (mined, always-on runtime contract checks).
