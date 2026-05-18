---
title: "Ctype Library (ctype.h)"
type: concept
tags: [c-language, strings, standard-library, header-file, character-classification]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# Ctype Library (`<ctype.h>`)

The **C character-classification library** is the standard-library [[HeaderFile|header]] `<ctype.h>` that supplies single-character **predicate** and **case-conversion** functions. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]] alongside the [[StringLibrary|`<string.h>`]] surface area as the *per-character* counterpart to the *whole-string* operations.

## How to use

```c
#include <ctype.h>
```

Like [[StringLibrary|`<string.h>`]], `<ctype.h>` is part of the freestanding-friendly subset of the C standard library — no extra linker flag.

## Predicate (classification) functions

All predicates take an `int` argument (the character value, or `EOF`) and return **nonzero for true, zero for false**. The chapter's convention restated: *returning nonzero* does not necessarily mean returning `1`.

| Function | True when the byte is ... |
|---|---|
| `islower(c)` | `'a'..'z'` |
| `isupper(c)` | `'A'..'Z'` |
| `isalpha(c)` | any letter `[A-Za-z]` |
| `isdigit(c)` | `'0'..'9'` |
| `isalnum(c)` | letter or digit |
| `ispunct(c)` | printable, not space, not alphanumeric |
| `isspace(c)` | whitespace (space, `\t`, `\n`, `\v`, `\f`, `\r`) |

Additional predicates the chapter doesn't enumerate but exist in `<ctype.h>`: `iscntrl`, `isprint`, `isgraph`, `isxdigit`.

## Conversion functions

| Function | Returns ... |
|---|---|
| `tolower(c)` | the lowercase version of `c` if uppercase; otherwise `c` unchanged |
| `toupper(c)` | the uppercase version of `c` if lowercase; otherwise `c` unchanged |

Both return the **ASCII value** of the (possibly converted) character as an `int`.

## Why `int`, not `char`?

The argument type `int` is historical: these functions were designed to accept the `int` return value of [[Getchar|`getchar`]] / [[Getc|`getc`]] / `fgetc` directly, which yields the character as an `int` widened from `unsigned char`, with `EOF` (typically `-1`) as a sentinel. Passing a raw signed `char` with the high bit set is technically undefined — cast to `unsigned char` first:

```c
char c = ...;
if (isalpha((unsigned char)c)) { ... }
```

## Locale dependence

By default (`"C"` locale) these functions implement plain ASCII rules. Under other locales (`setlocale(LC_CTYPE, "...")`), the classification may include locale-specific characters — `isalpha` may return true for accented Latin letters, etc.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `<ctype.h>` as the character-class library and enumerates the headline predicates + the two case-conversion functions.
