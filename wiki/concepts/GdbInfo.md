---
title: "GDB `info` (Reflection Sub-commands)"
type: concept
tags: [debugging, gdb, debugging-primitive, reflection]
sources: [dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `info` (Reflection Sub-commands)

The [[GDB]] command that **reflects over the debuggee's state and GDB's own bookkeeping**. `info` is a *hub* command — bare `info` is meaningless; you invoke it with a sub-command naming what you want to know.

## Sub-command surface

[[dis-3-2-gdb-commands|Ch 3.2]] names the canonical set:

| Sub-command | Shows |
|---|---|
| `info locals` | All [[LocalVariable|local variables]] visible in the current [[StackFrame|frame]] with their current values. |
| `info args` | All [[FunctionParameter|parameters]] of the current frame's function with their current values. |
| `info break` / `info breakpoints` | The full breakpoint table — ID, type, enable state, location, hit count, condition (for [[ConditionalBreakpoint|conditional breakpoints]]). |
| `info registers` | The CPU register file — `%rax` / `%rbx` / `%rcx` / `%rdx` / `%rsi` / `%rdi` / `%rbp` / `%rsp` / `%rip` / `%eflags` / … (architecture-specific). |
| `info frame` | The current frame's saved [[InstructionPointer|instruction pointer]], saved frame pointer, caller, frame address. |
| `info display` | All active [[GdbDisplay|auto-display]] expressions. |
| `info threads` | All threads in a multithreaded debuggee with their states. |
| `info sharedlibrary` | All dynamically loaded shared objects with their load addresses. |
| `info functions` | All functions known to the debuggee (filter via regex). |
| `info variables` | All globals known to the debuggee. |
| `info source` | The current source file's compilation details. |

## The three sub-commands [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]] use most

- **`info locals`** — at any halt, see every local without naming them one by one. Pairs with [[GdbBacktrace|`frame N`]] for caller-frame inspection: `frame 2; info locals` shows two-frames-up locals.
- **`info registers`** — the **hardware view**. What's actually in `%rax` right now, what `%rip` points at, what `%rsp` is. The bridge between [[CLanguage|C]] source debugging and assembly debugging (mandatory when you switch to [[GdbExamineMemory|`x/i $pc`]] instruction-level stepping).
- **`info frame`** — the per-frame metadata behind [[GdbBacktrace|`bt`]]: which return address gets popped on `return`, where this frame's parameters live, what the caller's frame pointer was. The runtime view of [[StackFrame]]'s static description.

## Why GDB has `info` instead of separate commands

GDB's command namespace would balloon if every reflection query got a top-level command (`locals`, `args`, `regs`, `breakpoints`, …). The `info` prefix keeps them organized — and TAB-completion after `info ` enumerates the full sub-command list interactively.

## Connections

- [[dis-3-2-gdb-commands]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[GdbBacktrace]] — `info frame` is the per-frame deep-dive after `bt` localizes which frame matters.
- [[GdbPrint]] / [[GdbDisplay]] / [[GdbExamineMemory]] — sibling inspection commands; `info` is the *reflection* slice (what exists), they are the *value* slice (what it holds).
- [[StackFrame]] / [[LocalVariable]] / [[FunctionParameter]] — what `info locals` / `info args` / `info frame` show.
- [[Breakpoint]] / [[ConditionalBreakpoint]] / [[GdbBreakpointManagement]] — what `info breakpoints` enumerates.
- [[InstructionPointer]] — what `info registers` exposes ($rip / $pc).
