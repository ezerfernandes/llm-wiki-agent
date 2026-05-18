---
title: "Dive into Systems — Ch 2.11 Exercises"
type: source
tags: [book, dive-into-systems, exercises, c-language]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/exercises.html
---

## Summary

Section 2.11 of [[DiveIntoSystems]] is the **exercise set that closes Ch 2 *A Deeper Dive Into C*** — a single-page redirect (*"All Chapter 2 Exercises"*) into the book's interactive exercises platform, structurally identical to [[dis-1-8-exercises|Ch 1.8]] at the end of Ch 1. Carries no new conceptual material; operationalizes [[dis-0-introduction|Ch 0]]'s *active-reading-by-typing-the-code* pedagogy across the Ch 2.1–Ch 2.9 surface area ([[Pointer|pointers]], [[DynamicMemoryAllocation|dynamic memory]], [[CArray|arrays]], [[CString|strings]], [[CStruct|structs]], [[StandardIOLibrary|I/O]], and the [[CConstant|`#define`]] / [[SwitchStatement|`switch`]] / [[CEnum|`enum`]] / [[Typedef|`typedef`]] / [[CommandLineArguments|`argc`/`argv`]] / [[VoidPointer|`void *`]] / [[PointerArithmetic|pointer arithmetic]] / [[CLibrary|libraries]] / [[AssemblyLanguage|C→assembly]] advanced features). **Final section of Ch 2 — Ch 2 *A Deeper Dive Into C* is now fully complete.**

## Key Claims

- **Closes Ch 2 with a problem set, not prose.** Ch 2.11 is a one-line section pointing readers to *"All Chapter 2 Exercises"* on the book's interactive exercises platform — no inline problems on the chapter page.
- **Drills the Ch 2.1–Ch 2.9 surface area.** The exercise set targets the deferred-then-delivered Ch 2 deepenings: [[ProcessMemory|four-region memory model]] + [[VariableScope|scope]] ([[dis-2-1-scope-memory|Ch 2.1]]), [[Pointer|pointer]] declaration / [[AddressOfOperator|`&`]] / [[DereferenceOperator|`*`]] ([[dis-2-2-pointers|Ch 2.2]]), [[PassByPointer|pass-by-pointer]] output parameters ([[dis-2-3-pointers-functions|Ch 2.3]]), [[Malloc|`malloc`]] / [[Free|`free`]] / [[NullPointer|`NULL`]]-after-`free` discipline ([[dis-2-4-dynamic-memory|Ch 2.4]]), [[DynamicallyAllocatedArray|dynamic 1D arrays]] / [[MultidimensionalArray|2D arrays]] / [[ArrayOfArrays|array-of-arrays]] / [[RowMajorOrder|row-major layout]] ([[dis-2-5-arrays|Ch 2.5]]), the full [[StringLibrary|`<string.h>`]] ([[dis-2-6-strings|Ch 2.6]]), [[PointerToStruct|pointer-to-struct]] with [[ArrowOperator|`->`]] / [[SelfReferentialStruct|self-referential structs]] / [[LinkedList|linked lists]] ([[dis-2-7-structs|Ch 2.7]]), [[FilePointer|`FILE *`]] file I/O / [[Fopen|`fopen`]] / [[Fscanf|`fscanf`]] / [[StreamRedirection|stream redirection]] ([[dis-2-8-io|Ch 2.8]]), and the seven advanced subsections ([[dis-2-9-1-advanced-switch|Ch 2.9.1]] [[CConstant|`#define`]] / [[SwitchStatement|`switch`]] / [[CEnum|`enum`]] / [[Typedef|`typedef`]]; [[dis-2-9-2-cmd-line-args|Ch 2.9.2]] [[CommandLineArguments|`argc`/`argv`]]; [[dis-2-9-3-voidstar|Ch 2.9.3]] [[VoidPointer|`void *`]]; [[dis-2-9-4-pointer-arithmetic|Ch 2.9.4]] [[PointerArithmetic|pointer arithmetic]]; [[dis-2-9-5-libraries|Ch 2.9.5]] [[CLibrary|library usage]]; [[dis-2-9-6-writing-libraries|Ch 2.9.6]] [[HeaderGuard|header-guarded]] [[StaticLibrary|`.a`]] / [[DynamicLibrary|`.so`]] authoring; [[dis-2-9-7-c-to-assembly|Ch 2.9.7]] [[GCC|`gcc -S`]] [[CLanguage|C]] → [[AssemblyLanguage|assembly]]).
- **Operationalizes the active-reading pedagogy.** Per [[dis-0-introduction|Ch 0]], *Dive into Systems* is an active-reading textbook — readers are expected to type, compile, and run the [[CLanguage|C]] examples. Ch 2.11 is where that stance is enforced at the chapter close, mirroring [[dis-1-8-exercises|Ch 1.8]] at the end of Ch 1.
- **Introduces no new concepts.** Like [[dis-2-10-summary|Ch 2.10 Summary]], Ch 2.11 carries no new claims about [[CLanguage|C]] — it is **purely a problem set**, and any concept it tests is already a wiki page added by [[dis-2-1-scope-memory|Ch 2.1]]–[[dis-2-9-7-c-to-assembly|Ch 2.9.7]].
- **Structural sibling of [[dis-1-8-exercises|Ch 1.8 Exercises]].** Same single-line "All Chapter N Exercises" redirect pattern at the close of a chapter; same role (problem-set close vs [[dis-2-10-summary|Ch 2.10]]'s prose summary close).

## Key Quotes

> "All Chapter 2 Exercises" — the section's sole inline content, a hyperlink to `/exercises/dive-into-systems-exercises-5.html` on the book's interactive exercises platform; the exercises themselves are hosted off-page.

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 2.11, the exercise set that **closes Ch 2** *A Deeper Dive Into C*. With Ch 2.11 ingested, **Ch 2 is fully complete (eleven sections: 2.1–2.9 hub + 2.9.1–2.9.7 + 2.10 + 2.11)**.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-0-introduction]] — supplies the *active-reading-by-typing-the-code* pedagogy that the exercises operationalize.
- [[dis-1-8-exercises]] — Ch 1.8; the structural sibling at the close of Ch 1 — same single-line redirect pattern.
- [[dis-2-10-summary]] — Ch 2.10; the immediately preceding section — a prose recap with no new material; Ch 2.11 is its problem-set companion (mirroring the [[dis-1-7-summary|Ch 1.7]] / [[dis-1-8-exercises|Ch 1.8]] pairing at Ch 1 close).
- [[dis-2-1-scope-memory]] — Ch 2.1; [[ProcessMemory|four-region program memory model]] + first formal [[VariableScope|scope]] definition.
- [[dis-2-2-pointers]] — Ch 2.2; [[Pointer|pointer]] declaration / [[AddressOfOperator|`&`]] / [[DereferenceOperator|`*`]] / [[NullPointer|`NULL`]] safety.
- [[dis-2-3-pointers-functions]] — Ch 2.3; [[PassByPointer|pass-by-pointer]] output parameters.
- [[dis-2-4-dynamic-memory]] — Ch 2.4; [[Malloc|`malloc`]] / [[Free|`free`]] / [[NullPointer|`NULL`]]-after-`free` discipline.
- [[dis-2-5-arrays]] — Ch 2.5; [[DynamicallyAllocatedArray|dynamic 1D]] / [[MultidimensionalArray|2D arrays]] / [[ArrayOfArrays|array-of-arrays]] / [[RowMajorOrder|row-major]] / [[ArrayDecay|array decay]].
- [[dis-2-6-strings]] — Ch 2.6; the full [[StringLibrary|`<string.h>`]] surface area.
- [[dis-2-7-structs]] — Ch 2.7; [[PointerToStruct|pointer-to-struct]] / [[ArrowOperator|`->`]] / [[SelfReferentialStruct|self-referential]] / [[LinkedList|linked list]].
- [[dis-2-8-io]] — Ch 2.8; [[FilePointer|`FILE *`]] file I/O / [[Fopen|`fopen`]] / [[Fscanf|`fscanf`]] / [[StreamRedirection|stream redirection]].
- [[dis-2-9-advanced]] — Ch 2.9 hub; forwards to the seven advanced subsections drilled below.
- [[dis-2-9-1-advanced-switch]] — Ch 2.9.1; [[CConstant|`#define`]] / [[SwitchStatement|`switch`]] / [[CEnum|`enum`]] / [[Typedef|`typedef`]].
- [[dis-2-9-2-cmd-line-args]] — Ch 2.9.2; [[CommandLineArguments|`argc`/`argv`]].
- [[dis-2-9-3-voidstar]] — Ch 2.9.3; [[VoidPointer|`void *`]].
- [[dis-2-9-4-pointer-arithmetic]] — Ch 2.9.4; [[PointerArithmetic|pointer arithmetic]].
- [[dis-2-9-5-libraries]] — Ch 2.9.5; [[CLibrary|library]] usage / [[CompilationProcess|five-stage pipeline]].
- [[dis-2-9-6-writing-libraries]] — Ch 2.9.6; authoring [[StaticLibrary|`.a`]] / [[DynamicLibrary|`.so`]] with [[HeaderGuard|header guards]].
- [[dis-2-9-7-c-to-assembly]] — Ch 2.9.7; [[GCC|`gcc -S`]] [[CLanguage|C]] → [[AssemblyLanguage|assembly]].
- [[CLanguage]] — the language the exercises exercise.

## Contradictions

- No contradictions — Ch 2.11 is a problem set with no new claims and introduces no concepts not already established in [[dis-2-1-scope-memory|Ch 2.1]]–[[dis-2-9-7-c-to-assembly|Ch 2.9.7]].
