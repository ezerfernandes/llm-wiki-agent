---
title: "strcat"
type: concept
tags: [c-language, strings, standard-library, security, buffer-overflow]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strcat`

`strcat` is the [[StringLibrary|`<string.h>`]] **string concatenation** function — appends a copy of `src` (including its [[NullTerminator|`'\0'`]]) to the end of the existing string in `dst`. Per [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]], `strcat` shares [[Strcpy|`strcpy`]]'s destination-size assumption and the same [[BufferOverflow|buffer-overflow]] hazard.

## Signature

```c
#include <string.h>

char *strcat(char *dst, const char *src);
```

Returns the destination pointer (`dst`). Finds the existing `'\0'` in `dst` (so `dst` **must already be a valid [[CString|C string]]**), then copies `src` (including its trailing `'\0'`) starting at that position — overwriting the old terminator.

## The destination-size requirement

Per [[dis-2-6-strings|Ch 2.6]]: *"failure to allocate enough memory will yield undefined results that range from program crashes to major security vulnerabilities."* `dst` must have capacity at least `strlen(dst) + strlen(src) + 1` bytes — original contents + appended bytes + new terminator. No [[BoundsChecking|bounds checking]] is performed.

## Example — intended use

```c
char buf[32] = "hello, ";
strcat(buf, "world");      // buf now holds "hello, world"
```

## Example — the security failure

```c
char buf[10] = "hello";
strcat(buf, " world");     // 12 bytes into a 10-byte buffer — UB
```

## Bounded variant

[[Strncat|`strncat`]] is the bounded version. **Unlike [[Strncpy|`strncpy`]], `strncat` *always* null-terminates** — making it the rare bounded variant without the non-termination footgun.

## Idiomatic substitute — `snprintf`

For non-trivial concatenation chains, `snprintf` is the modern best-practice:

```c
snprintf(buf, sizeof(buf), "%s%s", a, b);
```

It bounds the write, always terminates, and supports formatting in one call — eliminating the separate-`strcpy`-then-`strcat` pattern.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strcat` and reiterates the destination-size discipline from the `strcpy` discussion.
