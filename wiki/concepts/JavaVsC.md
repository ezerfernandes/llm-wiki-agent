---
title: "Java vs C"
type: concept
tags: [c-language, java, comparison, programming-paradigm]
sources: [dis-app1-1-getting-started, dis-app1-2-input-output, dis-app1-3-conditionals, dis-app1-4-functions, dis-app1-5-arrays-strings, dis-app1-6-structs, dis-app1-7-summary]
last_updated: 2026-05-18
---

# Java vs C

A structural cross-walk between [[Java]] and [[CLanguage|C]], extracted from Appendix 1 of [[DiveIntoSystems]] (the **Java-programmer's** retelling of [[dis-1-1-getting-started|Ch 1]] *By the C, the Beautiful C* — same systems content, different starting language). Sister cross-walk to the Python-vs-C framing that drives the main Ch 1 prose.

## Headline distinction

> *"C is an imperative and procedural language and Java is an object-oriented language."*

C has no classes, no methods, no inheritance, no garbage collection, and no reference-typed objects. Every C program is a flat collection of [[Function|functions]] and [[CStruct|structs]] operating directly over [[ProcessMemory|memory]].

## Surface-by-surface deltas

| Surface | [[Java]] | [[CLanguage|C]] |
|---|---|---|
| **Compilation** | `javac` → [[JVM|JVM]] bytecode; `java` runs it | [[GCC|`gcc`]] → [[BinaryExecutable|native binary]]; `./a.out` runs it directly |
| **Entry point** | `public static void main(String[] args)` inside a class | [[MainFunction|`int main(void)`]] / `int main(int argc, char **argv)` — no class wrapper |
| **Code organization** | Classes & methods (mandatory) | Free-standing [[Function|functions]] (procedural) |
| **Library import** | `import java.lang.Math;` | [[PreprocessorDirective|`#include <math.h>`]] + `-lm` link flag for libm |
| **Output** | `System.out.println()` / `System.out.printf()` | [[Printf|`printf()`]] — **no auto-newline** (explicit `\n` required) |
| **Input** | `Scanner` object + `nextInt()` / `nextLine()` | [[Scanf|`scanf()`]] + format string + [[AddressOfOperator|`&`]] for output variables |
| **Boolean type** | First-class `boolean` | None — `0` = false, nonzero = true ([[CBooleanExpression]]) |
| **Strings** | `String` class (immutable, rich methods, `.length()`) | [[CString|`char` array]] + [[NullTerminator|`'\0'`]] sentinel + [[StringLibrary|`<string.h>`]] |
| **Arrays** | `int[] a = new int[N];` — built-in `.length`, [[BoundsChecking|`ArrayIndexOutOfBoundsException`]] on overflow | `int a[N];` — no `.length`, no [[BoundsChecking|bounds checking]] at compile or run time |
| **Records** | Classes (heap, reference semantics) | [[CStruct|`struct`]] (stack or heap, **value** semantics — `s2 = s1` copies everything) |
| **Parameter passing** | Primitives by value; **objects by reference** | Everything [[PassByValue|by value]] (including structs); arrays decay to pointers — [[PassByReference|effective pass-by-reference]] |
| **Memory management** | Garbage-collected | Manual — programmer owns allocation and deallocation |

## Shared surface (no delta)

- [[CArithmeticOperators|Arithmetic operators]] `+` `-` `*` `/` `%`, compound-assignment, and [[IncrementOperator|`++` / `--`]] are syntactically identical (the pre/post distinction matches Java's exactly).
- [[RelationalOperator|Relational]] (`==` `!=` `<` `<=` `>` `>=`) and [[LogicalOperator|logical]] (`!` `&&` `||`) operators are identical, including [[ShortCircuitEvaluation|short-circuit evaluation]].
- [[ControlFlow|Control-flow]] constructs ([[IfStatement|`if`]] / [[ElseStatement|`else`]] / [[SwitchStatement|`switch`]] / [[WhileLoop|`while`]] / [[DoWhileLoop|`do`–`while`]] / [[ForLoop|`for`]] / [[BreakStatement|`break`]] / [[ContinueStatement|`continue`]]) are syntactically identical — Java adds an enhanced for-each loop that C lacks.
- Both require **declare-before-use** typed variables ([[StaticallyTyped|statically typed]]).
- [[EscapeSequence|Escape sequences]] (`\n`, `\t`, etc.) are shared in format strings.

## The pedagogical payoff

> *"C's simpler abstractions grant programmers direct memory access control, enabling greater optimization and efficiency management."* — Appendix 1 summary

The same thesis as [[dis-1-7-summary|Ch 1.7's]] Python-vs-C close: trading Java's rich object machinery for C's mechanical transparency is what makes the rest of [[DiveIntoSystems]] (memory model, assembly, hardware) directly inspectable.

## Connections

- [[DiveIntoSystems]] — the textbook; Appendix 1 is the Java-cross-walk variant of Ch 1.
- [[Java]] — the source language for this cross-walk.
- [[CLanguage]] — the target language.
- [[dis-1-1-getting-started]] through [[dis-1-8-exercises]] — the **Python**-vs-C sibling chapters that share the same systems content.
- [[dis-app1-1-getting-started]] through [[dis-app1-8-exercises]] — the **Java**-vs-C ingested pages this concept summarizes.
