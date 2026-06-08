---
title: "Option Grammar"
type: concept
tags: [fuzzing, grammar, configuration, command-line, argparse, ebnf, python]
sources: [fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# Option Grammar

An **option grammar** is a [[Grammar|grammar]] describing the set of *valid command-line invocations* of a program — its options, their parameters and types, their arities, and any mutual-exclusion structure. It lets a [[GrammarBasedFuzzing|grammar-based fuzzer]] generate well-formed command lines that the program's argument parser will accept, turning [[ConfigurationFuzzing|configuration fuzzing]] into ordinary grammar fuzzing.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] uses an option grammar of the canonical shape:

```
<start>   ::= <option>* <arguments>
<option>  ::= ' -h' | ' --help' | ' --jobs <n>' | ...
<arguments> ::= ' foo.py'
```

Options carry a leading space and, where they take a value, a typed metavariable (`<n>`, `<filename>`, `<int>`, `<str>`, …). The grammar is built either by hand (the `PROCESS_NUMBERS_EBNF_GRAMMAR` example) or, more usefully, **mined automatically** from a Python program's `argparse` setup by the [[OptionGrammarMiner|`OptionGrammarMiner`]] (exposed through `OptionRunner.ebnf_grammar()`). Mined details include:
- **Routing** — names starting with `-` become `<option>` alternatives; bare names become `<arguments>`.
- **Arities** — `argparse`'s `nargs` is honored: an integer `n` repeats the parameter `n` times; `?`/`+`/`*` map to the matching EBNF operator.
- **Types** — `type=int` yields an `<int>` rule (`(-)?<digit>+`); otherwise `<str>` (`<char>+`); `action=...` options take no parameter; `metavar=` names the placeholder.
- **Groups** — a mutually-exclusive group becomes a `<group>` symbol prefixed to `<start>`, with the operator chosen by the `required`/`exclusive` flags (bare / `+` / `?` / `*`).

The grammar is convertible to BNF (`convert_ebnf_grammar`) and validated with `is_valid_grammar`, then fed to a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] to cover every option. It can also be transformed — e.g. `set_arguments()` pins positional arguments, and `pairwise()` rewrites `<option>` into pairs for [[CombinatorialTesting|combinatorial testing]].

## Connections
- [[OptionGrammarMiner]] — the class that mines option grammars from `argparse`.
- [[ConfigurationFuzzing]] — the technique that fuzzes option grammars.
- [[CombinatorialTesting]] — rewrites the `<option>` rule into pairs.
- [[Grammar]] / [[ContextFreeGrammar]] / [[GrammarBasedFuzzing]] — the general grammar machinery an option grammar specializes.
- [[GrammarCoverageFuzzer]] / [[GrammarCoverage]] — consume the option grammar to cover all options.
- [[fuzzingbook-09-grammars|Ch 9]] — the grammar data structure and EBNF helpers reused here.
- [[fuzzingbook-23-configuration-fuzzer]] — the chapter that mints the option grammar.

## Sources
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations."
