---
title: "PGGCFuzzer"
type: concept
tags: [fuzzing, grammar, generators, probability, coverage, testing, class-hierarchy, multiple-inheritance, syntactic-fuzzing, python]
sources: [fuzzingbook-14-generator-grammar-fuzzer]
last_updated: 2026-06-06
---

# PGGCFuzzer

**`PGGCFuzzer`** (Probabilistic Generator Grammar Coverage Fuzzer) is *The Fuzzing Book*'s capstone grammar fuzzer — "the one grammar-based fuzzer that supports all fuzzingbook features." It combines, by **multiple inheritance**, every grammar-fuzzing axis developed across Part III: the efficient tree-based [[GrammarFuzzer|`GrammarFuzzer`]] ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]), [[GrammarCoverage|coverage-driven]] selection ([[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]], [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]), [[ProbabilisticGrammar|probability]]-weighted selection ([[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]], [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]), and [[GeneratorGrammar|generator]] functions ([[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]], [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]]).

```python
class PGGCFuzzer(ProbabilisticGeneratorGrammarCoverageFuzzer):
    """The one grammar-based fuzzer that supports all fuzzingbook features"""
    pass
```

## How the combination is built
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] assembles `PGGCFuzzer` in stages, all relying on the fact that the fuzzers extend `GrammarFuzzer` along *different* axes:
1. **`ProbabilisticGeneratorGrammarFuzzer`** = `GeneratorGrammarFuzzer` + `ProbabilisticGrammarFuzzer`. `supported_opts()` is the union of both parents' opts; the constructor calls both superclass `__init__`s (passing `replacement_attempts` to the generator side). `inheritance_conflicts()` is used to find which methods both define.
2. **`ProbabilisticGeneratorGrammarCoverageFuzzer`** = `GeneratorGrammarFuzzer` + `ProbabilisticGrammarCoverageFuzzer`. The hard part is coverage: during expansion the fuzzer may *generate* (and record) coverage for expansions it later **drops** when a `post` function returns `False`. It resolves this by **rebuilding coverage from the final tree** — `fuzz_tree()` saves the original `covered_expansions`, restores it after building, then walks the produced tree with `add_tree_coverage()` to re-add only the surviving coverage; `restart_expansion()` likewise restores coverage when starting from scratch.
3. **`PGGCFuzzer`** is the trivial alias subclass of the above.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] mints `PGGCFuzzer` in its "All Together" section as the demonstration that the four independently-developed grammar-fuzzing features compose cleanly through Python multiple inheritance. The chapter notes this echoes `ProbabilisticGrammarCoverageFuzzer` (Ch 13 exercises) and is mainly possible because grammars are defined and used in an all-Python environment. A worked example tunes `CONSTRAINED_VAR_GRAMMAR` with `opts(prob=0.9)` to favor long identifiers while still enforcing the generator-based def/use constraint and accumulating expansion coverage. The only shortcoming the authors concede is the unwieldy name — hence the short alias.

## Connections
- [[GeneratorGrammarFuzzer]] — supplies generator (`pre`/`post`/`order`) support.
- [[ProbabilisticGrammarFuzzer]] — supplies probability-weighted expansion choice.
- [[GrammarCoverageFuzzer]] — supplies coverage-driven expansion choice (whose coverage is rebuilt from the final tree).
- [[GrammarFuzzer]] — the shared base class all four axes extend.
- [[GeneratorGrammar]] / [[ProbabilisticGrammar]] — the annotated grammars it can consume simultaneously.
- [[GrammarCoverage]] — the adequacy criterion it tracks (carefully, post-repair).
- [[DerivationTree]] — the tree it builds; `add_tree_coverage()` walks it to recompute coverage.
- [[GrammarBasedFuzzing]] — the technique it realizes in its most complete form.
- [[SemanticConstraint]] — still enforced via its generator half.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] / [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] / [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] — supply the three reused fuzzers.
- [[fuzzingbook-14-generator-grammar-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators."
