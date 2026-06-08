---
title: "LangFuzz"
type: entity
tags: [tool, fuzzer, fuzzing, security, javascript, grammar, fragments]
sources: [fuzzingbook-15-greybox-grammar-fuzzer]
last_updated: 2026-06-06
---

# LangFuzz

**LangFuzz** is a highly effective grammar-based fuzzer for (mostly) JavaScript, authored by [[ChristianHoller|Christian Holler]] and presented in *"Fuzzing with Code Fragments"* (Holler, Herzig & Zeller, USENIX Security 2012). It works by **[[FragmentBasedFuzzing|parsing valid inputs into fragments]]** (subtrees of a [[DerivationTree|parse tree]]) and **recombining** those fragments — along with newly generated parts — into new, structurally valid programs that are then fed to a language interpreter to provoke crashes. It is the canonical real-world fragment-recombination fuzzer and the inspiration for *The Fuzzing Book*'s `FragmentMutator`/`LangFuzzer`.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] reconstructs LangFuzz's approach in miniature: parse seeds with an [[EarleyParser|`EarleyParser`]], disassemble into a per-symbol [[FragmentBasedFuzzing|fragment pool]], and recombine by swapping/deleting subtrees of the same nonterminal type (the `FragmentMutator`, driven by the blackbox `LangFuzzer` or the coverage-guided [[GrammarAwareGreyboxFuzzing|`GreyboxGrammarFuzzer`]]). The chapter reports LangFuzz's real-world impact: **>2,600 bugs** found in the JavaScript engines of Firefox, Chrome, and Edge, **>USD 50,000 in bug bounties in four weeks**, and a workflow that [[SeedMining|seeds from JavaScript CVE reports]]. *Superion* is described as essentially "LangFuzz + greybox fuzzing" (without AFL-style byte mutation).

## Connections
- [[FragmentBasedFuzzing]] — the technique LangFuzz pioneered; the book's `FragmentMutator` reconstructs it.
- [[ChristianHoller]] — LangFuzz's author and book co-author.
- [[GrammarAwareGreyboxFuzzing]] — the book's `LangFuzzer`/`GreyboxGrammarFuzzer` are inspired by it.
- [[SeedMining]] — LangFuzz seeded from CVE-reported failure-inducing inputs.
- [[AFLSmart]] — the sibling inspiration for the chapter ([[RegionMutation|region-based]] + validity schedules).
- [[DerivationTree]] / [[EarleyParser]] / [[GrammarBasedFuzzing]] — the parsing/structure machinery it relies on.
- [[CSmith]] — another flagship real-world grammar-based fuzzer (for C compilers).
- [[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] — where LangFuzz is reconstructed.
- [[fuzzingbook-09-grammars|Ch 9]] — cites LangFuzz among real-world grammar fuzzers.

## Sources
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars."
