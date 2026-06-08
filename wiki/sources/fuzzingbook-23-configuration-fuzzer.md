---
title: "The Fuzzing Book Ch 23 — Testing Configurations"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, configuration, combinatorial-testing, pairwise-testing, argparse, grammar-mining, command-line]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-23-configuration-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Testing Configurations

## Summary
Chapter 23 opens Part V ("Domain-Specific Fuzzing") by arguing that a program's *configuration* — chiefly its command-line options and arguments, but also configuration files — is an input source just as worthy of testing as its data, and a fertile target for finding bugs and security vulnerabilities. It first shows that one *could* hand-write a [[Grammar|grammar]] of valid invocations (the `PROCESS_NUMBERS_EBNF_GRAMMAR` example) and fuzz it with a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]), but that this creates a maintenance burden. The chapter's central technique is therefore [[ConfigurationFuzzing|automatic option-grammar mining]]: the `OptionGrammarMiner` runs a Python program with `sys.settrace` up to its `argparse.parse_args()` call, intercepting every `add_argument()`/`add_mutually_exclusive_group()` to reconstruct an [[OptionGrammar|option grammar]] of valid command lines with no hand-written spec. The reusable `OptionRunner` (a `ProgramRunner` subclass) and `OptionFuzzer` (a `GrammarCoverageFuzzer` subclass) package this end-to-end and are demonstrated on real tools (`autopep8`, `mypy`, `notedown`). Finally it adds [[CombinatorialTesting|combinatorial testing]]: rather than the exponential full configuration space, it rewrites the option list into all *pairs* (`pairwise()`) so that one fuzzing pass covers every interaction between two options — pairwise/k-way coverage. It is a prerequisite-light chapter requiring only [[fuzzingbook-09-grammars|Ch 9]] and [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]].

## Key Concepts
- **[[ConfigurationFuzzing|Configuration testing]]** — treating the settings that govern a run (options, arguments, config files) as a fuzz target distinct from regular input data. Options "can become fuzz targets on their own," and any one may trigger an unknown vulnerability.
- **Hand-written configuration grammar** — `PROCESS_NUMBERS_EBNF_GRAMMAR` encodes a program's `--sum`/`--min`/`--max` operators and integer arguments; `GrammarCoverageFuzzer(..., min_nonterminals=10)` then covers each option, and `fuzz().split()` turns the string into an `argv` list to invoke the program. Works, but must be maintained by hand on every change.
- **[[OptionGrammar|Option grammar]] mining** — the `OptionGrammarMiner` class: given a callable that uses `argparse`, it installs a trace function (`traceit`) that watches for four method calls — `add_argument` (records an option/argument), `add_mutually_exclusive_group`/`add_argument_group` (opens a group), and `parse_args` (raises a `ParseInterrupt` to stop execution before the program actually runs). The grammar takes the shape `<start> ::= <option>* <arguments>`; `process_arg()` routes `-`-prefixed names into `<option>` and bare names into `<arguments>`, honoring `nargs` (int → repeat the parameter; `?`/`+`/`*` → EBNF operator). `add_parameter()`/`add_type_rule()` infer parameter types (`int` vs `str`) from the `type=`/`action=`/`metavar=` keyword arguments, minting `<int>`/`<str>`/`<digit>`/`<char>` rules. `mine_ebnf_grammar()`/`mine_grammar()` return the grammar in EBNF/BNF.
- **`OptionRunner`** — a `ProgramRunner` subclass that locates a Python executable (`find_executable`), reads its source, and runs it as `__main__` via `exec` so the miner can hook `argparse` *in-process* up to `parse_args()` (no subprocess). `ebnf_grammar()`/`grammar()` expose the mined grammar; `set_arguments()` pins the positional arguments (e.g. to a single `foo.py`) so fuzzing concentrates on options.
- **`OptionFuzzer`** — a `GrammarCoverageFuzzer` subclass constructed from an `OptionRunner`; it pulls the runner's grammar and `fuzz()`es command lines, and its `run()` invokes the (possibly different) runner with the generated arguments — so options mined from one program can be applied to another.
- **[[CombinatorialTesting|Combinatorial / pairwise testing]]** — the `pairwise()` function concatenates every 2-combination (`itertools.combinations(option_list, 2)`) of options, and the `<option>` rule is rewritten to that list so covering it covers all pairs. Rationale: bugs rarely depend on three-plus interacting settings, so pairwise coverage finds most interferences at a fraction of the cost; the count is the binomial coefficient `C(n,2) = n(n-1)/2`.

## Key Claims
- Configuration is a first-class input source: program behavior is governed not only by data but by settings set via options or config files, so configurations "can and should be tested."
- For programs using a standard option-parsing library (`argparse` in Python), the options, their parameters, types, arities, and mutually-exclusive groups can be **automatically extracted** by tracing the parse and converted into a fuzzing grammar — eliminating the need to write or maintain a grammar by hand.
- The mining trick is to interrupt execution exactly at `parse_args()` (via a `ParseInterrupt` exception), by which point the program has set up its argument parser but not yet processed anything — so the miner observes the full option specification cheaply and safely.
- `OptionGrammarMiner` correctly recovers options the author never wrote (e.g. `argparse`'s auto-added `--help`/`-h`), parameter types, and the structure of mutually-exclusive groups (mapping `required`/`exclusive` flags to the EBNF operators bare/`+`/`?`/`*`).
- Running `autopep8` with mined options yields a "surprisingly high number of passing runs"; option dependencies and mutual exclusions enforced by program logic (not the parser) fall outside the miner's scope.
- The technique is `argparse`-specific and experimental — not all `argparse` features are supported — yet "does a pretty good job even on nontrivial programs" such as `mypy` (140+ options) and `notedown`.
- The full configuration space is exponential and untestable; **pairwise coverage** ("frequently suffices to cover all interferences between options") is the practical target. `autopep8`'s 30 options need 870 pair tests; `mypy`'s 140+ options need 20,000+, still runnable in a few hours.
- Exercises generalize the idea beyond `argparse`: mining C-preprocessor `#ifdef` variables into `-D` compiler options, fuzzing `.ini` files via a tracking `ConfigParser`, and extracting C `getopt()`/`getopt_long()` strings.

## Key Quotes
> "The configuration of a program – that is, the settings that govern the execution of a program on its (regular) input data, as set by options or configuration files – just as well influences behavior, and thus can and should be tested." — opening framing of configuration as a fuzz target.

> "By mining options and arguments from existing programs, we can now fuzz these options out of the box – without having to specify a grammar." — the payoff of `OptionGrammarMiner`.

> "Testing every such pair of options frequently suffices to cover all interferences between options. (Programs rarely have conditions involving three or more configuration settings.)" — the rationale for pairwise combinatorial testing.

## Connections
- [[ConfigurationFuzzing]] — the chapter's headline technique (the `OptionRunner`/`OptionFuzzer` toolkit).
- [[OptionGrammar]] — the data structure mined from `argparse` and fuzzed.
- [[CombinatorialTesting]] — pairwise/k-way option coverage via `pairwise()`.
- [[OptionGrammarMiner]] — the trace-based `argparse` introspection class minting the option grammar.
- [[GrammarCoverageFuzzer]] — the engine that ensures every mined option (and digit/letter) is covered at least once; `OptionFuzzer` subclasses it.
- [[GrammarCoverage]] / [[ContextCoverage]] — the coverage criterion driving option selection; Exercise 4 duplicates expansions to cover each option's parameters independently (coverage in context).
- [[GrammarMining]] / [[GrammarMiner]] — a third sense of "grammar mining": from `argparse` introspection rather than input substrings ([[fuzzingbook-18-grammar-miner|Ch 18]]) or expansion counts ([[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]]).
- [[Grammar]] / [[GrammarBasedFuzzing]] — `convert_ebnf_grammar`, `extend_grammar`, `is_valid_grammar`, `new_symbol`, `crange`/`srange` are reused to build and transform the option grammar.
- [[Coverage]] — the `OptionGrammarMiner.traceit` hook reuses the `sys.settrace` tracing machinery introduced in [[fuzzingbook-04-coverage|Ch 4]].
- [[Testing]] — situates configuration testing within systematic software testing.
- [[AndreasZeller]] — lead author; [[CISPA]] — publisher.
- [[MyPy]] — a real fuzz target in the chapter (140+ mined options).
- [[fuzzingbook-09-grammars|Ch 9]] — prerequisite; supplies the `Grammar` data structure and EBNF helpers.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — prerequisite; supplies `GrammarCoverageFuzzer` and the coverage criterion.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — the "Next Steps" pointer for mining grammars of *input data* rather than options.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] / [[fuzzingbook-12-parser|Ch 12]] / [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] / [[fuzzingbook-16-reducer|Ch 16]] — related grammar machinery cited as further steps.

## Contradictions
- None identified.
