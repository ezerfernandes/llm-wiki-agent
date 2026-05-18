---
title: "Linking Stage (Link-Editing)"
type: concept
tags: [c-language, linker, toolchain, compilation-process, build]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Linking Stage (Link-Editing)

The **linking stage** (a.k.a. **link-editing**) is stage 4 of the five-stage [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies. The [[Linker|`ld`]] consumes one or more [[ObjectFile|`.o` object files]] plus any [[StaticLibrary|`.a`]] archives and [[DynamicLibrary|`.so`]] shared objects named on the command line (via `-l<name>`), **matches every undefined reference to a defined symbol**, and emits a final [[BinaryExecutable|executable]] (or a [[DynamicLibrary|`.so`]] if `-shared`).

## What "link-editing" means

The classical Unix term *link-editor* names this stage to distinguish it from **stage 5** ([[RuntimeLinking|runtime linking]]) — both are "linking" in the colloquial sense, but link-editing happens **once at build time** while runtime linking happens **every time the program launches**. Per [[dis-2-9-5-libraries|Ch 2.9.5]], dynamic-linking executables defer some of the work to stage 5; static-linking executables do everything here.

## What it does

1. Reads each input `.o` and `.a`.
2. Builds a global symbol table.
3. For each undefined reference in a `.o`, searches for a defining symbol in another `.o`, in any `.a` member, or in any `.so` (`-l<name>`). For `.so` matches, records a deferred dynamic reference rather than copying code.
4. Selectively pulls in only the `.a` archive members that satisfy a need.
5. Applies relocations — patches addresses now that final positions are known.
6. Writes the final ELF executable with a program header table describing memory layout.

## Errors at this stage

- **[[UndefinedReferenceError|Undefined reference]]** — *"undefined reference to `pow`"* from `ld`. The prototype was visible (so the [[CompilationStage|compiler]] was satisfied) but the **library binary** containing the implementation wasn't linked. Fix: add `-lm`. Per Ch 2.9.5 this is the **signature link-stage error** that distinguishes link failures from compile failures.
- **Duplicate definition** — two `.o` files both define the same global symbol; `ld` refuses to choose.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CompilationProcess]] — the surrounding pipeline.
- [[Linker]] — the agent (`ld`).
- [[ObjectFile]] — the input file format.
- [[StaticLibrary]] / [[DynamicLibrary]] — the two library formats consumed.
- [[StaticLinking]] / [[DynamicLinking]] — the two resolution modes.
- [[UndefinedReferenceError]] — the signature error.
- [[BinaryExecutable]] — the output product.
- [[RuntimeLinking]] — the deferred stage 5 for dynamic references.
- [[AssemblyStage]] — the previous stage.
- [[GCC]] — `-l<name>` and `-L<path>` flags drive this stage.
