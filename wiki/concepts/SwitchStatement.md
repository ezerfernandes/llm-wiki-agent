---
title: "switch Statement (C)"
type: concept
tags: [c-language, control-flow, branching]
sources: [dis-1-3-conditionals-loops, dis-2-9-1-advanced-switch]
last_updated: 2026-05-17
---

# switch Statement (C)

The **`switch` statement** in [[CLanguage|C]] dispatches on an integer-valued expression to one of several labeled arms ([[CaseLabel|`case` labels]]) — a structured multi-way branch over a single value.

```c
switch (expr) {
    case CONST1:
        /* statements */
        break;
    case CONST2:
        /* statements */
        break;
    default:
        /* statements */
}
```

## Rules (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

- **`expr` must have integer type** — `int`, `char`, `enum`, etc. Not `float` / `double` / strings.
- **Each [[CaseLabel|`case` label]] is a compile-time integer constant**. No ranges (`1..5`), no variables, no expressions involving runtime values.
- **`default:`** matches any value not handled by an explicit `case`. Optional but recommended.
- **Fall-through is the default**: when a `case` body finishes, execution **continues into the next case** unless a [[BreakStatement|`break`]] terminates the switch. This is occasionally useful (collapsing multiple labels onto one body) and frequently a bug source.

## switch vs. if/else if chains

A `switch` is **only equivalent to an `if`/`else if` chain** when every test is `expr == const` against a compile-time constant. For range tests, floating-point tests, or general boolean expressions, use [[IfStatement|`if`]] / [[ElseStatement|`else if`]] instead.

## Intentional fall-through example

```c
switch (grade) {
    case 'A':
    case 'a':
        printf("excellent\n");
        break;
    case 'B':
    case 'b':
        printf("good\n");
        break;
    default:
        printf("see me\n");
}
```

Two labels share the *"excellent"* body by letting `'A'` fall through to `'a'` (which has no `break` between them).

## Codification in [[dis-2-9-1-advanced-switch|Ch 2.9.1]]

Ch 2.9.1 returns to `switch` with three explicit rules: (1) **case values must be literal values, not expressions** — a runtime expression in a [[CaseLabel|case label]] is a compile error; (2) without [[BreakStatement|`break`]] execution **falls through** — sometimes deliberate, often a bug; (3) the **`default:` label is optional and conventionally appears last**. The chapter also frames `switch` as the natural dispatch construct for [[CEnum|`enum`]] values — and notes that the compiler can often turn a dense `switch` into a **jump table** more efficient than the equivalent [[IfStatement|`if`]] / [[ElseStatement|`else if`]] chain.

```c
switch (val) {
    case FRI:
        printf("Orchestra practice\n");
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

The Ch 2.9.1 worked example demonstrates both **stacked labels for shared bodies** and **intentional fall-through** in one snippet.

## Connections

- [[dis-1-3-conditionals-loops]] — source (first sketch).
- [[dis-2-9-1-advanced-switch]] — source (codification + [[CEnum|`enum`]] pairing).
- [[CaseLabel]] — the labels inside a `switch`; must be compile-time integer constants.
- [[CEnum]] — natural source of dispatch values; Ch 2.9.1 makes the pairing explicit.
- [[BreakStatement]] — terminates a `case` arm to prevent fall-through.
- [[IfStatement]] / [[ElseStatement]] — the more general alternative for non-equality tests.
- [[ControlFlow]] — branching family.
- [[CLanguage]] / [[DiveIntoSystems]].
