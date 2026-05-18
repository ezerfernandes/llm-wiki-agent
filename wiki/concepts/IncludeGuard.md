---
title: "Include Guard"
type: concept
tags: [c-language, preprocessor, header-file, build]
sources: [dis-2-9-6-writing-libraries]
last_updated: 2026-05-17
---

# Include Guard

**Include guard** is the industry-standard name for the [[HeaderGuard|header-guard]] idiom — the `#ifndef`/`#define`/`#endif` wrapper that prevents a [[HeaderFile|`.h` file]] from being processed more than once in a single translation unit. The terms are interchangeable; *header guard* emphasizes *what is guarded* (the header), *include guard* emphasizes *what is prevented* (a repeat `#include`).

```c
#ifndef MYLIB_H
#define MYLIB_H

// ... header body ...

#endif
```

Introduced in [[dis-2-9-6-writing-libraries|DIS Ch 2.9.6]] as part of the author-side library recipe — every [[HeaderFile|`.h` file]] the library exports should carry one. See [[HeaderGuard]] for the full discussion of mechanism, conventions, and the [[Pragma|`#pragma once`]] alternative.

## Connections

- [[dis-2-9-6-writing-libraries]] — introducing source.
- [[HeaderGuard]] — synonym; full treatment lives there.
- [[HeaderFile]] — what is guarded.
- [[PreprocessorDirective]] — the directive family the guard uses.
- [[CompilationProcess]] — stage 1 (preprocess) interprets the guard.
