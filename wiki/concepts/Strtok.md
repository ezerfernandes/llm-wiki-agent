---
title: "strtok"
type: concept
tags: [c-language, strings, standard-library, tokenization, thread-safety]
sources: [dis-2-6-strings, dis-14-6-thread-safety]
last_updated: 2026-05-18
---

# `strtok`

`strtok` is the [[StringLibrary|`<string.h>`]] **tokenization** function — splits a [[CString|C string]] into a sequence of *tokens* separated by delimiter characters. Introduced in [[dis-2-6-strings|Ch 2.6]] of [[DiveIntoSystems]].

## What a token is

Per [[dis-2-6-strings|Ch 2.6]]:

> *"A **token** refers to a subsequence of characters in a string separated by any number of delimiter characters of the programmer's choosing."*

## Signature

```c
#include <string.h>

char *strtok(char *str, const char *delim);
```

Returns a pointer to the next token, or [[NullPointer|`NULL`]] when no more tokens remain. The `delim` parameter is a C string listing *all* characters to treat as delimiters — multiple delimiters can be specified at once, and runs of consecutive delimiters are skipped.

## The two-call pattern

```c
char input[] = "alpha,beta;gamma,delta";

/* First call: pass the string */
char *tok = strtok(input, ",;");
while (tok != NULL) {
    printf("%s\n", tok);
    /* Subsequent calls: pass NULL to continue the same scan */
    tok = strtok(NULL, ",;");
}
```

The function holds **internal `static` state** between calls — passing `NULL` says *"continue where you left off."* The first call seeds this state with the input string.

## Two surprising consequences of the design

1. **Destructive.** `strtok` writes a [[NullTerminator|`'\0'`]] over each delimiter byte it finds, splitting the input buffer in place. After tokenization, the original string is *unrecoverable* unless copied first. The returned token pointers are addresses inside the (now-modified) input buffer.

2. **Not thread-safe; not reentrant.** Because state lives in a `static` variable inside `strtok`, two threads (or two interleaved tokenization scans on different strings) corrupt each other. The reentrant alternative `strtok_r` (POSIX) takes the state as an explicit `char **saveptr` parameter:

   ```c
   char *saveptr;
   char *tok = strtok_r(input, ",;", &saveptr);
   while (tok != NULL) {
       /* ... */
       tok = strtok_r(NULL, ",;", &saveptr);
   }
   ```

## Use cases

CSV / TSV line parsing, command-line argument splitting, simple lexers, parsing environment-variable lists (`PATH`). For anything with quoting, escaping, or nested delimiters, hand-rolled parsing or a dedicated library is needed.

## Revisit in the parallel-programming context

[[dis-14-6-thread-safety|DIS Ch 14.6]] returns to `strtok` as the **canonical thread-unsafe libc example** — *"`strtok()` is thread-unsafe because it maintains internal state. Multiple threads calling it simultaneously produce inconsistent results"*. The worked `countElemsStr` parallel-tokenization example demonstrates: two threads calling `strtok` concurrently on *different strings* race on the same `static` saved-position pointer; one thread's call advances past its delimiter then the other thread's call overwrites the state, and both threads' next-token resumption returns garbage. The reentrant fix is [[StrtokR|`strtok_r`]] — see [[ThreadSafety]] and [[Reentrant]] for the general pattern.

## Sources

- [[dis-2-6-strings]] — Ch 2.6 §2.6.3 introduces `strtok`, defines *token*, and warns about the internal-state thread-safety issue (and the `strtok_r` reentrant variant).
- [[dis-14-6-thread-safety]] — Ch 14.6 revisits `strtok` as the canonical thread-unsafe libc function in the parallel-programming context; introduces [[StrtokR|`strtok_r`]] as the fix.
