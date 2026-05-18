---
title: "Compilation Stage"
type: concept
tags: [c-language, compiler, toolchain, compilation-process]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Compilation Stage

The **compilation stage** is stage 2 of the five-stage [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies. It takes the preprocessed translation unit (output of the [[PreprocessingStage|preprocessor]]) and translates it to **target-architecture [[AssemblyLanguage|assembly]] code**, performing all language-level [[CCompiler|compilation]] work: type checking, name resolution, optimization, instruction selection, register allocation.

## Output

A `.s` [[AssemblyLanguage|assembly]] file — human-readable architecture-specific assembly. [[GCC|`gcc -S foo.c`]] stops after compilation and emits `foo.s`. Per [[dis-2-9-5-libraries|Ch 2.9.5]] this is the stage that **separates language-level errors from link-level errors** — anything wrong with C semantics surfaces here.

## Errors at this stage

- **Implicit declaration** — *"implicit declaration of function `pow`"* / *"`pow` undeclared"* — the [[HeaderFile|header]] declaring `pow` was not `#include`d. Distinct from a missing **library link** which surfaces one stage later at [[LinkingStage|link]] time as [[UndefinedReferenceError|*"undefined reference"*]].
- **Type errors** — argument count/type mismatches against the visible prototype.
- **Syntax errors** — unbalanced braces, missing semicolons, etc.

## Why this is its own stage

Separating language semantics (this stage) from machine-code packaging (the [[AssemblyStage|assemble]] stage) and from symbol resolution ([[LinkingStage|link]]) gives **error locality**: each diagnostic comes from the tool that owns its category. The compiler reports language errors, the linker reports symbol errors, the loader reports runtime errors.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CompilationProcess]] — the surrounding pipeline.
- [[CCompiler]] — the agent.
- [[AssemblyLanguage]] — the output language.
- [[GCC]] — `-S` flag.
- [[PreprocessingStage]] — the previous stage.
- [[AssemblyStage]] — the next stage.
- [[CompilerVsLinker]] — error-stage taxonomy distinguishing this stage from link.
