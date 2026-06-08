---
title: "Control Flow"
type: concept
tags: [programming, control-flow, c-language]
sources: [dis-1-3-conditionals-loops, dis-1-4-functions, fuzzingbook-19-information-flow, fuzzingbook-20-concolic-fuzzer, fuzzingbook-21-symbolic-fuzzer]
last_updated: 2026-06-06
---

# Control Flow

**Control flow** is the order in which the statements of a program are executed. A program with only sequential statements runs each line once, top to bottom. Real programs need to **branch** (make decisions) and **iterate** (repeat), which is the role of [[ControlFlow|control-flow]] constructs.

In [[CLanguage|C]] (per [[dis-1-3-conditionals-loops|Ch 1.3]] of [[DiveIntoSystems]]), the control-flow vocabulary is:

- **Branching** — [[IfStatement|`if`]] / [[ElseStatement|`else`]] / `else if` for boolean-driven decisions; [[SwitchStatement|`switch`]] / [[CaseLabel|`case`]] for integer-dispatched multi-way branches.
- **Iteration** — [[WhileLoop|`while`]] (test-first, zero-or-more), [[DoWhileLoop|`do`–`while`]] (test-last, one-or-more), [[ForLoop|`for`]] (general three-clause loop).
- **Structured jumps** — [[BreakStatement|`break`]] (exit innermost loop / `switch`), [[ContinueStatement|`continue`]] (skip to next iteration).
- **Function call/return** — a [[FunctionCall|call]] transfers control into a [[Function|function]], pushing a [[StackFrame|stack frame]]; a [[ReturnStatement|`return`]] transfers control back to the caller, popping the frame. Introduced in [[dis-1-4-functions|Ch 1.4]] as a control-flow operation layered *on top of* the branches and loops of Ch 1.3.

[[CLanguage|C]]'s control-flow surface is **syntactically distinct** from [[Python]]'s (parenthesized tests, `{ }` blocks, `;` terminators) but **semantically nearly identical** for the branching constructs. The one structural divergence is the [[ForLoop|`for` loop]]: in C, it is a *general* three-clause loop equivalent in power to [[WhileLoop|`while`]]; in Python, `for` iterates a sequence.

## From The Fuzzing Book — Tracking Information Flow
Beyond syntax, control flow is also a channel for *information*. [[fuzzingbook-19-information-flow|Ch 19]] shows that an input value can determine a program's output purely by deciding *which branch executes* (e.g. `if c == 'a': t += 'a'`), with no direct data assignment between input and output. This [[ImplicitInformationFlow|implicit (control-flow) information flow]] is the explicit counterpart's blind spot: it cannot be observed by [[DynamicTaintAnalysis|dynamic taint analysis]], which is why the chapter recommends treating untainted values as worst-case and defers full handling to the symbolic methods of [[fuzzingbook-20-concolic-fuzzer|Ch 20]].

## From The Fuzzing Book — Concolic Fuzzing
[[fuzzingbook-20-concolic-fuzzer|Ch 20]] treats control flow as the *object of analysis*: it visualizes a function's coverage as control-flow-graph **arcs** (via an `ArcCoverage(Coverage)` subclass and `gen_cfg`/`to_graph` from the `ControlFlow` module), then targets the *un-taken* (red) branches. [[ConcolicExecution|Concolic execution]] records, for each branch decision on the executed path, the predicate that decided it — the [[PathConstraint|path condition]] — so negating one predicate and re-solving with an [[SMTSolver|SMT solver]] forces the opposite branch. The chapter also reaffirms Ch 19's caveat: **implicit / indirect control flow** can obscure the predicates encountered, the same blind spot that defeats [[DynamicTaintAnalysis|dynamic taint analysis]].

## From The Fuzzing Book — Symbolic Fuzzing
[[fuzzingbook-21-symbolic-fuzzer|Ch 21]] makes the **control-flow graph** the central data structure of [[SymbolicExecution|symbolic execution]]. The `ControlFlow` module's `PyCFG().gen_cfg()` (with `gen_cfg`/`to_graph`/`show_cfg`) builds a CFG from a function's source; the [[SymbolicFuzzer|`SymbolicFuzzer`]] then statically *walks* this graph to enumerate every execution path — each branch node forks into children, and a path through the CFG is a chain of `PNode`s (an [[ExecutionTree|execution tree]]). For each path it collects the branch predicates as a [[PathConstraint|path condition]] (negating the predicate when the else-edge is taken) and solves it with [[Z3Prover|Z3]]. Loops in the CFG are handled by bounded *unrolling* (`max_iter`/`max_depth`) rather than invariant inference, and the resulting branch+statement coverage is visualized back onto the CFG arcs via the reused `ArcCoverage`/`VisualizedArcCoverage`. This is the static counterpart to [[fuzzingbook-20-concolic-fuzzer|Ch 20]]'s dynamic, arc-targeting view of the same graph.

## Connections

- [[ImplicitInformationFlow]] — information that flows through control flow (branch selection) rather than data, per [[fuzzingbook-19-information-flow|Ch 19]].
- [[SymbolicExecution]] / [[SymbolicFuzzer]] / [[ExecutionTree]] / [[PathConstraint]] — Ch 21 statically walks the CFG (`PyCFG`/`gen_cfg`) to enumerate paths and solve their conditions.
- [[ConcolicExecution]] / [[PathConstraint]] / [[BranchCoverage]] — Ch 20 records and negates per-branch predicates to drive execution down un-taken control-flow arcs.
- [[dis-1-3-conditionals-loops]] — the [[DiveIntoSystems]] section that introduces this concept for C.
- [[dis-1-4-functions]] — adds the call/return layer on top of the branch/loop layer.
- [[Function]] / [[FunctionCall]] / [[ReturnStatement]] / [[StackFrame]] / [[ExecutionStack]] — the call/return control-flow vocabulary.
- [[IfStatement]] / [[ElseStatement]] / [[SwitchStatement]] / [[CaseLabel]] — branching primitives.
- [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] — iteration primitives.
- [[BreakStatement]] / [[ContinueStatement]] — structured jumps inside loops / `switch`.
- [[CBooleanExpression]] / [[RelationalOperator]] / [[LogicalOperator]] / [[ShortCircuitEvaluation]] — the decision-vocabulary used by every branch and loop test.
- [[CLanguage]] — the host language for the [[DiveIntoSystems]] treatment.
- [[Python]] — contrast language for the *syntax-different, semantics-same* cross-walk.
