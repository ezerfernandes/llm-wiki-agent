---
title: "GDB `thread <N>` (Thread Context Switch)"
type: concept
tags: [gdb, debugging, threads, multithreading, pthreads, c, dive-into-systems]
sources: [dis-3-6-gdb-pthreads]
last_updated: 2026-05-17
---

# GDB `thread <N>`

[[GDB]] command that **switches the inspection context to a specific thread**, identified by the GDB thread number ([[GdbInfoThreads|`info threads`]]'s leftmost column). The multi-threaded analog of [[GdbBacktrace|`frame N`]]'s single-thread stack-frame switch.

## Semantics

After `thread 3`:

- [[GdbBacktrace|`bt`]] / `where` — prints **thread 3's** call stack.
- [[GdbPrint|`print var`]] — resolves `var` in **thread 3's** topmost [[StackFrame|stack frame]] / [[VariableScope|scope]].
- [[GdbInfo|`info locals`]] / [[GdbInfo|`info args`]] — prints **thread 3's** [[LocalVariable|locals]] and [[FunctionParameter|parameters]].
- [[GdbList|`list`]] — shows source around **thread 3's** paused position.
- [[CpuRegister|`info registers`]] — dumps **thread 3's** register file.

The asterisk `*` in [[GdbInfoThreads|`info threads`]] output relocates to the new current thread.

## Why per-thread switching matters

Each thread owns a **separate [[ExecutionStack|execution stack]]** with its own [[StackFrame|frames]] / [[LocalVariable|locals]] / [[FunctionParameter|parameters]] / [[CpuRegister|register]] snapshot. Variables sharing a name across threads (e.g., loop counters in identical worker functions) resolve to different memory locations depending on the current thread context. Without `thread <N>`, [[GdbPrint|`print`]] silently inspects only **whichever thread tripped the [[Breakpoint|breakpoint]]**, masking the state of every other thread.

## Default stop-the-world

When **any** thread hits a [[Breakpoint|breakpoint]], **all** threads pause by default. After the global halt, `info threads` + `thread <N>` is how you tour each thread's state. [[GdbSet|`set scheduler-locking`]] can flip the default so only the triggering thread halts.

## Connections

- [[dis-3-6-gdb-pthreads]] — *Dive into Systems* Ch 3.6 *Debugging Multi-threaded Programs* introduces this command.
- [[GDB]] — the host debugger.
- [[GdbInfoThreads]] — the enumeration command that supplies the thread number.
- [[GdbThreadApply]] — the broadcast complement (run a command across **all** threads instead of switching to one).
- [[GdbBacktrace]] — `bt` is the canonical first command after a `thread <N>` switch.
- [[GdbPrint]] / [[GdbInfo]] / [[GdbList]] — frame-scope-resolving commands that follow the thread switch.
- [[Pthreads]] — the threading library whose threads are being switched between.
- [[Breakpoint]] — thread-qualified `break <loc> thread <N>` constrains which thread the halt fires on.
- [[Thread]] — the abstraction being switched between.
- [[StackFrame]] / [[ExecutionStack]] — the per-thread runtime state `thread <N>` re-binds inspection to.
