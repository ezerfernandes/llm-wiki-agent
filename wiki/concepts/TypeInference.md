---
title: "Type Inference"
type: concept
tags: [testing, fuzzing, verification, types, specification-mining, dynamic-analysis, python, software-engineering]
sources: [fuzzingbook-22-dynamic-invariants]
last_updated: 2026-06-06
---

# Type Inference

**Type inference**, in the [[SpecificationMining|specification-mining]] sense of [[fuzzingbook-22-dynamic-invariants|Ch 22]], is the recovery of a function's argument and return *types* by observing the values it is actually called with at runtime, then emitting those types as code annotations. This is a *dynamic*, execution-driven form of type inference (distinct from the compile-time type inference of statically typed languages): it learns types from runs and is therefore only as complete as the runs observed.

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] mines types in three steps: (1) trace calls with a `CallTracker` (built on `sys.settrace`, capturing each call's `(arguments, return_value)`); (2) read off each value's runtime type with `type_string(value)` (`type(value).__name__`); (3) splice the types back into the function as [[TypeHints|PEP 484 annotations]] by rewriting the function's AST with a `TypeTransformer(ast.NodeTransformer)` and unparsing it. The all-in-one `TypeAnnotator.typed_functions()` yields, e.g., `def my_sqrt(x: float) -> float`. When different calls disagree on a parameter's type, the inferred type collapses to `typing.Any` (`my_sqrt` seen with both `int` and `float`; `sum3` seen with strings *and* numbers). The chapter notes composite types are kept coarse — the type of `[3]` is `list`, not `list[int]`. Mined annotations can be fed to a static checker like [[MyPy]] to catch caller/callee type mismatches, and they sharpen [[SymbolicExecution|symbolic analysis]] by constraining the value space of each variable. The Background credits Facebook's MonkeyType and Dropbox's PyAnnotate as production tools that implement exactly this trace-and-annotate approach.

## Connections
- [[SpecificationMining]] — type inference is one of the two mining tasks in Ch 22 (the other being [[InvariantInference]]).
- [[TypeHints]] — the PEP 484 annotation format the mined types are emitted as.
- [[MyPy]] — the static checker that consumes mined annotations to flag type errors.
- [[DynamicInvariant]] — value-level invariants; `isinstance(X, int)`-style properties overlap with type mining.
- [[SymbolicExecution]] — benefits from mined types, which constrain the symbolic value space.
- [[DynamicAnalysis]] — the runtime tracing that drives the inference.

## Sources
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications."
