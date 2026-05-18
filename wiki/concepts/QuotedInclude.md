---
title: "Quoted Include (#include \"...\")"
type: concept
tags: [c-language, preprocessor, header-file, build]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# Quoted Include (`#include "..."`)

The **double-quote form** of the [[PreprocessorDirective|`#include`]] directive — `#include "myheader.h"` — tells the [[CLanguage|C]] [[PreprocessorDirective|preprocessor]] to search the **current directory first**, then fall through to the standard system header paths if not found. Per [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]]: *"use quotes for local headers and angle brackets for standard library files."*

The convention encodes **author intent**:

- `#include "mylib.h"` — *"this header lives next to my source; I control it."*
- [[AngleInclude|`#include <stdio.h>`]] — *"this header is part of a library; the system installs it."*

## Search order (typical, per [[GCC|GCC]])

1. The directory of the file containing the `#include` directive.
2. Directories listed in `-iquote <dir>` flags (rare).
3. Directories listed in `-I<dir>` flags.
4. System-include directories (`/usr/include`, `/usr/local/include`, the compiler's built-in include path).

Steps 3 and 4 are shared with the [[AngleInclude|angle-bracket]] form; the **only** difference is step 1 — angle-bracket includes skip the current-directory search.

## Implications for project structure

A typical multi-file project layout:

```
myproject/
├── main.c           // #include "mylib.h"
├── mylib.c          // #include "mylib.h"
└── mylib.h
```

`#include "mylib.h"` finds the header via step 1 (same directory as `main.c`). No `-I` flag needed.

For larger projects with a `src/` and `include/` split, the header may be at `include/mylib.h` while sources sit in `src/`. The build then passes `-Iinclude` so `#include "mylib.h"` (or even `#include <mylib.h>` once the path is established) resolves.

## Footgun: mismatched quote style

- A project-local header written as `#include <myheader.h>` *fails* on the standard system, then *succeeds* only when a system-wide install happens to put `myheader.h` under `/usr/include` — masking the project's local-development path.
- A standard-library header written as `#include "stdio.h"` *works* but signals confused authorship.

DIS Ch 2.9.6's discipline — quotes for local, angle brackets for system — is the universal convention; treat any deviation as a code smell.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[AngleInclude]] — the sibling angle-bracket form.
- [[PreprocessorDirective]] — `#include` lives here.
- [[HeaderFile]] — what is included.
- [[CompilationProcess]] — stage 1 (preprocess) executes the search.
- [[GCC]] — `-I<dir>` extends the search path.
- [[CLanguage]] — the language.
