---
title: "fprintf (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fprintf

**`fprintf(fp, format, ...)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that writes a [[FormatSpecifier|format-string]]-driven interpolation to a [[FilePointer|`FILE *`]]. The file-I/O sibling of [[Printf|`printf`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4.

```c
fprintf(outfile, "%d:%c\n", x, c);
fprintf(stderr, "Error: return code %d\n", ret);
```

## Defining properties

- **First argument is a [[FilePointer|`FILE *`]].** Otherwise the format string and varargs are identical to [[Printf|`printf`]].
- **`printf(fmt, ...)` ≡ `fprintf(stdout, fmt, ...)`.** [[StandardOutput|`stdout`]] *is* a `FILE *`, so `printf` is just `fprintf` with the destination implied.
- **Returns the number of characters written** (negative on error).
- **All the [[FormatSpecifier|specifiers]] [[Printf|`printf`]] supports**: `%d` / `%u` / `%f` / `%g` / `%c` / `%s` / `%p` / `%ld` / `%lld` / `%x` / `%o` / `%e` plus width / precision / justification modifiers like `%5.3f`, `%20s`, `%-8d`.

## Canonical use: error reporting on `stderr`

```c
fprintf(stderr, "fopen failed: %s\n", strerror(errno));
```

This is **why** [[StandardError|`stderr`]] exists as a third stream — error output stays visible even when `stdout` is redirected to a file (`./prog > out.txt` doesn't swallow the error message).

## Connections

- [[Printf]] — the [[StandardOutput|`stdout`]]-specialized sibling.
- [[Fscanf]] — the reader counterpart.
- [[FilePointer]] — the destination type.
- [[StandardError]] — the canonical destination for error reporting via `fprintf`.
- [[FormatSpecifier]] — the format-string vocabulary.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
