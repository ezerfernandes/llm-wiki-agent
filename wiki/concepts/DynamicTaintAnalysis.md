---
title: "Dynamic Taint Analysis"
type: concept
tags: [security, taint-analysis, information-flow, dynamic-analysis, fuzzing, testing, python]
sources: [fuzzingbook-19-information-flow, fuzzingbook-20-concolic-fuzzer]
last_updated: 2026-06-06
---

# Dynamic Taint Analysis

**Dynamic taint analysis** labels selected data at runtime (a *taint*) and propagates that label through the operations the data flows into, so that at any later point a value's taint records where it came from. The classic security framing has three roles: **sources** taint data as it enters (e.g. user input gets an `UNTRUSTED` taint), **sinks** check the taint before performing a dangerous operation, and **sanitizers** are the only places allowed to remove or change the taint. A policy such as "no `UNTRUSTED` data may reach a sink unsanitized" or "no `SECRET` data may reach output" then becomes a runtime-checkable property — a far stronger oracle than waiting for a crash. (The closely related per-input-origin variant tracked by this wiki is [[DynamicTaintTracking]].)

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] implements dynamic taint analysis as a *library* rather than via binary/VM instrumentation, following Conti et al. (2010): it subclasses Python's `str` to carry the taint and overrides the string methods to propagate it. [[TaintedString|`tstr`]] attaches a single taint label to a whole string; [[CharacterOrigin|`ostr`]] refines this to a per-character *origin* index. The chapter demonstrates all three roles on an `eval()`-vulnerable database — `sanitize()` whitelists characters and re-taints as `TRUSTED`, `TrustedDB`/`TaintedDB` are the sinks that check the taint — and on a privacy leak where `SECRET`-tainted memory must not reach the reply. Crucially it documents *where the technique fails*: taint is lost across string→number conversions, across calls into Python's internal C code (`''.join(...)` loses origins that `+` keeps), and across [[ImplicitInformationFlow|implicit/control flow]]. The recommended mitigation is to treat any untainted value as worst-case and re-taint from its source.

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] positions [[ConcolicExecution|concolic execution]] as the more complete (and far costlier) alternative to dynamic taint analysis: where taint records *which* input bytes reach a place, concolic execution records *what must be true* of the input to reach it — a full [[PathConstraint|path condition]] solvable by an [[SMTSolver|SMT solver]]. The chapter reuses the same library-instrumentation idea (Python subclassing / proxy objects) but on `zbool`/`zint`/`zstr` proxies that carry symbolic Z3 expressions instead of taint labels. It explicitly notes the two techniques share the same blind spots — implicit/indirect control flow and calls into internal C functions discard the analysis information — but concludes that concolic-derived predicates make a stronger bug indicator than taints, "at a much larger runtime cost," so real-time analysis is usually infeasible.

## Connections
- [[InformationFlow]] — the property dynamic taint analysis is used to track.
- [[ConcolicExecution]] / [[SymbolicExecution]] — the richer (costlier) Ch 20/21 alternative that records path conditions, not just byte provenance.
- [[DynamicTaintTracking]] — the origin-precise flavor (each input position is its own taint/"color"); the umbrella concept from [[fuzzingbook-18-grammar-miner|Ch 18]] whose mechanism this chapter builds.
- [[TaintedString]] (`tstr`) / [[CharacterOrigin]] (`ostr`) — the two concrete implementations in Ch 19.
- [[CodeInjection]] — the integrity threat caught by source→sink taint policies.
- [[TaintDirectedFuzzing]] — extends taint analysis from oracle to fuzzing guidance.
- [[ImplicitInformationFlow]] — the principal blind spot of dynamic taint analysis.
- [[fuzzingbook-20-concolic-fuzzer|Ch 20]] — symbolic execution as the more complete (and costlier) alternative.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
- [[fuzzingbook-20-concolic-fuzzer]] — *The Fuzzing Book* Ch 20, "Concolic Fuzzing" (concolic execution as the richer, costlier alternative to taint analysis).
