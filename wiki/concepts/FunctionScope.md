---
title: "Function Scope (C)"
type: concept
tags: [c-language, functions, scope, semantics]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function Scope (C)

**Function scope** is the lexical-scope rule [[CLanguage|C]] applies to [[FunctionParameter|parameters]] and [[LocalVariable|local variables]] declared inside a [[Function|function]] body: they are *visible only within that function*. Outside the function, those names do not exist; inside any other function, they refer (if anything) to different bindings.

Per [[dis-1-4-functions|DIS Ch 1.4]] §1.4.1, this rule is reinforced by the runtime: when a function is active, its [[StackFrame|stack frame]] is on top of the [[ExecutionStack|execution stack]] and *"only its local variables and parameters are in scope."* When the function returns, the frame is popped and those names are *unreachable*.

## Example

```c
int max(int n1, int n2) {
    int result;        /* result, n1, n2 are in scope here */
    result = n1;
    if (n2 > n1) result = n2;
    return result;
}

void print_table(int start, int stop) {
    /* result, n1, n2 do NOT exist here */
    int i;             /* i is in scope only here */
    /* ... */
}
```

Even though both functions could legally declare a local `int result;`, those two `result`s are *different variables* — distinct names in distinct scopes, distinct frames at runtime.

## Lifetime ≠ scope (preview)

For [[LocalVariable|local variables]] in [[CLanguage|C]] without `static`, lifetime and scope coincide: the variable exists for as long as its [[StackFrame|frame]] is on the [[ExecutionStack|stack]]. The wiki will revisit *static locals* and *globals* — which have *file scope* and *static lifetime* — when later [[DiveIntoSystems]] chapters introduce them.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionParameter]] / [[LocalVariable]] — the named entities whose visibility is governed.
- [[StackFrame]] / [[ExecutionStack]] — the runtime substrate that *enforces* scope.
- [[FunctionCall]] / [[ReturnStatement]] — push and pop the frames that gate scope.
- [[VariableDeclaration]] — declaration is what *creates* a name in a scope.
- [[CLanguage]] / [[DiveIntoSystems]].
