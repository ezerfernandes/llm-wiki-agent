---
title: "Character Origin Tracking (ostr)"
type: concept
tags: [security, taint-analysis, information-flow, python, string, dynamic-analysis, fuzzing]
sources: [fuzzingbook-19-information-flow]
last_updated: 2026-06-06
---

# Character Origin Tracking (`ostr`)

**Character-origin tracking** attaches a taint not to a whole string but to *each character*: every character remembers the index in the original input it came from (its *origin*). A string composed from several sources then carries a per-character origin list, so one can ask precisely *which input positions a given fragment derived from*. In [[fuzzingbook-19-information-flow|The Fuzzing Book]] this is the `ostr` class, a refinement of [[TaintedString|`tstr`]] and the fine-grained form of [[DynamicTaintTracking|dynamic taint tracking]] (each input index is effectively its own "color").

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] introduces `ostr` to solve the composition problem that whole-string [[TaintedString|`tstr`]] taints cannot. An `ostr` stores `self.origin`, a list of integer indices (default starting at `0`, or `origin=N`), with `UNKNOWN_ORIGIN = -1` for characters of unknown provenance. Because origin is per-character, it splices correctly under composition, so the chapter must re-implement many string methods to maintain it: `__getitem__` (int → single origin, slice → sliced origin list), `__add__`/`__radd__` (concatenate origin lists, padding `str` operands with `-1`), `split`/`rsplit`/`splitlines`, `replace`, `strip`/`lstrip`/`rstrip`, `expandtabs`, `join`, `partition`/`rpartition`, `ljust`/`rjust`, `__mod__`/`__rmod__`, and the case-changing methods. The helper `x(i)` extracts the characters whose origin equals input index `i`, and origin queries reduce to set operations (`set(frag.origin) <= set(src.origin)`). This precision exactly detects the `heartbeat()` privacy leak: with a `SECRET_ORIGIN = 1000` secret, a safe reply has all-`UNKNOWN_ORIGIN` characters, while a leaking reply contains characters with origins `>= SECRET_ORIGIN`. Origins are also the backbone of [[TaintDirectedFuzzing|taint-directed fuzzing]] (each grammar token gets a distinct origin so the rules reaching a sink can be identified). Like all such tracking, origins are lost across number conversions, internal C calls, and [[ImplicitInformationFlow|implicit flow]].

## Connections
- [[TaintedString]] (`tstr`) — the coarser superclass `ostr` extends with origins.
- [[DynamicTaintTracking]] / [[DynamicTaintAnalysis]] — `ostr` is the origin-precise mechanism; [[fuzzingbook-18-grammar-miner|Ch 18]]'s grammar miner can use `ostr` origin-inclusion in place of substring matching.
- [[InformationFlow]] — origins make per-character flow checkable (e.g. secret-leak detection).
- [[TaintDirectedFuzzing]] — uses per-token grammar origins to trace input back to grammar rules.
- [[ImplicitInformationFlow]] — origins, like all dynamic taints, do not survive control-flow-only dependence.
- [[fuzzingbook-19-information-flow]] — the chapter that defines `ostr`.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
