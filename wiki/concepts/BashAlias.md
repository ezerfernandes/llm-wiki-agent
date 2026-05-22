---
title: "Bash Alias"
type: concept
tags: [unix, shell, bash]
sources: [dis-app2-14-dotfiles]
last_updated: 2026-05-18
---

# Bash Alias

A bash **alias** is a per-shell shorthand — typing the alias name expands to the aliased string before execution.

```bash
alias ll="ls -la"
alias gs="git status"
alias rm="rm -i"        # safety: confirm before delete
```

Defined interactively or (more usefully) in [[BashRC|`.bashrc`]] so they persist across shells.

## Inspection

```bash
alias              # list all aliases
alias ll           # show one alias's expansion
unalias ll         # remove
\rm file.txt       # run the *real* rm, bypassing the alias
```

## Aliases vs functions

Aliases do **literal text substitution** — they can't take arguments mid-string. For anything beyond a fixed prefix, use a shell function:

```bash
mkcd() { mkdir -p "$1" && cd "$1"; }
```

## Connections

- [[BashRC]] — canonical persistence location.
- [[Bash]] — host shell.
- [[DotFile]] — umbrella.
- [[dis-app2-14-dotfiles]] — source.
