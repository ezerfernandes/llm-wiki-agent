---
title: "Grammar Inference"
type: concept
tags: [fuzzing, grammar, grammar-inference, grammar-mining, parsing, dynamic-analysis, testing, semantic-fuzzing, python]
sources: [fuzzingbook-18-grammar-miner]
last_updated: 2026-06-06
---

# Grammar Inference

**Grammar inference** is the task of *recovering* an input [[ContextFreeGrammar|grammar]] for a program rather than writing it by hand. It comes in two broad flavors: **black-box** induction of a language from a *set of sample strings* alone (the classical grammatical-inference literature — Higuera, Clark), and **program-guided** inference, which uses the *program that consumes the inputs* as an oracle for their structure. *The Fuzzing Book* focuses on the second, which is far more tractable for fuzzing because the program reveals exactly how it decomposes its input.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] develops program-guided grammar inference. Its founding assumption is that *specific methods are responsible for parsing specific fragments of the input* — true of "almost all ad hoc parsers." The key insight: a variable that holds a **substring of the input** marks a [[Nonterminal|nonterminal]] spanning that substring, and the method/variable name supplies the nonterminal's name. By dynamically tracing execution (reusing the [[Coverage|`Coverage`]] tracer), recording every `str` local that is a substring of the input, stitching those fragments into a per-input [[DerivationTree|derivation tree]], and abstracting many trees into a grammar, the [[GrammarMiner|`recover_grammar()`]] pipeline infers a usable grammar from a function plus a few seeds. The recovered grammar drives the book's [[GrammarFuzzer|`GrammarFuzzer`]]/[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]], so a handful of inputs becomes an unbounded supply of valid ones. The chapter's "came-from-input" test is plain substring inclusion (gated by `FRAGMENT_LEN`); [[fuzzingbook-19-information-flow|Ch 19]]'s [[DynamicTaintTracking|dynamic taint tracking]] is the more precise alternative. The approach descends from the **AUTOGRAM** work of Höschele & Zeller (2017), with Lin et al. (2008) as the pioneering program-guided parse-tree recovery.

## Connections
- [[GrammarMiner]] — the concrete tool/class implementation of program-guided grammar inference.
- [[GrammarMining]] — the umbrella term; inference recovers *structure*, while [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] mines *probabilities* for an existing grammar.
- [[ContextFreeGrammar]] / [[Grammar]] — the formalism / data structure that inference produces.
- [[DerivationTree]] — the per-input intermediate the program's execution is mapped onto.
- [[DynamicTaintTracking]] — the precise alternative to substring inclusion for the "came-from-input" check.
- [[Parser]] — inference recovers the grammar a hand-written parser implicitly encodes.
- [[GrammarBasedFuzzing]] — the downstream consumer of inferred grammars.
- [[RahulGopinath]] / [[AndreasZeller]] — researchers behind the AUTOGRAM/Mimid lineage this builds on.

## Sources
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars."
