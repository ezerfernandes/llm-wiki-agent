---
title: "Control Flow"
type: concept
tags: [programming, control-flow, c-language]
sources: [dis-1-3-conditionals-loops, dis-1-4-functions]
last_updated: 2026-05-17
---

# Control Flow

**Control flow** is the order in which the statements of a program are executed. A program with only sequential statements runs each line once, top to bottom. Real programs need to **branch** (make decisions) and **iterate** (repeat), which is the role of [[ControlFlow|control-flow]] constructs.

In [[CLanguage|C]] (per [[dis-1-3-conditionals-loops|Ch 1.3]] of [[DiveIntoSystems]]), the control-flow vocabulary is:

- **Branching** — [[IfStatement|`if`]] / [[ElseStatement|`else`]] / `else if` for boolean-driven decisions; [[SwitchStatement|`switch`]] / [[CaseLabel|`case`]] for integer-dispatched multi-way branches.
- **Iteration** — [[WhileLoop|`while`]] (test-first, zero-or-more), [[DoWhileLoop|`do`–`while`]] (test-last, one-or-more), [[ForLoop|`for`]] (general three-clause loop).
- **Structured jumps** — [[BreakStatement|`break`]] (exit innermost loop / `switch`), [[ContinueStatement|`continue`]] (skip to next iteration).
- **Function call/return** — a [[FunctionCall|call]] transfers control into a [[Function|function]], pushing a [[StackFrame|stack frame]]; a [[ReturnStatement|`return`]] transfers control back to the caller, popping the frame. Introduced in [[dis-1-4-functions|Ch 1.4]] as a control-flow operation layered *on top of* the branches and loops of Ch 1.3.

[[CLanguage|C]]'s control-flow surface is **syntactically distinct** from [[Python]]'s (parenthesized tests, `{ }` blocks, `;` terminators) but **semantically nearly identical** for the branching constructs. The one structural divergence is the [[ForLoop|`for` loop]]: in C, it is a *general* three-clause loop equivalent in power to [[WhileLoop|`while`]]; in Python, `for` iterates a sequence.

## Connections

- [[dis-1-3-conditionals-loops]] — the [[DiveIntoSystems]] section that introduces this concept for C.
- [[dis-1-4-functions]] — adds the call/return layer on top of the branch/loop layer.
- [[Function]] / [[FunctionCall]] / [[ReturnStatement]] / [[StackFrame]] / [[ExecutionStack]] — the call/return control-flow vocabulary.
- [[IfStatement]] / [[ElseStatement]] / [[SwitchStatement]] / [[CaseLabel]] — branching primitives.
- [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] — iteration primitives.
- [[BreakStatement]] / [[ContinueStatement]] — structured jumps inside loops / `switch`.
- [[CBooleanExpression]] / [[RelationalOperator]] / [[LogicalOperator]] / [[ShortCircuitEvaluation]] — the decision-vocabulary used by every branch and loop test.
- [[CLanguage]] — the host language for the [[DiveIntoSystems]] treatment.
- [[Python]] — contrast language for the *syntax-different, semantics-same* cross-walk.
