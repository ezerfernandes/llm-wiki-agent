---
title: "Shell Script"
type: concept
tags: [unix, shell, bash, scripting]
sources: [dis-app2-15-shell-programming]
last_updated: 2026-05-18
---

# Shell Script

A **shell script** is an executable text file containing [[UnixShell|shell]] commands and [[ShellProgramming|control flow]]. Three rules make a script runnable:

1. **First line is a [[Shebang|shebang]]** specifying the interpreter:
   ```bash
   #!/bin/bash
   ```
2. **File has the executable bit** set via [[Chmod|`chmod`]]:
   ```bash
   chmod u+x my_script.sh
   ```
3. **Run by path** (not by name alone, unless the directory is in [[PathVariable|`PATH`]]):
   ```bash
   ./my_script.sh arg1 arg2
   ```

## Minimal example

```bash
#!/bin/bash
# greet.sh — print a personalized greeting

if [ $# -ne 1 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

echo "Hello, $1!"
```

## Alternative execution

```bash
bash my_script.sh arg1     # run via interpreter directly — no chmod needed
source my_script.sh        # run in current shell (no subshell, modifies env)
. my_script.sh             # POSIX equivalent of source
```

## Exit status

Scripts return an integer exit status — `0` for success, non-zero for failure. Set via `exit N`; readable in the caller as `$?`.

## Connections

- [[ShellProgramming]] — umbrella concept.
- [[Shebang]] — the `#!` line.
- [[Chmod]] — `chmod u+x` makes the file executable.
- [[Bash]] — most common interpreter.
- [[CommandLineArguments]] — `$@` / `$#` / `$1` etc.
- [[dis-app2-15-shell-programming]] — source.
