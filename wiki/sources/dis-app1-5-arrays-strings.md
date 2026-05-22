---
title: "Dive into Systems — Appendix 1.5 Arrays and Strings (for Java Programmers)"
type: source
tags: [book, dive-into-systems, c-language, java, arrays, strings, cross-walk]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix1/arrays_strings.html
---

## Summary

Appendix 1.5 of [[DiveIntoSystems]] is the [[Java]]-programmer's retelling of [[dis-1-5-arrays-strings|Ch 1.5]]. The cross-walk has **larger deltas than any other Appendix 1 section** because Java's `String` class and bounds-checked `int[]` arrays abstract heavily over what C exposes directly: [[CArray|raw `char` arrays]], [[NullTerminator|`'\0'` termination]], [[BoundsChecking|no bounds checking]], and the explicit [[BufferOverflow|buffer-overflow]] hazard of [[Strcpy|`strcpy`]]. See [[JavaVsC]] for the consolidated cross-walk.

## Key Claims (Java-vs-C deltas)

- **Java arrays have built-in `.length`; C arrays do not.** Java: `arr.length`. C: programmer must track capacity in a separate variable.
- **Java throws [[BoundsChecking|`ArrayIndexOutOfBoundsException`]] on overflow; C has no [[BoundsChecking|bounds checking]] at compile or runtime.** *"It's up to the programmer to ensure that their code uses only valid index values."* Out-of-bounds access in C is undefined behavior and a security hazard.
- **Array syntax differs**: Java `int[] arr = new int[N];` vs. C `int arr[N];`. C arrays of fixed capacity live on the stack; dynamic-size arrays require [[Malloc|`malloc`]] (Ch 2.4).
- **Java's `String` class is a heap-allocated immutable object with rich methods**; C's [[CString|string]] is a **`char` array terminated by `'\0'`**. *"Strings in C are arrays of char values."*
- **Capacity planning matters in C**: storing `"hi"` requires **3 chars** (`'h'`, `'i'`, `'\0'`). Java's `String` handles this implicitly.
- **[[StringLibrary|`<string.h>`]] is C's analog to Java's `String` methods**: [[Strlen|`strlen`]] ↔ `.length()`, [[Strcpy|`strcpy`]] ↔ assignment, [[Sprintf|`sprintf`]] ↔ `String.format`. But — *"`strcpy` poses a security risk because it assumes that its destination is large enough to store the entire string."* Java's immutable `String` makes this category of bug impossible.
- **Array pass to function is [[PassByReference|effective pass-by-reference]] in C** (array name decays to pointer) — matches **Java's array-passing behavior** (Java arrays are objects, passed by reference). This is the **one Java cross-walk where pass semantics line up** with C's "default."

## Key Quotes

> *"There is no bounds checking by the compiler or at runtime."* — the headline C-vs-Java safety delta.

> *"`strcpy` poses a security risk because it assumes that its destination is large enough to store the entire string."* — Ch 1.5's headline security warning, identical to the Python cross-walk.

## Worked example — Java `String` → C `char[]`

```c
#include <stdio.h>
#include <string.h>
int main(void) {
    char greeting[10] = "hello";       // capacity 10, contents "hello\0"
    printf("len = %zu\n", strlen(greeting));   // 5, not 10
    char copy[10];
    strcpy(copy, greeting);            // OK — copy is large enough
    // strcpy(copy, "this string is way too long!");  // buffer overflow
    return 0;
}
```

Java equivalent: `String greeting = "hello"; int len = greeting.length();` — no `\0`, no capacity, no overflow risk.

## Connections

- [[DiveIntoSystems]] — Appendix 1 sister of [[dis-1-5-arrays-strings|Ch 1.5]].
- [[dis-1-5-arrays-strings]] — the Python-cross-walk sibling.
- [[JavaVsC]] — consolidated cross-walk table.
- [[Java]] — Java's `String` class and bounds-checked arrays are the major abstractions C strips away.
- [[CArray]] / [[CString]] / [[NullTerminator]] / [[ArrayIndexing]] / [[BoundsChecking]] / [[PassByReference]] / [[StringLibrary]] / [[Strlen]] / [[Strcpy]] / [[Sprintf]] / [[BufferOverflow]] — reused unchanged from Ch 1.5.

## Contradictions

- None. Pure Java-perspective retelling of [[dis-1-5-arrays-strings|Ch 1.5]].
