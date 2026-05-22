---
title: "stderr"
type: concept
tags: [unix, io]
sources: [dis-app2-12-io-redirect]
last_updated: 2026-05-18
---

# stderr

**stderr** (standard error, [[FileDescriptor|fd]] **2**) is the output stream a process writes **error and diagnostic** messages to. Kept separate from [[Stdout]] so that errors remain visible even when stdout is redirected or piped.

- Redirect with `cmd 2> errs.log`.
- **Unbuffered** by default — error messages appear immediately, even on crash.
- C wrappers: `fprintf(stderr, ...)`, `perror`.

## Why the separation matters

```bash
make > build.log    # build chatter into log, errors still on screen
make &> all.log     # capture everything (rare; loses interactive feedback)
```

## Connections

- [[StandardStream]] / [[Stdin]] / [[Stdout]] — siblings.
- [[IORedirection]] — `2>` / `2>&1` operators.
- [[Perror]] — C library helper that writes to stderr.
- [[dis-app2-12-io-redirect]] — source.
