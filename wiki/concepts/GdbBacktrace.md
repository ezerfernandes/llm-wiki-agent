---
title: "GDB Backtrace (`bt` / `where` / `frame N`)"
type: concept
tags: [debugging, gdb, stack, call-stack, c-language]
sources: [dis-3-1-gdb]
last_updated: 2026-05-17
---

# GDB Backtrace (`bt` / `where` / `frame N`)

The [[GDB]] command family that **inspects the active call stack** at the current halt point — the runtime view of the [[ExecutionStack|execution stack]] of [[StackFrame|stack frames]] [[dis-1-4-functions|DIS Ch 1.4]] introduced. [[dis-3-1-gdb|Ch 3.1]] codifies three aliases for the same operation plus the per-frame switch:

| Command | Behavior |
|---|---|
| `backtrace` (`bt`) | Print the full active call stack, innermost frame first. Each line shows `#N <function>(args) at file:line`. |
| `where` | Alias for `bt`. |
| `frame N` (`f N`) | Switch the **inspection context** to frame `N` — subsequent [[GdbPrint|`print var`]] reads that frame's [[LocalVariable|locals]] / [[FunctionParameter|parameters]]. |

## The headline workflow

[[dis-3-1-gdb|Ch 3.1]]'s canonical crash-debugging recipe:

```text
$ gdb ./buggy
(gdb) run arg1 arg2
... segfault ...
Program received signal SIGSEGV, Segmentation fault.
0x000000000040118a in dereference (p=0x0) at buggy.c:7
7         return *p;
(gdb) bt
#0  0x000000000040118a in dereference (p=0x0) at buggy.c:7
#1  0x00000000004011b3 in process (data=0x7fffffffe1c0) at buggy.c:15
#2  0x00000000004011d2 in main (argc=3, argv=0x7fffffffe2c8) at buggy.c:22
(gdb) frame 1
#1  0x00000000004011b3 in process (data=0x7fffffffe1c0) at buggy.c:15
(gdb) print *data
$1 = {name = "...", ptr = 0x0}
```

The `bt` output **immediately localizes** the crash: frame `#0` is the offending instruction, and the chain `#0 ← #1 ← #2` shows the call path. `frame 1` switches context to `process` so `print *data` reads the caller's view of the data that contained the null pointer.

## What's in a frame, per debugger

Each `bt` line names:
- **Frame index** (`#0` = innermost / current, increasing toward `main`).
- **Saved instruction pointer** (the return address into the caller).
- **Function name** and **argument values** as captured at call time.
- **Source location** (`file:line`).

This is the runtime materialization of [[dis-1-4-functions|Ch 1.4]]'s stack-of-frames model — what [[StackFrame]] described statically, `bt` walks dynamically.

## `frame N` — the inspection-context switch

After `frame N`, GDB treats frame `N` as **current** for the purposes of:
- [[GdbPrint|`print expr`]] — variable names resolve in frame `N`'s scope.
- `info locals` — list all locals visible in frame `N`.
- `info args` — list the parameters frame `N` was called with.
- [[GdbList|`list`]] — show source around frame `N`'s current line.

This is the mechanism for **"what did the caller think it was passing me?"** — descend through frames to read intermediate state without rerunning the program.

## Use cases

- **Crash localization** — `bt` immediately after a [[SegmentationFault|segfault]] to find the offending function and its call chain.
- **Stack-overflow diagnosis** — a runaway recursion produces a very long `bt`; the repeating pattern of frames identifies the recursion point.
- **State at a breakpoint** — after halting at a [[Breakpoint|breakpoint]] deep in a call tree, `bt` shows how you got there.
- **Post-mortem** — `gdb ./a.out core` + `bt` reads the call stack from the [[CoreFile|core file]] of an already-terminated process.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[StackFrame]] — the per-call record `bt` walks.
- [[ExecutionStack]] — the LIFO substrate frames live on.
- [[FunctionCall]] / [[ReturnStatement]] — push / pop frame events.
- [[FunctionParameter]] / [[LocalVariable]] — what `info args` / `info locals` show in the current frame.
- [[GdbPrint]] — reads expressions in the current frame's scope.
- [[GdbList]] — shows source around the current frame's line.
- [[Breakpoint]] / [[StepDebug]] — the halt mechanisms that make `bt` interesting.
- [[CoreFile]] — alternative input source (post-mortem rather than live).
- [[SegmentationFault]] — the crash that motivates an immediate `bt`.
- [[MainFunction]] — the *outermost* frame on every healthy `bt`.
