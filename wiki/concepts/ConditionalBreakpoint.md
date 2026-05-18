---
title: "Conditional Breakpoint"
type: concept
tags: [debugging, gdb, breakpoint, debugging-primitive]
sources: [dis-3-1-gdb, dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# Conditional Breakpoint

A [[Breakpoint|breakpoint]] that **only halts the debuggee when an attached expression evaluates to true**. The expression is evaluated in the breakpoint's [[VariableScope|scope]] every time the breakpoint location is reached; if true, execution stops as with a normal breakpoint, and if false, execution continues without the user noticing.

[[dis-3-1-gdb|DIS Ch 3.1]] introduces conditional breakpoints in passing (*"`break 42 if x > 100` only halts when the condition holds"*); [[dis-3-2-gdb-commands|Ch 3.2]] surfaces them as a **first-class debugging workflow** with the headline justification:

> *"Conditional breakpoints allow developers to pause at a breakpoint inside a loop only after some number of iterations or pause the program at a breakpoint only when the value of a variable has an interesting value."*

## Two syntactic forms in GDB

```text
(gdb) break compute.c:42 if i > 1000      # set-and-condition in one command
(gdb) break compute.c:42                   # set the breakpoint, get ID = 3
(gdb) condition 3 (i > 1000)               # attach the condition after the fact
```

The second form (`condition N (expr)`) is the one [[GdbBreakpointManagement|Ch 3.2 documents in detail]] — it lets you add, change, or remove the condition on an existing breakpoint without re-setting it. `condition N` with no expression clears the condition.

## The use cases that motivate them

- **Loop iteration of interest** — `condition 1 (i == 1000)` skips 999 hits, halts on iteration 1000. The standing alternative is [[GdbBreakpointManagement|`ignore N 999`]] — semantically similar but counter-based instead of expression-based.
- **State-triggered halt** — `condition 1 (ptr == NULL)` halts only when a [[NullPointer|null pointer]] would be dereferenced.
- **Bug reproduction** — `condition 1 (strcmp(name, "alice") == 0)` halts when a specific input drives the code through the suspect line.
- **Race detection** — in multithreaded code, `condition 1 (thread_id() == 7)` halts only when the suspect thread executes the line.

## How GDB implements them

The breakpoint trap fires **unconditionally** — the trap-and-handler mechanism described in [[Breakpoint]] is unchanged. After the trap, GDB **evaluates the condition in the debuggee's halted state**; if false, GDB silently resumes the debuggee without surfacing the halt to the user. The cost is therefore *one trap per loop iteration even when the condition is false* — measurable for hot loops with cheap iteration bodies. ([[Watchpoint|Watchpoints]] have the analogous trade-off in the memory-write direction.)

## Composition with `info breakpoints` and `commands`

[[GdbInfo|`info breakpoints`]] shows the attached condition; the `commands N ... end` block runs a GDB script every time breakpoint `N` halts (e.g., `print x; cont` for an auto-logged trace). Conditional breakpoints + `commands` = lightweight printf-debugging without recompiling.

## Connections

- [[dis-3-1-gdb]] — first mention.
- [[dis-3-2-gdb-commands]] — fully treated.
- [[Breakpoint]] — the unconditional parent primitive.
- [[GdbBreakpointManagement]] — `condition N (expr)` is one of the management commands.
- [[GdbInfo]] — `info breakpoints` lists active conditions.
- [[Watchpoint]] — the sibling primitive that triggers on memory writes rather than PC reach.
- [[GDB]] / [[Debugger]] — the host tool.
