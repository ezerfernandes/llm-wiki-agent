---
title: "GDB `display`"
type: concept
tags: [debugging, gdb, c-language, debugging-primitive, expression-evaluation]
sources: [dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB `display`

The [[GDB]] command that **registers an expression to be automatically printed at every pause** — every [[Breakpoint|breakpoint]] hit, every [[StepDebug|`step` / `next`]], every signal. Where [[GdbPrint|`print`]] is a one-shot inspection, `display` is a **persistent watch** that re-evaluates and re-prints on each halt.

## Forms

| Form | Behavior |
|---|---|
| `display expr` | Register `expr` for auto-print at every pause. |
| `display/f expr` | Same with format specifier (`/x` / `/t` / `/c` / `/d`), mirroring [[GdbPrint|`print`]]. |
| `display` | List all currently active auto-display expressions. |
| `undisplay N` | Remove auto-display entry `N`. |
| `disable display N` / `enable display N` | Temporarily silence / re-enable entry `N` without removing it. |

Each `display` registration gets a numeric ID, just like [[Breakpoint|breakpoints]].

## Use case

The canonical workflow [[dis-3-2-gdb-commands|Ch 3.2]] motivates:

```text
(gdb) break compute_sum
(gdb) display i
(gdb) display sum
(gdb) run
... breakpoint hits, GDB prints i and sum automatically ...
(gdb) next
... GDB prints i and sum again after the step ...
```

Instead of typing `print i; print sum` after every step, the user **declares the interest once** and watches the values evolve as execution progresses. The pattern is especially useful when [[StepDebug|stepping through a loop]] where the relevant state is a small handful of variables.

## Display vs print vs watchpoint

The three "show me this variable" mechanisms have distinct triggers:

| Command | When it prints |
|---|---|
| [[GdbPrint|`print expr`]] | Once, immediately, at the moment you typed it. |
| `display expr` | At every pause (breakpoint / step / signal). |
| [[Watchpoint|`watch expr`]] | At every *write* to the variable (a hardware-assisted breakpoint on memory writes). |

`display` is the **passive-poll** primitive; [[Watchpoint|`watch`]] is the **change-triggered** primitive. They complement each other.

## Connections

- [[dis-3-2-gdb-commands]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[GdbPrint]] — the one-shot sibling.
- [[Watchpoint]] — the change-triggered sibling.
- [[Breakpoint]] / [[StepDebug]] — the pause events that trigger auto-display.
- [[GdbInfo]] — `info display` lists active auto-display expressions.
