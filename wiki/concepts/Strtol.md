---
title: "strtol"
type: concept
tags: [c-language, strings, standard-library, conversion, stdlib, error-handling]
sources: [dis-2-9-2-cmd-line-args]
last_updated: 2026-05-17
---

# `strtol`

`strtol` (**str**ing **to** **l**ong) is the [[CLanguage|C]] standard-library function that parses an integer from a [[CString|C string]] **with full error reporting** — the production replacement for [[Atoi|`atoi`]]. Declared in `<stdlib.h>`. Surfaced in [[dis-2-9-2-cmd-line-args|DIS Ch 2.9.2]] as the modern alternative when parsing numeric [[CommandLineArguments|command-line arguments]] in `argv[]`.

## Signature

```c
#include <stdlib.h>

long strtol(const char *str, char **endptr, int base);
```

- `str` — the [[CString|C-string]] to parse.
- `endptr` — out-parameter (a pointer-to-pointer): on return, `*endptr` points to the **first unparsed byte** in `str`. Pass `NULL` if you don't care.
- `base` — radix, `2..36`, or `0` to auto-detect (`0x` → hex, `0` → octal, otherwise decimal).

## Why it beats [[Atoi|`atoi`]]

[[Atoi|`atoi`]] is **silent on every failure mode**: empty input, non-numeric input, and [[IntegerOverflow|overflow]] all collapse to `0` or undefined behavior. `strtol` fixes all three:

| Failure | [[Atoi|`atoi`]] | `strtol` |
|---|---|---|
| Empty string `""` | returns `0` | `*endptr == str` — no characters consumed |
| Garbage `"abc"` | returns `0` | `*endptr == str` — no characters consumed |
| Trailing garbage `"42xyz"` | returns `42` (silently) | returns `42`, `*endptr` points at `"xyz"` — *caller can see what's left* |
| Overflow `"99999999999999999999"` | undefined behavior | returns `LONG_MAX` / `LONG_MIN`, sets [[Errno|`errno`]] = `ERANGE` |

## Idiomatic usage

```c
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

errno = 0;                          // 1. clear errno first
char *end;
long n = strtol(argv[1], &end, 10);

if (end == argv[1])         { /* no digits parsed */ }
else if (*end != '\0')      { /* trailing garbage */ }
else if (errno == ERANGE)   { /* overflow */ }
else                        { /* n is a clean long */ }
```

The four-branch check is the price `strtol` charges for honesty. [[Atoi|`atoi`]] hides all four cases — which is **exactly** why production code does not use it.

## Siblings

- `strtoul` — unsigned long.
- `strtoll` / `strtoull` — `long long` / `unsigned long long` (C99).
- `strtod` / `strtof` / `strtold` — floating-point counterparts (replace `atof`).

## Connections

- [[CLanguage]] — the language whose stdlib this lives in.
- [[Atoi]] — the simpler-but-silent predecessor `strtol` supersedes.
- [[Errno]] — the global error-flag `strtol` writes on overflow.
- [[IntegerOverflow]] — the failure mode `strtol` detects via `errno == ERANGE`.
- [[CommandLineArguments]] / [[MainArgcArgv]] — the canonical use case (parsing `argv[i]`).
- [[CString]] / [[Pointer]] — the input type and the out-parameter mechanism.
- [[dis-2-9-2-cmd-line-args]] — the introducing source.
- [[DiveIntoSystems]] — the source textbook.
