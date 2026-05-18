---
title: "Comma Operator (C)"
type: concept
tags: [c-language, operator]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# Comma Operator (C)

The **comma operator** `,` in [[CLanguage|C]] evaluates its left operand, **discards** the result, then evaluates and yields its right operand. It is a sequencing operator that lets multiple expressions appear where a single expression is grammatically required.

```c
expr1, expr2     /* evaluates expr1 (discarded), then expr2; yields expr2 */
```

## Primary use: [[ForLoop|`for`]] init / step (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

The chapter's only real use of the comma operator is chaining the *init* and *step* clauses of a [[ForLoop|`for` loop]] when you need multiple counters / side effects:

```c
for (i = 0, j = 0; i < 10; i += 1, j += 10) {
    printf("%d %d\n", i, j);
}
```

[[DiveIntoSystems]] explicitly **cautions against overuse** — when the loop body is short, comma-chained init/step can be cleaner; when complex, separate the secondary updates into the body.

## *Not* the same as `,` in function calls

The commas separating function arguments — `printf("%d %d\n", i, j)` — are **argument separators**, **not** the comma operator. Argument evaluation order is unspecified in C (until C17 sequencing rules); the comma operator imposes left-to-right sequencing.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[ForLoop]] — the primary host of the comma operator in idiomatic code.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
