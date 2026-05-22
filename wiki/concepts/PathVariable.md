---
title: "PATH Environment Variable"
type: concept
tags: [unix, shell, process]
sources: [dis-app2-14-dotfiles]
last_updated: 2026-05-18
---

# `PATH`

The **`PATH`** [[EnvironmentVariable|environment variable]] is a colon-separated list of directories the shell searches for executables when the user types a bare command name (no `/` prefix).

```bash
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/home/user/mybin
```

When you type `gcc`, the shell walks `PATH` left-to-right and runs the first match — typically `/usr/bin/gcc`.

## Extending PATH

```bash
export PATH=$PATH:/home/user/mybin   # append (lowest priority)
export PATH=/home/user/mybin:$PATH   # prepend (highest priority — override system)
```

Put the line in [[BashRC|`.bashrc`]] to make it persistent.

## Inspecting

```bash
which gcc        # show the PATH-resolved binary
type gcc         # show alias/function/builtin status too
command -v ls    # POSIX equivalent
```

## Security caveat

Never include `.` (current directory) early in `PATH` — running a command in a directory with a malicious `ls` would execute it instead of the system one.

## Connections

- [[EnvironmentVariable]] — umbrella.
- [[BashRC]] — where users typically extend `PATH`.
- [[UnixCommandLine]] — `which` / `type` lookup commands.
- [[dis-app2-14-dotfiles]] — source.
