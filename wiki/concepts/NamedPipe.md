---
title: "Named Pipe (FIFO)"
type: concept
tags: [posix, unix, ipc, named-pipe, fifo, mkfifo, message-passing]
sources: [dis-13-4-2-message-passing]
last_updated: 2026-05-18
---

# Named Pipe (FIFO)

The **named** variant of the [[Pipe|POSIX pipe]] — also called a **FIFO** (first-in-first-out). Same kernel-buffered one-way byte-stream semantics as an anonymous [[Pipe|pipe]], but **identified by a filesystem path** rather than by inherited file descriptors. This lifts the [[Pipe|anonymous pipe]]'s key limitation: **unrelated processes** (not just [[Fork|fork]]ed parent/child pairs) can rendezvous on a named pipe.

Forward-referenced in [[dis-13-4-2-message-passing|DIS Ch 13.4.2]] — the textbook confines coverage to anonymous pipes, but the FIFO is the natural generalization needed once communicating processes don't share a [[Fork|fork]] ancestor.

## API shape

Creation (shell):

```bash
mkfifo /tmp/myfifo
```

Creation (C):

```c
#include <sys/stat.h>
mkfifo("/tmp/myfifo", 0666);
```

Use — by **any two processes** that can `open` the path:

```bash
# Process A (writer)
echo "hello" > /tmp/myfifo
# Process B (reader)
cat /tmp/myfifo   # prints "hello"
```

Each side calls `open(path, O_WRONLY)` or `open(path, O_RDONLY)`; `read` / `write` proceed exactly as for an anonymous pipe.

## Pipe vs FIFO

| Property | [[Pipe\|Anonymous Pipe]] | Named Pipe (FIFO) |
|---|---|---|
| Filesystem name | No | Yes |
| Created by | `pipe(2)` | `mkfifo(3)` |
| Processes that can share | Related (via [[Fork]] inheritance) | **Any** that can `open` the path |
| Persistence after process exit | Closes when last fd closes | Path persists; pipe-instance closes when last fd closes |
| Lifecycle in filesystem | N/A | Removed via `unlink` / `rm` |

## Semantics carried over from anonymous pipes

- **One-way** byte stream.
- **Blocking** `open(O_WRONLY)` until a reader appears (and vice versa) by default — unless `O_NONBLOCK`.
- **`SIGPIPE`** delivered to the writer if all readers close.

## Related

- [[Pipe]] — the anonymous parent concept.
- [[MessagePassing]] — parent IPC family.
- [[Socket]] — the two-way / cross-network generalization.
- [[InterprocessCommunication]] — umbrella concept.
- [[SystemCall]] — `mkfifo` is the creation syscall (technically a libc wrapper around `mknod`).
- [[Signal]] — `SIGPIPE` integration point.
- [[dis-13-4-2-message-passing]] — primary source (FIFO forward-referenced).
