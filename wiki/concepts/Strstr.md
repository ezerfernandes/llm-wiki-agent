---
title: "strstr"
type: concept
tags: [c-language, strings, standard-library, search]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strstr`

`strstr` is the [[StringLibrary|`<string.h>`]] **substring search** function — finds the first occurrence of one [[CString|C string]] inside another. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]].

## Signature

```c
#include <string.h>

char *strstr(const char *haystack, const char *needle);
```

Returns a [[Pointer|pointer]] to the first occurrence of `needle` in `haystack`, or [[NullPointer|`NULL`]] if `needle` is not present.

## The returned pointer aliases the input

Like [[Strchr|`strchr`]], `strstr` does **not** copy — the returned pointer points *into* `haystack` at the address where `needle` begins as a substring. Idiomatic for *find-and-then-edit-in-place* patterns:

```c
char text[] = "the quick brown fox";
char *p = strstr(text, "quick");
if (p != NULL) {
    /* p points to text + 4 — the 'q' in "quick" */
    p[0] = 'Q';   // text is now "the Quick brown fox"
}
```

## Found-or-not test

```c
if (strstr(buf, "ERROR") != NULL) {
    /* the word "ERROR" appears somewhere in buf */
}
```

## Edge case: empty needle

`strstr(haystack, "")` returns `haystack` — every string contains the empty string at position 0.

## Algorithmic note

The C standard does not mandate a search algorithm. Most implementations use naive `O(n*m)` for short needles and switch to Boyer-Moore / two-way / KMP variants for longer needles. For general byte-search needs in non-terminated buffers, `memmem` (POSIX) is the bounded counterpart.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strstr` as the substring search.
