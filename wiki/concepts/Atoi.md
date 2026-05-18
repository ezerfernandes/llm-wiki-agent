---
title: "atoi"
type: concept
tags: [c-language, strings, standard-library, conversion, stdlib]
sources: [dis-2-6-strings, dis-2-9-2-cmd-line-args]
last_updated: 2026-05-17
---

# `atoi`

`atoi` (**A**SCII **to** **i**nteger) is the [[CLanguage|C]] standard-library function that parses the leading integer prefix of a [[CString|C string]] into an `int`. Declared in `<stdlib.h>`, not [[StringLibrary|`<string.h>`]]. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]] alongside `atof` (ASCII to floating point) as the simple string-to-number entry points.

## Signature

```c
#include <stdlib.h>

int atoi(const char *str);
```

## Behavior

Skips leading whitespace, parses an optional `+`/`-` sign, then reads the longest run of digits. Returns the corresponding `int`. Stops at the first non-digit character.

```c
atoi("42");           // returns 42
atoi("  -17xyz");     // returns -17 (whitespace skipped, parsing stops at 'x')
atoi("hello");        // returns 0
atoi("");             // returns 0
```

## Why modern code prefers `strtol`

`atoi`'s headline weakness is its **silence on errors**:

- Empty / non-numeric input returns `0` — indistinguishable from the string `"0"`.
- Overflow is undefined behavior — `atoi("99999999999999")` is UB on platforms with 32-bit `int`.
- No way to detect *"parsed N digits, here's what's left."*

The modern replacement [[Strtol|`strtol`]]`(str, &end, base)` returns the value, writes a pointer to the first unparsed byte into `*end`, and reports overflow via [[Errno|`errno`]] = `ERANGE`. The chapter introduces `atoi` as the simple-but-quiet entry point and leaves [[Strtol|`strtol`]] as the production substitute — re-surfaced explicitly in [[dis-2-9-2-cmd-line-args|Ch 2.9.2]] as the recommended way to parse numeric [[CommandLineArguments|command-line arguments]] in `argv[]`.

## Sibling `atof`

`atof(str)` parses a `double` from the leading prefix of `str` — same silence-on-error caveat applies; modern code uses `strtod`.

## Usage pattern in the textbook

[[dis-2-6-strings|Ch 2.6]] introduces `atoi` as the bridge between the [[CString|C string]] world and the numeric world — the natural follow-up to *parsing command-line arguments* (`argv[]` is a `char *` array; integer arguments come in as strings and need conversion):

```c
int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);    // works but silent on malformed input
    ...
}
```

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `atoi` (and `atof`) as the `<stdlib.h>` string-to-number conversion functions.
- [[dis-2-9-2-cmd-line-args]] — Ch 2.9.2 re-surfaces `atoi` as the canonical bridge for parsing numeric [[CommandLineArguments|command-line arguments]] in `argv[]`, with [[Strtol|`strtol`]] called out as the production replacement.
