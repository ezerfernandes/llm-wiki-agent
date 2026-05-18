---
title: "Header File"
type: concept
tags: [c-language, preprocessor, build]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Header File

A **header file** (conventionally `.h`) declares the functions, types, and macros that an implementation file (`.c`) can use after a [[PreprocessorDirective|`#include`]]. The C preprocessor literally splices the header's text into the translation unit at the `#include` site during stage 1 of the [[CompilationProcess]].

Introduced in [[dis-1-1-getting-started|DIS Ch 1.1]] through `<stdio.h>` — the standard-input/output header that declares [[Printf|`printf`]]. Other standard-library headers the book uses later:

- **`<stdio.h>`** — formatted I/O (`printf`, `scanf`, `fopen`, …).
- **`<math.h>`** — math (`sqrt`, `sin`, `pow`, …); requires linker flag `-lm`.
- **`<stdlib.h>`** — general utilities (`malloc`, `free`, `exit`, …).
- **`<string.h>`** — C-string handling (`strlen`, `strcpy`, …).

## Connections

- [[PreprocessorDirective]] — `#include` pulls headers in.
- [[CompilationProcess]] — stage 1 (preprocess) splices them.
- [[Printf]] — declared in `<stdio.h>`.
- [[GCC]] — `-lm` linker flag for `<math.h>`.
- [[CLanguage]] — the language they serve.
- [[dis-1-1-getting-started]] — introducing source.
