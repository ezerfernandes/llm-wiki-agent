---
title: "strncmp"
type: concept
tags: [c-language, strings, standard-library, comparison]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strncmp`

`strncmp` is the **bounded** variant of [[Strcmp|`strcmp`]] in [[StringLibrary|`<string.h>`]] — compares at most `n` bytes of two strings. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]] alongside [[Strcmp|`strcmp`]].

## Signature

```c
#include <string.h>

int strncmp(const char *s1, const char *s2, size_t n);
```

Same tri-valued return convention as [[Strcmp|`strcmp`]]: `0` for equal, negative for `s1 < s2`, positive for `s1 > s2` — but only the first `n` bytes participate in the comparison.

## Two motivating use cases

1. **Prefix match.** The idiomatic *does this string start with X?* test:

   ```c
   if (strncmp(url, "https://", 8) == 0) {
       /* url begins with "https://" */
   }
   ```

2. **Comparing not-necessarily-terminated buffers.** When working with fixed-width fields (the [[Strncpy|`strncpy`]] non-terminated case), `strncmp` provides safe byte-bounded comparison without risk of reading past the end.

## Stops at `'\0'` too

`strncmp` stops at either `n` bytes *or* a [[NullTerminator|`'\0'`]] in either string, whichever comes first. So for normal terminated strings, `strncmp(s1, s2, BIG_N)` behaves identically to `strcmp(s1, s2)` when `BIG_N >= max(strlen(s1), strlen(s2))`.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strncmp` as the bounded comparison.
