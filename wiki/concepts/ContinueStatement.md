---
title: "continue Statement (C)"
type: concept
tags: [c-language, control-flow, structured-jump]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# continue Statement (C)

The **`continue` statement** in [[CLanguage|C]] skips the rest of the current loop iteration and jumps to the next test-of-condition. Unlike [[BreakStatement|`break`]], it does **not** exit the loop — it just shortcuts to the next iteration.

```c
for (int i = 0; i < N; i++) {
    if (i % 2 != 0) continue;   /* skip odd i */
    printf("%d\n", i);
}
```

## Semantics per loop form (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

- **In a [[WhileLoop|`while`]] / [[DoWhileLoop|`do`–`while`]]**: jump directly to the next condition evaluation.
- **In a [[ForLoop|`for`]]**: jump to the **step** clause first, then evaluate the condition. This is the subtle reason a `while` translation of a `for` with `continue` must place *step* before the test.

## Targets only the innermost loop

Like [[BreakStatement|`break`]], `continue` affects only the **innermost enclosing** loop. To skip an iteration of an outer loop, restructure with a flag variable or `goto`.

## `continue` outside a loop

Inside a [[SwitchStatement|`switch`]] that is itself inside a loop, `continue` applies to the **enclosing loop**, not the switch. Outside any loop, `continue` is a compile-time error.

## Typical idioms

- **Filter-and-process** — skip items not matching a predicate, process the rest.
- **Guard-skip** — at the top of a loop, `if (!valid) continue;` flattens nesting that would otherwise be an `if (valid) { ... }` wrapper.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[BreakStatement]] — sibling structured jump; exits the loop entirely.
- [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] — loops `continue` can shortcut.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
