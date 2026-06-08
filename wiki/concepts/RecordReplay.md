---
title: "Record and Replay"
type: concept
tags: [testing, fuzzing, carving, record-replay, determinism, python]
sources: [fuzzingbook-25-carver]
last_updated: 2026-06-06
---

# Record and Replay

**Record-and-replay** captures the observable interactions of a program (here, its function calls and arguments) during one execution and then re-executes them later — as a whole or selectively — without re-running the original driver. It is the paradigm underlying [[TestCarving|carving]]: record real calls during a system test, replay each as a fast standalone [[UnitTesting|unit test]].

## From The Fuzzing Book — Carving Unit Tests
[[fuzzingbook-25-carver|Ch 25]] applies record-and-replay at the *function-call* level. The **record** side is the [[Carver|`Carver`/`CallCarver`]] tracer, which captures each call's `(parameter, value)` arguments via `sys.settrace`. The **replay** side renders those calls back into runnable code (`simple_call_string()`, then `call_string()`) and runs them with `eval`. The chapter names three replay challenges that make general record-and-replay hard:

1. **Name visibility** — the called function's name must be in scope; internal/module-private names must be made visible.
2. **External resources** — values referring to files, sockets, or network resources cannot simply be re-created from a recording.
3. **Complex objects** — non-primitive argument objects must be reconstructed, which the chapter solves with [[Serialization|pickling]].

Because of (1) and (2), only about a quarter of the calls carved from `webbrowser()` successfully re-run, even though most convert to call strings. Replay is reliable for functions that behave as pure transforms of their arguments — the same determinism caveat that limits the `ResultCarver` [[RegressionTesting|regression]] exercise (values depending on time/randomness/external state may differ on replay).

## Connections
- [[TestCarving]] — the technique built on record-and-replay.
- [[Carver]] — the recorder.
- [[Serialization]] — solves the complex-object replay challenge.
- [[UnitTesting]] — replayed calls become unit tests.
- [[RegressionTesting]] — replaying with recorded return values yields regression checks (limited by determinism).
- [[Coverage]] — the `sys.settrace` mechanism the recorder uses.
- [[OfflineReplayEnvironment]] — a related record/replay idea in a different (RL/recommendation) setting.

## Sources
- [[fuzzingbook-25-carver]] — *The Fuzzing Book* Ch 25, "Carving Unit Tests."
