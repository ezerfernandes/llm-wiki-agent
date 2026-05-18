---
title: "Angle Include (#include <...>)"
type: concept
tags: [c-language, preprocessor, header-file, build]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# Angle Include (`#include <...>`)

The **angle-bracket form** of the [[PreprocessorDirective|`#include`]] directive — `#include <stdio.h>` — tells the [[CLanguage|C]] [[PreprocessorDirective|preprocessor]] to search **only** the system header paths, skipping the source file's directory. Per [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]], it is the form used for *"standard library files"* — headers the system or a package manager installs at well-known locations (`/usr/include`, `/usr/local/include`).

## Search path

[[GCC|GCC]] searches, in order:

1. Directories listed in `-I<dir>` flags.
2. System-include directories: `/usr/local/include`, the compiler's built-in include directory, `/usr/include`.

No current-directory search — this is the only contrast with the [[QuotedInclude|quoted form]].

## When to use

Per the DIS convention:

- `#include <stdio.h>` / `<stdlib.h>` / `<math.h>` — [[CStandardLibrary|C standard library]].
- `#include <pthread.h>` — [[PThreads]] (system-installed library).
- `#include <SDL2/SDL.h>` — system-installed third-party library.
- `#include "mylib.h"` — project-local, controlled by the author ([[QuotedInclude|quoted form]]).

## Implementation detail

The C standard doesn't actually require system headers to exist as files on disk — `<stdio.h>` may be a compiler intrinsic, or a wrapper around a hidden implementation header. The angle-bracket form signals to the compiler *"this is a library header; resolve it however you do that"*. In practice, every mainstream implementation resolves it as a file lookup, but the abstraction matters for environments like [[BareMetalProgramming|bare-metal]] toolchains that may stub out `<stdio.h>`.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[QuotedInclude]] — the sibling quoted form.
- [[PreprocessorDirective]] — `#include` lives here.
- [[HeaderFile]] — what is included.
- [[CStandardLibrary]] — the headers most often resolved via angle brackets.
- [[CompilationProcess]] — stage 1 (preprocess) executes the search.
- [[GCC]] — `-I<dir>` extends the search path.
- [[CLanguage]] — the language.
