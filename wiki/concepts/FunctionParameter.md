---
title: "Function Parameter (C)"
type: concept
tags: [c-language, functions]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function Parameter (C)

A **parameter** is a named, typed placeholder declared in a [[Function|function]]'s header. At each [[FunctionCall|call site]], C matches [[FunctionArgument|arguments]] to parameters *positionally* and *by type*, then **initializes each parameter to the value of its corresponding argument** ([[PassByValue|pass-by-value]]).

```c
int max(int n1, int n2) {   /* n1, n2 are parameters */
    /* ... */
}

larger = max(x, y);         /* x, y are arguments */
```

In the call above, `x` is the argument that initializes parameter `n1`, and `y` is the argument that initializes `n2`.

## Parameter vs. argument

| Term | Where it lives | What it is |
|---|---|---|
| **[[FunctionParameter|Parameter]]** | In the function *header* | A named, typed placeholder |
| **[[FunctionArgument|Argument]]** | At each *call site* | The concrete value supplied |

The two terms are often confused; per [[dis-1-4-functions|DIS Ch 1.4]] they are not interchangeable.

## Parameters are local variables

Inside the function body, parameters behave exactly like [[LocalVariable|local variables]] — they live in the call's [[StackFrame|stack frame]], are in [[FunctionScope|scope]] only within that function, and may be reassigned freely. Crucially, *reassigning a parameter does not affect the caller's variable* — that's [[PassByValue|pass-by-value]].

## Empty parameter lists: `void`

A function that takes no parameters declares its parameter list as `void`:

```c
int main(void) { /* ... */ }
```

Without the `void`, an older C dialect interprets the empty list as *unspecified* (any args allowed) — see [[MainFunction]].

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionDefinition]] / [[FunctionPrototype]] — where parameters appear.
- [[FunctionArgument]] — the contrast term (value at the call site).
- [[PassByValue]] — the rule that says each parameter is **assigned** the argument's value.
- [[LocalVariable]] / [[FunctionScope]] / [[StackFrame]] — where a parameter lives at runtime.
- [[VoidType]] — `void` parameter list = no parameters.
- [[CLanguage]] / [[DiveIntoSystems]].
