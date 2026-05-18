---
title: "Function Call (C)"
type: concept
tags: [c-language, functions, runtime, control-flow]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function Call (C)

A **function call** in [[CLanguage|C]] is the syntactic and runtime act of invoking a previously [[FunctionDefinition|defined]] (or [[FunctionPrototype|prototyped]]) [[Function|function]]:

```c
larger = max(x, y);          /* value-returning call: result captured */
print_table(x, larger);      /* void call: result discarded / none */
```

Syntactically: `<function name>(<argument list>)`. The [[FunctionArgument|argument list]] is comma-separated expressions, matched positionally to the function's [[FunctionParameter|parameters]].

## Runtime semantics (per [[dis-1-4-functions|DIS Ch 1.4]] §1.4.1)

A call:

1. **Evaluates each [[FunctionArgument|argument]]** expression in the caller.
2. **Pushes a new [[StackFrame|stack frame]]** onto the [[ExecutionStack|execution stack]] with space for the callee's [[FunctionParameter|parameters]] and [[LocalVariable|locals]].
3. **Initializes the parameters [[PassByValue|by value]]** from the argument values.
4. **Transfers control** into the callee's body; *only* the new frame is in [[FunctionScope|scope]].
5. On [[ReturnStatement|`return`]], **pops the frame** and resumes the caller with the returned value (if any) in place of the call expression.

Each step is reversible at return, which is what makes nested and recursive calls work — every active call has its own frame on the stack at the same time.

## Where calls can appear

A call expression has the function's [[ReturnType|return type]] as its type — so it can appear anywhere an expression of that type is legal: as the right-hand side of an assignment (`larger = max(x, y);`), inside a larger expression (`if (max(a, b) > 10) ...`), as an argument to another call, or as a standalone statement (`print_table(...);`) for [[VoidType|`void`]] functions.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionDefinition]] / [[FunctionPrototype]] — what is called.
- [[FunctionArgument]] / [[FunctionParameter]] — what is supplied and what receives it.
- [[PassByValue]] — *how* arguments become parameters.
- [[StackFrame]] / [[ExecutionStack]] / [[FunctionScope]] / [[LocalVariable]] — the per-call runtime substrate.
- [[ReturnStatement]] / [[ReturnType]] — the value (or none) the call expression evaluates to.
- [[ControlFlow]] — calls/returns are control-flow operations on top of [[IfStatement|`if`]] / [[ForLoop|`for`]] / [[WhileLoop|`while`]].
- [[CLanguage]] / [[DiveIntoSystems]].
