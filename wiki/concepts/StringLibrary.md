---
title: "String Library (string.h)"
type: concept
tags: [c-language, strings, standard-library, header-file]
sources: [dis-1-5-arrays-strings, dis-2-6-strings]
last_updated: 2026-05-17
---

# String Library (`<string.h>`)

The **C string library** is the standard-library [[HeaderFile|header]] `<string.h>` that supplies the canonical [[CString|C string]] manipulation functions. It is the standard tooling for working with the [[CLanguage|C]] *convention* of [[CArray|`char` arrays]] terminated by [[NullTerminator|`'\0'`]].

## How to use

```c
#include <string.h>
```

`<string.h>` is part of the freestanding-friendly subset of the C standard library; it does **not** need `-lstring` or any extra linker flag — `libc` provides it.

## Functions [[dis-1-5-arrays-strings|Ch 1.5]] introduces

The chapter opens with a deliberately small slice — three functions — to keep the focus on the [[NullTerminator|null-terminator]] discipline and the [[BoundsChecking|no-bounds-checking]] rule. Safer variants and the larger library are deferred to Ch 2.6.

| Function | Purpose | Safety note |
|---|---|---|
| [[Strlen\|`strlen(s)`]] | Returns the number of characters in `s`, **excluding** the null terminator. | Reads forward from `s` until it finds `'\0'` — if the string isn't properly terminated, this reads past the end of the buffer. |
| [[Strcpy\|`strcpy(dst, src)`]] | Copies `src` (including its `'\0'`) into `dst`. | **Unsafe.** Per [[dis-1-5-arrays-strings\|Ch 1.5]]: *"poses a security risk because it assumes that its destination is large enough."* Source of countless [[BufferOverflow\|buffer overflows]]. Safer alternative `strncpy` deferred to Ch 2.6. |
| [[Sprintf\|`sprintf(dst, fmt, …)`]] | Formatted construction of a [[CString\|C string]] — the [[Printf\|`printf`]] family member that writes into a buffer instead of [[StandardOutput\|stdout]]. | Same unbounded-write hazard as [[Strcpy\|`strcpy`]]; `snprintf` is the safer variant introduced later. |

## Full surface area — Ch 2.6 deepening

[[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]] opens up the rest of `<string.h>`. The function families:

| Family | Functions | Notes |
|---|---|---|
| **Length** | [[Strlen\|`strlen`]] | O(n) scan to the `'\0'`. |
| **Copy (unbounded)** | [[Strcpy\|`strcpy`]] | Unsafe — see [[BufferOverflow]]. |
| **Copy (bounded)** | [[Strncpy\|`strncpy`]], [[Strlcpy\|`strlcpy`]] | [[Strncpy\|`strncpy`]] *may not terminate*; [[Strlcpy\|`strlcpy`]] always terminates (glibc 2.38+). |
| **Concatenation** | [[Strcat\|`strcat`]], [[Strncat\|`strncat`]] | Same destination-size discipline as copy. |
| **Comparison** | [[Strcmp\|`strcmp`]], [[Strncmp\|`strncmp`]] | Tri-valued return (`<0`, `0`, `>0`); the answer to *why `==` doesn't work*. |
| **Search** | [[Strchr\|`strchr`]], [[Strstr\|`strstr`]] | Return aliasing pointers into the input, or [[NullPointer\|`NULL`]] if not found. |
| **Tokenization** | [[Strtok\|`strtok`]], `strtok_r` | Destructive, internal `static` state; `strtok_r` is the reentrant variant. |
| **Formatted construction** | [[Sprintf\|`sprintf`]], `snprintf` | In `<stdio.h>`, not `<string.h>`, but conceptually a string-builder. |

The chapter's load-bearing safety rule restated: *"failure to allocate enough memory will yield undefined results that range from program crashes to major security vulnerabilities."* And for documentation beyond what the chapter covers, [[dis-2-6-strings|Ch 2.6]] routes the reader to [[ManPages|`man`]].

## Adjacent libraries

[[dis-2-6-strings|Ch 2.6]] also introduces the *per-character* counterpart [[CtypeLibrary|`<ctype.h>`]] (predicates `isalpha` / `isdigit` / `isspace` / ... + case-conversion `tolower` / `toupper`) and the *string-to-number* family from `<stdlib.h>` ([[Atoi|`atoi`]], `atof`).

## Why the standard library looks the way it does

[[StringLibrary|`<string.h>`]] is one of the oldest pieces of the C standard library; many of its functions were designed in the 1970s for systems where every byte of code mattered. The result is a library that is *fast* and *minimal*, but whose safety contract is *entirely* the caller's responsibility. The unsafe functions ([[Strcpy|`strcpy`]], `strcat`, [[Sprintf|`sprintf`]], `gets` — long since removed) are formally part of the language standard but are now considered legacy; modern style uses their bounded counterparts.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 opens the library with [[Strlen|`strlen`]], [[Strcpy|`strcpy`]], [[Sprintf|`sprintf`]] and previews the safety discussion for Ch 2.6.
- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 expands the library with [[Strncpy|`strncpy`]] / [[Strlcpy|`strlcpy`]] / [[Strcmp|`strcmp`]] / [[Strncmp|`strncmp`]] / [[Strcat|`strcat`]] / [[Strncat|`strncat`]] / [[Strchr|`strchr`]] / [[Strstr|`strstr`]] / [[Strtok|`strtok`]] and the supporting [[CtypeLibrary|`<ctype.h>`]] / [[Atoi|`atoi`]] / [[ManPages|`man`]].
