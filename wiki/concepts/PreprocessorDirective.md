---
title: "Preprocessor Directive"
type: concept
tags: [c-language, preprocessor, build]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Preprocessor Directive

A **preprocessor directive** is a line beginning with `#` that the C preprocessor — the first stage of the [[CompilationProcess]] — interprets *before* the actual C compile. The two introduced in [[dis-1-1-getting-started|DIS Ch 1.1]] are:

- **`#include <stdio.h>`** — splice the contents of a [[HeaderFile|header file]] into the current translation unit. Used to pull in standard-library declarations (`stdio.h` for [[Printf|`printf`]], `math.h` for `sqrt`/`sin`/…, etc.). C's analog of Python's `import`.
- *(Later in the book)* **`#define`**, **`#ifdef`** / **`#ifndef`** / **`#endif`**, **`#pragma`**.

`#include` lines must appear **at the top of the file, outside any function body** ([[dis-1-1-getting-started|Ch 1.1]]).

## Why this is its own step

The preprocessor is a textual pass — it does **not** understand C syntax. It runs first because the compile stage that follows needs all the declarations (function signatures, type defs, macros) already in scope. This separation is what lets the same C source compile against different headers on different platforms without changing the source.

## Connections

- [[CompilationProcess]] — its host stage (preprocess).
- [[HeaderFile]] — what `#include` consumes.
- [[CLanguage]] — the language it serves.
- [[dis-1-1-getting-started]] — introducing source.
- [[Python]] — the `import`-statement contrast (no separate preprocessor; runs at module-load time).
- [[RustMacro]] — the closest Rust analog to `#define`-style macros, contrasted in [[rust-embedded-book-c-tips-index]].
