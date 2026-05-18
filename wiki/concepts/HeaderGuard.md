---
title: "Header Guard"
type: concept
tags: [c-language, preprocessor, header-file, build]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# Header Guard

A **header guard** (also called an [[IncludeGuard|include guard]]) is the canonical [[CLanguage|C]] idiom that prevents a [[HeaderFile|`.h` file]] from being processed more than once in a single translation unit. The pattern wraps the entire header body in a [[PreprocessorDirective|preprocessor]] conditional keyed off a unique macro name:

```c
#ifndef _MYLIB_H_
#define _MYLIB_H_

// ... type definitions, prototypes, extern globals ...

#endif
```

Per [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]]: the first `#include` of the header sees `_MYLIB_H_` undefined, defines it, and exposes the body to the compiler. Any subsequent `#include` of the same header — whether direct or transitive through another header — sees the macro already defined and the [[PreprocessorDirective|preprocessor]] elides the entire body.

## Why it matters

Without a header guard, the **diamond include** pattern breaks compilation:

```
   A.h      C.h
    \      /
     \    /
      B.h
```

If `A.h` and `C.h` both `#include "B.h"`, and a translation unit `#include`s both `A.h` and `C.h`, then `B.h`'s contents are spliced **twice**. Any [[CStruct|`struct`]] / [[CEnum|`enum`]] / [[Typedef|`typedef`]] / [[CConstant|`#define`]] / [[FunctionPrototype|prototype]] in `B.h` becomes a duplicate definition — a compile error at stage 2 of the [[CompilationProcess|compile pipeline]].

## Macro-name conventions

The leading-and-trailing-underscore + uppercase form `_MYLIB_H_` is **stylistic**, not language-required. Common variants in the wild:

- `_MYLIB_H_` — DIS Ch 2.9.6's chosen form.
- `MYLIB_H` — POSIX-recommended (avoids the reserved leading-underscore namespace).
- `PROJECT_MODULE_H_INCLUDED` — verbose unique form for very large projects.

The C standard reserves identifiers beginning with an underscore followed by an uppercase letter (`_M`) for the implementation, so the DIS form is technically reserved-namespace; this is the dominant convention in practice and rarely collides.

## Alternative: `#pragma once`

A non-standard but widely-supported compiler extension that achieves the same effect with a single line at the top of the header:

```c
#pragma once
```

Supported by [[GCC|GCC]], Clang, MSVC. Faster than `#ifndef` (compiler can dedupe by file identity rather than re-tokenizing to find the matching `#endif`). Not in the [[CLanguage|C]] standard; DIS uses the portable `#ifndef` form.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[IncludeGuard]] — synonym; same concept, different name.
- [[HeaderFile]] — what the guard protects.
- [[PreprocessorDirective]] — `#ifndef` / `#define` / `#endif` are preprocessor directives.
- [[CompilationProcess]] — header inclusion happens at stage 1 (preprocess).
- [[CLanguage]] — the language.
