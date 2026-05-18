---
title: "strlcpy"
type: concept
tags: [c-language, strings, standard-library, security, glibc]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strlcpy`

`strlcpy` is the modern *always-null-terminates* alternative to [[Strncpy|`strncpy`]]. Per [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]]:

> *"The `strlcpy` function is similar to `strncpy`, except it always adds the `'\0'` character to the end of the destination string."*

## Signature

```c
#include <string.h>

size_t strlcpy(char *dst, const char *src, size_t size);
```

Returns the length of `src` (the would-be-copied byte count) — useful for truncation detection: if the return value is `>= size`, the source was truncated.

## What it guarantees

- Copies at most `size - 1` bytes from `src` into `dst`.
- **Always** writes a [[NullTerminator|`'\0'`]] at the end of `dst` (assuming `size > 0`).
- No padding of unused `dst` bytes (unlike [[Strncpy|`strncpy`]]).

The combined effect — *capped write* + *guaranteed terminator* — removes both [[Strcpy|`strcpy`]]'s [[BufferOverflow|buffer-overflow]] hazard *and* [[Strncpy|`strncpy`]]'s non-termination footgun in one call. The defensive `dst[size-1] = '\0';` post-call line that [[Strncpy|`strncpy`]] requires is no longer needed.

## Portability — the catch

Per [[dis-2-6-strings|Ch 2.6]]:

> *"Linux's GNU C library added `strlcpy` in a recent version (2.38). It's currently only available on some systems, but its availability will increase as newer versions of the C library become more widespread."*

[[Glibc]] 2.38 shipped August 2023. `strlcpy` has long been present in BSD libcs (OpenBSD originated it, ~1998), Solaris, and macOS. On older Linux systems, the function is unavailable; portable code typically falls back to `snprintf(dst, size, "%s", src)` (always available, always terminates, slightly slower).

## When `strlcpy` is the right tool

The modern best-practice string-copy on systems that have it. Use:

```c
strlcpy(dst, src, sizeof(dst));
if (strlcpy(dst, src, sizeof(dst)) >= sizeof(dst)) {
    /* src was truncated */
}
```

The size-takes-buffer-size convention (rather than [[Strncpy|`strncpy`]]'s *max bytes to write*) makes [[SizeOf|`sizeof(dst)`]] the natural argument on a fixed-size array.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strlcpy` as the [[Strncpy|`strncpy`]] fix and notes its glibc 2.38 availability.
