---
title: "strncpy"
type: concept
tags: [c-language, strings, standard-library, security, buffer-overflow]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strncpy`

`strncpy` is the [[StringLibrary|`<string.h>`]] **bounded** counterpart to [[Strcpy|`strcpy`]] — it copies at most `n` bytes from `src` into `dst`. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]] as the **safer-but-not-safe** alternative to the [[BufferOverflow|buffer-overflow]] hazard [[dis-1-5-arrays-strings|Ch 1.5]] flagged.

## Signature

```c
#include <string.h>

char *strncpy(char *dst, const char *src, size_t n);
```

## The non-termination footgun

The function's headline gotcha is its **null-termination behavior**: it does *not always* terminate the destination. Per [[dis-2-6-strings|Ch 2.6]]:

> *"When the length of the src string is greater than or equal to size, `strncpy` copies the first size characters from src to dst and does **not** add a null character to the end of the dst."*

Three cases:
- `strlen(src) < n` — copies `strlen(src) + 1` bytes (including the `'\0'`); remaining `dst` bytes pad-filled with `'\0'`.
- `strlen(src) == n` — copies `n` bytes, **no terminator**.
- `strlen(src) > n` — copies the first `n` bytes, **no terminator**.

The defensive idiom — *manually terminate after the call*:

```c
strncpy(dst, src, sizeof(dst));
dst[sizeof(dst) - 1] = '\0';   // force-terminate
```

Per the chapter: *"the programmer should explicitly add a null character to the end of dst after calling [[Strncpy|`strncpy`]]."*

## Why this is the *safer-but-not-safe* function

`strncpy` solves [[Strcpy|`strcpy`]]'s [[BufferOverflow|buffer-overflow]] problem — the size bound prevents writes past the end of `dst` — but introduces a *new* bug class: silently truncated and **non-terminated** strings. A subsequent [[Strlen|`strlen`]] / [[Strcmp|`strcmp`]] / [[Printf|`printf`]]-with-`%s` on the unterminated buffer reads off the end (see [[NullTerminator]]). Modern code increasingly prefers [[Strlcpy|`strlcpy`]] (always terminates, glibc 2.38+) or `snprintf(dst, n, "%s", src)`.

## When `strncpy` is the right tool

The function was originally designed for **fixed-width fields in legacy file formats** (e.g., UNIX `utmp` records) where the destination is a fixed-size byte slot that is *not* expected to be null-terminated — the null-padding behavior on short sources is a *feature* in that context. For general string copying, [[Strlcpy|`strlcpy`]] or `snprintf` are the correct choice.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strncpy` as the bounded `strcpy` and warns about the non-termination footgun.
