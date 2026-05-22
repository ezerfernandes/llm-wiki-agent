---
title: "Shell Programming"
type: concept
tags: [unix, shell, bash, scripting]
sources: [dis-app2-15-shell-programming]
last_updated: 2026-05-18
---

# Shell Programming

**Shell programming** treats the [[UnixShell|shell]] (typically [[Bash]]) as a programming language: variables, control flow, functions, I/O — packaged into executable [[ShellScript|scripts]]. Sweet spot: gluing together existing Unix tools with conditional logic.

## Core constructs (from [[dis-app2-15-shell-programming|DIS App 2.15]])

### Variables

```bash
name="Alice"          # NO spaces around =
echo "Hello, $name"   # $-prefix to dereference
count=$((1 + 2))      # arithmetic expansion
```

### Command-line arguments

| Symbol | Meaning |
|---|---|
| `$0` | Script name |
| `$1`, `$2`, ... | Positional arguments |
| `$@` | All arguments as separate words |
| `$*` | All arguments as one word |
| `$#` | Argument count |
| `$?` | Last command's exit status |

Numeric C-like analogs of `argv` and `argc` from [[dis-2-9-2-cmd-line-args|Ch 2.9.2]].

### Conditionals

```bash
if [ "$x" -eq 5 ]; then
    echo "five"
elif [ "$x" -gt 5 ]; then
    echo "big"
else
    echo "small"
fi
```

Test operators: `-eq` `-ne` `-lt` `-le` `-gt` `-ge` (numeric); `=` `!=` (string); `-f file` `-d dir` `-z str` (existence/empty).

**Crucial:** *"the space chars between them and the condition are very important"* — `[ "$x" -eq 5 ]` works; `["$x"-eq 5]` is a parse error.

### Loops

```bash
# C-style
for ((i = 0; i < 10; i++)); do
    echo $i
done

# Element iteration
for f in *.txt; do
    echo "Processing $f"
done

# While
while [ "$count" -lt 10 ]; do
    count=$((count + 1))
done
```

### Functions

```bash
greet() {
    echo "Hello, $1"
}
greet "World"
```

## When to use shell vs Python

- **Shell:** Pipelines of existing commands, file munging, system administration glue.
- **Python:** Complex data structures, math, anything > ~200 lines.

## Connections

- [[ShellScript]] — the artifact form.
- [[Shebang]] — the `#!/bin/bash` first line.
- [[Bash]] — host language.
- [[CommandLineArguments]] — the [[dis-2-9-2-cmd-line-args|Ch 2.9.2]] C-side cross-walk.
- [[Chmod]] — needed to make scripts executable (`chmod u+x`).
- [[dis-app2-15-shell-programming]] — source.
