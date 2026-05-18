---
title: "Step Debugging (next / step / continue)"
type: concept
tags: [debugging, gdb, c-language, control-flow, debugging-primitive]
sources: [dis-3-1-gdb]
last_invariant: distinct-from-pointer-step
last_updated: 2026-05-17
---

# Step Debugging (`next` / `step` / `continue`)

After a [[Debugger|debugger]] halts the debuggee at a [[Breakpoint|breakpoint]] (or at a crash), the user advances execution one **source line** at a time. [[dis-3-1-gdb|DIS Ch 3.1]] codifies the **three [[GDB]] step primitives**:

| Command | Behavior |
|---|---|
| `next` (`n`) | Execute the next source line. If it contains a function call, treat the **entire call** as one step — the called function runs to completion without the user seeing its internals. |
| `step` (`s`) | Execute the next source line. If it contains a function call, **enter** the called function and halt at its first executable line. |
| `cont` (`c`) | Resume execution until the next breakpoint (or program termination, or crash). |

## The `next` vs `step` distinction

The chapter's headline navigation rule:

> *"To inspect the function's behavior, use `step` instead of `next`."*

- Use `next` to treat called functions as **opaque** — useful when you're debugging the *caller's* logic and the callee is known-good (e.g., [[Printf|`printf`]], library calls).
- Use `step` to **descend into** a called function — useful when the bug might be in the callee, or when you want to see how the callee uses the arguments the caller passed.

The two commands are otherwise identical: both advance one source line, both halt before executing the next, both leave you at the GDB prompt for inspection.

## When `step` falls back to `next`

If the called function has no [[DebugSymbol|debug symbols]] (e.g., it's a library function compiled without [[GccDashG|`-g`]]), `step` cannot descend meaningfully and behaves like `next`. GDB will land in machine-level disassembly if symbols are entirely absent — usually not what the user wants. `finish` exits back to the caller in such cases.

## `cont` — resume until next halt

`cont` releases the debuggee until the next [[Breakpoint|breakpoint]] fires, the program crashes, or the program terminates normally. The typical workflow after the user has inspected state and identified the next location of interest:

```text
(gdb) break compute_sum
(gdb) run
... halts at compute_sum entry ...
(gdb) next
(gdb) next
(gdb) print sum
$1 = 42
(gdb) cont      # release to next breakpoint or end
```

## Related commands

- `stepi` / `nexti` — instruction-level variants (one machine instruction rather than one source line). Used when debugging assembly or optimized code where source-line mapping is unreliable.
- `finish` — run until the current function returns, then halt in the caller.
- `until` — run until execution leaves the current source line (useful inside loops to advance past the end of the loop).

## Naming clash with [[PointerIncrement|pointer step]]

The term *step* is overloaded in this corpus:

- **This page** ([[StepDebug]]) — the GDB *advance one line* primitive, alongside `next` / `cont`.
- [[PointerIncrement|Pointer increment]] / [[PointerArithmetic|pointer arithmetic]] — `ptr++` advancing a [[Pointer|pointer]] by `sizeof(*ptr)` bytes (from [[dis-2-9-4-pointer-arithmetic|Ch 2.9.4]]).
- [[StepFunctions|Step functions]] — discrete piecewise-constant functions (from analysis / probability sources).

The three are unrelated. [[dis-3-1-gdb|Ch 3.1]] introduces the debugger meaning.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[Breakpoint]] — what these commands resume *from*.
- [[GdbPrint]] / [[GdbBacktrace]] / [[GdbList]] — the inspection commands run between steps.
- [[DebugSymbol]] — required for `step` to descend meaningfully.
- [[GccDashG]] — the build flag that supplies the symbols.
- [[StackFrame]] — `step` pushes a new frame on function entry; `finish` pops back.
- [[FunctionCall]] / [[ReturnStatement]] — the call/return events `step` versus `next` discriminate around.
