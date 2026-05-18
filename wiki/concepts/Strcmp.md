---
title: "strcmp"
type: concept
tags: [c-language, strings, standard-library, comparison]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strcmp`

`strcmp` is the [[StringLibrary|`<string.h>`]] **string-comparison** function. Per [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]]: *"the `strcmp` function compares strings character by character based on their ASCII representation."* The function exists because the obvious-but-wrong `s1 == s2` on two `char *` compares **base addresses**, not contents.

## Signature

```c
#include <string.h>

int strcmp(const char *s1, const char *s2);
```

## Return value — tri-valued

Per [[dis-2-6-strings|Ch 2.6]]:

> *"returns 0 if s1 and s2 are the same strings / a value < 0 if s1 is less than s2 / a value > 0 if s1 is greater than s2"*

The exact magnitude of the nonzero return is **not specified** by the standard beyond *sign matches lexicographic order* — typically it is the byte difference of the first non-matching pair (`s1[i] - s2[i]`).

## The `==` footgun

```c
char *a = "hello";
char *b = "hello";
if (a == b)            /* comparing pointers, not contents */ ...
if (strcmp(a, b) == 0) /* comparing contents — what you almost always want */ ...
```

A surprisingly common beginner bug: `if (s1 == s2)` *appears* to work for string literals on some compilers (constant pooling can make literally-identical literals share an address) but fails as soon as one of the strings is built at runtime, read from input, or copied with [[Strcpy|`strcpy`]].

## Mechanics

`strcmp` walks both strings in lockstep, comparing one byte at a time, until either (a) a pair of bytes differs (return their signed difference) or (b) one or both strings reach their [[NullTerminator|`'\0'`]] (return 0 if both, or the difference if only one ended).

## Bounded variant

[[Strncmp|`strncmp`]] is the bounded counterpart — compares at most `n` bytes, useful for prefix-match (`strncmp(s, "http://", 7) == 0`) and for comparing strings that may not be null-terminated.

## Locale and case sensitivity

`strcmp` is **byte-level on raw ASCII** — not locale-aware, not case-insensitive. `strcasecmp` / `strncasecmp` (POSIX extensions, in `<strings.h>`) provide case-insensitive comparison; `strcoll` provides locale-aware comparison.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strcmp` and its tri-valued return convention.
