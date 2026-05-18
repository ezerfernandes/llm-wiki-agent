---
title: "while Loop (C)"
type: concept
tags: [c-language, control-flow, iteration, loop]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# while Loop (C)

The **`while` loop** is [[CLanguage|C]]'s test-first iteration construct. It evaluates a parenthesized [[CBooleanExpression|boolean expression]] *before* each potential iteration; while the test is nonzero, it executes the body and re-tests.

```c
while (condition) {
    /* body */
}
```

## Semantics (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

1. Evaluate `condition`.
2. If `0` (false), exit the loop.
3. Otherwise, execute the body.
4. Goto 1.

**Zero-iteration property**: if `condition` is false on first evaluation, the body **never executes** — distinguishing `while` from [[DoWhileLoop|`do`–`while`]], which always runs the body at least once.

## When to use `while`

[[DiveIntoSystems]] recommends `while` for **[[IndefiniteIteration|indefinite iteration]]** — loops where the number of iterations isn't known in advance and the loop runs *until some condition emerges* (parse until EOF, retry until success, wait for an event). For **[[DefiniteIteration|definite iteration]]** (a known iteration count), the [[ForLoop|`for` loop]] is the more idiomatic choice — though `while` and `for` are equivalent in power.

## Example: powers of 2 up to `limit`

```c
int p = 1;
while (p <= limit) {
    printf("%d\n", p);
    p *= 2;
}
```

If the user enters `limit < 1`, the body runs zero times.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[DoWhileLoop]] — test-*last* sibling; always runs body once.
- [[ForLoop]] — equivalent-in-power general loop; preferred for definite iteration.
- [[BreakStatement]] / [[ContinueStatement]] — structured exits / skips inside the body.
- [[IndefiniteIteration]] / [[DefiniteIteration]] — the design-rule pair.
- [[CBooleanExpression]] / [[RelationalOperator]] / [[LogicalOperator]] — the test vocabulary.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
