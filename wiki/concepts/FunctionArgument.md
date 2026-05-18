---
title: "Function Argument (C)"
type: concept
tags: [c-language, functions]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Function Argument (C)

An **argument** is the *concrete expression* (often a value, variable, or sub-expression) supplied at a [[FunctionCall|function call site]] to initialize a [[FunctionParameter|parameter]] in the called [[Function|function]].

```c
larger = max(x, y);     /* x and y are arguments to max */
print_table(x, larger); /* x and larger are arguments to print_table */
```

[[CLanguage|C]] matches arguments to parameters **positionally** and **by type**, then **[[PassByValue|passes by value]]** — the value of each argument expression is *copied* into the parameter slot in the new [[StackFrame|stack frame]].

## Argument vs. parameter

- **[[FunctionParameter|Parameter]]** — the *name* declared in the function header.
- **[[FunctionArgument|Argument]]** — the *value* supplied at the call site.

[[dis-1-4-functions|DIS Ch 1.4]] treats this distinction as load-bearing. *Parameters are placeholders; arguments fill them.*

## Pass-by-value consequence

Because of [[PassByValue|pass-by-value]], an argument may safely be an arbitrary expression — `max(x + 1, 2 * y)` — and the function cannot observe the *origin* of its parameter values, only the values themselves. The function also cannot modify the caller's variable through the parameter; for output-parameter semantics, [[CLanguage|C]] requires explicit address passing (introduced in the pointer chapter that follows).

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[FunctionParameter]] — the *placeholder* term; this is the *value* term.
- [[FunctionCall]] — the construct that supplies arguments.
- [[PassByValue]] — argument values are *copied* into parameter slots.
- [[Function]] / [[CLanguage]] / [[DiveIntoSystems]].
