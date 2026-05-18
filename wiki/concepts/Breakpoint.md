---
title: "Breakpoint"
type: concept
tags: [debugging, gdb, c-language, control-flow, debugging-primitive]
sources: [dis-3-1-gdb]
last_updated: 2026-05-17
---

# Breakpoint

A **breakpoint** is a marker that tells a [[Debugger|debugger]] to **pause** the debuggee at a chosen location — almost always a source line, function entry, or instruction address — handing control back to the user for inspection. [[dis-3-1-gdb|DIS Ch 3.1]] frames it as *"a location in your program where you'd like execution to pause so you can examine the program's state"*. It is the debugger's primary **control primitive**.

## Setting in GDB

[[dis-3-1-gdb|Ch 3.1]] covers the four canonical [[GDB]] forms:

- **By line in current file** — `break 42` pauses at line 42 of the currently-listed file.
- **By line in named file** — `break main.c:42` qualifies the file.
- **By function name** — `break compute_sum` pauses at the function's entry.
- **By address** — `break *0x4011a0` (machine-level, used when source isn't available).

GDB assigns each breakpoint a numeric ID printed at creation; subsequent commands (`disable N` / `enable N` / `delete N` / `info breakpoints`) reference that ID.

## How the program reaches a breakpoint

The breakpoint is **dormant** until execution begins. The flow [[dis-3-1-gdb|Ch 3.1]] walks:

1. Set breakpoint with `break <loc>`.
2. Run program with [[GdbRun|`run [args]`]] — program executes from `main`.
3. When execution reaches the breakpoint location, GDB **halts** the debuggee **before** executing that line and returns to the GDB prompt.
4. User inspects state ([[GdbPrint|`print`]] / [[GdbList|`list`]] / [[GdbBacktrace|`bt`]]) at that exact moment.
5. User advances with [[StepDebug|`next` / `step`]] one line at a time, or `cont` to resume until the next breakpoint.

## Mechanism (named-and-deferred)

Under the hood, GDB implements a software breakpoint by **overwriting the target instruction byte** with an architecture-specific trap instruction (`int3` / `0xCC` on x86) — when the CPU executes it, the OS delivers a signal (`SIGTRAP`) that the debugger catches via [[Ptrace|`ptrace`]]. GDB then restores the original instruction byte, presents the prompt, and (on resume) single-steps the original instruction before reinstalling the trap. **Hardware breakpoints** (limited count, set in CPU debug registers) are the alternative for read-only / Flash code. Ch 3.1 does not unpack these mechanisms — left for later architecture chapters.

## Conditional and one-shot variants

[[dis-3-1-gdb|Ch 3.1]] mentions **conditional breakpoints** in passing — `break 42 if x > 100` only halts when the condition holds. Used to skip irrelevant iterations of a loop while debugging a corner case. (**Watchpoints** — pause when a *memory location* changes value — are a related primitive deferred to later coverage.)

## When to set one

[[dis-3-1-gdb|Ch 3.1]]'s heuristic: place the **first breakpoint just before the suspected misbehavior**, then [[StepDebug|`step`]] / `next` through the suspect region inspecting variables. For crash debugging, no breakpoint is needed — `run` until the crash, then [[GdbBacktrace|`bt`]] at the halt site.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool category.
- [[StepDebug]] — the *advance* primitives a breakpoint hands off to.
- [[GdbBacktrace]] — the *inspect* primitive most commonly run right after hitting a breakpoint.
- [[GdbRun]] — the command that launches the debuggee so breakpoints can fire.
- [[GdbPrint]] / [[GdbList]] — the variable / source inspection commands run at a breakpoint pause.
- [[Ptrace]] — the OS mechanism (named-and-deferred) underlying breakpoint trap delivery.
- [[SegmentationFault]] — the *implicit* breakpoint: a crash also halts the debuggee at the offending instruction.
- [[StackFrame]] — what `bt` walks once the breakpoint fires.
