---
title: "strtok_r (C library function)"
type: concept
tags: [c, libc, parallel-programming, thread-safe, reentrant]
sources: [dis-14-6-thread-safety]
last_updated: 2026-05-18
---

# strtok_r

`char *strtok_r(char *str, const char *delim, char **saveptr)` — the **reentrant** and **thread-safe** replacement for [[Strtok|`strtok`]]. The `_r` suffix is the [[POSIX]] convention for *reentrant*. The canonical "how to fix a thread-unsafe libc function" worked example in [[dis-14-6-thread-safety|DIS Ch 14.6]].

## Signature

```c
#include <string.h>
char *strtok_r(char *str, const char *delim, char **saveptr);
```

The single architectural change vs [[Strtok|`strtok`]]: the previously-hidden saved-position pointer is now the **explicit third parameter** `char **saveptr`. The caller allocates the storage (typically a `char *saveptr;` automatic variable on the thread's private [[Stack|stack]]) and threads it through every call.

## Calling Convention

```c
char *saveptr;                                  /* per-thread on private stack */
char *tok = strtok_r(str, ",", &saveptr);       /* first call */
while (tok != NULL) {
    /* ...process tok... */
    tok = strtok_r(NULL, ",", &saveptr);        /* subsequent calls */
}
```

- **First call**: `str` is the string to tokenize.
- **Subsequent calls**: pass `NULL` for `str`; `strtok_r` uses `*saveptr` to resume.
- **Returns** `NULL` when no more tokens.

## Why It's Thread-Safe

Each thread owns its **own `saveptr`** on its **own private [[Stack|stack]]**. No two threads ever read or write the same saved-position storage. The hidden-state hazard that doomed [[Strtok|`strtok`]] is structurally eliminated — there is no shared state to race on. *"`strtok_r()` uses an explicit pointer parameter (`saveptr`) to track parsing state, allowing independent thread execution without data corruption"* ([[dis-14-6-thread-safety|DIS Ch 14.6]]).

## The Pattern Generalizes

The `_r` redesign is a recurring [[POSIX]] discipline:

| Unsafe | Reentrant variant | Caller-owned state |
|---|---|---|
| [[Strtok|`strtok`]] | [[StrtokR|`strtok_r`]] | `char **saveptr` |
| `rand` | `rand_r` | `unsigned int *seed` |
| `localtime` | `localtime_r` | `struct tm *result` |
| `gmtime` | `gmtime_r` | `struct tm *result` |

Every reentrant variant follows the same rule: **eliminate hidden static state by making it an explicit parameter the caller owns**.

## Connections

- [[Strtok]] — the unsafe predecessor.
- [[ThreadSafety]] — the property `strtok_r` achieves.
- [[Reentrant]] — the property the `_r` suffix names.
- [[POSIX]] — defines the `_r` suffix convention.
- [[Pthreads]] — the threading API whose users need `strtok_r`.
- [[dis-14-6-thread-safety]] — DIS introduction.
