---
title: "fputs (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fputs

**`fputs(s, fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that writes a [[CString|C string]] to a [[FilePointer|`FILE *`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4 the string-level file-I/O writer paired with [[Fgets|`fgets`]].

```c
fputs("Hello, World!\n", outfile);
```

## Defining properties

- **Two arguments**: `const char *s` (a [[NullTerminator|null-terminated]] [[CString|C string]]) and [[FilePointer|`FILE *fp`]].
- **Does not append a newline** — like [[Printf|`printf`]], the caller controls the `\n`. Contrast Python `print` and the obsolete `puts(s)` which *does* auto-append.
- **Does not write the [[NullTerminator|`'\0'`]]** — only the string contents.
- **Returns non-negative on success, [[EOF|`EOF`]] on error.**

## Standard ↔ file symmetry

`fputs(s, stdout)` is the rough equivalent of `printf("%s", s)` for the no-formatting case — no format-string parsing overhead, and no [[FormatSpecifier|specifier]] vocabulary involved.

## Connections

- [[Fgets]] — the reader sibling.
- [[Printf]] — the formatted-output alternative.
- [[FilePointer]] — the destination type.
- [[CString]] — the input type.
- [[NullTerminator]] — must be present on the input; not written to output.
- [[EOF]] — the error-return sentinel.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
