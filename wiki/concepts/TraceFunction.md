---
title: "Trace Function (sys.settrace)"
type: concept
tags: [python, dynamic-analysis, instrumentation, coverage, fuzzing, debugging]
sources: [fuzzingbook-04-coverage]
last_updated: 2026-06-06
---

# TraceFunction

A **trace function** is a callback installed with Python's `sys.settrace(f)` that the interpreter invokes for events during execution — most usefully on **every line executed**. It is the primitive that makes lightweight [[DynamicAnalysis|dynamic analysis]] (and hence [[Coverage|coverage measurement]]) easy in Python without recompiling or rewriting the target.

## Signature and frame access
The trace function has the signature `f(frame, event, arg) -> Optional[Callable]`:

- `frame` — the current stack frame. `frame.f_code.co_name` is the executing function's name, `frame.f_lineno` is the current line number, and `frame.f_locals` holds the live local variables and arguments.
- `event` — a string such as `"line"` (a new line was reached), `"call"` (a function is being entered), or `"return"`.
- `arg` — event-specific extra data (for `"return"`, the value being returned).

Returning the function itself keeps it installed for the traced scope. `sys.gettrace()` reads the currently installed function; passing `None` to `sys.settrace` turns tracing off.

## From The Fuzzing Book — Code Coverage
[[fuzzingbook-04-coverage|Ch 4]] introduces `sys.settrace` as "an ideal tool for dynamic analysis." A prototype `traceit(frame, event, arg)` filters on `event == 'line'` and appends `frame.f_lineno` to a global `coverage` list; `cgi_decode_traced()` brackets a call with `sys.settrace(traceit)` … `sys.settrace(None)`. The chapter then wraps this in the **`Coverage`** context-manager class: `__enter__` saves `sys.gettrace()` and installs `self.traceit`, `__exit__` restores the saved function, and `traceit` records `(frame.f_code.co_name, frame.f_lineno)` `Location` pairs (skipping `__exit__` itself to avoid tracing the harness). The same mechanism underpins the chapter's [[LineCoverage|statement-]] and [[BranchCoverage|branch-coverage]] tooling and recurs throughout the book wherever execution must be observed.

## Connections
- [[Coverage]] / [[LineCoverage]] / [[BranchCoverage]] — coverage tooling built directly on the trace function.
- [[DynamicAnalysis]] — observing real execution (vs static analysis of source); trace functions are its Python workhorse.
- [[Python]] — `sys.settrace` is a CPython interpreter hook.
- [[Debugger|Debuggers]] — the same trace-function/frame machinery powers Python debuggers and profilers.
- [[fuzzingbook-04-coverage|Ch 4]] — where this is introduced for coverage.

## Sources
- [[fuzzingbook-04-coverage]] — *The Fuzzing Book* Ch 4, "Code Coverage."
