---
title: "do–while Loop (C)"
type: concept
tags: [c-language, control-flow, iteration, loop]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# do–while Loop (C)

The **`do`–`while` loop** is [[CLanguage|C]]'s test-last iteration construct. It executes the body *first*, then evaluates a parenthesized [[CBooleanExpression|boolean expression]]; while the test is nonzero, it loops back to re-execute the body.

```c
do {
    /* body */
} while (condition);
```

Note the **trailing semicolon** after `while (condition)` — required, unlike [[WhileLoop|`while`]].

## Semantics (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

1. Execute body.
2. Evaluate `condition`.
3. If nonzero (true), goto 1; otherwise exit.

**Always-at-least-once property**: the body **always executes at least once**, even if `condition` is false on first evaluation. This is the structural distinction from [[WhileLoop|`while`]].

## When to use `do`–`while`

Reach for `do`–`while` when the loop body must run *before* the termination condition can be evaluated — the canonical examples being:

- **Input validation** — prompt and read first, then test whether the input is acceptable; loop until it is.
- **Menu loops** — display the menu and read a choice; loop until the user picks *quit*.

## Example: prompt until non-negative

```c
int n;
do {
    printf("Enter a non-negative integer: ");
    scanf("%d", &n);
} while (n < 0);
```

The prompt always shows once; if the user enters a valid value first try, the loop ends after one iteration.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[WhileLoop]] — test-*first* sibling; body may run zero times.
- [[ForLoop]] — general loop form.
- [[BreakStatement]] / [[ContinueStatement]] — structured exits / skips.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
