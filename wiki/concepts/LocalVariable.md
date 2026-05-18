---
title: "Local Variable (C)"
type: concept
tags: [c-language, variables, functions, scope]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Local Variable (C)

A **local variable** in [[CLanguage|C]] is a variable [[VariableDeclaration|declared]] inside a [[Function|function]] body. Per [[dis-1-4-functions|DIS Ch 1.4]] §1.4.1, *"each function call creates a new stack frame … containing its parameter and local variable values"* — so local variables:

- live in that call's [[StackFrame|stack frame]] on the [[ExecutionStack|execution stack]];
- are in scope only within their enclosing function ([[FunctionScope|function scope]]);
- vanish when the function [[ReturnStatement|returns]] (its frame is popped).

```c
int max(int n1, int n2) {
    int result;       /* local variable */
    result = n1;
    if (n2 > n1) result = n2;
    return result;
}
```

`result` is local to `max`. Every new [[FunctionCall|call]] to `max` allocates a fresh `result` in a fresh [[StackFrame|frame]] — calls do not see each other's locals.

## Parameter vs. local

A [[FunctionParameter|parameter]] behaves like a local variable that was *initialized from the [[FunctionArgument|argument]]*. Both live in the same [[StackFrame|stack frame]]; both are in [[FunctionScope|scope]] only within the function; both vanish on [[ReturnStatement|return]]. The single difference is *initialization* — parameters get their value [[PassByValue|by-value]] from the call, locals are declared explicitly.

## Style note

[[DiveIntoSystems]] recommends declaring locals at the top of the function body for readability, though modern [[CLanguage|C]] (C99+) allows declarations anywhere a statement is legal — see [[VariableDeclaration]].

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionScope]] / [[StackFrame]] / [[ExecutionStack]] — the framing concepts.
- [[FunctionParameter]] — a parameter is a local variable initialized from the [[FunctionArgument|argument]].
- [[VariableDeclaration]] — the *syntactic* construct that creates a local.
- [[FunctionCall]] / [[ReturnStatement]] — create and destroy local-variable storage.
- [[CLanguage]] / [[DiveIntoSystems]].
