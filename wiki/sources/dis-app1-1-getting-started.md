---
title: "Dive into Systems — Appendix 1.1 Getting Started Programming in C (for Java Programmers)"
type: source
tags: [book, dive-into-systems, c-language, java, programming, cross-walk]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix1/getting_started.html
---

## Summary

Appendix 1.1 of [[DiveIntoSystems]] is the **[[Java]]-programmer's retelling** of [[dis-1-1-getting-started|Ch 1.1]] — same C content, but cross-walked from Java instead of [[Python]]. It introduces the [[CLanguage|C]] [[CompilationProcess|compile-then-run]] model with [[GCC|`gcc`]] (vs. `javac` → [[JVM]]), the [[MainFunction|`int main(void)`]] entry point (vs. `public static void main(String[] args)` inside a class), [[PreprocessorDirective|`#include`]] (vs. `import`), [[Printf|`printf`]] (vs. `System.out.println` / `System.out.printf` — no auto-newline either way), [[CPrimitiveType|primitive types]] with explicit byte widths, [[CArithmeticOperators|arithmetic operators]] (essentially identical), and the [[IncrementOperator|`++` / `--`]] pre/post distinction (also identical). See [[JavaVsC]] for the consolidated cross-walk table.

## Key Claims (Java-vs-C deltas)

- **Compilation pipeline differs**: Java compiles to bytecode for the [[JVM]] (`javac HelloWorld.java` → `java HelloWorld`); C compiles to a [[BinaryExecutable|native binary]] (`gcc -o hello hello.c` → `./hello`). C has no virtual machine layer.
- **C is procedural, Java is object-oriented**: *"C is purely imperative and procedural"* — no classes, no methods, no `public static`. Every C file is a flat collection of [[Function|functions]].
- **`main` signature differs**: Java needs `public static void main(String[] args)` inside a class. C uses [[MainFunction|`int main(void)`]] at file scope — returns `int` (exit status), `void` parameter list means "no command-line arguments yet."
- **Library inclusion differs syntactically but conceptually maps**: Java's `import java.lang.Math;` ↔ C's [[PreprocessorDirective|`#include <math.h>`]]. C additionally requires explicit linking (`-lm` for libm).
- **Output differs but maps**: Java's `System.out.printf(...)` ↔ C's [[Printf|`printf(...)`]]. C's `printf` does **not** auto-append a newline — explicit `\n` required (Java's `println` does add one; Java's `printf` matches C's "no auto-newline" behavior).
- **Both require declare-before-use typed variables.** Same [[StaticallyTyped|static-typing]] discipline.
- **C exposes byte-widths**: `char` = 1, `short` = 2, `int` = 4, `long` = 4-or-8, `long long` = 8, `float` = 4, `double` = 8 bytes — [[SizeOf|`sizeof`]] reveals them. Java abstracts these (and standardizes `int` = 4 bytes).
- **Arithmetic and increment operators are essentially identical** — `+` `-` `*` `/` `%`, `+=` `-=`, [[IncrementOperator|`++x` / `x++`]] with the same pre/post semantics. C's [[IntegerDivision|integer-division truncation]] trap also exists in Java for `int`-typed operands.

## Key Quotes

> *"C is a imperative and procedural language and Java is an object oriented language."* — the headline structural difference.

> *"Code like the preceding example that uses an arithmetic expression with an increment operator is often hard to read."* — same readability advice as [[dis-1-1-getting-started|Ch 1.1]].

## Worked example — minimum `hello.c` vs `HelloWorld.java`

```c
#include <stdio.h>
int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Compile & run: `gcc -o hello hello.c && ./hello` vs `javac HelloWorld.java && java HelloWorld`.

## Connections

- [[DiveIntoSystems]] — Appendix 1 is the Java-programmer's variant of Ch 1.
- [[dis-1-1-getting-started]] — the Python-cross-walk sibling. Same C surface area.
- [[JavaVsC]] — consolidated comparison table that this section feeds.
- [[Java]] / [[JVM]] — the source language and its execution model.
- [[CLanguage]] / [[GCC]] / [[CompilationProcess]] / [[BinaryExecutable]] — the C side.
- [[MainFunction]] / [[PreprocessorDirective]] / [[Printf]] / [[CPrimitiveType]] / [[SizeOf]] / [[CArithmeticOperators]] / [[IncrementOperator]] / [[IntegerDivision]] / [[StaticallyTyped]] — Ch 1.1 concepts reused unchanged.

## Contradictions

- None. Pure retelling of [[dis-1-1-getting-started|Ch 1.1]] with a different starting-language analogy.
