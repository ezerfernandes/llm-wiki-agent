---
title: "The Fuzzing Book Ch 24 — Fuzzing APIs"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, api-fuzzing, function-testing, grammar, generators, oracles, urlparse, python]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-24-api-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Fuzzing APIs

## Summary
Chapter 24 (Part V, "Domain-Specific Fuzzing") shifts the target of fuzzing from *system input* (bytes fed to a whole program through its input channels) to the *API level* — exercising a library's individual functions directly with generated arguments and **synthesized function-call code**. The central technique is to write a [[Grammar|grammar]] whose terminals are snippets of program code (e.g. `urlparse("<url>")`), so a [[GrammarFuzzer|`GrammarFuzzer`]] produces *callable strings* that `eval`/`exec` runs as a test — decoupling test generation from test execution and even letting the same grammar emit calls in another language (a C variant is shown). It then builds reusable [[APIFuzzing|grammar constructors]] for argument values — `INT_GRAMMAR`, `FLOAT_GRAMMAR`, `ASCII_STRING_GRAMMAR`, range-bounded `int_grammar_with_range`/`float_grammar_with_range`, and the composite `list_grammar` — that plug into any call. To check results, the chapter synthesizes [[TestOracle|oracles]] using the **generator functions** of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] (e.g. asserting `urlparse('<url>').geturl() == '<url>'`, where the matched `<url>` equality is enforced by a `post` function). It builds on [[fuzzingbook-09-grammars|Ch 9]] (grammars), [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] (generators), and [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] (probabilities), and sets up [[fuzzingbook-25-carver|Ch 25]] (Carver), which *automatically records* real call arguments from executions instead of writing grammars by hand.

## Key Concepts
- **[[APIFuzzing|API / function-level fuzzing]]** — rather than feeding bytes to a whole program, generate *calls* to the function(s) under test. For an interpreted language this is "pretty straight-forward": build a grammar that produces call snippets and run them. Two execution styles are shown: a *scaffold* (generate input, immediately feed it to the function — `for url in url_fuzzer: urlparse(url)`) and the preferred *code synthesis* (generate the string `urlparse('http://www.cispa.de/')` and `eval`/`exec` it later — decoupling generation from execution).
- **Call-synthesis grammar** — `URLPARSE_GRAMMAR` has `"<call>": ['urlparse("<url>")']`, then `.update(URL_GRAMMAR)` imports the URL grammar from [[fuzzingbook-09-grammars|Ch 9]] and sets `<start>` to `<call>`. A `GrammarFuzzer` over it yields executable test strings; the `do_call(call_string)` helper prints the call, `eval`s it, and prints the result. The same idea retargets languages: `URLPARSE_C_GRAMMAR` wraps calls in a generated C `void test() { ... }` function with `#include "urlparse.h"`.
- **[[CallSequenceFuzzing|Call sequences]]** — the C grammar's recursive rule `"<calls>": ["<call>", "<calls><call>"]` emits *many* calls in one synthesized function, the seed of generating call *sequences* that exercise an API repeatedly (and, with state-building, build up objects) — a thread continued automatically by [[fuzzingbook-25-carver|Ch 25]].
- **Synthesizing [[TestOracle|oracles]]** — generic execution only catches crashes/exceptions; a real test needs an oracle. Because a context-free grammar cannot express the equality of two `<url>` occurrences, the chapter uses a [[GeneratorGrammar|generator-grammar]] `post` function (from [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]) to force them equal: `URLPARSE_ORACLE_GRAMMAR` produces `assert urlparse('<url>').geturl() == '<url>'`. A richer variant asserts `result.scheme`/`netloc`/`path`/`query` against the generated components. A pure-Python alternative (`fuzzed_url_element`) generates each element via a fuzzer and writes a plain unit-test assertion — easier to read, but it loses systematic [[GrammarCoverage|coverage]] and probabilistic guidance and only targets Python.
- **Data-type grammar constructors** — reusable grammars for basic argument types: `INT_GRAMMAR` (from `INT_EBNF_GRAMMAR` via `convert_ebnf_grammar`), `FLOAT_GRAMMAR` (with a probabilistic `inf`/`NaN` and `e<int>` exponent), `ASCII_STRING_GRAMMAR` (quoted ASCII chars). Range variants attach a generator `pre` function via `set_opts(...)`: `int_grammar_with_range(start, end)` plugs `random.randint(start, end)` into `<_int>`; `float_grammar_with_range` does the analogue. These are meant for `ProbabilisticGeneratorGrammarFuzzer` (the producer that honors both `prob` and `pre`/`post`).
- **Composite data** — `list_grammar(object_grammar)` instantiates `LIST_EBNF_GRAMMAR` with the objects of any element grammar, producing `[obj, obj, ...]` strings (`eval`-able to real Python lists). Composing constructors lets you build arbitrary argument structures (lists of ints, lists of strings, lists of ranged floats); dicts/sets follow the same pattern.

## Key Claims
- Generating inputs that go *directly into individual functions* gains "flexibility and speed" over whole-program system fuzzing.
- Synthesizing call *code* (a string that is `eval`/`exec`'d) rather than running the function inline *decouples* test generation from execution — tests can be re-run later, saved, or emitted for a different language (the C example).
- A pure context-free grammar cannot enforce that two occurrences of a value (e.g. the input URL and the URL in an assertion) are equal; a generator-function `post` annotation supplies that equality, enabling oracle synthesis.
- Range-bounded numeric arguments are produced not by enumerating the grammar but by attaching a `pre` generator (`random.randint`/`random.random`) that overrides the expansion with an in-range value.
- The grammar route preserves the ability to systematically cover URL elements (via [[GrammarCoverage|`GrammarCoverageFuzzer`]]) and to bias generation (via [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]]) and to target arbitrary languages — advantages a hand-written Python unit test loses.
- **Lesson learned:** API-level fuzzing "can be much faster than fuzzing at the system level, but brings the risk of false alarms by violating implicit preconditions" — calling a function with arguments it would never legitimately receive can report bugs that are not real.

## Key Quotes
> "We can also generate inputs that go directly into individual functions, gaining flexibility and speed in the process." — the chapter's premise.

> "Rather than generating inputs and immediately feeding this input into a function, we _synthesize code_ instead that invokes functions with a given input." — the decoupling argument behind code synthesis.

> "Fuzzing at the API level can be much faster than fuzzing at the system level, but brings the risk of false alarms by violating implicit preconditions." — the headline trade-off (Lessons Learned).

## Connections
- [[APIFuzzing]] — the chapter's headline technique: synthesizing function-call code from grammars and running it.
- [[CallSequenceFuzzing]] — generating sequences of calls (the C grammar's `<calls>` recursion; bridged to [[fuzzingbook-25-carver|Ch 25]]).
- [[TestOracle]] — synthesized via generator `post` functions to check `urlparse` results, not just catch crashes.
- [[GeneratorGrammar]] / [[GeneratorGrammarFuzzer]] — supply the `pre`/`post` annotations used both for oracle equalities and for range-bounded argument generation.
- [[ProbabilisticGrammarFuzzer]] / [[ProbabilisticGrammar]] — the `inf`/`NaN`/empty-string probabilities in `FLOAT_GRAMMAR`/`ASCII_STRING_GRAMMAR`; `ProbabilisticGeneratorGrammarFuzzer` is the recommended producer.
- [[Grammar]] / [[GrammarFuzzer]] / [[GrammarBasedFuzzing]] — reuses `URL_GRAMMAR`, `is_valid_grammar`, `extend_grammar`, `opts`, `set_opts`, `convert_ebnf_grammar`, `crange`, `START_SYMBOL`.
- [[EBNF]] — the data-type grammars are written in EBNF (`(-)?`, `<digit>*`, `(.<digit>+)?`) then converted to BNF.
- [[GrammarCoverage]] — the systematic-coverage advantage the grammar route retains over a hand-written unit test.
- [[API]] — the interface being exercised at the function level.
- [[Runner]] — the book's harness abstraction; this chapter instead uses ad-hoc `eval`/`exec` (`do_call`), but a `Runner`/`FunctionRunner` could wrap the synthesized calls.
- [[Fuzzing]] / [[Testing]] / [[UnitTesting]] — API fuzzing as a way to auto-generate unit tests for individual functions.
- [[Hypothesis]] — the Background section cites it as the leading Python library for the same idea (generator-function-based API/data-structure testing), tracing to QuickCheck.
- [[AndreasZeller]] — lead author; [[CISPA]] — publisher.
- [[fuzzingbook-09-grammars|Ch 9]] — prerequisite; supplies `URL_GRAMMAR` and the grammar machinery.
- [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] — prerequisite; supplies generator functions and `GeneratorGrammarFuzzer`.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] — prerequisite; supplies probabilities and `ProbabilisticGrammarFuzzer`.
- [[fuzzingbook-25-carver|Ch 25]] — "Next Steps": carving automatically records real call args/sequences, so grammars need not be written by hand.

## Contradictions
- None identified.
