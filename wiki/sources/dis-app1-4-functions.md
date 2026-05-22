---
title: "Dive into Systems — Appendix 1.4 Functions (for Java Programmers)"
type: source
tags: [book, dive-into-systems, c-language, java, functions, cross-walk]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix1/functions.html
---

## Summary

Appendix 1.4 of [[DiveIntoSystems]] is the [[Java]]-programmer's retelling of [[dis-1-4-functions|Ch 1.4]]. Introduces standalone [[Function|functions]] (vs. Java's class methods), [[FunctionPrototype|prototypes]] (Java doesn't need them), explicit [[ReturnStatement|return]] types including [[VoidType|`void`]], and crucially the [[ExecutionStack|execution stack]] of [[StackFrame|stack frames]] — the runtime structure C exposes but Java hides. **Pass-by-value semantics are identical for primitives**, but Java's "objects by reference" model has no direct C analog (Ch 1.4 covers only primitives; structs/arrays are deferred to Ch 1.5–1.6). See [[JavaVsC]] for the consolidated cross-walk.

## Key Claims (Java-vs-C deltas)

- **C functions are standalone; Java methods live in classes.** *"C is an imperative and procedural language and Java is an object oriented language."* No `static` keyword, no class wrapper, no `this`.
- **C requires [[FunctionPrototype|prototypes]] or full definitions before use.** Java's compiler resolves forward references inside a class automatically; C's compiler reads top-to-bottom and needs the signature ahead of any call site.
- **[[PassByValue|Pass-by-value]] is identical for primitives**: *"any change to a parameter's value in the function is not visible to the caller."* Same rule in both languages.
- **The Java "objects by reference" exception does not apply here** — Ch 1.4 only covers primitive-typed functions. The C analog (passing addresses) is deferred to Ch 2 pointers; the array/struct cases are in Appendix 1.5 / 1.6.
- **[[ReturnStatement|`return`]] type declared explicitly** in both languages, including [[VoidType|`void`]] for no-return functions.
- **C exposes the [[ExecutionStack|execution stack]] explicitly**: *"when a function is called, a new stack frame is created and space for its local variables and parameters is allocated."* Java has the same runtime structure but abstracts it away (no `sizeof`, no addresses, no stack-frame inspection outside the debugger).
- **[[FunctionScope|Scope]] is per-stack-frame** in C — variables disappear when the frame pops. Same effective rule in Java, but Java's GC + closure capture (in lambdas) changes the surface.

## Key Quote

> *"any change to a parameter's value in the function … is not visible to the caller."* — pass-by-value rule, identical between Java primitives and all C non-pointer arguments.

## Worked example — function with prototype

```c
#include <stdio.h>

int max(int a, int b);   // prototype required before main can call it

int main(void) {
    printf("%d\n", max(3, 7));
    return 0;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}
```

In Java, `static int max(int a, int b) { ... }` inside a class — no separate prototype.

## Connections

- [[DiveIntoSystems]] — Appendix 1 sister of [[dis-1-4-functions|Ch 1.4]].
- [[dis-1-4-functions]] — the Python-cross-walk sibling.
- [[JavaVsC]] — consolidated cross-walk table.
- [[Java]] — the source language; method-in-class organization is the headline delta.
- [[Function]] / [[FunctionDefinition]] / [[FunctionPrototype]] / [[FunctionParameter]] / [[FunctionArgument]] / [[ReturnStatement]] / [[VoidType]] / [[PassByValue]] / [[ExecutionStack]] / [[StackFrame]] / [[LocalVariable]] / [[FunctionScope]] / [[MainFunction]] — reused unchanged from Ch 1.4.

## Contradictions

- None. Pure Java-perspective retelling of [[dis-1-4-functions|Ch 1.4]].
