---
title: "Dive into Systems — Ch 3.2 GDB Commands in Detail"
type: source
tags: [dive-into-systems, c-debugging, gdb, debugger, breakpoints, watchpoints, examine-memory, tooling]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C3-C_debug/gdb_commands.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 3.2** of *[[DiveIntoSystems]]* — the **command-reference companion** to [[dis-3-1-gdb|Ch 3.1]]'s narrative-workflow introduction. Where Ch 3.1 framed [[GDB]] as a [[Debugger|debugger]] and walked the typical session, Ch 3.2 fans the command vocabulary out into a **categorized reference**: execution control, code listing, breakpoint management, program-state inspection, and expression evaluation.

Codifies the **TAB-completion / short-abbreviation / RETURN-repeat** ergonomic primitives that make GDB livable at the CLI (*"particularly useful when stepping through the execution with a sequence of `next` or `step` commands"*), then walks each command family with the full syntactic surface: [[GdbBreak|`break`]] in four forms (function / line / file:line / address), [[GdbRun|`run [args]`]], [[StepDebug|`step` / `next` / `cont` / `until`]] with line-count multipliers, [[GdbList|`list`]] with range and function targets, [[GdbBacktrace|`where` / `bt` / `frame N`]], [[GdbBreakpointManagement|`enable` / `disable` / `delete` / `clear` / `ignore` / `condition`]], [[GdbPrint|`print`]] with format specifiers (`/x` / `/t` / `/c`), [[GdbDisplay|`display`]], [[GdbExamineMemory|`x` (examine memory)]] with the `n` / `f` / `u` format triplet, [[GdbWhatis|`whatis`]], [[GdbSet|`set`]], and [[GdbInfo|`info`]] sub-commands (`locals` / `args` / `break` / `registers` / `frame` / `breakpoints`).

Closes the [[GDB]] command surface for [[dis-3-1-gdb|Ch 3.1]]'s readers — every command Ch 3.1 named-and-deferred is detailed here, with the **conditional-breakpoint workflow** (*"pause at a breakpoint inside a loop only after some number of iterations"*) and the **examine-memory `x/nfu`** syntax as the chapter's two load-bearing additions over Ch 3.1's vocabulary.

## Key Claims

- **CLI ergonomics primitives**: GDB ships [[GdbTabCompletion|TAB completion]], **short abbreviations** (`p` for `print`, `l` for `list`, `n` for `next`, `c` for `cont`, `r` for `run`, `b` for `break`), arrow-key history, and **RETURN-repeats-last-command** (*"particularly useful when stepping through the execution with a sequence of `next` or `step` commands"*). The session is interactive but extremely terse.
- **`break` in four forms**: `break main` (function entry), `break 13` (line in current file), `break gofish.c:34` (line in named file), `break *0x4011a0` (instruction address) — completing [[Breakpoint|Ch 3.1]]'s breakpoint vocabulary.
- **`run` accepts arguments**: `run 2 40 100` passes `argc=4` / `argv = {"./prog", "2", "40", "100"}` to the debuggee, eliminating the [[CommandLineArguments|argc/argv]] gap [[dis-3-1-gdb|Ch 3.1]] left implicit.
- **`step` and `next` accept counts**: `step 10` advances 10 source lines (entering function bodies as it goes), `next 5` advances 5 lines treating calls as opaque — multiplier syntax not surfaced in [[dis-3-1-gdb|Ch 3.1]].
- **`until N`**: runs until execution reaches source line `N` — useful for skipping the tail of a loop without setting a breakpoint, complementing [[StepDebug|`step` / `next` / `cont`]].
- **`list` accepts range / function targets**: `list 30 100` shows lines 30–100, `list main` shows code around `main`'s entry — superset of [[dis-3-1-gdb|Ch 3.1]]'s no-arg `list` that shows the current line context.
- **Breakpoint lifecycle — six commands** ([[GdbBreakpointManagement|breakpoint management]]): `enable N` / `disable N` (toggle without removing), `delete N` / `delete` (remove one / remove all), `clear N` (remove by source-line rather than ID), `ignore N M` (skip breakpoint `N` the next `M` hits), `condition N (expr)` (the **[[ConditionalBreakpoint|conditional breakpoint]]** — pause only when `expr` is true, e.g., `condition 1 (i > 1000)`).
- **`print` with format specifiers**: bare `p i` prints `i` in default format; `print/x 123` prints as hex (`0x7b`); `print/t 123` as binary (`1111011`); `print/c 99` as ASCII (`'c'`); `print *(int *)0x8ff4bc10` dereferences a raw address with explicit type — covering hex / binary / character / typed-address-deref formats.
- **`display expr`** ([[GdbDisplay|auto-display]]): registers `expr` to be **re-printed automatically at every pause** (every breakpoint, every step). Use for variables you want to watch evolve across many steps without re-typing `print`.
- **`x/nfu address`** ([[GdbExamineMemory|examine memory]]): the **lowest-level inspection primitive**. `n` = repeat count, `f` = format (`d` / `x` / `o` / `c` / `s` / `f`), `u` = unit size (`b` byte / `h` halfword / `w` word / `g` giant). Examples: `x/d ptr` (one decimal int at `ptr`), `x/4c s1` (4 chars from `s1`), `x/s s1` (null-terminated string), `x/8d s1` (8 decimals showing the ASCII codes). The escape hatch when [[GdbPrint|`print`]] is too type-aware.
- **`whatis expr`** ([[GdbWhatis|type query]]): reports the static type GDB infers for `expr` — e.g., `whatis (x + 3.4)` → `type = double`. Useful when [[CompilerOptimization|optimization]] or implicit conversion has obscured what a sub-expression actually evaluates to.
- **`set var = expr`** ([[GdbSet|set]]): **modifies a live variable's value** mid-session — `set x = 123 * y` rewrites `x` without recompiling. Lets the user **patch around bugs interactively** to test downstream behavior without rebuilding.
- **`info` sub-commands** ([[GdbInfo|info]]): `info locals` (locals in current frame), `info args` (parameters), `info break` / `info breakpoints` (all set breakpoints with ID, location, hit count, condition, enable state), `info registers` (CPU register file — `%rax` / `%rbx` / `%rsp` / `%rip` / …), `info frame` (current frame's saved IP, frame pointer, caller). The reflection layer over GDB's own state.
- **Conditional breakpoints unlock loop debugging**: *"breakpoints—especially conditional ones—allow developers to pause at a breakpoint inside a loop only after some number of iterations or pause the program at a breakpoint only when the value of a variable has an interesting value"* — the headline workflow rationale for `condition N (expr)`.

## Key Quotes

> "[Pressing RETURN to re-execute the most recent command is] particularly useful when stepping through the execution with a sequence of `next` or `step` commands." — on CLI ergonomics.

> "[Conditional breakpoints allow developers to] pause at a breakpoint inside a loop only after some number of iterations [or] pause the program at a breakpoint only when the value of a variable has an interesting value." — the rationale for `condition N (expr)`.

> "[`where` / `backtrace` is useful for] pinpointing the location of a program crash and for examining state at the interface between function calls and returns." — restating [[GdbBacktrace|Ch 3.1]]'s crash-localization rule.

## Connections

- [[DiveIntoSystems]] — book; this is **Ch 3.2**, the command-reference companion to [[dis-3-1-gdb|Ch 3.1]].
- [[dis-3-1-gdb]] — the narrative workflow introduction this section drills into.
- [[GDB]] — the host tool; this source **completes** GDB's command surface for the *Dive into Systems* corpus.
- [[Breakpoint]] — already in wiki; this source extends the breakpoint vocabulary with `enable` / `disable` / `delete` / `clear` / `ignore` / `condition`.
- [[StepDebug]] — already in wiki; this source adds the count-multiplier syntax (`step N` / `next N`) and the `until N` variant.
- [[GdbBacktrace]] — already in wiki; this source restates the crash-localization use case and adds `info frame`.
- [[GdbPrint]] — **new concept page**; the variable / expression printer with format specifiers `/x` / `/t` / `/c` and typed-address dereference.
- [[GdbDisplay]] — **new concept page**; auto-print on every pause.
- [[GdbExamineMemory]] — **new concept page**; the `x/nfu address` raw-memory inspection primitive.
- [[GdbInfo]] — **new concept page**; the `info <subcommand>` family (`locals` / `args` / `break` / `registers` / `frame` / `breakpoints`).
- [[GdbBreakpointManagement]] — **new concept page**; the breakpoint-lifecycle commands (`enable` / `disable` / `delete` / `clear` / `ignore` / `condition`).
- [[ConditionalBreakpoint]] — **new concept page**; the `condition N (expr)` workflow for loop / corner-case debugging.
- [[GdbSet]] — **new concept page**; live variable mutation mid-session.
- [[Watchpoint]] — **new concept page**; the related primitive (pause on *memory write* rather than *PC reach*) — named-and-deferred in [[dis-3-1-gdb|Ch 3.1]] / [[Breakpoint]], partially covered here via `display` and `info`.
- [[GdbRun]] / [[GdbList]] / [[GdbWhatis]] — **new concept pages** for previously stub-referenced commands.
- [[CommandLineArguments]] — already in wiki; `run` finally shows how `argc`/`argv` populate at debug time.
- [[CompilerOptimization]] / [[GccDashG]] / [[DebugSymbol]] — already in wiki; build-side prerequisites unchanged from [[dis-3-1-gdb|Ch 3.1]].
- [[StackFrame]] / [[ExecutionStack]] / [[LocalVariable]] / [[FunctionParameter]] — already in wiki; what `info frame` / `info locals` / `info args` walk.
- [[Valgrind]] — sibling debugging tool (Ch 3.3+); still pending.

## Contradictions

None — this is a **command-reference deepening** of [[dis-3-1-gdb|Ch 3.1]]'s narrative coverage; the same tool, the same workflow, just more commands and more syntactic detail. The Ch 3.1 description of `next` / `step` / `cont` / `bt` / `frame N` / `print` / `list` is preserved verbatim; this source extends the set with format specifiers, count multipliers, examine-memory, info sub-commands, set, watch-style auto-display, and conditional / hit-count-suppressed breakpoints.
