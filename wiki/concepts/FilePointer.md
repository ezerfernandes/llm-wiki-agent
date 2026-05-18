---
title: "FILE * (File Pointer, C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# FILE * (File Pointer)

A **`FILE *`** is the opaque [[Pointer|pointer]]-typed handle that the [[CLanguage|C]] standard library — [[StandardIOLibrary|`<stdio.h>`]] — exposes for **all** stream I/O. Both **open files** ([[Fopen|`fopen`]] return value) and the **three default streams** ([[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]] / [[StandardError|`stderr`]]) are `FILE *` values, so the same family of `f*` functions ([[Fgetc|`fgetc`]] / [[Fputc|`fputc`]] / [[Fgets|`fgets`]] / [[Fputs|`fputs`]] / [[Fprintf|`fprintf`]] / [[Fscanf|`fscanf`]]) works on both.

Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.3:

```c
FILE *infile;
FILE *outfile;
infile  = fopen("input.txt",  "r");
outfile = fopen("/tmp/out.txt", "w");
if (infile == NULL || outfile == NULL) { /* handle */ }
```

## Defining properties

- **Opaque.** The struct behind `FILE` is implementation-defined — programmers only ever hold a [[Pointer|pointer]] to it and pass it through the `f*` functions.
- **Carries position state.** A `FILE *` tracks the *current position* inside its stream, advanced by every read/write and queryable / settable via [[Fseek|`fseek`]] / [[Rewind|`rewind`]] / `ftell`.
- **Carries buffering state.** The C library buffers reads and writes through the `FILE *`; flushes happen on [[Fclose|`fclose`]], on newline (for line-buffered terminal `stdout`), or on explicit `fflush(fp)`.
- **Carries error / EOF flags.** Set by failed I/O and tested via [[Feof|`feof`]] and `ferror`.
- **Unifies files and standard streams.** [[StandardInput|`stdin`]] / [[StandardOutput|`stdout`]] / [[StandardError|`stderr`]] are pre-opened `FILE *` values, which is why `fprintf(stdout, "%d", x)` is exactly `printf("%d", x)`.

## Lifecycle (the four-step protocol)

1. **Declare**: `FILE *fp;`
2. **Open**: `fp = fopen(path, mode);` — check `fp != NULL`.
3. **Use**: any `f*` function.
4. **Close**: `fclose(fp);`

Forgetting step 4 leaks the handle and may lose buffered output that never gets flushed.

## Connections

- [[Fopen]] / [[Fclose]] — creates / destroys `FILE *` values for on-disk files.
- [[FileMode]] — the `"r"` / `"w"` / `"a"` string controlling what `fopen` returns a `FILE *` for.
- [[Fgetc]] / [[Fputc]] / [[Fgets]] / [[Fputs]] / [[Fprintf]] / [[Fscanf]] — the family of functions consuming a `FILE *`.
- [[Fseek]] / [[Rewind]] — position primitives.
- [[Feof]] — end-of-file predicate on a `FILE *`.
- [[StandardInput]] / [[StandardOutput]] / [[StandardError]] — the three pre-opened `FILE *` values.
- [[StandardIOLibrary]] — declares the `FILE` type and the `f*` functions.
- [[NullPointer]] — `fopen` returns it on failure.
- [[Pointer]] — `FILE *` is one.
- [[dis-2-8-io]] — introducing source.
