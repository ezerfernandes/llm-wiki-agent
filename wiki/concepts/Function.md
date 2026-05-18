---
title: "Function (C)"
type: concept
tags: [c-language, functions, modularity]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function (C)

A **function** in [[CLanguage|C]] is a named, typed, parameterized block of code — the language's primary unit of *modularity* and *reuse*. Per [[dis-1-4-functions|DIS Ch 1.4]], a function accepts zero or more inputs ([[FunctionParameter|parameters]]) and returns *at most one* value, whose type is named in the header.

```c
<return type> <name>(<parameter list>) {
    <body>
}
```

The [[FunctionParameter|parameter list]] is a comma-separated sequence of `<type> <name>` pairs (or `void` if there are no parameters, as in `int main(void)`). The body is a `{ }` block.

## Two artifacts: definition vs. prototype

- A [[FunctionDefinition|**definition**]] supplies the full body.
- A [[FunctionPrototype|**prototype** / declaration]] gives only the header (`int max(int n1, int n2);`) so callers can name the function before its body appears in the file.

[[CLanguage|C]] is single-pass over declarations: a function must be *either* defined *or* prototyped before it is called. The standard idiom is **prototypes at the top of the file (above [[MainFunction|`main`]]), full definitions below**.

## The call/return discipline

- A [[FunctionCall|call]] pushes a new [[StackFrame|stack frame]] onto the [[ExecutionStack|execution stack]].
- That frame holds the [[FunctionParameter|parameters]] (initialized [[PassByValue|by value]] from the arguments) and the [[LocalVariable|local variables]].
- Only the **top** frame is *active*; only its names are in [[FunctionScope|scope]].
- A [[ReturnStatement|`return`]] pops the frame and yields one value back to the caller.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[FunctionDefinition]] / [[FunctionPrototype]] — the two artifacts of a function.
- [[FunctionParameter]] / [[FunctionArgument]] — parameter (in header) vs. argument (at call site).
- [[ReturnType]] / [[ReturnStatement]] / [[VoidType]] — what comes back, and how.
- [[PassByValue]] — the **headline semantic rule** for C function calls.
- [[FunctionCall]] / [[StackFrame]] / [[ExecutionStack]] / [[FunctionScope]] / [[LocalVariable]] — the runtime model.
- [[MainFunction]] — the *first* function on the [[ExecutionStack|stack]]; just one [[Function]] among many.
- [[CLanguage]] / [[DiveIntoSystems]] — host language and source book.
- [[ControlFlow]] — function calls/returns are a control-flow mechanism layered on [[IfStatement|`if`]] / [[ForLoop|`for`]] / [[WhileLoop|`while`]].
- [[Python]] — contrast: `def`, dynamic types, no prototype/definition split.
