---
title: "else / else if Clause (C)"
type: concept
tags: [c-language, control-flow, branching]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# else / else if Clause (C)

The **`else` clause** is the optional companion to an [[IfStatement|`if` statement]] in [[CLanguage|C]]. Its body executes when the preceding `if` test was false (`0`).

```c
if (cond) {
    /* taken when cond is nonzero */
} else {
    /* taken when cond is zero */
}
```

## else if chains

Chaining `else if` produces a **multi-way branch**:

```c
if (x > 0) {
    printf("positive\n");
} else if (x == 0) {
    printf("zero\n");
} else {
    printf("negative\n");
}
```

The first arm whose test is nonzero runs; the rest are skipped. A trailing bare [[ElseStatement|`else`]] is always optional — without it, none of the bodies runs when all tests are false.

(Note: in C, `else if` is not a keyword pair — it is just an [[IfStatement|`if` statement]] sitting in the body of the preceding `else`. The braces are dropped because an `if`-statement is itself a single statement.)

## Dangling-else binding

When two `if`s share an `else` without braces, the `else` binds to the **nearest** unmatched `if`. [[DiveIntoSystems]] recommends always using `{ }` to make the binding explicit.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[IfStatement]] — the construct `else` attaches to.
- [[ControlFlow]] — branching family.
- [[CBooleanExpression]] — what the `if` test evaluates.
- [[CLanguage]] / [[DiveIntoSystems]].
