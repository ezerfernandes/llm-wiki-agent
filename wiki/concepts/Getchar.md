---
title: "getchar (C)"
type: concept
tags: [c-language, stdlib, io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# getchar

**`getchar()`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that reads **one character** from [[StandardInput|`stdin`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.1, it is exactly `fgetc(stdin)`.

```c
int ch;
while ((ch = getchar()) != EOF) {
    putchar(ch);
}
```

## Defining properties

- **Returns [[CPrimitiveType|`int`]], not `char`** — to fit the [[EOF|`EOF`]] sentinel alongside all 256 byte values.
- **No arguments**: source is implicitly [[StandardInput|`stdin`]].
- **Equivalent to [[Fgetc|`fgetc(stdin)`]]** — Ch 2.8's framing of the standard ↔ file symmetry.
- **Useful for robust per-character input**, including filtering or building character-by-character state machines that [[Scanf|`scanf`]]'s format-string approach is too coarse for.

## Connections

- [[Putchar]] — the writer sibling.
- [[Fgetc]] — the general file form (`getchar()` = `fgetc(stdin)`).
- [[StandardInput]] — the implicit source.
- [[EOF]] — the sentinel return.
- [[Scanf]] — the formatted alternative.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
