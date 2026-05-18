---
title: "void Type (C)"
type: concept
tags: [c-language, types, functions]
sources: [dis-1-4-functions]
last_updated: 2026-05-17
---

# void Type (C)

**`void`** in [[CLanguage|C]] is the *no-value* type. It appears in two positions a beginner most often meets in [[dis-1-4-functions|DIS Ch 1.4]]:

## (1) Return type — *function yields nothing*

```c
void print_table(int start, int stop) {
    /* ...prints squares... */
}
```

Per [[dis-1-4-functions|Ch 1.4]]: *"Functions that don't return a value should specify the `void` return type."* In a `void` [[Function|function]], a bare [[ReturnStatement|`return;`]] (or simply falling off the closing `}`) ends the call.

## (2) Parameter list — *function takes nothing*

```c
int main(void) { /* ... */ }
```

`void` in the parameter list declares the function *takes no parameters*. Distinct from an *empty* parameter list `int main()`, which in classic C means *"parameters unspecified"* — `void` is the explicit, recommended form ([[MainFunction|see `main`]]).

## (3) Generic pointer — `void *` (not in Ch 1.4)

[[CLanguage|C]] also uses `void *` as the *type-erased pointer*, the wiki will get to that when later [[DiveIntoSystems]] chapters introduce pointers and `malloc`.

## Connections

- [[dis-1-4-functions]] — introducing source.
- [[Function]] / [[FunctionDefinition]] / [[FunctionPrototype]] — `void` is a legal return type.
- [[ReturnType]] — the slot `void` can fill.
- [[ReturnStatement]] — `return;` (bare) exits a void function.
- [[FunctionParameter]] / [[MainFunction]] — `void` in the parameter list = no parameters.
- [[CPrimitiveType]] — `void` sits *next to* the primitive types as a special non-value type.
- [[CLanguage]] / [[DiveIntoSystems]].
