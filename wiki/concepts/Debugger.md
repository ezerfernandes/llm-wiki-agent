---
title: "Debugger"
type: concept
tags: [debugging, tooling, c-language, systems-programming, process-control]
sources: [dis-3-1-gdb, fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# Debugger

A **debugger** is *"a program that controls the execution of another program… it allows programmers to see what their programs are doing as they run"* — [[dis-3-1-gdb|DIS Ch 3.1]]'s opening definition. The defining property is **process control**: a debugger is itself a process (the **debugger process**) that loads or attaches to a target process (the **debuggee** / **inferior**) and can pause, resume, single-step, inspect state, and modify state of the debuggee.

## What it lets you do

[[dis-3-1-gdb|Ch 3.1]] enumerates the canonical operations for an interactive debugger:

- **Pause execution** at chosen source locations ([[Breakpoint|breakpoints]]) or program-state conditions (conditional / watch).
- **Single-step** through code one source line at a time ([[StepDebug|`next` / `step`]]) to observe state transitions.
- **Inspect program state** — variable values ([[GdbPrint|`print`]]), call stack ([[GdbBacktrace|`backtrace`]]), CPU registers, memory contents.
- **Switch contexts** between [[StackFrame|stack frames]] to read suspended callers' [[LocalVariable|locals]] / [[FunctionParameter|parameters]].
- **Post-mortem analysis** — open a [[CoreFile|core file]] (OS dump of a crashed process's memory + registers) and ask the same questions as in a live session.

## Two bug taxonomies a debugger addresses

[[dis-3-1-gdb|Ch 3.1]] frames the use cases through the bug class:

1. **Logic bugs** — program runs to completion but produces wrong output. Debugger usage: set [[Breakpoint|breakpoint]] near the suspected mis-step, inspect input / intermediate / output state, identify the divergence.
2. **Crashes** — program terminates abnormally, typically with a [[SegmentationFault|segmentation fault]] in [[CLanguage|C]]. Debugger usage: run under the debugger to halt at the crash site (or open a [[CoreFile|core file]] post-mortem), then [[GdbBacktrace|`backtrace`]] to find the offending call chain.

The two-axis split maps onto Ch 2.4–2.6's memory-failure-mode list — [[NullPointer|null-deref]] / [[UseAfterFree|use-after-free]] / [[BufferOverflow|buffer overflow]] all surface as **crashes** for the debugger, while incorrect-result bugs (off-by-one, sign error, control-flow bug) are **logic bugs**.

## What the OS provides

A debugger is not magic — it requires OS cooperation. The Unix mechanism (named-and-deferred by [[dis-3-1-gdb|Ch 3.1]] and developed in later OS chapters) is [[Ptrace|`ptrace(2)`]]: a process declares itself debuggable (`PTRACE_TRACEME`) or attaches to another (`PTRACE_ATTACH`), and the OS routes signals / process control events to the tracer.

## Categories

- **Source-level debugger** — operates in terms of source-language constructs (line numbers, variable names, types). Requires [[DebugSymbol|debug symbols]] from [[GccDashG|`gcc -g`]]. [[GDB]] is the canonical example.
- **Machine-level debugger** — operates on instructions, registers, memory addresses. GDB falls back to this mode for code compiled without `-g`.
- **GUI wrapper** — front-end on top of a CLI debugger; [[DataDisplayDebugger|DDD]] wraps GDB.
- **Remote debugger** — debuggee runs on a different machine; debugger speaks a wire protocol. GDB's **Remote Serial Protocol** is the embedded-systems case ([[rust-embedded-book-intro-tooling|Embedded Rust I.4]] uses GDB + [[OpenOCD]] / [[ProbeRs]] to debug ARM Cortex-M targets).

## From The Fuzzing Book — Reducing Failure-Inducing Inputs
[[fuzzingbook-16-reducer|Ch 16]] addresses debugging from the *input* side rather than the *execution-control* side this page describes. Before a programmer ever opens a debugger, a large failure-inducing input (typically from a fuzzer) should be reduced to its essential core — [[InputReduction|input reduction]] via [[DeltaDebugging|delta debugging]] ([[DDMin|`ddmin`]]) or [[GrammarReducer|grammar-based reduction]]. A [[OneMinimality|1-minimal]] reproducer shrinks the search space, shortens executions, simplifies program state, and de-duplicates reports — making the subsequent debugger session (breakpoints, single-stepping, `backtrace`) far more tractable. Reduction is a complementary, *pre-debugger* technique to the interactive process control of [[GDB]].

## Connections

- [[InputReduction]] / [[DeltaDebugging]] / [[GrammarReducer]] — automatic input minimization that precedes and eases interactive debugging.
- [[dis-3-1-gdb]] — introducing source.
- [[GDB]] — the canonical C debugger this concept abstracts.
- [[Breakpoint]] / [[StepDebug]] / [[GdbBacktrace]] / [[GdbPrint]] — the operations a debugger provides.
- [[CoreFile]] — the post-mortem input.
- [[DebugSymbol]] — the metadata source-level debugging requires.
- [[GccDashG]] — the build flag that produces debug symbols.
- [[CompilerOptimization]] — the build setting debuggers prefer **off**.
- [[StackFrame]] / [[ExecutionStack]] — what `backtrace` walks.
- [[SegmentationFault]] — the crash class debuggers diagnose.
- [[DataDisplayDebugger]] — the GUI front-end.
- [[Valgrind]] — sibling C debugging tool; covers **memory-error detection** as a complement to GDB's **execution control**.
- [[OnChipDebugging]] / [[OpenOCD]] / [[ProbeRs]] — the embedded analogue from [[TheEmbeddedRustBook|Embedded Rust]].
