---
title: "Return Type (C)"
type: concept
tags: [c-language, functions, types]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# Return Type (C)

The **return type** is the typed slot at the front of a [[Function|function]] header that names the type of the value the function yields back to its [[FunctionCall|caller]] via a [[ReturnStatement|`return`]].

```c
int  max(int n1, int n2)            { /* returns int */ }
void print_table(int start, int stop) { /* returns nothing */ }
```

A [[CLanguage|C]] function returns **at most one** value, whose type the [[CCompiler|compiler]] checks against every [[ReturnStatement|`return`]] inside the body. Functions that produce no useful value declare their return type as [[VoidType|`void`]].

## Why explicit

[[CLanguage|C]] is [[StaticallyTyped|statically typed]] — the [[CCompiler|compiler]] needs the return type at every [[FunctionCall|call site]] to know what type the expression `f(...)` has, what register/ABI convention to use, and whether assignments like `int x = f();` type-check. This is why even a [[FunctionPrototype|prototype]] must carry the return type.

## Conversions and the `main` special case

If the function declares `int` and `return` is given a `double` (or vice versa), the [[CCompiler|compiler]] inserts the usual C conversions. The [[MainFunction|`main`]] function is a special case: its `int` return value becomes the process's [[ExitStatus|exit status]] — `0` for success.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionDefinition]] / [[FunctionPrototype]] — return type sits at the front of every header.
- [[ReturnStatement]] — the construct that supplies a value of this type.
- [[VoidType]] — the *no-value* return type.
- [[MainFunction]] / [[ExitStatus]] — the special-case return-type-as-exit-status.
- [[CPrimitiveType]] — the set of available return types alongside `void`.
- [[CLanguage]] / [[DiveIntoSystems]].
