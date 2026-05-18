---
title: "C Language"
type: concept
tags: [c-language, programming-language, systems, embedded]
sources: [dis-1-1-getting-started, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# C Language

**C** is a [[StaticallyTyped|statically typed]], compiled, general-purpose systems programming language. In [[DiveIntoSystems]] it is the lingua franca for talking about [[ComputerSystem|computer systems]]: every later chapter — [[BinaryRepresentation|binary representation]], assembly, computer architecture, [[OperatingSystem|OS]] internals, [[MemoryHierarchy|caching]], and multicore [[ParallelComputing|parallelism]] — is taught through C programs.

## Defining traits (per [[dis-1-1-getting-started|Ch 1.1]])

- **Compiled, not interpreted.** Source `.c` files are translated by a [[CCompiler|C compiler]] (canonically [[GCC]]) into a [[BinaryExecutable|binary executable]] before they can run — see [[CompilationProcess]].
- **Statically typed.** All [[VariableDeclaration|variables must be declared before use]], with explicit [[CPrimitiveType|primitive types]] (`int`, `char`, `float`, …).
- **Block-structured with curly braces `{ }`.** Indentation has no semantic meaning — only style.
- **Statements end with a `;`.**
- **Single program entry point: [[MainFunction|`int main(void)`]].**
- **Standard library pulled in via [[PreprocessorDirective|`#include`]]** of [[HeaderFile|header files]] (`<stdio.h>`, `<math.h>`, …).
- **Hosted I/O via the C standard library**: [[Printf|`printf`]] for formatted output (which, notably, does **not** auto-append `\n`).

## Contrasts

- **vs. [[Python]]** — C requires declarations, compilation, `{}` blocks, `;` terminators, and explicit newlines in output. Python infers types, runs interpreted, uses indentation, omits `;`, and `print` adds `\n` automatically. The [[dis-1-1-getting-started|Ch 1.1]] hello-world cross-walk is the wiki's canonical side-by-side.
- **vs. the embedded-Rust world** — both use C-style [[ExternC|`extern "C"`]] ABI for FFI, but the [[DiveIntoSystems]] track assumes a hosted [[OperatingSystem|OS]] with a standard `libc` and stdout, while [[TheEmbeddedRustBook]] explicitly opts out via [[NoStd]].

## In embedded contexts (per [[embedded-controllers-fiore]])

The same language reappears as the *embedded* lingua franca, with shifted priorities: no `printf`/`scanf` (no console), heavy use of [[BitwiseOperations|bitwise operators]] for register-poking, `volatile` mandatory on anything shared with [[InterruptServiceRoutine|ISRs]] or modified by hardware, `#define` macros pervasive (Arduino's `bitSet` / `bitClear` / `digitalWrite` are macros / inlines), and integer / [[FixedPointArithmetic|fixed-point]] math preferred over float because the [[AVR|AVR]] has no FPU. Build flow is host-compile then download via [[CrossCompiler|cross-compiler]] — `int` is dangerous because its width depends on the target (16 bits on AVR vs 32 bits on most desktop C), so embedded code reaches for `uint8_t` / `int16_t` from `stdint.h`.

## Connections

- [[DiveIntoSystems]] — the wiki's canonical C-language-through-systems textbook.
- [[dis-1-1-getting-started]] — first content section to introduce the language.
- [[CCompiler]] / [[GCC]] — the toolchain.
- [[CompilationProcess]] — source → binary pipeline.
- [[MainFunction]] / [[PreprocessorDirective]] / [[HeaderFile]] / [[Printf]] — minimum surface area for a runnable program.
- [[CPrimitiveType]] / [[VariableDeclaration]] / [[CArithmeticOperators]] — the data and operator layer.
- [[StaticallyTyped]] — the typing discipline.
- [[Python]] — the contrast language [[dis-1-1-getting-started|Ch 1.1]] uses to teach C.
