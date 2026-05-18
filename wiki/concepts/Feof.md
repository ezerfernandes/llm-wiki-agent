---
title: "feof (C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# feof

**`feof(fp)`** is the [[CLanguage|C]] standard-library predicate — declared in [[StandardIOLibrary|`<stdio.h>`]] — that returns nonzero **after** a read on the [[FilePointer|`FILE *`]] has hit end-of-file. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.4.

## Subtle: `feof` is *not* a pre-read EOF test

The textbook footgun is:
```c
while (!feof(fp)) {            /* WRONG */
    int ch = fgetc(fp);
    fputc(ch, fp_out);          /* writes EOF (-1) when read fails */
}
```

`feof` only becomes true **after** an I/O call has failed by hitting EOF. So the loop above does one extra iteration. The idiomatic form tests the return of the read instead:

```c
int ch;
while ((ch = fgetc(fp)) != EOF) {
    fputc(ch, fp_out);
}
```

`feof` is used **after** a failed read, to disambiguate **end-of-file** (`feof(fp)` true) from a **hard read error** (`ferror(fp)` true).

## Connections

- [[EOF]] — the return-value sentinel that `feof` complements.
- [[Fgetc]] / [[Fgets]] / [[Fscanf]] — readers whose failure mode `feof` disambiguates.
- [[FilePointer]] — what `feof` queries.
- [[StandardIOLibrary]] — declares `feof` and its sibling `ferror`.
- [[dis-2-8-io]] — introducing source.
