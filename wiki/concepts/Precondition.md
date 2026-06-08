---
title: "Precondition"
type: concept
tags: [testing, fuzzing, verification, design-by-contract, software-engineering]
sources: [fuzzingbook-02-intro-testing, fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Precondition

A **precondition** is a condition the *caller* must guarantee to hold on entry to a function for that function to behave correctly. It is the caller-side obligation in [[DesignByContract|design-by-contract]] (paired with a [[Postcondition|postcondition]], the callee's obligation). Violating a precondition means the function is being used outside its specification, and any resulting misbehavior is the caller's fault, not the function's.

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] surfaces preconditions through the running `my_sqrt(x)` example, which has unstated preconditions: `x` must be non-negative and finite. Violating them is catastrophic — `my_sqrt(-1)` and `my_sqrt(float('inf'))` loop forever, and `my_sqrt(0)` divides by zero. The chapter's fix makes the precondition *explicit and checked* with an [[Assertion|assert]]:

```python
def my_sqrt_fixed(x):
    assert 0 <= x
    if x == 0:
        return 0
    return my_sqrt(x)
```

The chapter ties preconditions directly to fuzzing: distinguishing *function input* from third-party *system input*, it argues robust code must validate external input so internal functions are only ever called within their preconditions — and crucially, that to call a function with *generated* values "we have to *know* its precise preconditions." Precondition awareness is therefore a prerequisite for sound [[TestGeneration|test generation]] (Exercise 3 shows `quadratic_solver` violating `my_sqrt_fixed`'s precondition for certain coefficients).

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] turns preconditions from hand-written caller obligations into *mined* ones. By tracing a function's calls and keeping every candidate property over the arguments that held across all runs (see [[DynamicInvariant]] / [[InvariantInference]]), the `InvariantAnnotator` emits the surviving non-`return_value` properties as `@precondition(lambda ...)` decorators — e.g. `my_sqrt` mines `@precondition(lambda x: x > 0)`. The chapter warns these mined preconditions *overspecialize* to the observed inputs (a lone `sum2(2, 2)` mines the bogus precondition `a == b`), so they only become trustworthy with diverse runs from a [[TestGeneration|test generator]]. This is the dynamic, learned mirror of the chapter's `@precondition` runtime-check decorator and of the hand-written precondition in [[fuzzingbook-02-intro-testing|Ch 2]].

## Connections
- [[Postcondition]] — the callee-side counterpart in a contract.
- [[DesignByContract]] — the framework that names preconditions/postconditions/invariants as mutual obligations.
- [[Assertion]] — the usual way to make a precondition explicit and checked.
- [[TestGeneration]] / [[Fuzzing]] — generated inputs must respect (or deliberately violate, at the system level) a function's preconditions.
- [[RunTimeVerification]] — precondition checks are one half of always-on runtime contract checking.
- [[DynamicInvariant]] / [[InvariantInference]] / [[SpecificationMining]] — Ch 22 *mines* preconditions from observed executions.
- [[fuzzingbook-22-dynamic-invariants]] — Ch 22, where preconditions are mined and emitted as `@precondition` decorators.

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications" (preconditions mined from observed calls).
