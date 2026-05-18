---
title: "Dive into Systems — Ch 1.8 Exercises"
type: source
tags: [book, dive-into-systems, exercises, c-language]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/exercises.html
---

## Summary

Section 1.8 of [[DiveIntoSystems]] is the **exercises section** that closes Ch 1 *By the C, the Beautiful C* — a single-page redirect (*"All Chapter 1 Exercises"*) into the book's interactive exercises platform rather than inline problems. The exercise set drills the Ch 1 surface area the reader is expected to actively type and run: the [[CompilationProcess|compile-then-run]] toolchain ([[dis-1-1-getting-started|Ch 1.1]]), [[Printf|`printf`]] / [[Scanf|`scanf`]] [[StandardIOLibrary|hosted I/O]] ([[dis-1-2-input-output|Ch 1.2]]), [[ControlFlow|conditionals and loops]] ([[dis-1-3-conditionals-loops|Ch 1.3]]), [[Function|functions]] with [[PassByValue|pass-by-value]] semantics ([[dis-1-4-functions|Ch 1.4]]), [[CArray|arrays]] / [[CString|strings]] ([[dis-1-5-arrays-strings|Ch 1.5]]), and [[CStruct|structs]] ([[dis-1-6-structs|Ch 1.6]]). Carries no new conceptual material — its role is to **operationalize** Ch 1's claims by making the reader exercise the [[CLanguage|C]] constructs end-to-end, in line with [[dis-0-introduction|Ch 0]]'s *active-reading-by-typing-the-code* pedagogy.

## Key Claims

- **Closes Ch 1 with a problem set, not prose.** Ch 1.8 is a one-line section pointing readers to *"All Chapter 1 Exercises"* on the book's interactive exercises platform — no inline problems are presented on the chapter page itself.
- **Drills the Ch 1.1–Ch 1.6 surface area.** The exercise set targets exactly the constructs Ch 1 introduced: the [[CompilationProcess|compile / link / run]] cycle with [[GCC|`gcc`]] ([[dis-1-1-getting-started|Ch 1.1]]), [[VariableDeclaration|typed declarations]] and [[CPrimitiveType|primitive types]], [[CArithmeticOperators|arithmetic operators]] with the [[IntegerDivision|integer-division]] trap, [[Printf|`printf`]] / [[Scanf|`scanf`]] [[FormatSpecifier|format specifiers]] and the [[AddressOfOperator|`&` address-of]] discipline ([[dis-1-2-input-output|Ch 1.2]]), [[IfStatement|`if`]] / [[ElseStatement|`else`]] / [[SwitchStatement|`switch`]] branching and the three loop forms [[WhileLoop|`while`]] / [[DoWhileLoop|`do`-`while`]] / [[ForLoop|`for`]] ([[dis-1-3-conditionals-loops|Ch 1.3]]), [[FunctionDefinition|function definitions]] + [[FunctionPrototype|prototypes]] with [[PassByValue|pass-by-value]] semantics ([[dis-1-4-functions|Ch 1.4]]), [[CArray|array]] indexing / iteration and [[CString|C-string]] [[NullTerminator|`'\0'`]] handling with [[StringLibrary|`<string.h>`]] ([[dis-1-5-arrays-strings|Ch 1.5]]), and [[CStruct|struct]] declaration / [[MemberAccessOperator|`.` field access]] / [[StructAssignment|whole-record copy]] ([[dis-1-6-structs|Ch 1.6]]).
- **Operationalizes the active-reading pedagogy.** Per [[dis-0-introduction|Ch 0]], *Dive into Systems* is an active-reading textbook — readers are expected to type, compile, and run the [[CLanguage|C]] examples rather than skim. Ch 1.8 is the place that pedagogical stance is enforced at chapter close: the exercises make the reader exercise the constructs end-to-end before progressing to Ch 2.
- **Introduces no new concepts.** Like [[dis-1-7-summary|Ch 1.7]], Ch 1.8 carries no new claims about [[CLanguage|C]] — it is **purely a problem set**, and any concept it tests is already a wiki page added by [[dis-1-1-getting-started|Ch 1.1]]–[[dis-1-6-structs|Ch 1.6]].

## Key Quotes

> "All Chapter 1 Exercises" — the section's sole inline content, a hyperlink to the book's interactive exercises platform; the exercises themselves are hosted off-page.

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 1.8, the exercise set that **closes Ch 1** *By the C, the Beautiful C*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-0-introduction]] — supplies the *active-reading-by-typing-the-code* pedagogy that the exercises operationalize.
- [[dis-1-1-getting-started]] — Ch 1.1; the [[CompilationProcess|compile-then-run]] toolchain, [[VariableDeclaration|typed declarations]], [[CPrimitiveType|primitive types]], [[CArithmeticOperators|arithmetic]] / [[IntegerDivision|integer-division]] traps the exercises drill.
- [[dis-1-2-input-output]] — Ch 1.2; [[Printf|`printf`]] / [[Scanf|`scanf`]] with [[FormatSpecifier|`%`-specifiers]] and the [[AddressOfOperator|`&` address-of]] discipline.
- [[dis-1-3-conditionals-loops]] — Ch 1.3; [[ControlFlow|control-flow]] constructs ([[IfStatement|`if`]] / [[SwitchStatement|`switch`]] / [[WhileLoop|`while`]] / [[DoWhileLoop|`do`-`while`]] / [[ForLoop|`for`]]) the exercises iterate on.
- [[dis-1-4-functions]] — Ch 1.4; [[Function|function]] [[FunctionDefinition|definitions]] / [[FunctionPrototype|prototypes]] / [[PassByValue|pass-by-value]] semantics.
- [[dis-1-5-arrays-strings]] — Ch 1.5; [[CArray|array]] indexing and [[CString|C-string]] / [[NullTerminator|null-terminator]] handling with [[StringLibrary|`<string.h>`]].
- [[dis-1-6-structs]] — Ch 1.6; [[CStruct|struct]] declaration and [[MemberAccessOperator|`.`-field-access]] / [[StructAssignment|whole-record copy]] discipline.
- [[dis-1-7-summary]] — Ch 1.7; the immediately preceding section — a recap with no new material; Ch 1.8 is its exercise companion.
- [[CLanguage]] — the language the exercises exercise.

## Contradictions

- No contradictions — Ch 1.8 is a problem set with no new claims and introduces no concepts not already established in [[dis-1-1-getting-started|Ch 1.1]]–[[dis-1-6-structs|Ch 1.6]].
