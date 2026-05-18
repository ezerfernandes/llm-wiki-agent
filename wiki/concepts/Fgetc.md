---
title: "fgetc / getc (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fgetc / getc

**`fgetc(fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that reads the **next single character** from a [[FilePointer|`FILE *`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4 the per-byte file-I/O primitive; the [[Getchar|`getchar`]] sibling reads from [[StandardInput|`stdin`]] specifically.

```c
int ch;
ch = fgetc(infile);
if (ch != EOF) {
    fputc(ch, outfile);
}
```

`getc` is a macro form of `fgetc` with otherwise-identical semantics — Ch 2.8's worked copy loop uses `getc` / [[Fputc|`putc`]].

## Defining properties

- **Returns [[CPrimitiveType|`int`]], not `char`.** This is the load-bearing detail. The return is either a value in `0..255` (the byte read, zero-extended) or the special sentinel [[EOF|`EOF`]] (typically `-1`) on end-of-file or error. Storing the result in `char ch` *before* the [[EOF|`EOF`]] test is a corpus-wide bug — `EOF` truncates to a valid byte.
- **Advances the position** of the [[FilePointer|`FILE *`]] by one byte (success) or zero (EOF).
- **Buffered.** Reads through the C-library buffer, not one syscall per byte.
- **`ungetc(c, fp)`** complements it: pushes one byte back onto the stream so the *next* `fgetc` returns it.

## Standard ↔ file symmetry

| Source | Per-byte read | Per-byte write |
|---|---|---|
| File | `fgetc(fp)` / `getc(fp)` | [[Fputc|`fputc(c, fp)` / `putc(c, fp)`]] |
| Standard streams | [[Getchar|`getchar()`]] = `fgetc(stdin)` | [[Putchar|`putchar(c)`]] = `fputc(c, stdout)` |

## Connections

- [[Fputc]] — the per-byte writer sibling.
- [[Getchar]] / [[Putchar]] — the standard-stream specializations.
- [[FilePointer]] — the argument type.
- [[EOF]] — the sentinel return value.
- [[Ungetc]] — pushes a byte back.
- [[Feof]] — predicate variant.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
