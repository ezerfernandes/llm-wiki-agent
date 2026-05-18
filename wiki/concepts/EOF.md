---
title: "EOF (End-of-File Sentinel, C)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# EOF

**`EOF`** is the [[CLanguage|C]] standard-library macro — defined in [[StandardIOLibrary|`<stdio.h>`]], typically as `-1` — used as the **end-of-file sentinel** by every character-reading I/O function. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.2 / §2.8.4.

```c
int ch;
while ((ch = fgetc(infile)) != EOF) {
    fputc(ch, outfile);
}
```

## Why character-I/O functions return `int`, not `char`

This is the load-bearing detail: [[Fgetc|`fgetc`]] / [[Getchar|`getchar`]] return [[CPrimitiveType|`int`]] so they can encode any of **257 distinct values** — the 256 possible byte values (`0..255`) **plus** the additional `EOF` sentinel. A `char` only has 256 values, so any choice of `EOF` would alias a real byte.

**Bug pattern:**
```c
char ch;                          /* WRONG — should be int */
while ((ch = fgetc(fp)) != EOF) { /* fails on signed-char systems for byte 0xFF;
                                     fails on unsigned-char systems always */
    ...
}
```

The fix is `int ch;` — the chapter's worked example does this correctly.

## Where `EOF` shows up

| Function | Returns `EOF` on |
|---|---|
| [[Fgetc|`fgetc`]] / [[Getchar|`getchar`]] | end-of-file or read error |
| [[Fputc|`fputc`]] / [[Putchar|`putchar`]] | write error |
| [[Fclose|`fclose`]] | close error |
| [[Fputs|`fputs`]] | write error |
| [[Fscanf|`fscanf`]] / [[Scanf|`scanf`]] | read error before any conversion |

## EOF vs. [[Feof|`feof`]]

`EOF` is a **return value** — checked at the call site of each I/O function. [[Feof|`feof(fp)`]] is a **predicate** — checked *after* an I/O call returned a failure value, to disambiguate end-of-file from a hard read error.

## Connections

- [[Fgetc]] / [[Fputc]] / [[Getchar]] / [[Putchar]] — character-I/O functions that return / detect this sentinel.
- [[Feof]] — the predicate variant.
- [[CPrimitiveType]] — `int` is the return type chosen specifically to fit `EOF` alongside all 256 bytes.
- [[StandardIOLibrary]] — defines the macro.
- [[FilePointer]] — what most EOF-returning functions consume.
- [[NullPointer]] — the analogous *failure-sentinel* in pointer-returning functions like [[Fgets|`fgets`]] and [[Fopen|`fopen`]].
- [[dis-2-8-io]] — introducing source.
