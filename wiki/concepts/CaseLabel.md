---
title: "case Label (C)"
type: concept
tags: [c-language, control-flow, branching]
sources: [dis-1-3-conditionals-loops, dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# case Label (C)

A **`case` label** is a target within a [[SwitchStatement|`switch` statement]] that names a specific value of the switch expression. Execution jumps to the matching label and proceeds from there until a [[BreakStatement|`break`]] (or the end of the `switch`) is reached.

```c
case CONST_EXPR:
```

## Rules (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

- **The label must be a compile-time integer constant** — a literal, an `enum` value, or a `#define`d constant. Not a variable, not a runtime expression, not a range.
- **Each `case` value must be unique** within the same [[SwitchStatement|`switch`]].
- **Multiple labels may share a body** by stacking them with no statements between — `case 'A': case 'a': ...`. This is the canonical *intentional fall-through* idiom.
- **`default:`** is the catch-all label; it matches any value not named by an explicit `case`. It may appear anywhere in the switch body but conventionally goes last.

## Fall-through

Without a terminating [[BreakStatement|`break`]] (or `return`, `goto`, etc.), control flows from one case body into the next — a feature inherited from B/BCPL that is occasionally used deliberately and frequently the source of accidental bugs. Some compilers warn on implicit fall-through.

## Connections

- [[dis-1-3-conditionals-loops]] — source (first sketch).
- [[dis-2-9-1-advanced-switch]] — source (codification: *"case values must be literal values, not expressions"*).
- [[CEnum]] — typical source of named compile-time case values; Ch 2.9.1 makes the pairing explicit.
- [[SwitchStatement]] — the construct that hosts case labels.
- [[BreakStatement]] — terminates a case arm to suppress fall-through.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
