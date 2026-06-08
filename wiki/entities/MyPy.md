---
title: "MyPy"
type: entity
tags: [tool, static-analysis, type-checking, python, open-source, verification]
sources: [fuzzingbook-03-fuzzer, fuzzingbook-22-dynamic-invariants, fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# MyPy

**MyPy** is the de facto **static type checker** for Python (mypy-lang.org). It reads PEP 484 type annotations and flags type errors *without running the program*, catching a class of bugs at analysis time rather than during execution.

## Role in The Fuzzing Book
[[fuzzingbook-03-fuzzer|Ch 3]] presents MyPy as the [[StaticAnalysis|static-analysis]] complement to runtime [[RepresentationInvariant|`repOK()`]] checks. The example: declaring `typed_airport_codes: Dict[str, str]` lets MyPy reject `typed_airport_codes[1] = "First"` (`Invalid index type "int"`) immediately. The chapter is candid about the limits — MyPy cannot statically verify richer properties like "the code is exactly three uppercase letters" or "the tree is acyclic" — so type checking is layered with dynamic `repOK()` assertions and a good test generator. (The book itself is type-annotated and MyPy-checked.)

## From The Fuzzing Book — Mining Function Specifications
[[fuzzingbook-22-dynamic-invariants|Ch 22]] uses MyPy as the *consumer* of mined types. It runs `mypy --strict` over a generated file to show static type checking in action (MyPy flags a `my_sqrt_with_type_annotations('123')` call passing a `str` where a number is expected), then builds a `TypeAnnotator` that *mines* [[TypeHints|PEP 484 annotations]] from observed runs ([[TypeInference|type inference]]) — output that can be fed straight back into MyPy to catch caller/callee type mismatches without runtime overhead. The chapter's Background cites Facebook's MonkeyType and Dropbox's PyAnnotate as production tools doing exactly this trace-and-annotate-for-static-checking workflow.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] uses MyPy as a real-world *fuzz target* for [[ConfigurationFuzzing|configuration fuzzing]]: `OptionRunner("mypy", "foo.py")` runs the MyPy executable up to its `argparse.parse_args()` call and mines its [[OptionGrammar|option grammar]], recovering MyPy's **140+ command-line options** — by far the largest of the chapter's examples. The chapter notes this scale makes [[CombinatorialTesting|pairwise testing]] cost 20,000+ tests (`C(140,2)`), still runnable in a few hours, whereas the full configuration space is intractable. Here MyPy is fuzzed as a program, not used as a type checker.

## Connections
- [[ConfigurationFuzzing]] / [[OptionGrammar]] / [[CombinatorialTesting]] — Ch 23 mines and fuzzes MyPy's 140+ command-line options.
- [[TypeInference]] / [[SpecificationMining]] — Ch 22 mines the annotations MyPy then statically checks.
- [[TypeHints]] — the PEP 484 annotations MyPy reads.
- [[StaticAnalysis]] — MyPy is the chapter's concrete static checker.
- [[RepresentationInvariant]] / [[Assertion]] — the dynamic checks MyPy complements but cannot replace for rich invariants.
- [[Python]] — the language MyPy type-checks.
- [[Fuzzing]] — the dynamic counterpart in the chapter's layered-defense argument.
- [[fuzzingbook-03-fuzzer|Ch 3]] — demonstrates MyPy alongside `repOK()`.

## Sources
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3, "Fuzzing: Breaking Things with Random Inputs."
- [[fuzzingbook-22-dynamic-invariants]] — *The Fuzzing Book* Ch 22, "Mining Function Specifications" (static checking of mined type annotations).
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (MyPy's 140+ options mined and fuzzed).
