---
title: "Dive into Systems — Ch 1.1 Getting Started Programming in C"
type: source
tags: [book, dive-into-systems, c-language, programming]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/getting_started.html
---

## Summary

Section 1.1 of [[DiveIntoSystems]] (the first content section of Ch 1 *By the C, the Beautiful C*) introduces foundational [[CLanguage|C]] programming by cross-walking from [[Python]] — same "hello world" task, side-by-side syntax. It then covers the C [[CompilationProcess|compile-then-run]] model with [[GCC]], primitive [[CPrimitiveType|numeric types]] and their byte widths (`char`/`short`/`int`/`long`/`long long`/`float`/`double`), [[VariableDeclaration|declaration]] syntax with the *all variables must be declared before use* rule, and the basic [[CArithmeticOperators|arithmetic operators]] including the [[IntegerDivision|integer-vs-real division]] trap and [[IncrementOperator|pre/post-increment]] subtlety. The section sets up every later chapter's "active reading by typing the code" pedagogy from [[dis-0-introduction|Ch 0]] by giving the reader the minimum machinery to actually compile and run a C program.

## Key Claims

- **C is compiled, not interpreted.** A [[CCompiler|C compiler]] like [[GCC|`gcc`]] translates source code into a [[BinaryExecutable|binary executable]] that the [[ComputerHardware|hardware]] can directly execute — there is no Python-style REPL in the standard workflow.
- **Every C program needs a [[MainFunction|`main` function]].** The signature `int main(void) { ... }` declares it; the `int` return type carries an exit status (`0` = success); the `void` parameter list signals "no command-line arguments yet" (later extended to `int main(int argc, char **argv)`).
- **Libraries are pulled in by the [[PreprocessorDirective|`#include` directive]]**, not Python-style `import` — and `#include` lines must appear at the **top of the file, outside any function body**.
- **Code blocks use `{ }`, not indentation**, and **every statement ends with a `;`**. Indentation has *no* semantic meaning in C — only style.
- **`printf` does not auto-append a newline**, unlike Python's `print` — explicit `\n` is required.
- **All variables must be declared before use**, with syntax `type_name variable_name;`. C is a [[StaticallyTyped|statically typed]] language with no inference at this layer.
- **Numeric primitive widths matter and are platform-dependent for some types.** `char` = 1 byte, `short` = 2 bytes, `int` = 4 bytes, `long` = 4-or-8 bytes (platform-dependent), `long long` = 8 bytes, `float` = 4 bytes, `double` = 8 bytes. The `sizeof` operator returns the byte count of a type or expression.
- **Char and string literals are different types.** `'h'` is a single-byte `char` (numeric value 104, the ASCII code); `"h"` is a two-byte string literal (the byte `'h'` followed by a `'\0'` terminator).
- **[[IntegerDivision|Integer division truncates]].** `11 / 2` yields `5`; promote one operand to floating-point (`11 / 2.0`) to get `5.5`.
- **Pre- vs. post-[[IncrementOperator|increment]] differ in *when* the side effect lands relative to the value of the expression**: `++x` increments first, then reads; `x++` reads first, then increments. The book recommends *not* mixing them inside larger expressions — separate statements are clearer.
- **The math library needs explicit linking.** `#include <math.h>` is not enough — the compile command must add `-lm` to link against `libm`.

## Key Quotes

> "A C compiler is a program that translates C source code into a binary executable form that the computer hardware can directly execute." — defines the [[CompilationProcess|compile-then-run]] model that separates C from Python.

> "The main function returns the int value 0 to signify running to completion without error." — first formal statement of the [[ExitStatus|exit-status convention]] used throughout Unix-derived systems.

> "In C, each statement ends with a semicolon `;`." — the syntactic rule that makes indentation purely stylistic.

> "In C, all variables must be declared before they can be used." — the rule that distinguishes static-typed C from dynamic-typed Python.

## Worked example — minimum `hello.c`

```c
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

Compile and run:

```
$ gcc hello.c
$ ./a.out
$ gcc -o hello hello.c      # name the output binary
$ ./hello
$ gcc -Wall -g hello.c      # warnings + debug symbols
$ gcc hello.c -lm           # link math library
```

## Connections

- [[DiveIntoSystems]] — the book itself; this is its first content section in Ch 1.
- [[dis-0-introduction]] — Ch 0; this section delivers on Ch 0's "active-reading by typing the code" promise by giving the reader the minimum C-compile pipeline.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[CLanguage]] — the language being introduced.
- [[GCC]] — the canonical [[CCompiler|C compiler]] the book uses (`gcc hello.c`).
- [[CompilationProcess]] — the source→binary translation step that C requires and Python does not.
- [[BinaryExecutable]] — the output the compiler produces (`a.out` by default).
- [[MainFunction]] — the program entry point with `int main(void)`.
- [[PreprocessorDirective]] — `#include`, the library-pull-in mechanism.
- [[HeaderFile]] — `<stdio.h>` etc., what `#include` consumes.
- [[Printf]] — the formatted-output function; no auto-newline.
- [[VariableDeclaration]] — `type_name variable_name;`.
- [[CPrimitiveType]] — `char` / `short` / `int` / `long` / `long long` / `float` / `double` + their `unsigned` variants.
- [[SizeOf]] — operator returning the byte width of a type or expression.
- [[CArithmeticOperators]] — `+`, `-`, `*`, `/`, `%`, compound-assignment, `++`, `--`.
- [[IntegerDivision]] — the truncation-versus-promote-to-float trap.
- [[IncrementOperator]] — the pre/post `++` / `--` semantic distinction.
- [[ExitStatus]] — the integer `main` returns; `0` = success.
- [[StaticallyTyped]] — the typing discipline; contrasts with Python.

## Contradictions

- None with existing wiki content. The C-compile / OS-required worldview here is the natural continuation of [[dis-0-introduction]]'s "computer system = hardware + OS" definition and is **complementary** to the embedded-`no_std` Rust world covered in [[TheEmbeddedRustBook]] — both worlds use C-style ABI conventions ([[ExternC]]), but the [[DiveIntoSystems]] track assumes a hosted OS, a [[CompilationProcess|standard `libc`]], and `printf`-to-stdout, while the embedded-Rust track explicitly opts out via [[NoStd]] and uses [[ARMSemihosting|semihosting]] for I/O.
