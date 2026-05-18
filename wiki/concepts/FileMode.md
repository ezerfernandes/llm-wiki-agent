---
title: "File Mode (fopen mode string)"
type: concept
tags: [c-language, stdlib, io, file-io]
sources: [dis-2-8-io]
last_updated: 2026-05-17
---

# File Mode (fopen mode string)

The **mode string** is the second argument to [[Fopen|`fopen`]] — a short [[CString|C-string]] selecting whether the resulting [[FilePointer|`FILE *`]] is for **read**, **write**, or **append**, and where its initial position lies. Per [[dis-2-8-io|DIS Ch 2.8]] §2.8.3.

```c
fopen("input.txt", "r");   // read
fopen("output.txt", "w");  // write (truncates)
fopen("log.txt",   "a");   // append
```

## The three Ch 2.8 modes

| Mode | Reads? | Writes? | If file exists | If file missing | Initial position |
|---|---|---|---|---|---|
| `"r"` | yes | no | open as-is | **fail** ([[Fopen|`fopen`]] returns [[NullPointer|`NULL`]]) | start |
| `"w"` | no | yes | **truncate to zero length** | create | start |
| `"a"` | no | yes | open as-is | create | end (every write is at end) |

## Extensions (background, not in Ch 2.8)

- **`"+"`** suffix (`"r+"`, `"w+"`, `"a+"`) — read **and** write.
- **`"b"`** suffix (`"rb"`, `"wb"`) — **binary** mode (no-op on Unix; line-ending translation on Windows).
- POSIX `"x"` (`"wx"`) — exclusive create; fails if file exists.

## Footguns

- `"w"` **silently destroys** any existing file at the path. Bug-prone when the path is computed from user input.
- `"r"` is the only mode that returns [[NullPointer|`NULL`]] when the file doesn't exist; `"w"` and `"a"` both create it.

## Connections

- [[Fopen]] — the function consuming this string.
- [[FilePointer]] — the value `fopen` returns (or [[NullPointer|`NULL`]] on failure).
- [[NullPointer]] — `"r"`-mode failure sentinel for missing file.
- [[dis-2-8-io]] — introducing source.
