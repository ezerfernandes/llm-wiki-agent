---
title: "Postcondition"
type: concept
tags: [testing, fuzzing, verification, design-by-contract, software-engineering]
sources: [fuzzingbook-02-intro-testing, fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Postcondition

A **postcondition** is a condition the *callee* guarantees to hold on return, provided its [[Precondition|preconditions]] were met on entry. It is the callee-side obligation in [[DesignByContract|design-by-contract]], and in practice it doubles as a built-in [[TestOracle|test oracle]] for the function's result.

## From The Fuzzing Book — Introduction to Software Testing
[[fuzzingbook-02-intro-testing|Ch 2]] expresses `my_sqrt`'s postcondition as the property `root * root ≈ x` and checks it via [[RunTimeVerification|run-time verification]]:

```python
def my_sqrt_checked(x):
    root = my_sqrt(x)
    assertEquals(root * root, x)   # postcondition
    return root
```

The chapter is careful about what such a postcondition check guarantees: it ensures the result is correct *if* a result is produced, but it cannot guarantee that a result will be produced at all — that stronger guarantee requires symbolic verification or proofs. A well-chosen property postcondition (like √x·√x = x) is exactly what enables an [[TestOracle|oracle]] for [[RandomTesting|randomly generated]] inputs whose expected values are unknown in advance.

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] *mines* postconditions: any candidate property that mentions the special variable `return_value` and held across every observed call becomes a `@postcondition(lambda return_value, ...)`. Examples include `my_sqrt`'s `return_value >= 0`, `sum2`'s `return_value == a + b` (in all its commuted forms), and `list_length`'s `return_value == len(L)` (which the catalog can express directly). Because mined postconditions become always-on [[TestOracle|oracles]], the chapter shows they catch *regressions*: flipping `my_sqrt` to `return -approx` violates the mined `return_value >= 0` postcondition on the very first call. As with [[Precondition|preconditions]], a single observed call overspecializes the postcondition (e.g. `sum2(2, 2)` mines the bogus `return_value == a * b`), so diverse runs from a [[TestGeneration|test generator]] are needed for trustworthy results.

## Connections
- [[Precondition]] — the caller-side counterpart in a contract.
- [[DesignByContract]] — names preconditions/postconditions/invariants as mutual obligations.
- [[TestOracle]] — a postcondition is effectively a result oracle baked into the function.
- [[RunTimeVerification]] — always-on postcondition checking on every call.
- [[Assertion]] — the usual encoding of a postcondition check.
- [[PropertyBasedTesting]] — declared properties generalize per-function postconditions.
- [[DynamicInvariant]] / [[InvariantInference]] / [[SpecificationMining]] — Ch 22 *mines* postconditions from observed executions and emits them as `@postcondition` decorators.
- [[fuzzingbook-22-dynamic-invariants]] — Ch 22, where mined postconditions act as regression-catching oracles.

## Sources
- [[fuzzingbook-02-intro-testing]] — *The Fuzzing Book* Ch 2, "Introduction to Software Testing."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications" (postconditions mined from observed calls).
