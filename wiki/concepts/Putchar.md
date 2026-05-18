---
title: "putchar (C)"
type: concept
tags: [c-language, stdlib, io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# putchar

**`putchar(c)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that writes **one character** to [[StandardOutput|`stdout`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.1, it is exactly `fputc(c, stdout)`.

```c
putchar('A');     /* prints A */
putchar('\n');    /* prints newline */
```

## Defining properties

- **Takes [[CPrimitiveType|`int`]], not `char`** — same reason character-reading functions return `int`: must support any byte value plus the [[EOF|`EOF`]] error sentinel.
- **Returns [[CPrimitiveType|`int`]]**: the character written, or [[EOF|`EOF`]] on error.
- **Equivalent to [[Fputc|`fputc(c, stdout)`]]** — the standard ↔ file symmetry.
- **Bypasses [[Printf|`printf`]]'s format-string overhead** when no formatting is needed.

## Connections

- [[Getchar]] — the reader sibling.
- [[Fputc]] — the general file form (`putchar(c)` = `fputc(c, stdout)`).
- [[StandardOutput]] — the implicit destination.
- [[EOF]] — the error-return sentinel.
- [[Printf]] — the formatted alternative.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
