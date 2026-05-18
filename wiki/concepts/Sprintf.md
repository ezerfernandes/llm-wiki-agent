---
title: "sprintf"
type: concept
tags: [c-language, strings, standard-library, formatted-output]
sources: [dis-1-5-arrays-strings]
last_updated: 2026-05-17
---

# `sprintf`

`sprintf` is the [[Printf|`printf`]] family member that writes its formatted output into a [[CString|C string]] buffer instead of to [[StandardOutput|stdout]]. The `s` in the name is for *"string"* — i.e., *print formatted, but into a string buffer*.

## Signature

```c
#include <stdio.h>

int sprintf(char *dst, const char *fmt, /* ... */);
```

`dst` is a caller-supplied `char` buffer; `fmt` is the [[FormatSpecifier|`%`-specifier]] format string with the same vocabulary as [[Printf|`printf`]] (`%d`, `%g`, `%s`, `%c`, …). Returns the number of characters written (excluding the trailing [[NullTerminator|`'\0'`]]).

`sprintf` is declared in `<stdio.h>` (not [[StringLibrary|`<string.h>`]]) because it is a member of the [[Printf|`printf`]] family; [[dis-1-5-arrays-strings|Ch 1.5]] introduces it in the string-library section anyway because its *use case* is constructing strings.

## Example

```c
char buf[32];
int x = 42;
double y = 3.14;
sprintf(buf, "x=%d, y=%g", x, y);   // buf now holds "x=42, y=3.14"
```

## The same unbounded-write hazard as `strcpy`

`sprintf` shares [[Strcpy|`strcpy`]]'s critical safety flaw: it cannot know how big the destination buffer is and will happily write past the end. A user-controlled `%s` substitution with a long input string is the textbook recipe for a [[BufferOverflow|buffer overflow]].

```c
char buf[16];
sprintf(buf, "Hello, %s!", user_name);   // if user_name is long enough, OVERFLOWS
```

## Safer alternative

`snprintf(dst, n, fmt, …)` — bounded variant that writes at most `n` bytes (including the [[NullTerminator|`'\0'`]]). The modern best-practice replacement; [[DiveIntoSystems]] introduces it in Ch 2.6.

## Cross-walk

- [[Python]] `f"x={x}, y={y}"` / `str.format` / `%` — all return a new `str` object; no buffer sizing concern.
- `sprintf` is the *raw byte-level* version: caller provides the storage, caller is responsible for sizing it correctly.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 introduces `sprintf` as the third [[StringLibrary|`<string.h>`]]-adjacent function for constructing C strings.
