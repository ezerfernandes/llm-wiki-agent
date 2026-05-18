---
title: "scanf"
type: concept
tags: [c-language, stdlib, io]
sources: [dis-1-2-input-output]
last_updated: 2026-05-17
---

# scanf

**`scanf`** is the [[CLanguage|C]] standard-library **formatted-input** function, declared in [[StandardIOLibrary|`<stdio.h>`]]. It reads characters from [[StandardInput|stdin]], parses them according to a [[FormatSpecifier|format string]], and stores the resulting typed values into caller-provided memory locations.

```c
#include <stdio.h>
int main(void) {
    int x;
    float pi;
    printf("Enter int and float: ");
    scanf("%d%g", &x, &pi);
    printf("got %d and %g\n", x, pi);
    return 0;
}
```

## Defining properties (per [[dis-1-2-input-output|DIS Ch 1.2]])

- **Receivers are passed by address, not by value.** Each argument after the format string must be the [[AddressOfOperator|`&`]]-prefixed address of a variable — `scanf("%d", &num1)`, never `scanf("%d", num1)`. The function needs a *place to put* the parsed value, not its current contents.
- **Format string mirrors `printf`'s vocabulary.** `%d` (int), `%g` (float/double), `%s` (string), `%c` (char) — same [[FormatSpecifier|`%`-specifiers]] in input mode.
- **Whitespace is skipped between numeric reads.** Spaces, tabs, and newlines separating user inputs are silently consumed: `scanf("%d%g", &x, &pi)` accepts any whitespace pattern between the two numbers.
- **Argument arity must match.** One receiver per specifier; type mismatches are undefined behavior, not a compile error.

## Fragility

[[dis-1-2-input-output|Ch 1.2]] explicitly warns that `scanf` is *"picky about the exact format in which the user enters data"*. Non-numeric input where a number is expected can leave the program spinning — **Ctrl-C** to escape. Production-grade interactive input is deferred to Ch 2 (`fgets` + `sscanf` recipe).

## Contrast with [[Python]]

| | C `scanf` | Python `input()` |
|---|---|---|
| Returns | nothing (writes via address) | a `str` |
| Type | parsed per format specifier | always `str`; explicit `int()` / `float()` |
| On bad input | undefined / hang | `ValueError` you can catch |

## Connections

- [[CLanguage]] — the language.
- [[StandardIOLibrary]] — declared in `<stdio.h>`.
- [[Printf]] — the output counterpart; shares the [[FormatSpecifier|specifier]] vocabulary.
- [[FormatSpecifier]] — `%d` / `%g` / `%s` / `%c`.
- [[AddressOfOperator]] — `&`; required on every receiver argument.
- [[StandardInput]] — the stream `scanf` reads from.
- [[CMemoryAddress]] — the abstract concept `&` produces and `scanf` consumes.
- [[Python]] — `input()` contrast (string-then-convert vs typed-direct).
- [[dis-1-2-input-output]] — introducing source.
