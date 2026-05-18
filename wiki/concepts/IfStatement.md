---
title: "if Statement (C)"
type: concept
tags: [c-language, control-flow, branching]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# if Statement (C)

The **`if` statement** is [[CLanguage|C]]'s primary branching construct. It evaluates a parenthesized [[CBooleanExpression|boolean expression]] and executes the following statement (or `{ }`-bracketed block) only when that expression is nonzero (true).

```c
if (condition) {
    /* executed iff condition is nonzero */
}
```

Three shapes (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]]):

- **One-way** — bare `if (cond) { ... }`. No alternative branch.
- **Two-way** — `if (cond) { ... } else { ... }` with [[ElseStatement|`else`]].
- **Multi-way** — `if (cond1) { ... } else if (cond2) { ... } else { ... }`. The final [[ElseStatement|`else`]] is always optional.

## Syntax non-negotiables

- **Parentheses around the test are required**: `if (x > 0)`, not `if x > 0`.
- **The body is a single statement or a `{ }` block.** A single statement may omit braces but [[DiveIntoSystems]] recommends always using braces for safety.
- **The test is integer-valued**: anything that evaluates to `0` is false; anything nonzero is true ([[CBooleanExpression]]).

## The `=` vs `==` footgun

`if (x = 0)` is **legal C** — it assigns `0` to `x`, then tests the *result of the assignment* (which is `0`, hence false). The intended comparison is `if (x == 0)`. Modern compilers (`-Wall`) warn, but the bug is silent without flags.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[ElseStatement]] — the optional companion clause.
- [[ControlFlow]] — branching is half the control-flow story (loops are the other half).
- [[CBooleanExpression]] / [[RelationalOperator]] / [[LogicalOperator]] / [[ShortCircuitEvaluation]] — the vocabulary of the test.
- [[SwitchStatement]] — the integer-dispatched alternative for many-way branches over a single value.
- [[CLanguage]] / [[DiveIntoSystems]].
- [[Python]] — contrast: `if cond:` with indented body, no parens, no braces.
