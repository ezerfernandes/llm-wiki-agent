---
title: "ungetc (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# ungetc

**`ungetc(c, fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that **pushes one character back** onto a [[FilePointer|`FILE *`]] so the *next* read returns it. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4.

```c
int ch = fgetc(fp);
if (ch != '<') {
    ungetc(ch, fp);   /* not a tag — leave the char for the next reader */
}
```

## Defining properties

- **At least one byte of pushback guaranteed** by the standard. Most implementations support more, but portable code assumes exactly one.
- **Useful for one-token lookahead** in hand-rolled parsers: the chapter introduces it as the inverse of [[Fgetc|`fgetc`]].
- **Affects the [[FilePointer|`FILE *`]] state only** — does not modify the underlying file on disk.
- **Returns the pushed byte on success, [[EOF|`EOF`]] on error.**

## Connections

- [[Fgetc]] — the read whose effect this undoes.
- [[FilePointer]] — the stream the pushback acts on.
- [[EOF]] — error-return sentinel.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
