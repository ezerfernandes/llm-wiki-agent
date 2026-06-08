---
title: "OptionGrammarMiner"
type: concept
tags: [fuzzing, grammar, grammar-mining, configuration, argparse, tracing, dynamic-analysis, python, tool]
sources: [fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# OptionGrammarMiner

**`OptionGrammarMiner`** is *The Fuzzing Book*'s helper class for extracting an [[OptionGrammar|option grammar]] from a Python program *without parsing its source statically* — instead by **dynamically introspecting** its use of the `argparse` module while it runs. It is the engine behind [[ConfigurationFuzzing|configuration fuzzing]] and represents a distinct sense of [[GrammarMining|grammar mining]]: from a program's *option specification* rather than from input substrings ([[GrammarMiner|`GrammarMiner`]], [[fuzzingbook-18-grammar-miner|Ch 18]]) or from expansion counts ([[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]).

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] constructs the miner around a single insight: a program built with `argparse` declares all its options *before* it does any work, so if you run it and stop exactly at `argparse.parse_args()`, you have observed the complete option specification at minimal cost.

**Mechanism.** `mine_ebnf_grammar()` seeds the grammar `<start> ::= <option>* <arguments>` and installs a trace function via `sys.settrace` (reusing the [[Coverage|`Coverage`]] tracing idiom of [[fuzzingbook-04-coverage|Ch 4]]). `traceit` watches every `call` event for four methods on the parser object:
- **`add_argument`** — `process_argument()`/`process_arg()` add the option/argument to the grammar; an `in_group` flag (detected by finding `"Group"` in the receiver's type) routes group members to the current `<group>` symbol.
- **`add_mutually_exclusive_group`** — `add_group()` mints a fresh `<group>` symbol, prefixes it to `<start>`, and picks the expansion operator from `required`/`exclusive` (bare / `+` / `?` / `*`).
- **`add_argument_group`** — currently ignored.
- **`parse_args`** — raises a custom `ParseInterrupt` exception to halt execution; `mine_ebnf_grammar()` catches it and restores the previous trace.

**Type and arity inference.** `process_arg()` reads `nargs` (int → repeat the parameter; `?`/`+`/`*` → EBNF operator). `add_parameter()` returns `""` if an `action=` is present (no value), else infers `int` vs `str` from `type=`, naming the placeholder from `metavar=`. `add_type_rule()`/`add_int_rule()`/`add_str_rule()`/`add_metavar_rule()` add the `<int>`/`<str>`/`<digit>`/`<char>`/`<metavar>` rules (using `crange`/`srange`).

It correctly recovers options the author never wrote (e.g. `argparse`'s auto-injected `--help`/`-h`) and the structure of mutually-exclusive groups. It is **experimental and `argparse`-specific** — it assumes one parser and at most one active mutually-exclusive group, and not all `argparse` features are supported — but works on nontrivial real programs (`autopep8`, `mypy`, `notedown`). The class is the default `miner_class` of `OptionRunner` and is designed to be subclassed for custom miners.

## Connections
- [[OptionGrammar]] — the artifact this class produces.
- [[ConfigurationFuzzing]] — the technique it enables (consumed by `OptionRunner`/`OptionFuzzer`).
- [[GrammarMining]] — the umbrella concept; this is the `argparse`-introspection variant.
- [[GrammarMiner]] — the *input-grammar* miner ([[fuzzingbook-18-grammar-miner|Ch 18]]); a sibling sense of mining (input substrings, not option specs).
- [[Coverage]] — the `sys.settrace` tracing machinery the miner reuses ([[fuzzingbook-04-coverage|Ch 4]]).
- [[Grammar]] / [[GrammarBasedFuzzing]] — the EBNF grammar it emits, ready for `convert_ebnf_grammar`.
- [[GrammarCoverageFuzzer]] — consumes the mined grammar to cover all options.
- [[fuzzingbook-23-configuration-fuzzer]] — the chapter that introduces the miner.

## Sources
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations."
