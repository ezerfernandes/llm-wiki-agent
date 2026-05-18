---
title: "fclose (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# fclose

**`fclose(fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that **closes a [[FilePointer|`FILE *`]]**: flushes any buffered output, releases the OS file descriptor, and frees the library-side `FILE` struct. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.3 the canonical second half of the **four-step file-I/O protocol** ([[Fopen|open]] → [[FilePointer|declare]] → use → close).

```c
fclose(infile);
fclose(outfile);
```

## Defining properties

- **One argument**: a [[FilePointer|`FILE *`]] previously returned by [[Fopen|`fopen`]].
- **Return value**: `0` on success, `EOF` on error. Most call sites ignore it — the chapter's worked example does — but production code checks (a failed flush can mean **data loss**).
- **Flushes before releasing.** A `FILE *` writing to disk holds buffered bytes that get to the OS only on flush, [[Fclose|`fclose`]], or `fflush`. Skipping `fclose` after writes risks losing the tail of the file.
- **Pairs 1-to-1 with `fopen`.** Calling `fclose` twice on the same handle is undefined behavior; same family of footguns as [[DoubleFree|`free`-twice]].

## Connections

- [[Fopen]] — the constructor that pairs with this destructor.
- [[FilePointer]] — the type the function consumes.
- [[StandardIOLibrary]] — declares `fclose`.
- [[EOF]] — the error-return sentinel.
- [[DoubleFree]] — the analogous *call-twice* footgun in [[Malloc]] land.
- [[dis-2-8-io]] — introducing source.
