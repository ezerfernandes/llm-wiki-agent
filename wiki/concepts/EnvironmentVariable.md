---
title: "Environment Variable"
type: concept
tags: [unix, shell, process]
sources: [dis-app2-14-dotfiles]
last_updated: 2026-05-18
---

# Environment Variable

An **environment variable** is a named string that the [[OperatingSystem|OS]] propagates from a parent process to its children — a per-process key/value table accessible to every program in the process tree.

## Shell syntax

```bash
export NAME="value"        # set + export to children
echo $NAME                 # read
unset NAME                 # remove
env                        # list all environment variables
```

## Common variables

| Variable | Purpose |
|---|---|
| [[PathVariable\|`PATH`]] | Directories searched for executables. |
| `HOME` | User's home directory (`~`). |
| `USER` / `LOGNAME` | Login name. |
| `SHELL` | Path of the user's login shell. |
| `EDITOR` / `VISUAL` | Default editor (e.g., `vim`). |
| `LANG` / `LC_ALL` | Locale settings. |
| `PWD` | Current working directory. |

## In C

```c
#include <stdlib.h>
char *p = getenv("PATH");
setenv("FOO", "bar", 1);
```

## Connections

- [[PathVariable]] — the canonical executable-search variable.
- [[BashRC]] — where users persist their environment variables.
- [[DotFile]] — umbrella.
- [[Process]] — env is per-process, inherited at [[Fork|`fork`]].
- [[dis-app2-14-dotfiles]] — source.
