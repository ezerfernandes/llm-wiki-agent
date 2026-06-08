---
title: "Invariant Inference"
type: concept
tags: [testing, fuzzing, verification, specification-mining, dynamic-analysis, software-engineering]
sources: [fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Invariant Inference

**Invariant inference** is the procedure that turns observed executions into [[DynamicInvariant|dynamic invariants]]: it takes a catalog of *candidate* properties and a record of variable values across many calls, and returns the subset of properties that held on every call. It is the inference engine inside [[SpecificationMining|specification mining]] tools such as [[Daikon]].

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] implements invariant inference with a small pipeline of helpers. `INVARIANT_PROPERTIES` is a list of property templates over metavariables `X, Y, Z` (any upper-case identifier). For each property:

- `metavars(prop)` extracts its metavariables by parsing the property and visiting `ast.Name` nodes that are upper-case.
- `instantiate_prop(prop, var_names)` substitutes concrete argument names for the metavariables (e.g. `"X > Y"` with `['a','b']` → `'a > b'`).
- `prop_function(prop)` compiles the property into a `lambda` via `eval` for direct evaluation.
- `true_property_instantiations(prop, vars_and_values)` tries the property over all `itertools.permutations` of the observed `(name, value)` pairs and returns those that evaluate to `True`.

`InvariantTracker.invariants()` then computes, per call, the set of satisfied `(property, var_names)` instantiations and **intersects** them across all calls — so the result is exactly the properties that always held. The special name `return_value` carries the result. The crucial consequence is *monotonic shrinkage*: more (and more diverse) calls can only remove invariants, never add them, so a single call overspecializes and a good [[TestGeneration|test generator]] is needed to converge on the true invariants. The catalog is deliberately small; [[Daikon]] uses a far richer pattern catalog plus implication elimination and statistical confidence.

## Connections
- [[DynamicInvariant]] — the artifact this inference procedure produces.
- [[SpecificationMining]] — invariant inference is the engine inside a specification miner.
- [[TypeInference]] — the sibling task that mines types rather than value properties (some properties here, like `isinstance(X, int)`, overlap).
- [[Daikon]] — the canonical, richer implementation of this inference.
- [[Precondition]] / [[Postcondition]] — inferred properties are split into these by whether they mention `return_value`.
- [[TestGeneration]] / [[Fuzzing]] — needed to supply diverse runs so inference converges past overspecialization.

## Sources
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications."
