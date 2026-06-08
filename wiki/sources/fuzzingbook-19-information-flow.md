---
title: "The Fuzzing Book Ch 19 — Tracking Information Flow"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, information-flow, taint-analysis, dynamic-analysis, python]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-19-information-flow.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Tracking Information Flow

## Summary
Chapter 19 sits in Part IV (Semantic Fuzzing) and builds the [[InformationFlow|information-flow]] machinery that underpins the rest of the part. It argues that crashes are a weak oracle — programs can misbehave (leak secrets, execute injected code) without crashing — and that *tracking how input data flows through a program* gives a much stronger oracle. The chapter implements [[DynamicTaintAnalysis|dynamic taint analysis]] in pure Python as two `str` subclasses: `tstr`, which attaches a single security-level *taint* to a whole string and propagates it through every string operation, and `ostr`, which goes finer by attaching a per-character *origin* (the input index each character came from). The running example is a deliberately [[CodeInjection|`eval()`-vulnerable]] in-memory SQL database (`DB`), against which the chapter shows three uses of taint: rejecting untrusted input (`TrustedDB`), aborting when tainted data reaches a dangerous sink (`TaintedDB`/`Tainted`), and [[TaintDirectedFuzzing|taint-directed fuzzing]] that traces which grammar rules produced the characters reaching `eval` and biases future generation toward them (`TrackingDB` + `TaintedGrammarFuzzer`). It is the detailed taint chapter that [[fuzzingbook-18-grammar-miner|Ch 18]]'s grammar mining can build on, and it explicitly hands off to the symbolic/[[ConcolicExecution|concolic]] techniques of [[fuzzingbook-20-concolic-fuzzer|Ch 20]] for the [[ImplicitInformationFlow|implicit flows]] that taint tracking cannot follow.

## Key Concepts
- **[[InformationFlow]]** — the central theme: tracking how data moves from *sources* (input functions) to *sinks* (dangerous operations) so that policies (no untrusted input reaches a sink; no secret reaches output) can be checked at runtime. Sources *taint*, sinks check the taint, and blessed *sanitizers* clear it.
- **[[DynamicTaintAnalysis]]** — labeling data at runtime and propagating the label through operations. Implemented here as a *library* (string-subclass) approach rather than VM/binary instrumentation, following Conti et al. (2010).
- **[[TaintedString]]** (`tstr`) — a `str` subclass carrying one `taint` label. Hooks `__new__()` (because `str` is immutable and never calls `__init__()` on subclasses), then wraps ~25 string methods (`make_str_wrapper()` / `informationflow_init_1()`) plus `__radd__()` so that any derived fragment (`thello[1:2]`, `'foo' + thello`, `thello * 5`, `'%s' % thello`) re-wraps as a `tstr` with the same taint. Offers `clear_taint()` / `has_taint()` for sanitization. Limitation: when two differently-tainted `tstr` strings are concatenated, `__add__()` wins over `__radd__()` and the right operand's taint is silently dropped — taint conflicts are application-dependent and not resolved generically.
- **[[CharacterOrigin]]** (`ostr`) — extends `tstr` with a per-character `origin` list: integer indices into the originating input (default starting at 0, settable via `origin=N`), with `UNKNOWN_ORIGIN = -1` for characters of unknown provenance. Re-implements `__getitem__` (int and slice), `__add__`/`__radd__`, `split`/`rsplit`/`splitlines`, `replace`, `strip`/`lstrip`/`rstrip`, `expandtabs`, `join`, `partition`/`rpartition`, `ljust`/`rjust`, `__mod__`/`__rmod__`, and case methods, each splicing origin lists to match. `x(i)` extracts the characters whose origin equals index `i`; origin checks reduce to Python set operations (`set(frag.origin) <= set(src.origin)`).
- **[[DataFlow]]** — explicit data flow is exactly what taints follow: a value's taint/origin records the input data it was derived from. The chapter contrasts this with [[ImplicitInformationFlow|implicit (control) flow]].
- **[[ImplicitInformationFlow]]** (control-flow taint) — data dependence routed through control flow (`if c == 'a': t += 'a'`) reconstructs a string with *no* explicit data flow between input and output, so taints are lost. This is a fundamental limit of dynamic taint analysis and a key motivation for the symbolic/concolic chapters.
- **[[CodeInjection]] / sanitization** — the `eval()`-based `DB` lets `select __import__("os").popen(...)` run arbitrary code. `TrustedDB` only accepts `taint == 'TRUSTED'` strings; `sanitize()` whitelists characters via regex and re-taints as `TRUSTED`, mirroring SQL/code-injection defenses from the Web Fuzzing chapter.
- **[[TaintDirectedFuzzing]]** — `Tainted` exception + `TaintedDB.my_eval()` (abort when input is not `TRUSTED`) gives *taint-aware* fuzzing (which statement *kinds* reach the sink). `TrackingDB` (raise on any non-empty origin) plus `TaintedGrammarFuzzer` (tags every grammar key/alternative/token with a distinct origin via `init_tainted_grammar`, preserves origins through `tree_to_string`) then enables *taint-directed* fuzzing: `update_grammar()` maps the origins reaching `eval` back to the grammar rules that produced them and increments their `use` count, biasing generation toward dangerous rules — a [[GreyboxFuzzing|greybox]]-style feedback loop on data flow rather than coverage.

## Key Claims
- Crashes are an impoverished oracle; tracking information flow detects incorrect behavior (injection, leakage) that produces no crash.
- Taints can be tracked in pure Python by subclassing `str` and wrapping its methods — no binary instrumentation needed — at the cost of completeness.
- Per-character origins (`ostr`) solve the taint-composition problem that whole-string taints (`tstr`) cannot: a composite string inherits taint *per character*, so the `heartbeat()` leak (which over-tainted *every* reply as `SECRET` under `tstr`) is precisely detectable under `ostr` (only the leaked characters carry `SECRET_ORIGIN`).
- Taint information is lost across (a) conversions out of strings (e.g. `chr(ord(c))`), (b) calls into internal C library code (`''.join([...])` drops origins that `+` preserves), and (c) implicit/control flow. The safe response is to treat any untainted string as worst-case (possibly untrusted / possibly secret) and re-taint from sources.
- Taint-directed fuzzing focuses generation on grammar rules whose output reaches a dangerous sink, a stronger signal than crash-only feedback.

## Key Quotes
> "One method that allows such differentiation is that of *dynamic taint analysis*. The idea is to identify the functions that accept user input as *sources* that *taint* any string that comes in through them, and those functions that perform dangerous operations as *sinks*." — motivating taint analysis against the `eval()`-vulnerable DB.

> "The key to composition of differently tainted strings is to assign taints not only to strings, but actually to every bit of information – in our case, characters." — the move from `tstr` to per-character `ostr` origins.

> "An untainted string should be treated as _possibly untrusted_ ... an untainted string should be treated as _possibly secret_." — the defensive default once taints can be lost.

## Connections
- [[InformationFlow]] / [[DynamicTaintAnalysis]] / [[TaintedString]] / [[CharacterOrigin]] / [[DataFlow]] / [[ImplicitInformationFlow]] / [[TaintDirectedFuzzing]] / [[CodeInjection]] — concepts this chapter mints.
- [[DynamicTaintTracking]] — the umbrella concept introduced by [[fuzzingbook-18-grammar-miner|Ch 18]]; this chapter is where its `ostr` mechanism is actually built.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — Mining Input Grammars; its `GrammarMiner` can swap substring matching for `ostr` origin inclusion (the chapter's final exercise imports `ostr` from here).
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — Concolic Fuzzing; the symbolic successor that follows the implicit/control flows taint tracking misses.
- [[fuzzingbook-04-coverage|Ch 4]] (Coverage) and [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] (Probabilistic Grammar Fuzzing) are listed prerequisites; `TaintedGrammarFuzzer` extends the [[GrammarFuzzer|`GrammarFuzzer`]] of [[fuzzingbook-10-grammar-fuzzer|Ch 10]].
- [[fuzzingbook-03-fuzzer|Ch 3]] — the `heartbeat()` (Heartbleed-style) leak example is reused as the privacy-leak motivation.
- [[GreyboxFuzzing]] — taint-directed fuzzing is a feedback-driven (greybox) strategy keyed on data flow.
- [[Parser]] / [[Grammar]] / [[DerivationTree]] — `TaintedGrammarFuzzer` propagates per-token origins through the canonical grammar and derivation tree.
- [[AndreasZeller]] / [[RahulGopinath]] / [[CISPA]] — author/co-author and publisher.

## Contradictions
- None identified.
