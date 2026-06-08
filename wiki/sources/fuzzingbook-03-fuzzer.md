---
title: "The Fuzzing Book Ch 03 — Fuzzing: Breaking Things with Random Inputs"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, random-testing, memory-safety, buffer-overflow]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-03-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Fuzzing: Breaking Things with Random Inputs

## Summary
This is the foundational chapter of *The Fuzzing Book* and the opener of **Part II — Lexical Fuzzing**, building directly on the testing fundamentals of [[fuzzingbook-02-intro-testing|Ch 2]]. It defines [[Fuzzing|fuzzing]] in its simplest form — feeding a string of *random characters* into a program to provoke failures — and traces its origin to [[BartonMiller|Barton Miller]]'s 1988/1989 University of Wisconsin–Madison experiment that found roughly a third of fuzzed UNIX utilities crashed or hung. The central worked example builds a one-function `fuzzer()` random generator, runs it against the external `bc` calculator via `subprocess`, then surveys the bug classes fuzzers expose ([[BufferOverflow|buffer overflows]], missing error checks, rogue numbers) and the runtime/assertion checkers that catch them (the [[AddressSanitizer|AddressSanitizer]]/[[Heartbleed]] story, [[RepresentationInvariant|`repOK()`]] checks, [[MyPy]] static typing). It closes by refactoring everything into the reusable **`Fuzzer`** and **`Runner`** class hierarchies that essentially every later chapter subclasses ([[fuzzingbook-05-mutation-fuzzer|Ch 5]], [[fuzzingbook-06-greybox-fuzzer|Ch 6]], [[fuzzingbook-10-grammar-fuzzer|Ch 10]], …). Next-step pointers go to [[fuzzingbook-05-mutation-fuzzer|mutation fuzzing]], [[fuzzingbook-09-grammars|grammars]], and [[fuzzingbook-16-reducer|reducing failing inputs]].

## Key Concepts
- **The `fuzzer()` function** — the minimal random generator: `random.randrange(0, max_length+1)` picks a length, then each character is `chr(random.randrange(char_start, char_start+char_range))`. Defaults (`max_length=100, char_start=32, char_range=32`) emit printable ASCII; re-parameterizing yields lowercase letters (`fuzzer(1000, ord('a'), 26)`) or digit strings (`fuzzer(100, ord('0'), 10)`). This is [[RandomTesting|random testing]] applied to raw strings.
- **`RandomFuzzer`** — the class form of `fuzzer()`, subclass of the abstract **`Fuzzer`** base. Adds a `min_length` parameter and stores configuration once at construction. See [[RandomFuzzer]].
- **`Fuzzer` base class** — abstract base providing `fuzz()` (returns an input string; default empty), `run(runner)` (fuzz once and feed a [[Runner]]), and `runs(runner, trials)` (repeat `trials` times, returning a list of results). The extension point all later fuzzers override. See [[RandomFuzzer]].
- **`Runner` abstraction** — the program-under-test / [[Runner|fuzzing harness]] interface. `run(input)` returns a `(result, outcome)` pair where `outcome ∈ {PASS, FAIL, UNRESOLVED}`. Subclasses: `PrintRunner` (echoes input, returns `UNRESOLVED`), `ProgramRunner` (feeds input to an external program via `subprocess.run`, mapping return code → outcome: 0=`PASS`, <0=`FAIL`, else `UNRESOLVED`), and `BinaryProgramRunner` (binary stdin). See [[Runner]].
- **Fuzzing external programs** — write fuzz to a temp file, invoke a target (e.g. `bc`) with `subprocess.run`, and inspect `stdout`/`stderr`/`returncode`. Most random inputs are invalid (parse/syntax errors), which is why mutation- and grammar-based fuzzing follow.
- **Bug classes fuzzers find** — [[BufferOverflow|buffer overflows]] (`strcpy` into an undersized buffer; simulated by `crash_if_too_long`), **missing error checks** (`while (getchar() != ' ')` looping forever on premature `EOF`; simulated by `hang_if_no_space`), and **rogue numbers** (`malloc(size)` with attacker-controlled `size`; simulated by `collapse_if_too_large`). Caught with the book's `ExpectError` / `ExpectTimeout` context managers.
- **Generic runtime checkers** — [[AddressSanitizer|AddressSanitizer]] (`clang -fsanitize=address`) detects out-of-bounds memory accesses at ~2× slowdown; the [[Heartbleed]] OpenSSL bug was found exactly this way (memory sanitizer + fuzzing at Codenomicon/Google). [[InformationLeak|Information leaks]] can occur within *valid* memory bounds (the `heartbeat()` over-read simulation), which ASan cannot catch — motivating [[fuzzingbook-19-information-flow|taint tracking (Ch 19)]].
- **Program-specific checkers** — [[Assertion|assertions]] and [[RepresentationInvariant|`repOK()`]] consistency checks ([[DesignByContract|design-by-contract]] style) for complex data structures (airport-code map, red-black tree), plus [[StaticAnalysis|static type checking]] with [[MyPy]]. The rule of thumb: *enable as many automatic checkers as possible* — CPU cycles are cheap, errors are expensive.

## Key Claims
- Fuzzing was born on "a dark and stormy night in the Fall of 1988"; line noise on a 1200-baud modem corrupted UNIX command input and crashed programs, prompting [[BartonMiller|Barton Miller]] to assign students to build the first fuzz generators.
- Miller's 1989 experiment crashed/hung **about a third** of the UNIX utilities tested — including `bc` — and the mistakes found then (buffer overflows, missing error checks, rogue numbers) are still common today.
- The `outcome` of a `ProgramRunner` is derived from the OS return code: `0 → PASS`, negative (killed by signal) `→ FAIL`, positive `→ UNRESOLVED`; plain `bc` rarely returns nonzero, so a crash is easy to miss without extra checkers.
- A buffer overflow can corrupt adjacent memory silently; `char weekday[9]; strcpy(weekday, input)` already overflows on the 9-character input `"Wednesday"`.
- AddressSanitizer detects out-of-bounds reads/writes but **not** in-bounds information leaks; an over-long `heartbeat()` reply spills secret/uninitialized memory while staying within array bounds.
- Random fuzzing is cheap and effective for robustness, but the bugs it finds are predominantly *input-processing* errors; structured generation (mutation, grammars) is needed for deeper coverage.
- Because fuzz runs millions of times, run fuzzers in a resettable sandbox (e.g. a Docker container) — a random `rm -fr` argument has a non-trivial chance of deleting real files.

## Key Quotes
> "The key idea of random text generation, also known as *fuzzing*, is to feed a string of random characters into a program in the hope to uncover failures." — chapter opening

> "First, you will build a *fuzz generator*. This is a program that will output a random character stream. Second, you will take the fuzz generator and use it to attack as many UNIX utilities as possible, with the goal of trying to break them." — Miller's 1988 CS736 assignment, quoted in the chapter

> "As a rule of thumb, you should always *enable as many automatic checkers as possible* during fuzzing. CPU cycles are cheap, and errors are expensive." — on combining fuzzing with sanitizers and assertions

## Connections
- [[Fuzzing]] — this chapter is the wiki's canonical definition of basic random fuzzing and the `Fuzzer`/`Runner` architecture.
- [[RandomTesting]] — fuzzing here *is* random testing over strings; the chapter is its direct successor (per [[fuzzingbook-02-intro-testing|Ch 2]]'s "Next Steps").
- [[RandomFuzzer]] / [[Runner]] — the two reusable class hierarchies minted here and subclassed throughout the book.
- [[BufferOverflow]] / [[AddressSanitizer]] / [[Heartbleed]] / [[InformationLeak]] — the memory-safety bug classes and the runtime checkers that catch them.
- [[Assertion]] / [[RepresentationInvariant]] / [[DesignByContract]] — program-specific checkers (`repOK()`) that extend what fuzzing can detect.
- [[StaticAnalysis]] / [[MyPy]] — the static complement to runtime `repOK()` checks.
- [[BartonMiller]] — originator of fuzzing and the experiment that frames the chapter.
- [[AndreasZeller]] — lead author of *The Fuzzing Book*.
- [[fuzzingbook-02-intro-testing|Ch 2]] — prerequisite (testing fundamentals, `ExpectTimeout`).
- [[fuzzingbook-05-mutation-fuzzer|Ch 5]] / [[fuzzingbook-06-greybox-fuzzer|Ch 6]] / [[fuzzingbook-09-grammars|Ch 9]] / [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — successors that subclass `Fuzzer`/`Runner`.
- [[fuzzingbook-16-reducer|Ch 16]] — reducing the failing inputs a fuzzer finds.
- [[fuzzingbook-19-information-flow|Ch 19]] — automatic detection of the information leaks introduced here.
- [[fuzzingbook-22-dynamic-invariants|Ch 22]] — generalizes the generic-checker idea (mining function specifications).

## Architecture note (reused by later chapters)
This chapter establishes the **class architecture the rest of the book builds on**, importable as `from fuzzingbook.Fuzzer import Fuzzer, RandomFuzzer, Runner, PrintRunner, ProgramRunner`:

- `Fuzzer` → `fuzz()`, `run(runner)`, `runs(runner, trials)`. Later fuzzers (`MutationFuzzer`, `GrammarFuzzer`, `GreyboxFuzzer`, `GeneratorGrammarFuzzer`, …) subclass `Fuzzer` and override `fuzz()`.
- `Runner` → `run(inp) -> (result, outcome)` with `PASS`/`FAIL`/`UNRESOLVED` constants. `PrintRunner`, `ProgramRunner`, and `BinaryProgramRunner` are the built-in subclasses; instrumented runners in later chapters (e.g. coverage-collecting runners in [[fuzzingbook-04-coverage|Ch 4]]/[[fuzzingbook-06-greybox-fuzzer|Ch 6]]) extend this same interface.

## Contradictions
- None identified. (Complements the existing [[Fuzzing]] page, which describes *modern coverage-guided* fuzzing; this chapter covers the *blackbox random* baseline that precedes it.)
