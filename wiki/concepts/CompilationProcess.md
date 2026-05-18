---
title: "Compilation Process"
type: concept
tags: [compiler, toolchain, c-language, build]
sources: [dis-1-1-getting-started, dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Compilation Process

The **compilation process** is the source-to-binary pipeline a [[CCompiler|C compiler]] like [[GCC]] runs to turn a `.c` file into a runnable [[BinaryExecutable|binary]]. In [[dis-1-1-getting-started|DIS Ch 1.1]] this is introduced as the single most important difference between [[CLanguage|C]] and [[Python]]: C cannot just be run — it must first be compiled. [[dis-2-9-5-libraries|DIS Ch 2.9.5]] **refines** the four-stage view by splitting **link** into a build-time and a launch-time half — yielding the **canonical five-stage pipeline** used throughout the rest of the corpus.

## Stages (canonical five — per [[dis-2-9-5-libraries|Ch 2.9.5]])

1. **[[PreprocessingStage|Preprocess]]** — handle [[PreprocessorDirective|`#include`]], `#define`, conditional compilation. Produces an expanded translation unit. `gcc -E` stops here.
2. **[[CompilationStage|Compile]]** — translate the preprocessed C into [[AssemblyLanguage|assembly]] for the target architecture. `gcc -S` stops here, emits `.s`.
3. **[[AssemblyStage|Assemble]]** — translate `.s` into machine-code [[ObjectFile|`.o` object file]] with **unresolved external symbol references**. `gcc -c` stops here.
4. **[[LinkingStage|Link-edit]]** — [[Linker|`ld`]] resolves external symbols across `.o` files and [[CLibrary|libraries]] (e.g., `-lm` to link `libm`). [[StaticLinking|Static]] symbols are inlined; [[DynamicLinking|dynamic]] symbols are recorded as runtime-resolved references.
5. **[[RuntimeLinking|Runtime link]]** — at process launch, the [[DynamicLinker|dynamic linker]] (`ld.so` / `ld-linux.so`) loads required [[DynamicLibrary|`.so`]] files into the process [[AddressSpace|address space]] and binds the dynamic references. [[LDLibraryPath|`LD_LIBRARY_PATH`]] augments the search path here.

[[GCC|`gcc`]] runs stages 1–4 by default; intermediate stages can be exposed with `-E` / `-S` / `-c`. Stage 5 happens **outside** the build, every time the program is launched.

## Four-stage view ([[dis-1-1-getting-started|Ch 1.1]]) vs five-stage view ([[dis-2-9-5-libraries|Ch 2.9.5]])

The Ch 1.1 four-stage list (preprocess → compile → assemble → link) is **correct for [[StaticLinking|statically linked]] programs** where stage 5 is a no-op. Ch 2.9.5 makes the runtime-link step explicit because [[DynamicLinking|dynamic linking]] is the default and the deployment-time errors (*"cannot open shared object file"*) are otherwise unaccounted for.

## Error taxonomy ([[CompilerVsLinker|stage-stage mapping]])

| Stage | Tool | Signature error |
|---|---|---|
| 1 [[PreprocessingStage|preprocess]] | preprocessor | *"No such file or directory"* (header on disk) |
| 2 [[CompilationStage|compile]] | [[CCompiler|compiler]] | *"implicit declaration"*, type errors |
| 4 [[LinkingStage|link-edit]] | [[Linker|`ld`]] | [[UndefinedReferenceError|*"undefined reference"*]] |
| 5 [[RuntimeLinking|runtime link]] | [[DynamicLinker|`ld.so`]] | *"cannot open shared object file"* |

## What this lets the programmer assume

Because compilation happens **before** execution, the C runtime is small: there is no interpreter in the loop and no per-statement type lookup. This is what makes [[CLanguage|C]] the natural language for the rest of [[DiveIntoSystems]] (assembly, architecture, OS, [[MemoryHierarchy|caches]], parallelism) — there is essentially nothing between the source and the metal except the compiler's output.

## Connections

- [[CLanguage]] / [[CCompiler]] / [[GCC]] — the actors.
- [[PreprocessorDirective]] / [[HeaderFile]] — what runs in stage 1.
- [[BinaryExecutable]] — the stage-4 output.
- [[DiveIntoSystems]] / [[dis-1-1-getting-started]] — Ch 1.1 four-stage introduction.
- [[dis-2-9-5-libraries]] — Ch 2.9.5 five-stage refinement.
- [[PreprocessingStage]] / [[CompilationStage]] / [[AssemblyStage]] / [[LinkingStage]] / [[RuntimeLinking]] — the five stages.
- [[Linker]] / [[DynamicLinker]] — the two link agents.
- [[CLibrary]] / [[StaticLibrary]] / [[DynamicLibrary]] — what stage 4 / 5 consume.
- [[StaticLinking]] / [[DynamicLinking]] — the two link modes.
- [[ObjectFile]] — the stage-3 output.
- [[UndefinedReferenceError]] — signature stage-4 error.
- [[CompilerVsLinker]] — error-stage taxonomy.
- [[Python]] — the interpreted contrast that needs no separate compile step.
