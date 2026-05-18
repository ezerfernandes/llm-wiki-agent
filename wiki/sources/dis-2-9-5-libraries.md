---
title: "Dive into Systems — Ch 2.9.5 C Libraries: Using, Compiling and Linking"
type: source
tags: [c-language, libraries, static-library, dynamic-library, linker, compilation-process, gcc, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_libraries.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **fifth subsection of [[dis-2-9-advanced|Ch 2.9]]** of *[[DiveIntoSystems]]* — the **first corpus crossing from *C the language* to *C the build workflow***. Decomposes a [[CLibrary|C library]] into **two halves** — an **API** delivered as one or more [[HeaderFile|`.h`]] files (function prototypes, types, macros — what the [[PreprocessorDirective|`#include`]] consumes) and a precompiled **implementation** delivered as either a **[[StaticLibrary|static archive]] `lib<name>.a`** or a **[[DynamicLibrary|shared object]] `lib<name>.so`**. Refines [[dis-1-1-getting-started|Ch 1.1]]'s four-stage [[CompilationProcess|compile-then-run]] cartoon into a **five-stage pipeline**: [[PreprocessingStage|preprocess]] → [[CompilationStage|compile]] → [[AssemblyStage|assemble]] → [[LinkingStage|link-edit]] → [[RuntimeLinking|runtime link]] — exposed by [[GCC|`gcc`]] flags `-E` / `-S` / `-c` for stages 1/2/3 and **two linker flags `-l<name>` / `-L<path>`** for the search-and-bind protocol at stage 4. Codifies the **`-l`-name-vs-`lib`-filename abstraction** — `-lpthread` looks up `libpthread.so` *or* `libpthread.a`, freeing the source from filename literalism and letting [[Linker|`ld`]] *"choose to dynamically link when both a shared object (`.so`) and an archive (`.a`) version of a library are available."* Separates the **three diagnostic error modes** by their stage: missing [[HeaderFile|header]] surfaces as *"implicit declaration"* / *"undeclared"* at compile time, missing **library link** surfaces as *"undefined reference"* from the [[Linker|linker]] (`ld`), missing **header file on disk** surfaces as *"No such file or directory"* at preprocess time. Closes with the [[LDLibraryPath|`LD_LIBRARY_PATH`]] environment variable for [[RuntimeLinking|runtime shared-object resolution]] when [[DynamicLibrary|`.so`]] files live outside the default search path.

## Key Claims

- **A C library is a header-plus-binary pair.** *"A C library consists of two parts: an API (header files) and the implementation (precompiled binary code)."* The [[HeaderFile|`.h`]] file is **textual** ([[PreprocessorDirective|`#include`]]'d into every translation unit that uses the library); the implementation is **binary** — already compiled by the library author into a [[StaticLibrary|`.a`]] archive or a [[DynamicLibrary|`.so`]] shared object. The user neither sees nor needs the library's `.c` sources.

- **The compile flow has five stages, not four.** [[dis-1-1-getting-started|Ch 1.1]]'s preprocess → compile → assemble → link list is refined here by **splitting link** into two stages: **(4) link-editing** (the [[Linker|`ld`]] pass that resolves symbols across `.o` files and `.a` archives at build time) and **(5) runtime linking** (the [[DynamicLinker|dynamic linker]] `ld.so` / `ld-linux.so` step that resolves [[DynamicLibrary|`.so`]] symbols when the executable launches). The first four stages are exposed by [[GCC|`gcc`]] flags — `-E` stops after preprocess (emits expanded source), `-S` stops after compile (emits `.s` [[AssemblyLanguage|assembly]]), `-c` stops after assemble (emits `.o` [[ObjectFile|object file]]); no flag stops cleanly *between* link-edit and runtime — the build produces an executable that defers stage 5 to launch.

- **`-l<name>` is an abstraction over the literal filename `lib<name>.{so,a}`.** *"This level of abstraction enables programmers to be flexible about the desired linking type (e.g., static or shared) without having to specify a specific filename."* `gcc prog.c -lpthread` makes [[Linker|`ld`]] search for `libpthread.so` *and* `libpthread.a` in the standard library search path; the linker prefers the [[DynamicLibrary|shared object]] when both are present, falling through to the [[StaticLibrary|archive]] otherwise. The `--static` flag forces archive-only resolution.

- **`-L<path>` extends the library search path; `-I<path>` extends the header search path.** The standard system locations (`/usr/lib`, `/usr/local/lib` for libraries; `/usr/include`, `/usr/local/include` for headers) are searched automatically; non-standard locations require explicit `-L<dir>` (for `-l<name>` to find the `.so`/`.a`) or `-I<dir>` (for `#include "foo.h"` to find the header). Mirroring at the source-syntax level: `<stdio.h>` (angle brackets) means *search system paths only*; `"myheader.h"` (quotes) means *search the current directory first, then system paths*.

- **[[PThreads|pthreads]] is the [[GCC|gcc]] exception that proves the rule.** Per Ch 2.9.5: *"the [[PThreads|pthreads]] library has a special compilation flag, `-pthread`, which is used instead of `-lpthread`."* The `-pthread` form is preferred because it also defines `_REENTRANT` and adjusts other compilation defaults; `-lpthread` works but is incomplete. The chapter flags this as the **one canonical gotcha** in an otherwise uniform `-l<name>` interface.

- **Three diagnostic error classes, three different stages.** (a) **Compile-time** *"implicit declaration of function `pow`"* / *"undeclared identifier"* — the [[HeaderFile|header]] was not `#include`'d, the compiler hasn't seen the prototype; fix is adding `#include <math.h>`. (b) **Link-time** *"undefined reference to `pow`"* from `ld` — the prototype was visible but the **library binary** wasn't linked; fix is adding `-lm`. (c) **Preprocess-time** *"foo.h: No such file or directory"* — the header is referenced but not findable on disk; fix is `-I<dir>` or installing the library's `-dev` package. (d) **Runtime** *"cannot open shared object file"* — the [[DynamicLibrary|`.so`]] was found at link time but the [[DynamicLinker|dynamic linker]] can't find it at launch; fix is [[LDLibraryPath|`LD_LIBRARY_PATH`]] or installing the runtime package.

- **Static linking inlines the library; dynamic linking references it.** [[StaticLinking|Static linking]] (`--static`) copies every used symbol's machine code from the [[StaticLibrary|`.a`]] archive into the final executable — the binary is **self-contained** (no runtime dependency), at the cost of larger size and no per-host security patching. [[DynamicLinking|Dynamic linking]] (the default when a [[DynamicLibrary|`.so`]] is available) records only the symbol references in the executable and resolves them at launch from the runtime-loaded [[DynamicLibrary|shared object]] — smaller binaries, multiple processes share one in-memory copy of `libc.so`, and security patches to `libc.so` apply system-wide without rebuilding every consumer.

## Key Quotes

> "A C library consists of two parts: an API (header files) and the implementation (precompiled binary code)." — the **two-half decomposition** that grounds the chapter.

> "The compiler can choose to dynamically link when both a shared object (`.so`) and an archive (`.a`) version of a library are available." — the **default-preference rule** for the `-l<name>` abstraction.

> "This level of abstraction enables programmers to be flexible about the desired linking type (e.g., static or shared) without having to specify a specific filename." — why `-lpthread` not `libpthread.so`.

> "The pthreads library has a special compilation flag, `-pthread`, which is used instead of `-lpthread`." — the **one canonical gotcha** in the `-l<name>` family.

> "Missing the implementation (the library) gives an 'undefined reference' error from the linker `ld`. Missing the header gives an 'implicit declaration' warning or 'undeclared' error from the compiler." — the **two-stage diagnostic split**.

## GCC Flags Introduced in Ch 2.9.5

| Flag | Stage | Purpose |
|---|---|---|
| `-E` | 1 (preprocess) | Stop after preprocessing — emit expanded source to stdout. |
| `-S` | 2 (compile) | Stop after compilation — emit `.s` [[AssemblyLanguage|assembly]]. |
| `-c` | 3 (assemble) | Stop after assembly — emit `.o` [[ObjectFile|object file]]. |
| `-l<name>` | 4 (link) | Link `lib<name>.{so,a}` from the library search path. |
| `-L<path>` | 4 (link) | Add `<path>` to the library search path. |
| `-I<path>` | 1 (preprocess) | Add `<path>` to the header search path. |
| `--static` | 4 (link) | Force [[StaticLinking|static linking]] (archive only). |
| `-pthread` | 1+4 | Enable [[PThreads|pthreads]] (preferred over `-lpthread`). |

## Five-Stage Pipeline (the refinement of [[CompilationProcess|the Ch 1.1 four-stage view]])

1. **[[PreprocessingStage|Preprocess]]** — handle [[PreprocessorDirective|`#include`]] / `#define` / `#if`. Headers spliced in. `-E` stops here.
2. **[[CompilationStage|Compile]]** — translate preprocessed C into [[AssemblyLanguage|assembly]] for the target architecture. `-S` stops here.
3. **[[AssemblyStage|Assemble]]** — translate `.s` into binary machine code as a [[ObjectFile|`.o` object file]] with **unresolved external symbol references**. `-c` stops here.
4. **[[LinkingStage|Link-edit]]** — [[Linker|`ld`]] combines `.o` files with [[StaticLibrary|`.a`]] archives and [[DynamicLibrary|`.so`]] references into the final executable. **Static** symbols are inlined; **dynamic** symbols are recorded as runtime-resolved references.
5. **[[RuntimeLinking|Runtime link]]** — at process launch, the [[DynamicLinker|dynamic linker]] (`ld.so` / `ld-linux.so`) loads the required `.so` files into the process [[AddressSpace|address space]] and binds the dynamic references. [[LDLibraryPath|`LD_LIBRARY_PATH`]] augments the search path for this stage.

## Connections

- [[DiveIntoSystems]] — the source textbook; this section is its Ch 2.9.5.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the authors.
- [[dis-2-9-advanced]] — the hub page that forwards to this subsection.
- [[dis-2-9-4-pointer-arithmetic]] — the **prior** subsection (closes the [[dis-2-2-pointers|Ch 2.2]] deferral list).
- [[dis-1-1-getting-started]] — supplied the four-stage [[CompilationProcess|compile-then-run]] cartoon Ch 2.9.5 refines into five stages, and the `-lm` example Ch 2.9.5 generalizes.
- [[CompilationProcess]] — **updated in place** with the Ch 2.9.5 five-stage refinement (link split into link-edit + runtime link).
- [[GCC]] — **updated in place** with the new `-l<name>` / `-L<path>` / `-I<path>` / `--static` / `-pthread` / `-E` / `-S` / `-c` flags surfaced in this chapter.
- [[HeaderFile]] — the API half of a library, already named; Ch 2.9.5 codifies its role at the boundary.
- [[PreprocessorDirective]] — `#include` is what consumes the header at stage 1.
- [[CLibrary]] — the **new** umbrella page for *header + binary* library structure.
- [[StaticLibrary]] — the **new** concept page for `lib<name>.a` archives.
- [[DynamicLibrary]] — the **new** concept page for `lib<name>.so` shared objects.
- [[Linker]] — the **new** concept page for `ld` and its symbol-resolution role.
- [[StaticLinking]] / [[DynamicLinking]] — the **new** pair of concept pages contrasting the two link modes.
- [[ObjectFile]] — the **new** concept page for `.o` files (stage 3 output).
- [[LinkingStage]] / [[PreprocessingStage]] / [[CompilationStage]] / [[AssemblyStage]] / [[RuntimeLinking]] — the **new** per-stage pages making the five-stage pipeline grep-able.
- [[LDLibraryPath]] — the **new** concept page for the runtime shared-object search-path env var.
- [[UndefinedReferenceError]] — the **new** concept page for the load-bearing link-time error.
- [[DynamicLinker]] — the **new** concept page for `ld.so` / `ld-linux.so`.
- [[CompilerVsLinker]] — the **new** concept page distilling the two diagnostic-stage error classes.
- [[CSourceFile]] — the `.c` half of the library author's source split (named-and-deferred; full treatment in [[dis-2-9-6-writing-libraries|Ch 2.9.6]]).
- [[PThreads]] — the `-pthread`-not-`-lpthread` exception flagged here.
- [[LinkerScript]] — the [[BareMetalProgramming|bare-metal]] analog from [[TheEmbeddedRustBook]]; **different role** — `ld` consumes a linker script to place sections in target memory regions, whereas Ch 2.9.5's hosted-Linux link step uses the system default linker script implicitly.

## Contradictions

- **Refines, does not contradict.** Ch 2.9.5 explicitly extends [[dis-1-1-getting-started|Ch 1.1]]'s four-stage [[CompilationProcess|compile-then-run]] cartoon by **splitting link** into build-time link-edit and launch-time runtime link — both views are correct at their respective levels of abstraction; the four-stage version is correct for [[StaticLinking|statically linked]] programs where stage 5 is a no-op. The `-lm` example from Ch 1.1 is now revealed as one instance of the general `-l<name>` mechanism.
