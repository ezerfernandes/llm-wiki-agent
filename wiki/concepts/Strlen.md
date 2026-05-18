---
title: "strlen"
type: concept
tags: [c-language, strings, standard-library]
sources: [dis-1-5-arrays-strings, dis-2-6-strings]
last_updated: 2026-05-17
---

# `strlen`

`strlen` is the [[StringLibrary|`<string.h>`]] function that returns the number of characters in a [[CString|C string]], **excluding** the [[NullTerminator|null terminator `'\0'`]].

## Signature

```c
#include <string.h>

size_t strlen(const char *s);
```

(`size_t` is an unsigned integer type; per [[SizeOf|`sizeof`]]'s return type. The chapter writes the result into an `int` for simplicity.)

## How it works

`strlen` walks the string from its base address **one byte at a time** until it finds a [[NullTerminator|`'\0'`]] byte, and returns the count of non-`'\0'` bytes seen. This is an **O(n)** operation in the string length — there is no length field to read.

```c
char s[] = "hello";    // 6 bytes in memory: 'h','e','l','l','o','\0'
strlen(s);             // returns 5  (the '\0' is NOT counted)
```

## What "excluding the null terminator" means in practice

Buffers that *store* a C string need capacity `strlen(s) + 1` to fit the trailing `'\0'`. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]]: *"failing to properly account for null characters is a common source of errors for novice C programmers."*

```c
char dst[strlen(src)];          // BUG: one byte too small for the '\0'
char dst[strlen(src) + 1];      // correct
```

## What goes wrong on a non-terminated buffer

If the input `char` array contains no `'\0'` byte at all, `strlen` reads past the end of the array, scanning forward through whatever memory follows, until it stumbles on a zero byte (or the operating system kills the process for accessing unmapped memory). The function has no way to know it has overrun anything — see [[BoundsChecking]].

```c
char buf[5] = {'h','e','l','l','o'};   // NO '\0' — not a valid C string
strlen(buf);                            // UNDEFINED BEHAVIOR — reads past buf
```

## Cross-walk

- [[Python]] `len(s)` — O(1) (length is stored on the `str` object).
- Java `s.length()` — O(1).
- [[CLanguage|C]] `strlen(s)` — O(n); the price of the [[CString|sentinel-terminated]] string representation.

## Canonical use in dynamic allocation (Ch 2.6)

Per [[dis-2-6-strings|Ch 2.6]], `strlen` is the canonical input to byte-counting [[Malloc|`malloc`]] calls when duplicating a string:

```c
size_t n = strlen(src);
char *dup = malloc(sizeof(char) * (n + 1));   // +1 for '\0'
```

The `+1` is the byte that distinguishes *string length* (what `strlen` returns) from *buffer capacity needed* (what `malloc` needs). Forgetting it is the prototypical [[dis-2-4-dynamic-memory|Ch 2.4]] / [[dis-2-6-strings|Ch 2.6]] string-allocation bug.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 introduces `strlen` alongside [[Strcpy|`strcpy`]] and [[Sprintf|`sprintf`]] as the first three [[StringLibrary|`<string.h>`]] functions.
- [[dis-2-6-strings]] — Ch 2.6 §2.6.2 uses `strlen` as the canonical input to [[Malloc|`malloc`]] byte-counting for dynamically allocated [[CString|C strings]].
