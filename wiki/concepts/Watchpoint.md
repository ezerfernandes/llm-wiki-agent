---
title: "Watchpoint"
type: concept
tags: [debugging, gdb, debugging-primitive, memory-tracking]
sources: [dis-3-1-gdb, dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# Watchpoint

A [[Debugger|debugger]] primitive that **pauses the debuggee whenever a chosen memory location's value changes** — the *write-triggered* counterpart to a [[Breakpoint|breakpoint]] (which is *PC-reach-triggered*). [[dis-3-1-gdb|DIS Ch 3.1]] mentions watchpoints as a deferred companion to breakpoints; [[dis-3-2-gdb-commands|Ch 3.2]] uses [[GdbDisplay|`display`]] for the polling analog. The full GDB watchpoint command is [[GdbWatch|`watch`]].

## How it differs from a breakpoint

| Dimension | [[Breakpoint|`break`]] | `watch` |
|---|---|---|
| **Trigger** | PC reaches a chosen instruction (a *code location*). | Value at a chosen address changes (a *data location*). |
| **Hardware support** | Optional — software trap (`int3`) is the fallback. | **Hardware-assisted on most architectures** (x86: DR0–DR3 debug registers; ARM: watchpoint control units). 1–4 hardware slots typical. |
| **Software fallback** | Always works; just patches one byte. | Single-step the whole program checking the address after each instruction — **catastrophically slow** without hardware. |
| **Set with** | `break <loc>` | `watch <expr>` |

## GDB watchpoint variants

```text
watch x                # halt when x changes
watch p->field         # halt when p->field changes
watch *(int *)0x7fff…  # halt when the int at this address changes
rwatch x               # halt when x is READ (read-watchpoint)
awatch x               # halt when x is accessed (read OR write)
```

The expression is evaluated in the current [[VariableScope|scope]] when set — the watchpoint follows the **address** that `x` resolved to, not the name. Once the variable falls out of scope, GDB reports *"watchpoint X deleted because the program has left the block in which its expression is valid"*.

## The canonical use case

**Find the line that corrupts a variable.**

```text
(gdb) break main
(gdb) run
... halt at main ...
(gdb) watch important_state
Hardware watchpoint 2: important_state
(gdb) cont
Hardware watchpoint 2: important_state
Old value = 42
New value = 0xdeadbeef
0x000000000040118a in corrupt () at bug.c:23
23          *aliased_ptr = 0xdeadbeef;
```

GDB localizes the corruption to the exact line that wrote the bad value — no guessing where in 10,000 lines of code the variable got clobbered.

## Limits

- **Hardware slots are scarce** — most platforms ship 4 hardware watchpoints. `set can-use-hw-watchpoints 0` forces software fallback (single-step-and-check, often 100×+ slowdown).
- **Watch-by-value vs. watch-by-address** — `watch x` follows the address `x` resolves to *at the time the watchpoint is set*; if the variable goes out of scope, the watchpoint dies. To follow a heap object across function boundaries, watch via dereference: `watch *(int *)(p)` after pinning `p`.
- **Optimized-out variables** — under [[CompilerOptimization|`-O2`]], `x` may live in a register with no stable address; the watchpoint cannot be set.

## Relation to other GDB primitives

- [[Breakpoint]] — *"halt at this code location"*; the dual of a watchpoint.
- [[ConditionalBreakpoint]] — *"halt at this code location if condition"*; conditions on a watchpoint are also supported (`watch x if x > 100`).
- [[GdbDisplay|`display`]] — *"print this expression at every pause"*; the **passive-polling** alternative when watchpoints aren't available.
- [[GdbBreakpointManagement|`enable` / `disable` / `delete`]] — same lifecycle commands apply to watchpoints (they share GDB's breakpoint table; `info breakpoints` lists both).

## Connections

- [[dis-3-1-gdb]] — first mention (named-and-deferred).
- [[dis-3-2-gdb-commands]] — `display` is the polling analog.
- [[Breakpoint]] — the dual primitive.
- [[ConditionalBreakpoint]] — both support attached conditions.
- [[GdbDisplay]] — the passive-polling fallback.
- [[GdbBreakpointManagement]] — shared lifecycle commands.
- [[GdbInfo]] — `info breakpoints` lists watchpoints too.
- [[GDB]] / [[Debugger]] — the host tool.
- [[Pointer]] / [[CMemoryAddress]] — what a watchpoint addresses.
- [[CompilerOptimization]] — the orthogonal axis that can prevent watchpoints (no stable address).
