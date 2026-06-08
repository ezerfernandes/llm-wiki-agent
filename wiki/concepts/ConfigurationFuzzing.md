---
title: "Configuration Fuzzing"
type: concept
tags: [fuzzing, testing, configuration, command-line, argparse, domain-specific-fuzzing, security, python]
sources: [fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# Configuration Fuzzing

**Configuration fuzzing** is the systematic testing of a program's *configuration space* — the settings that govern how it processes its (regular) input data: command-line **options** and **arguments**, environment variables, and configuration files. The premise is that behavior is governed not only by data but by configuration, so configurations "can and should be tested," and any single option may itself trigger a bug or security vulnerability — making each option a [[Fuzzing|fuzz target]] in its own right. This is the opening technique of *The Fuzzing Book*'s domain-specific part (Part V).

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] develops configuration fuzzing for command-line options in three moves.

**1. A configuration grammar.** One can hand-write a [[Grammar|grammar]] of valid invocations (the chapter's `PROCESS_NUMBERS_EBNF_GRAMMAR`, with `--sum`/`--min`/`--max` plus integer arguments) and fuzz it with a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] so every option is covered; `fuzz().split()` turns the produced string into an `argv` list. The drawback is maintenance: the grammar must be updated on every program change.

**2. Mining the grammar automatically.** Since the option information is already encoded in the program, the chapter *extracts* it: the [[OptionGrammarMiner|`OptionGrammarMiner`]] traces a Python program (`sys.settrace`) up to its `argparse.parse_args()` call, intercepting `add_argument()`/`add_mutually_exclusive_group()` to reconstruct an [[OptionGrammar|option grammar]] with no hand-written spec. Two reusable classes package this:
- **`OptionRunner`** — a `ProgramRunner` subclass that finds a Python executable, reads its source, and runs it as `__main__` in-process via `exec` (no subprocess) up to `parse_args()`, then exposes the mined grammar via `ebnf_grammar()`/`grammar()`. `set_arguments()` pins positional arguments so fuzzing concentrates on options.
- **`OptionFuzzer`** — a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] subclass built from an `OptionRunner`; it `fuzz()`es valid command lines and `run()` invokes the (possibly different) runner with them — so options mined from one program can be applied in another context.

The toolkit is demonstrated on real tools: `autopep8`, the [[MyPy|`mypy`]] type checker (140+ options), and `notedown`. It is `argparse`-specific and experimental, but "does a pretty good job even on nontrivial programs."

**3. Covering combinations.** Single-option coverage misses *interactions* between options, so the chapter layers [[CombinatorialTesting|combinatorial (pairwise) testing]] on top — rewriting the option list into all pairs so one fuzzing pass covers every two-option interference.

The exercises generalize beyond `argparse`: mining C-preprocessor `#ifdef` variables into `-D` compiler options, fuzzing `.ini` files via a tracking `ConfigParser`, and extracting C `getopt()`/`getopt_long()` option strings. The Background notes configuration data has received relatively little test-generation attention despite being just as likely to cause failures (Pezzè & Young 2008; Petke et al. 2015; Sutton et al. 2007; Dai et al. 2010).

## Connections
- [[OptionGrammar]] — the grammar of valid invocations this technique fuzzes.
- [[OptionGrammarMiner]] — the trace-based class that mines that grammar from `argparse`.
- [[CombinatorialTesting]] — the pairwise/k-way layer for covering option interactions.
- [[GrammarCoverageFuzzer]] — ensures each mined option is covered at least once; `OptionFuzzer` subclasses it.
- [[GrammarCoverage]] / [[ContextCoverage]] — the coverage criterion (Exercise 4 covers each option's parameters independently via expansion duplication).
- [[GrammarMining]] / [[GrammarMiner]] — the broader family of learning grammars from programs (here from option specifications rather than input substrings).
- [[Grammar]] / [[GrammarBasedFuzzing]] — the configuration is encoded as a grammar and fuzzed like any other.
- [[Coverage]] — the `sys.settrace` machinery the miner reuses ([[fuzzingbook-04-coverage|Ch 4]]).
- [[Testing]] — situates configuration testing within systematic software testing.
- [[Fuzzing]] — the parent activity; options become fuzz targets.
- [[fuzzingbook-09-grammars|Ch 9]] / [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — prerequisites (the grammar data structure and coverage fuzzer).
- [[fuzzingbook-23-configuration-fuzzer]] — the chapter that introduces configuration fuzzing.

## Sources
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations."
