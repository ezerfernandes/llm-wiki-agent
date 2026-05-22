---
title: "Shebang"
type: concept
tags: [unix, shell, scripting]
sources: [dis-app2-15-shell-programming]
last_updated: 2026-05-18
---

# Shebang (`#!`)

The **shebang** is the two-byte sequence `#!` at the start of an executable script. It tells the [[OperatingSystem|OS]] which interpreter to load for the file's contents. Everything after `#!` on the first line is the interpreter path + optional args.

```bash
#!/bin/bash            # bash script
#!/bin/sh              # POSIX sh script
#!/usr/bin/env python3 # Python — use env for $PATH lookup
#!/usr/bin/perl        # Perl
```

## How it works

When the kernel `exec`'s a file:

1. If the file starts with `#!`, the kernel reads the rest of the line as `interpreter [arg]`.
2. The kernel `exec`'s the interpreter, passing the script path as an argument.
3. The interpreter reads and executes the script.

If there's no shebang, the [[UnixShell|shell]] falls back to running the file with `/bin/sh`.

## `#!/usr/bin/env` idiom

Hard-coding `/usr/bin/python3` breaks on systems where Python is elsewhere. The portable form is:

```bash
#!/usr/bin/env python3
```

`env` performs [[PathVariable|`PATH`]]-based lookup so the script finds whichever `python3` the user actually has.

## Connections

- [[ShellScript]] — the script artifact.
- [[ShellProgramming]] — umbrella.
- [[Chmod]] — executable bit must also be set.
- [[OperatingSystem]] — kernel `exec` handles the shebang.
- [[dis-app2-15-shell-programming]] — source.
