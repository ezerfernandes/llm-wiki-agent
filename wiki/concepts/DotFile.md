---
title: "Dotfile"
type: concept
tags: [unix, shell, configuration]
sources: [dis-app2-14-dotfiles]
last_updated: 2026-05-18
---

# Dotfile

A **dotfile** is a Unix file whose name begins with `.` — by convention these are **hidden** (omitted from default `ls` output) and typically hold **configuration** for a specific program. Visible via `ls -a`.

## Common dotfiles

| File | Application |
|---|---|
| [[BashRC|`.bashrc`]] | Per-shell-startup [[Bash]] config — aliases, env vars, prompt. |
| `.bash_profile` | Per-**login** bash config (often just sources `.bashrc`). |
| `.profile` | Login config readable by any [[BourneShell|sh]]-family shell. |
| `.vimrc` | [[VimEditor]] config. |
| `.emacs` / `.emacs.d/` | [[EmacsEditor]] config. |
| `.zshrc` | [[Zsh]] config. |
| `.gitconfig` | Per-user [[Git]] config. |
| `.ssh/config` | [[SSH]] client config. |
| `.xsession` | X11 window-manager config. |

## Why hide them?

Hiding by default keeps `ls` output focused on user content. Configuration is rarely browsed by listing; it's edited directly by path.

## Connections

- [[BashRC]] — the most-edited dotfile.
- [[EnvironmentVariable]] / [[PathVariable]] — what dotfiles typically set.
- [[VimEditor]] / [[EmacsEditor]] — sibling editor configs.
- [[UnixCommandLine]] — `ls -a` reveals dotfiles.
- [[dis-app2-14-dotfiles]] — source.
