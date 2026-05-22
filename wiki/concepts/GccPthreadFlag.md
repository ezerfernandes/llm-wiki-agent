---
title: "-pthread compile flag"
type: concept
tags: [gcc, pthreads, compilation, c, linking]
sources: [dis-14-2-posix]
last_updated: 2026-05-18
---

# `-pthread` compile flag

[[GCC]]'s flag for compiling and linking a [[Pthreads]] program.

```bash
gcc -o program program.c -pthread
```

[[dis-14-2-posix|DIS Ch 14.2]] introduces it as the required step to make `pthread_create` / `pthread_join` resolve at link time.

## Distinct from `-lpthread`

`-pthread` is **not** identical to `-lpthread`:
- `-lpthread` only **links** against `libpthread`.
- `-pthread` **also** predefines threading-related preprocessor macros (e.g. `_REENTRANT`) and may adjust default code-generation settings for thread-safety. Recommended over the bare library link.

## Connections

- [[Pthreads]] — the library being linked.
- [[PthreadCreate]] / [[PthreadJoin]] — the symbols whose resolution requires the flag.
- [[GCC]] — the compiler the flag belongs to.
- [[dis-14-2-posix]] — primary source.
