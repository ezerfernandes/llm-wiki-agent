---
title: "Dive into Systems — App 2.15 Shell Programming"
type: source
tags: [book, unix, shell, scripting, bash]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/shellprog.html
---

## Summary
Fifteenth subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Codifies [[ShellProgramming|shell programming]] — writing executable [[ShellScript|shell scripts]] using bash as a programming language. Covers the [[Shebang|shebang]] line, variable assignment + reference, [[CommandLineArguments|`$@`/`$#`]] for arguments, conditionals (`if-then-else-fi` with `-eq`/`-gt`/`-lt`), and `for` loops in both C-style and element-iteration forms.

## Key Claims
- Scripts begin with a [[Shebang|shebang]] `#!/bin/bash` and must be made executable with `chmod u+x`.
- Variables: `var=value` to assign, `$var` to reference — **no spaces around `=`**.
- Command-line args: `$@` (array of all args), `$#` (count), `$1`, `$2`, ... (individual args) — analog of C's `argv` / `argc` from [[dis-2-9-2-cmd-line-args|Ch 2.9.2]].
- Conditionals: `if [ $x -eq 5 ]; then ... else ... fi` — *"the space chars between them and the condition are very important"*.
- Loops: C-style `for ((i=0; i<10; i++)); do ... done`; iteration `for i in list; do ... done`.

## Connections
- [[ShellProgramming]] — minted here (umbrella).
- [[ShellScript]] — minted here (the artifact).
- [[Shebang]] — minted here.
- [[Chmod]] — needed to make scripts executable; ingested in [[dis-app2-7-permissions|App 2.7]].
- [[CommandLineArguments]] — Ch 2.9.2 cross-walk at the shell level.
- [[Bash]] — host language.
- [[DiveIntoSystems]] — Appendix 2.15.
