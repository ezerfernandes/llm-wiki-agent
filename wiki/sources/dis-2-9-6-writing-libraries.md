---
title: "Dive into Systems — Ch 2.9.6 Writing and Using Your Own C Libraries"
type: source
tags: [c-language, libraries, static-library, dynamic-library, header-file, header-guard, ar, gcc, fpic, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/advanced_writing_libraries.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **sixth subsection of [[dis-2-9-advanced|Ch 2.9]]** of *[[DiveIntoSystems]]* — the **author-side companion to [[dis-2-9-5-libraries|Ch 2.9.5]]**'s consumer-side library treatment. Where 2.9.5 told the user how to **link** against `lib<name>.{a,so}`, 2.9.6 walks the **author** through the three-step recipe: (1) **define the API** in a [[HeaderFile|`.h` file]] with a [[HeaderGuard|`#ifndef`/`#define`/`#endif` guard]] wrapping [[FunctionPrototype|function prototypes]], [[CConstant|`#define` constants]], type definitions, and `extern`-declared global variables; (2) **implement** in one or more [[CSourceFile|`.c` files]] that `#include "mylib.h"`, supply function bodies, define globals, and use [[StaticFunction|`static`]] for module-private helpers; (3) **compile to binary** as either a [[StaticLibrary|`.a` static archive]] via [[ArCommand|`ar -rcs libmylib.a mylib.o`]] or a [[DynamicLibrary|`.so` shared object]] via `gcc -fPIC -c mylib.c` + `gcc -shared -o libmylib.so mylib.o`. Codifies the [[PositionIndependentCode|`-fPIC`]] requirement for shared objects, the `extern` convention for [[GlobalVariable|globals]] exported through the header, the [[QuotedInclude|`#include "myheader.h"`]] vs `<stdio.h>` search-path distinction, and the multi-mode consumption taxonomy: `gcc -o myprog myprog.c mylib.o` (link the object directly), `gcc -o myprog myprog.c mylib.c` (compile-and-link in one step), or `gcc -o myprog myprog.c -L. -lmylib` (the standard `-l<name>` form). Closes with the structural observation that *"this approach applies equally to structuring and compiling larger C programs composed of multiple C source and header files"* — the `.h`/`.c` split is not library-specific; it is the **C modularization discipline** that scales from one-author programs to multi-author libraries.

## Key Claims

- **Building a library is a three-step recipe.** (1) Define the **interface** in a [[HeaderFile|`.h`]] file — [[FunctionPrototype|function prototypes]], type definitions ([[CStruct|`struct`]] / [[CEnum|`enum`]] / [[Typedef|`typedef`]]), [[CConstant|`#define`]] constants, and `extern`-declared [[GlobalVariable|global variables]] the library exports. (2) **Implement** in one or more [[CSourceFile|`.c`]] files that `#include` the header and supply function bodies + global definitions; mark module-private helpers with [[StaticFunction|`static`]] to hide them from the linker. (3) **Compile to binary form** — either a [[StaticLibrary|`.a` archive]] (via [[ArCommand|`ar`]]) or a [[DynamicLibrary|`.so` shared object]] (via `gcc -shared -fPIC`). Users then `#include "mylib.h"` and link against the binary.

- **Header files need a guard to prevent multiple inclusion.** The canonical [[HeaderGuard|include-guard]] idiom — *also called an [[IncludeGuard|include guard]]* — wraps the entire header in `#ifndef _MYLIB_H_ / #define _MYLIB_H_ / ... / #endif`. The first `#include` defines the macro and exposes the contents; any subsequent `#include` of the same header in the same translation unit sees `_MYLIB_H_` already defined and the [[PreprocessorDirective|preprocessor]] elides the body. Without the guard, transitive includes (header A includes B, header C includes B, source includes A and C) yield duplicate type definitions and a compile error. The leading-underscore-uppercase-trailing-underscore convention (`_MYLIB_H_`) is a stylistic norm, not a language requirement.

- **`extern` distinguishes a declaration from a definition.** The chapter calls this *"particularly important to include … before any global variables that the library exports, as it distinguishes a name and type definition (in the `.h` file) from a variable declaration in the library's implementation."* The `.h` says *"this name and type exist somewhere"* (declaration); the `.c` says *"the storage and initial value live here"* (definition). Without `extern`, every translation unit that `#include`s the header would emit a duplicate definition and the [[Linker|linker]] would reject the multi-`.o` build with a *"multiple definition of `var`"* error.

- **Static archive: one `ar` invocation per release.** Build `.o` files first with `gcc -c mylib.c`, then bundle with [[ArCommand|`ar -rcs libmylib.a mylib.o`]]. The flags decompose as `r` (insert with replacement), `c` (create archive if absent, suppress warning), `s` (write an index — the same job [[Ranlib|`ranlib`]] used to do separately). `ar` is an *archiver* in the literal `tar`-like sense — it bundles `.o` files without modifying them; the [[Linker|linker]] later pulls out only the archive members that satisfy unresolved symbols.

- **Shared object: build with `-fPIC`, link with `-shared`.** [[PositionIndependentCode|`-fPIC`]] (*Position-Independent Code*) generates machine code that doesn't bake in absolute addresses — required because a [[DynamicLibrary|`.so`]] is mapped at a runtime-chosen [[AddressSpace|address]] that the [[DynamicLinker|dynamic linker]] picks per process. Two-step build: `gcc -fPIC -c mylib.c` produces a relocatable `mylib.o`, then `gcc -shared -o libmylib.so mylib.o` produces the shared object. Skipping `-fPIC` silently builds a `.so` that crashes when loaded at any address other than its link-time default — a footgun that scales with [[ASLR|ASLR]] adoption.

- **Three ways to consume your own library.** (a) **Direct object link** — `gcc -o myprog myprog.c mylib.o` — treats `mylib.o` as just another object file; works without any `.a`/`.so` archive but doesn't scale past a handful of files. (b) **Compile-and-link in one step** — `gcc -o myprog myprog.c mylib.c` — useful during library development when sources are at hand. (c) **Standard `-l<name>` form** — `gcc -o myprog myprog.c -L. -lmylib` — the production path; the [[Linker|linker]] searches the path supplied by `-L<dir>` for `libmylib.{so,a}` per the [[dis-2-9-5-libraries|Ch 2.9.5]] abstraction. `-L.` adds the current directory to the search path so a build-tree `.a`/`.so` is discoverable before installation.

- **Include-path syntax encodes search-order intent.** [[QuotedInclude|`#include "myheader.h"`]] (double quotes) tells the [[PreprocessorDirective|preprocessor]] to *"search the current directory first, then system paths"* — used for **project-local** headers the author controls. [[AngleInclude|`#include <stdio.h>`]] (angle brackets) restricts the search to *system paths only* — used for **library** headers installed system-wide. The `-I<dir>` flag extends the angle-bracket search list. Mismatching the syntax doesn't fail catastrophically but it muddies the build's invariants — a project-local `myheader.h` accidentally written `<myheader.h>` fails until a system-wide directory is reachable, masking the local-development path.

- **The `.h`/`.c` split scales beyond libraries.** The closing observation: *"this approach applies equally to structuring and compiling larger C programs composed of multiple C source and header files."* The library-author discipline (`.h` declares, `.c` defines, `static` hides, `extern` exports) is identical to the **C modularization discipline** for any multi-file program — the only difference is whether the binary is shipped as a [[StaticLibrary|`.a`]]/[[DynamicLibrary|`.so`]] or linked directly into a single executable. The 2.9.6 recipe is therefore the **canonical C-program organization pattern**, not a library-specific construct.

## Key Quotes

> "This approach applies equally to structuring and compiling larger C programs composed of multiple C source and header files." — the **scaling generalization** that elevates 2.9.6's library recipe to a general C-modularization discipline.

> "The `extern` keyword … is particularly important to include … before any global variables that the library exports, as it distinguishes a name and type definition (in the `.h` file) from a variable declaration in the library's implementation." — the **declaration-vs-definition** split that makes multi-`.o` builds linkable.

> `#ifndef _MYLIB_H_` / `#define _MYLIB_H_` / `#endif` — the canonical [[HeaderGuard|include-guard]] idiom.

## Three-Step Library Recipe (the chapter's headline pattern)

1. **API — write `mylib.h`** with the [[HeaderGuard|include-guard]] + [[FunctionPrototype|prototypes]] + types + `extern` globals.
2. **Implementation — write `mylib.c`** that `#include "mylib.h"` + supplies function bodies + global definitions + [[StaticFunction|`static`]] helpers.
3. **Binary — package** either:
   - **Static archive**: `gcc -c mylib.c` → `ar -rcs libmylib.a mylib.o`.
   - **Shared object**: `gcc -fPIC -c mylib.c` → `gcc -shared -o libmylib.so mylib.o`.

## Tools and Flags Introduced

| Tool/Flag | Role |
|---|---|
| [[ArCommand|`ar -rcs`]] | Bundle `.o` files into a `lib<name>.a` static archive. |
| `gcc -shared` | Produce a `.so` shared object (stage-4 link mode). |
| [[PositionIndependentCode|`-fPIC`]] | Emit position-independent code (required for `.so`). |
| `extern` (in `.h`) | Declare a global without defining storage. |
| [[StaticFunction|`static`]] (in `.c`) | Hide a function or global from the linker. |
| `#ifndef`/`#define`/`#endif` | The [[HeaderGuard|include-guard]] idiom. |
| `"myheader.h"` | Local header, current-dir-first search. |
| `<stdio.h>` | System header, system-path-only search. |

## Connections

- [[DiveIntoSystems]] — the source textbook; this section is its Ch 2.9.6.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — the authors.
- [[dis-2-9-advanced]] — the hub page that forwards to this subsection.
- [[dis-2-9-5-libraries]] — the **prior** subsection; consumer-side counterpart to this author-side treatment. 2.9.5 introduced `-l<name>` / `-L<path>` / [[LDLibraryPath|`LD_LIBRARY_PATH`]] for the user; 2.9.6 closes the loop on the **producer** side.
- [[HeaderFile]] — the API half; this chapter codifies its authoring discipline.
- [[CSourceFile]] — the `.c` implementation half; 2.9.5 named-and-deferred to here.
- [[CLibrary]] — the umbrella concept; 2.9.6 adds the author-side workflow.
- [[StaticLibrary]] / [[DynamicLibrary]] — the two binary packaging formats; 2.9.6 supplies the build commands.
- [[Linker]] — consumes the `.a`/`.o`/`.so` outputs at stage 4.
- [[HeaderGuard]] — the **new** concept page for the `#ifndef`/`#define`/`#endif` idiom.
- [[IncludeGuard]] — the **new** alias/concept page for the same idiom (industry-standard name).
- [[ArCommand]] — the **new** concept page for the `ar` archiver tool.
- [[PositionIndependentCode]] — the **new** concept page for `-fPIC` and runtime relocation.
- [[StaticFunction]] — the **new** concept page for `static` at file scope (module-private linkage).
- [[QuotedInclude]] / [[AngleInclude]] — the **new** pair of concept pages for the `"..."` vs `<...>` distinction.
- [[CompilationProcess]] — the five-stage pipeline 2.9.6's commands traverse.
- [[GCC]] — the toolchain driver (`-c`, `-shared`, `-fPIC`, `-L.`).
- [[PreprocessorDirective]] — `#ifndef` / `#define` / `#endif` / `#include` all live here.

## Contradictions

- **None.** Ch 2.9.6 *extends* [[dis-2-9-5-libraries|Ch 2.9.5]]'s consumer-side library treatment with the author-side workflow. The header/binary decomposition, the `-l<name>` abstraction, and the five-stage [[CompilationProcess|compile pipeline]] are reused unchanged. The chapter adds three new mechanisms (the [[HeaderGuard|include-guard]] idiom, the [[ArCommand|`ar`]] archiver, [[PositionIndependentCode|`-fPIC`]] for shared objects) that 2.9.5 did not need to introduce on the consumer side.
