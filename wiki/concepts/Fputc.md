---
title: "fputc / putc (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fputc / putc

**`fputc(c, fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that writes **one character** to a [[FilePointer|`FILE *`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4 the per-byte file-I/O writer paired with [[Fgetc|`fgetc`]]; [[Putchar|`putchar`]] is the [[StandardOutput|`stdout`]]-specialized sibling.

```c
int ch = fgetc(infile);
if (ch != EOF) {
    fputc(ch, outfile);   // copy one byte
}
```

`putc` is a macro form of `fputc` with otherwise-identical semantics — Ch 2.8's worked copy loop uses `putc`.

## Defining properties

- **Returns [[CPrimitiveType|`int`]]** — the character written on success, [[EOF|`EOF`]] on error. The return matches [[Fgetc|`fgetc`]]'s convention.
- **Takes the character as [[CPrimitiveType|`int`]]** — same reason: must accept any byte value plus the [[EOF|`EOF`]] sentinel.
- **Advances the [[FilePointer|`FILE *`]] position** by one.
- **Buffered.** Goes to the C-library buffer; [[Fclose|`fclose`]] / `fflush` / line-end-on-line-buffered-stream actually pushes to the OS.

## Connections

- [[Fgetc]] — the per-byte reader sibling.
- [[Putchar]] — the [[StandardOutput|`stdout`]]-specialized form.
- [[Getchar]] — the corresponding [[StandardInput|`stdin`]] reader.
- [[FilePointer]] — the destination type.
- [[EOF]] — the error-return sentinel.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
