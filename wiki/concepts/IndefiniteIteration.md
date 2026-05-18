---
title: "Indefinite Iteration"
type: concept
tags: [control-flow, iteration, design-rule]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Indefinite Iteration

**Indefinite iteration** is the family of loops that run **until a condition emerges**, with no iteration count known at loop start — read input until EOF, retry until success, wait for an event, parse until a delimiter. It contrasts with [[DefiniteIteration]], where the loop count is known in advance.

## In [[CLanguage|C]]

Per [[dis-1-3-conditionals-loops|DiS Ch 1.3]]: although [[ForLoop|`for`]] and [[WhileLoop|`while`]] are *equivalent in expressive power*, [[DiveIntoSystems]] recommends the [[WhileLoop|`while` loop]] for **indefinite iteration** because the loop's single clause — *condition* — directly expresses *"continue while this holds"*:

```c
while (read_token(&tok) == OK) {
    process(tok);
}
```

There is no natural *init* or *step* to put in a [[ForLoop|`for`]]'s three-clause header — the loop's *real* progress is hidden inside `read_token`. Forcing this into `for (;cond;)` loses no power but reads worse.

## Test-first vs. test-last variants

- **[[WhileLoop|`while` (cond) { ... }]]** — test first; body may run zero times. Use when *"don't even start if not needed"*.
- **[[DoWhileLoop|`do` { ... } `while` (cond);]]** — test last; body always runs at least once. Use when *"must run at least once to get the value the condition will test"* (input prompts, menu loops, retry loops).

## Why the distinction matters

- **Readability** — choosing the right loop form telegraphs intent.
- **Termination reasoning** — indefinite-iteration loops require an explicit termination argument (the condition will eventually become false, or a [[BreakStatement|`break`]] will fire). A common bug source.
- **Liveness** — an indefinite loop with no progress toward its termination condition is a hang.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[DefiniteIteration]] — the contrasting family; pairs with [[ForLoop]].
- [[WhileLoop]] — the test-first C construct of choice.
- [[DoWhileLoop]] — the test-last variant.
- [[BreakStatement]] / [[ContinueStatement]] — escapes that often participate in indefinite-loop control.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
