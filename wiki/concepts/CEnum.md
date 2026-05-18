---
title: "Enumerated Type (enum, C)"
type: concept
tags: [c-language, enum, type, constant]
sources: [dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# Enumerated Type (`enum`, C)

A **`enum`** in [[CLanguage|C]] groups **related integer constants** under a named type, giving them a logical home and (for variables typed `enum tag`) a documentation-level type tag. At runtime an `enum` value *is* an [[CPrimitiveType|`int`]] — the construct is a source-level convenience for naming and grouping.

```c
enum type_name {
    CONST_1_NAME,
    CONST_2_NAME,
    ...
    CONST_N_NAME
};
```

## Default sequential numbering

The first constant receives **0**, the next **1**, and so on:

```c
enum days_of_week {
    MON,    // 0
    TUES,   // 1
    WED,    // 2
    THURS,  // 3
    FRI     // 4
};
```

## Variable declaration and usage

```c
enum days_of_week day;
day = THURS;
if (day > WED) {
    printf("Weekend approaching!\n");
}
```

## Custom value assignment

You can override any value; subsequent constants continue from the override:

```c
enum days_of_week {
    SUN = 1,
    MON,    // 2
    TUES,   // 3
    WED     // 4
};
```

## Four advantages over [[CConstant|`#define`]] for integer constants

Per [[dis-2-9-1-advanced-switch|DiS Ch 2.9.1]]:

1. **Logical grouping** — related constants live together under one named type, not scattered across `#define` lines.
2. **Type safety** — function parameters typed `enum days_of_week` document caller intent in a way `int` cannot.
3. **Implicit sequential values** — no manual `#define MON 0` / `#define TUES 1` ladder.
4. **Easy insertion/removal** — adding a constant in the middle doesn't require renumbering its neighbors.

## Runtime reality check

**`enum` constants print as their integer values, not their names.** `printf("%d\n", TUES);` outputs `2`, not `"TUES"`. The named-constant abstraction is purely source-level — at runtime an `enum` *is* an `int` with no string metadata. (Contrast: many other languages — Python's `Enum`, Rust's `enum` — carry the name reflectively.)

## Pairing with [[SwitchStatement|`switch`]]

`enum` and [[SwitchStatement|`switch`]] are natural partners — the enum names the dispatch values and the switch dispatches on them:

```c
switch (val) {
    case FRI:
        printf("Orchestra practice\n");
        // intentional fall-through
    case MON:
    case WED:
        printf("Classes today\n");
        break;
    case TUES:
    case THURS:
        printf("Math and history\n");
        break;
}
```

This example demonstrates both **stacked labels for shared bodies** (MON/WED) and **deliberate [[BreakStatement|fall-through]]** (FRI flows into MON/WED).

## Typical [[Typedef|`typedef`]] pairing

```c
typedef enum class_year classYr;
classYr yr;   // shorthand for `enum class_year yr;`
```

See [[TypedefExpansion]] for the broader pattern.

## Connections

- [[dis-2-9-1-advanced-switch]] — source.
- [[CConstant]] — the `#define` alternative for ungrouped constants.
- [[ConstQualifier]] — the `const` alternative for individually-named typed constants.
- [[SwitchStatement]] / [[CaseLabel]] — the natural dispatch construct for enum values.
- [[Typedef]] / [[TypedefExpansion]] — the alias that drops the `enum` keyword from declarations.
- [[CPrimitiveType]] — `enum` is an `int` at runtime.
- [[CLanguage]] / [[DiveIntoSystems]].
