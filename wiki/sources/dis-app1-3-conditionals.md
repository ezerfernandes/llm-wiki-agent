---
title: "Dive into Systems — Appendix 1.3 Conditionals and Loops (for Java Programmers)"
type: source
tags: [book, dive-into-systems, c-language, java, control-flow, cross-walk]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix1/conditionals.html
---

## Summary

Appendix 1.3 of [[DiveIntoSystems]] is the [[Java]]-programmer's retelling of [[dis-1-3-conditionals-loops|Ch 1.3]]. The cross-walk is **almost a no-op**: [[IfStatement|`if`]] / [[ElseStatement|`else`]] / [[SwitchStatement|`switch`]] / [[WhileLoop|`while`]] / [[DoWhileLoop|`do`–`while`]] / [[ForLoop|`for`]] / [[BreakStatement|`break`]] / [[ContinueStatement|`continue`]] are syntactically identical between Java and C. The headline delta is **C has no `boolean` type** — [[CBooleanExpression|truth values are integers]] (`0` = false, nonzero = true), the rule Java programmers most often stumble on. See [[JavaVsC]] for the consolidated cross-walk.

## Key Claims (Java-vs-C deltas)

- **C has no dedicated boolean type** — *"any integer expression that is zero evaluates to false; nonzero (any positive or negative value) evaluates to true."* This is the **single load-bearing delta** for this section.
- **[[RelationalOperator|Relational operators]]** (`==`, `!=`, `<`, `<=`, `>`, `>=`) and **[[LogicalOperator|logical operators]]** (`!`, `&&`, `||`) are identical between Java and C, including [[ShortCircuitEvaluation|short-circuit evaluation]].
- **[[IfStatement|`if`]] / [[ElseStatement|`else`]] / `else if` chains** are syntactically identical.
- **Loop constructs** (`for`, `while`, `do-while`) are identical in syntax and semantics. Java adds the **enhanced for-each loop** (`for (int x : array)`) that C lacks — C requires explicit index-based iteration.
- **[[BreakStatement|`break`]] / [[ContinueStatement|`continue`]]** behave identically. Java's labeled break/continue has no C analog.
- **The `==` on objects vs primitives gotcha doesn't apply in C** — C has no reference equality vs value equality distinction (there are no reference types in the Java sense).

## Key Quote

> *"In C, any integer expression that is zero (0) evaluates to false, while nonzero (any positive or negative value) evaluates to true."*

## Worked example — same control flow, no `boolean`

```c
int x = 7;
if (x > 0 && x % 2) {        // nonzero = true; x % 2 returns 1 for odd
    printf("%d is positive and odd\n", x);
}
for (int i = 0; i < 10; i++) {
    if (i == 5) break;
    if (i % 2 == 0) continue;
    printf("%d ", i);
}
```

Java is line-for-line identical except `if (x > 0 && x % 2 != 0)` — Java requires the explicit `!= 0` because its `if` predicate must be `boolean`, not `int`.

## Connections

- [[DiveIntoSystems]] — Appendix 1 sister of [[dis-1-3-conditionals-loops|Ch 1.3]].
- [[dis-1-3-conditionals-loops]] — the Python-cross-walk sibling.
- [[JavaVsC]] — consolidated cross-walk table.
- [[Java]] — the source language for this cross-walk.
- [[CBooleanExpression]] — the integer-as-boolean rule, the section's headline delta.
- [[ControlFlow]] / [[IfStatement]] / [[ElseStatement]] / [[SwitchStatement]] / [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] / [[BreakStatement]] / [[ContinueStatement]] / [[RelationalOperator]] / [[LogicalOperator]] / [[ShortCircuitEvaluation]] — reused unchanged from Ch 1.3.

## Contradictions

- None. Pure Java-perspective retelling of [[dis-1-3-conditionals-loops|Ch 1.3]].
