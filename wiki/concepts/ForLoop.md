---
title: "for Loop (C)"
type: concept
tags: [c-language, control-flow, iteration, loop]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# for Loop (C)

The **`for` loop** is [[CLanguage|C]]'s general three-clause iteration construct. Unlike [[Python]]'s sequence-iteration `for`, C's `for` is **equivalent in power to [[WhileLoop|`while`]]** — any `while` translates mechanically to a `for` and vice versa.

```c
for (init; condition; step) {
    /* body */
}
```

## Semantics (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

1. Execute *init* **once**.
2. Evaluate *condition*; if `0` (false), exit the loop.
3. Execute the body.
4. Execute *step*.
5. Goto 2.

Any of the three clauses may be **empty**:

- `for (;;) { ... }` is the idiomatic **infinite loop** (no init, no test ≡ always true, no step). Exit via [[BreakStatement|`break`]] or `return`.
- `for (; cond;) { ... }` is identical in behavior to `while (cond) { ... }`.

## Definite vs. indefinite iteration

[[DiveIntoSystems]] recommends:

- **`for` for [[DefiniteIteration|definite iteration]]** — known iteration count / index range — because the loop variable's initialization, bound, and step all appear in one line, making the iteration count visible at a glance.
- **`while` for [[IndefiniteIteration|indefinite iteration]]** — loop *until* a condition emerges, no a-priori bound.

The two forms are *capability-equivalent*; the choice is stylistic.

## Comma operator in init / step

The *init* and *step* clauses can chain multiple expressions via the [[CommaOperator|comma operator]]:

```c
for (i = 0, j = 0; i < 10; i += 1, j += 10) {
    printf("%d %d\n", i, j);
}
```

[[DiveIntoSystems]] cautions against overusing this for readability — when the body of the loop is short, comma-chained init/step can be cleaner; when complex, separate the secondary updates into the body.

## Variable scoping note

In C99 and later, `for (int i = 0; ...; ...)` declares `i` scoped to the loop only — preferred over a function-scope declaration when `i` is not needed afterward.

## Equivalence with `while`

```c
/* for form */
for (init; cond; step) { body; }

/* equivalent while form */
init;
while (cond) { body; step; }
```

The translation is exact except in the presence of [[ContinueStatement|`continue`]], where the `for` form still runs *step* before re-testing while the naive `while` translation would skip it.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[WhileLoop]] — equivalent-in-power sibling; preferred for indefinite iteration.
- [[DoWhileLoop]] — test-last sibling.
- [[BreakStatement]] / [[ContinueStatement]] — structured exits / skips inside the body.
- [[CommaOperator]] — chains expressions in *init* / *step*.
- [[DefiniteIteration]] / [[IndefiniteIteration]] — the design-rule pair.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
- [[Python]] — contrast: Python's `for` iterates a sequence, not a general three-clause loop.
