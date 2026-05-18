---
title: "strchr"
type: concept
tags: [c-language, strings, standard-library, search]
sources: [dis-2-6-strings]
last_updated: 2026-05-17
---

# `strchr`

`strchr` is the [[StringLibrary|`<string.h>`]] **character search** function — finds the first occurrence of a single character in a [[CString|C string]]. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]].

## Signature

```c
#include <string.h>

char *strchr(const char *s, int c);
```

Returns a [[Pointer|pointer]] to the first occurrence of byte `c` in `s`, or [[NullPointer|`NULL`]] if `c` does not appear in `s`. The character argument is `int` (not `char`) for historical reasons; only the low byte is used.

## The returned pointer aliases the input

`strchr` does **not** copy. The returned pointer points *into* the input buffer — at the address of the matched byte. This is the same aliasing pattern as [[Strstr|`strstr`]]: search functions hand back addresses inside the original string.

```c
char s[] = "hello, world";
char *p = strchr(s, ',');         // p points to s + 5
*p = ';';                         // mutates s in place — s is now "hello; world"
```

## Idiomatic use — found-or-not test

```c
if (strchr(filename, '.') != NULL) {
    /* filename contains a dot — has an extension */
}
```

## Finding `'\0'`

`strchr(s, '\0')` is a valid (and surprisingly idiomatic) call: it returns a pointer to the [[NullTerminator|null terminator]], i.e., the end of the string. Equivalent to `s + strlen(s)` but in a single pass.

## Variants

- `strrchr` — finds the *last* occurrence of `c` in `s`.
- `memchr` — same idea but bounded by an explicit length parameter (useful for non-null-terminated buffers).

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strchr` as the single-character search.
