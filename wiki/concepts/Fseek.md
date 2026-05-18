---
title: "fseek (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fseek

**`fseek(fp, offset, whence)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that **repositions** the current-position indicator of a [[FilePointer|`FILE *`]]. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.3.

```c
fseek(fp, 0, SEEK_SET);    /* go to start (same as rewind(fp)) */
fseek(fp, 3, SEEK_CUR);    /* skip 3 bytes forward */
fseek(fp, -3, SEEK_END);   /* 3 bytes before end */
```

## The three whence anchors

| Macro | Anchor |
|---|---|
| `SEEK_SET` | Beginning of file. Offset is absolute. |
| `SEEK_CUR` | Current position. Offset is relative (can be negative). |
| `SEEK_END` | End of file. Offset is usually 0 or negative. |

## Defining properties

- **Three arguments**: [[FilePointer|`FILE *`]], `long offset`, `int whence`.
- **Returns `0` on success, non-zero on error.**
- **Discards [[Ungetc|`ungetc`]] pushback.**
- **Works on binary files cleanly; text-mode offsets are implementation-defined** (Windows line-ending translation can make byte offsets ≠ character offsets).
- **Sibling `ftell(fp)`** returns the current position as a `long`, suitable for later `fseek(fp, pos, SEEK_SET)`.

## Connections

- [[Rewind]] — the *seek to start* shortcut (`rewind(fp)` ≈ `fseek(fp, 0, SEEK_SET)`).
- [[FilePointer]] — the stream being repositioned.
- [[Fgetc]] / [[Fputc]] / [[Fgets]] / [[Fputs]] — readers/writers whose position this changes.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
