---
title: "strncat"
type: concept
tags: [c-language, strings, standard-library]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strncat`

`strncat` is the **bounded** counterpart to [[Strcat|`strcat`]] in [[StringLibrary|`<string.h>`]] — appends at most `n` bytes of `src` to `dst`. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]].

## Signature

```c
#include <string.h>

char *strncat(char *dst, const char *src, size_t n);
```

## The good news — always terminates

Unlike [[Strncpy|`strncpy`]] (which may leave `dst` *un-terminated* when the source meets/exceeds the size bound), **`strncat` always writes a [[NullTerminator|`'\0'`]] at the end of the result**. The function appends at most `n` bytes from `src`, then writes one additional `'\0'` byte after them. So the required capacity is `strlen(dst) + n + 1`.

## The `n` argument's surprising semantics

The `n` in `strncat(dst, src, n)` is **the maximum number of bytes from `src`** to append — *not* the total capacity of `dst`. This is the inverse of [[Strlcpy|`strlcpy`]]'s convention and a classic API trap:

```c
char buf[10] = "hello";
strncat(buf, " world this is too long", sizeof(buf) - strlen(buf) - 1);
//                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//                                       must be space-left, not buf size
```

The defensive arithmetic — *remaining capacity minus 1 for terminator* — is the part that goes wrong; for general-purpose concatenation `snprintf` is the safer modern choice.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strncat` as the bounded `strcat`.
