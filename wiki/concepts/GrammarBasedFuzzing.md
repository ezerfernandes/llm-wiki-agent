---
title: "Grammar-Based Fuzzing"
type: concept
tags: [fuzzing, grammar, context-free-grammar, testing, security, syntactic-fuzzing]
sources: [fuzzingbook-09-grammars, fuzzingbook-10-grammar-fuzzer, fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-12-parser, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-17-fuzzing-with-constraints, fuzzingbook-18-grammar-miner]
last_updated: 2026-06-06
---

# Grammar-Based Fuzzing

**Grammar-based fuzzing** generates test inputs by *expanding a [[ContextFreeGrammar|grammar]]* that specifies the target program's input language, rather than by emitting random bytes ([[fuzzingbook-03-fuzzer|blackbox random fuzzing]]) or mutating seeds ([[MutationBasedFuzzing|mutation-based fuzzing]]). Because every produced string is derived from the grammar, the inputs are **syntactically valid by construction** — so they get past the program's parser and exercise deeper logic, which is decisive for complex/structured input formats. This is the "syntactic fuzzing" branch of the field (Part III of *The Fuzzing Book*) and the foundation for configuration, API, and GUI fuzzing later in the book.

A grammar-based *producer* starts at the start symbol and repeatedly replaces a [[Nonterminal|nonterminal]] with a randomly chosen [[ProductionRule|expansion alternative]] until only [[Terminal|terminals]] remain.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] founds this technique. It introduces the [[Grammar|`Grammar`]] data structure and the naive producer `simple_grammar_fuzzer()`, which expands a grammar by string rewriting with a `max_nonterminals` growth cap and a `max_expansion_trials` retry bound (raising `ExpansionError` on failure). The chapter demonstrates it on `EXPR_GRAMMAR`, `CGI_GRAMMAR`, and `URL_GRAMMAR`, and is candid that the naive producer is inefficient and can fail or grow without bound. It also shows two complementary uses: feeding grammar-produced (always-valid) inputs as **seeds** into the [[MutationBasedFuzzing|mutation fuzzer]] to probe valid/invalid boundaries, and using [[EBNF]] shortcuts plus character classes to write grammars more easily. The efficient, growth-bounded successor — the [[DerivationTree|derivation-tree]]-based `GrammarFuzzer` — arrives in [[fuzzingbook-10-grammar-fuzzer|Ch 10]], and is refined with [[fuzzingbook-11-grammar-coverage-fuzzer|coverage (Ch 11)]], [[fuzzingbook-13-probabilistic-grammar-fuzzer|probabilities (Ch 13)]], [[fuzzingbook-14-generator-grammar-fuzzer|generators (Ch 14)]], and [[fuzzingbook-17-fuzzing-with-constraints|constraints (Ch 17)]]. The chapter's `Background` notes real-world grammar fuzzers — [[CSmith]] (C compilers), LangFuzz, Grammarinator, and Domato (browsers) — that have found thousands of bugs.

## From The Fuzzing Book — Efficient Grammar Fuzzing
[[fuzzingbook-10-grammar-fuzzer|Ch 10]] makes the technique *practical*. It replaces the naive string-rewriting producer with the [[DerivationTree|derivation-tree]]-based [[GrammarFuzzer|`GrammarFuzzer`]], which expands a tree in place (fast) and uses [[ExpansionCost|symbol/expansion cost]] to grow then close trees in a three-phase strategy. This fixes both core weaknesses of the Ch 9 producer — quadratic slowdown and uncontrolled/infinite growth — so grammar fuzzing terminates with small, controllable inputs even on left-recursive grammars like `expr_grammar`. `GrammarFuzzer` becomes the base class that the coverage, probabilistic, generator, and constraint variants all subclass, cementing grammar-based fuzzing as the hub of Part III.

## From The Fuzzing Book — Grammar Coverage
[[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] adds *systematic* selection to grammar-based fuzzing: rather than expanding alternatives uniformly at random, [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] prefers expansions that yield new [[GrammarCoverage|grammar coverage]], steering toward variety so every production is exercised at least once. It also introduces [[ContextCoverage|coverage in context]] (`duplicate_context()`) to cover a reused symbol per-occurrence, and shows that high grammar coverage strongly predicts high [[Coverage|code coverage]]. This makes coverage-aware production the recommended default for the technique.

## From The Fuzzing Book — Parsing Inputs
[[fuzzingbook-12-parser|Ch 12]] closes the loop from *generation* back to *ingestion*: instead of only producing strings from a grammar, it [[Parser|parses]] existing valid seed inputs into [[DerivationTree|derivation trees]] so their subtrees can be mutated, crossed over, and recombined into new valid inputs. This is decisive when a hand-written grammar under-specifies a format (the chapter's CSV example, where a plain `GrammarFuzzer` produces almost no valid `car`/`van` rows) — real seeds carry structure the grammar alone misses. It contributes the [[ParsingExpressionGrammar|`PEGParser`]] (fast, ordered-choice) and the [[EarleyParser|`EarleyParser`]] (any CFG, all parses), whose output feeds directly into the seed-recombination fuzzer of [[fuzzingbook-13-probabilistic-grammar-fuzzer|the next chapters]] and the grammar miner of [[fuzzingbook-18-grammar-miner|Ch 18]].

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] adds a *distributional* control axis to grammar production. Where [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] makes expansion choice *systematic*, Ch 13 makes it *weighted*: a [[ProbabilisticGrammar|probabilistic grammar]] annotates expansions with `opts(prob=X)`, and the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] (overloading only `choose_node_expansion()` on the [[GrammarFuzzer|`GrammarFuzzer`]] base) picks alternatives by weight. This enables [[DirectedFuzzing|directed fuzzing]] — steering tests toward changed/critical code or, by *inverting* probabilities, toward rarely-used (often buggier) features — and the probabilities can be [[GrammarMining|learned]] from a corpus by parsing it (with the [[fuzzingbook-12-parser|Ch 12]] [[EarleyParser|`EarleyParser`]]) and counting expansions. The motivating example uses [[BenfordsLaw|Benford's law]] to produce (and detect) "natural"-looking numbers, cementing grammar production as a tunable input distribution rather than just a validity generator.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] adds a *computational* axis: it attaches Python functions to expansions ([[GeneratorGrammar|generator grammars]], via `opts(pre=...)`/`opts(post=...)`) so that values are produced, checked, or repaired by code rather than only expanded syntactically. This lets grammar fuzzing satisfy [[SemanticConstraint|semantic constraints]] a [[ContextFreeGrammar|context-free grammar]] cannot express — checksums ([[LuhnAlgorithm|Luhn]]-valid credit cards), in-range integers, matched XML tags, and define-before-use dependencies. The [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]] (another [[GrammarFuzzer|`GrammarFuzzer`]] subclass) interprets these annotations, and the chapter folds generators together with the coverage and probabilistic variants by *multiple inheritance* into [[PGGCFuzzer|`PGGCFuzzer`]] — "the one grammar-based fuzzer that supports all fuzzingbook features." This is the *imperative* route to semantic validity, complementary to the *declarative* constraints of [[fuzzingbook-17-fuzzing-with-constraints|Ch 17]].

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] *fuses* grammar-based fuzzing with [[GreyboxFuzzing|coverage-guided greybox fuzzing]], closing Part III. Until now grammars were used in a *black-box* way (generate inputs regardless of the program); Ch 15 makes grammar mutation [[CoverageGuidedFuzzing|coverage-guided]] and adds structure-awareness to mutation along three rungs: [[DictionaryMutation|dictionary insertion]] (`DictMutator`), [[FragmentBasedFuzzing|fragment recombination]] ([[Parser|parse]] seeds into [[DerivationTree|subtrees]], swap/delete subtrees of the same symbol — `FragmentMutator`/`LangFuzzer`, the [[LangFuzz]] technique), and [[RegionMutation|region-based mutation]] (label byte regions of even *unparsable* seeds via the [[EarleyParser|Earley]] chart — `RegionMutator`, the [[AFLSmart]] technique). These plug into the [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]], optionally with a [[DegreeOfValidity|validity]]-weighted `AFLSmartSchedule`. The chapter's takeaway: structure-aware mutation yields *more valid* inputs but byte-level mutation often yields *more coverage*, so the strongest fuzzer stacks both.

## From The Fuzzing Book — Fuzzing with Constraints
[[fuzzingbook-17-fuzzing-with-constraints|Ch 17]] opens Part IV (Semantic Fuzzing) by adding a *declarative semantic* axis on top of grammar-based fuzzing. Grammar-based fuzzers produce *syntactically* valid inputs; [[ISLa]] pairs the same [[ContextFreeGrammar|grammar]] with declared [[SemanticConstraint|constraints]] (lengths, value ranges, checksums, matched XML tags, define-before-use) and has an [[SMTSolver|SMT solver]] satisfy them, so produced inputs are also *semantically* valid. This is the [[ConstraintBasedFuzzing|constraint-based]] / declarative counterpart to the imperative [[GeneratorGrammar|generator grammars]] of [[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] — portable, composable, and usable as both fuzzer and checker — and it sets up the [[fuzzingbook-21-symbolic-fuzzer|symbolic]] and [[fuzzingbook-20-concolic-fuzzer|concolic]] fuzzers later in Part IV that also rely on constraint solving.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] removes grammar fuzzing's biggest prerequisite — *having a grammar in the first place*. Rather than authoring a [[Grammar|grammar]], [[GrammarMiner|`recover_grammar()`]] performs [[GrammarInference|grammar inference]] from a program plus a few seed inputs, then hands the recovered grammar to the same [[GrammarFuzzer|`GrammarFuzzer`]]/[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]. This makes grammar-based fuzzing applicable to programs whose input format was never formally specified, and acts as a multiplier on whatever sample inputs exist. It is the "where do grammars come from?" complement to the rest of Part III/IV's "what to do with a grammar."

## Connections
- [[GrammarInference]] / [[GrammarMiner]] — Ch 18 supplies the grammar that grammar fuzzing needs, inferred from the program itself.
- [[ConstraintBasedFuzzing]] / [[ISLa]] / [[InputSpecificationLanguage]] / [[SMTSolver]] — Ch 17's declarative semantic layer on grammar-based fuzzing.
- [[ContextFreeGrammar]] / [[Grammar]] — the input specification grammar fuzzing expands.
- [[GrammarAwareGreyboxFuzzing]] / [[FragmentBasedFuzzing]] / [[RegionMutation]] / [[DictionaryMutation]] — Ch 15's fusion of grammar structure with coverage-guided greybox mutation.
- [[GeneratorGrammar]] / [[GeneratorGrammarFuzzer]] / [[SemanticConstraint]] / [[PGGCFuzzer]] — Ch 14's computation-augmented form of grammar production.
- [[ProbabilisticGrammar]] / [[ProbabilisticGrammarFuzzer]] / [[DirectedFuzzing]] — Ch 13's probability-weighted, steerable form of grammar production.
- [[Parser]] / [[EarleyParser]] / [[ParsingExpressionGrammar]] — parse seeds into trees to recombine (the inverse of production).
- [[GrammarCoverage]] / [[GrammarCoverageFuzzer]] / [[ContextCoverage]] — Ch 11's coverage-driven, systematic form of grammar production.
- [[DerivationTree]] / [[GrammarFuzzer]] / [[ExpansionCost]] — the efficient tree-based realization (Ch 10).
- [[Nonterminal]] / [[Terminal]] / [[ProductionRule]] — the symbols and rules the producer rewrites.
- [[EBNF]] / [[BNF]] — the notation for authoring the grammars.
- [[Fuzzing]] — the parent technique; grammar fuzzing is its structured-input branch.
- [[MutationBasedFuzzing]] — grammar outputs make good mutation seeds; the two combine.
- [[CSmith]] — flagship grammar-based compiler fuzzer.
- [[fuzzingbook-09-grammars]] — the chapter that founds grammar-based fuzzing.
- [[fuzzingbook-10-grammar-fuzzer]] — the efficient producer that supersedes the naive one.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
- [[fuzzingbook-10-grammar-fuzzer]] — *The Fuzzing Book* Ch 10, "Efficient Grammar Fuzzing."
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage" (systematic, coverage-driven grammar production).
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs" (parse seeds into trees to recombine for fuzzing).
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (probability-weighted, directed grammar production).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (functions attached to expansions for semantic validity).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (fusing grammar structure with coverage-guided greybox mutation — dictionaries, fragments, regions).
- [[fuzzingbook-17-fuzzing-with-constraints]] — *The Fuzzing Book* Ch 17, "Fuzzing with Constraints" (declarative ISLa constraints add semantic validity on top of grammar production).
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (infers the grammar to fuzz with, from the program itself).
