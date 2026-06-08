---
title: "Tainted String (tstr)"
type: concept
tags: [security, taint-analysis, information-flow, python, string, dynamic-analysis, fuzzing]
sources: [fuzzingbook-19-information-flow]
last_updated: 2026-06-06
---

# Tainted String (`tstr`)

A **tainted string** is a string that carries a *taint* label recording its provenance or security level, propagated automatically through every operation that derives a new string from it. In [[fuzzingbook-19-information-flow|The Fuzzing Book]] this is the `tstr` class — a subclass of Python's `str` that adds a single `taint` attribute. It is the coarsest level of [[DynamicTaintAnalysis|dynamic taint analysis]]: one label per whole string.

## From The Fuzzing Book — Tracking Information Flow
[[fuzzingbook-19-information-flow|Ch 19]] builds `tstr` as the first taint mechanism. Because `str` is immutable and never calls `__init__()` on subclasses, `tstr` hooks `__new__()` to construct the underlying `str` and `__init__()` to record `self.taint`. Propagation is achieved by wrapping the string methods: `make_str_wrapper(fun)` produces a proxy that runs the original method and re-wraps the result via `create()` (which copies the taint); `informationflow_init_1()` installs these proxies over ~25 methods (`__getitem__`, `__add__`, `__mul__`, `__mod__`, `lower`, `strip`, `replace`, `join`, …), and a hand-written `__radd__()` handles `str + tstr`. Thus `tstr('hello', taint='LOW')[1:3]`, `tstr('foo', taint='HIGH') + 'bar'`, and `'%s' % thello` all yield tainted results. `clear_taint()` / `has_taint()` support sanitization. Two limitations surface: concatenating two differently-tainted `tstr` strings lets `__add__()` take precedence over `__radd__()`, silently dropping the right operand's taint (taint-conflict resolution is application-dependent); and a single whole-string taint over-approximates — the `heartbeat()` example marks *every* reply `SECRET` even when no secret was read. Both motivate the per-character [[CharacterOrigin|`ostr`]] refinement. The exercises extend the same pattern to a tainted integer (`tint`).

## Connections
- [[DynamicTaintAnalysis]] / [[DynamicTaintTracking]] — `tstr` is the simplest concrete taint carrier.
- [[CharacterOrigin]] (`ostr`) — the finer subclass that fixes `tstr`'s composition/over-tainting problems by tracking per-character origins.
- [[InformationFlow]] — what `tstr` is used to track (e.g. `TRUSTED`/`UNTRUSTED`, `SECRET`/`PUBLIC`).
- [[CodeInjection]] — `TrustedDB` uses `tstr` taints to reject untrusted SQL.
- [[fuzzingbook-19-information-flow]] — the chapter that defines `tstr`.

## Sources
- [[fuzzingbook-19-information-flow]] — *The Fuzzing Book* Ch 19, "Tracking Information Flow."
