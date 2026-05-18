---
title: "rewind (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# rewind

**`rewind(fp)`** is the [[CLanguage|C]] standard-library function — declared in [[StandardIOLibrary|`<stdio.h>`]] — that **resets the position** of a [[FilePointer|`FILE *`]] to the start of the file. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.3 — the shortcut for `fseek(fp, 0, SEEK_SET)`.

```c
rewind(infile);   /* equivalent to fseek(infile, 0, SEEK_SET) plus clearerr */
```

## Defining properties

- **Returns `void`** — unlike [[Fseek|`fseek`]], no error indicator is reported.
- **Also clears the error and EOF flags** on the stream (an extra effect [[Fseek|`fseek`]] does not have).
- **Useful for two-pass scanning** of an input file (first pass to count, second pass to process).

## Connections

- [[Fseek]] — the general repositioning function.
- [[FilePointer]] — the stream being reset.
- [[Feof]] — the EOF flag `rewind` clears.
- [[StandardIOLibrary]] — declares the function.
- [[dis-2-8-io]] — introducing source.
