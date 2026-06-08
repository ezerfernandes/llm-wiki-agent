---
title: "Call Sequence Fuzzing"
type: concept
tags: [fuzzing, testing, api-fuzzing, call-sequence, stateful-testing, grammar, code-synthesis]
sources: [fuzzingbook-24-api-fuzzer, fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Call Sequence Fuzzing

**Call sequence fuzzing** generates a *series* of function/method calls — not just a single call — to test an API. It is the natural extension of [[APIFuzzing|API fuzzing]] for code where one call alone is not interesting: many functions are only meaningful in context (e.g. you must `open()` before you `read()`, `insert()` before `query()`), so the test of interest is a *sequence* that builds up state and then probes it.

## In The Fuzzing Book Ch 24
[[fuzzingbook-24-api-fuzzer|Ch 24]] introduces the building block rather than a full stateful-fuzzing engine. Because synthesized calls are just *code strings* produced by a [[Grammar|grammar]], a recursive rule emits arbitrarily many of them in one synthesized unit. The C example makes this explicit:

```python
URLPARSE_C_GRAMMAR = {
    "<cfunction>": ["void test() {\n<calls>}\n"],
    "<calls>": ["<call>", "<calls><call>"],          # one or more calls
    "<call>": ['    urlparse("<url>");\n'],
}
```

Each derivation of `<calls>` produces a different-length batch of `urlparse(...)` calls wrapped in a generated test function. With distinct functions and shared objects, the same recursion would let a grammar build up an object's state across calls.

The chapter's "Lessons Learned" caveat applies with extra force to sequences: arbitrary call orders can violate an API's **implicit preconditions** (e.g. reading a closed handle), producing *false alarms* rather than real bugs.

## Relationship to Carver (Ch 25)
Hand-writing grammars for realistic call *sequences* is laborious, which motivates [[fuzzingbook-25-carver|Ch 25]] ([[TestCarving|carving]]): instead of authoring sequences, the [[Carver|`CallCarver`]] **records actual function calls and arguments** from real program executions, and [[APIGrammarMining|`CallGrammarMiner`]] turns them into grammars — automatically yielding call sequences that already invoke functions in valid application contexts.

## Connections
- [[APIFuzzing]] — the single-call technique this generalizes.
- [[Grammar]] / [[GrammarBasedFuzzing]] — recursive call rules (`<calls> ::= <call> | <calls><call>`) generate sequences.
- [[TestOracle]] — sequences still need oracles to judge the resulting state.
- [[Fuzzing]] — call-sequence fuzzing is the stateful, API-level variant.
- [[fuzzingbook-24-api-fuzzer|Ch 24]] — introduces the call-sequence building block.
- [[fuzzingbook-25-carver|Ch 25]] — automatically carves real call sequences from executions.

## Sources
- [[fuzzingbook-24-api-fuzzer]] — *The Fuzzing Book* Ch 24, "Fuzzing APIs."
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests" (carves real call sequences from executions).
