---
title: "Bash History"
type: concept
tags: [unix, shell, bash]
sources: [dis-app2-11-history]
last_updated: 2026-05-18
---

# Bash History

**Bash history** is the [[Bash]] shell's record of previously executed commands, accessible through the `history` built-in and the `!`-prefix recall syntax. Persists to `~/.bash_history` across shell sessions.

## Commands (from [[dis-app2-11-history|DIS App 2.11]])

- `history` — print numbered list of recent commands.
- `!n` — re-execute history entry number `n`.
- `!!` — re-execute the **most recent** command. Useful when prior command needed `sudo`:
  ```bash
  apt install something
  # Permission denied
  sudo !!
  ```
- `!string` — re-execute the most recent command starting with `string`.

## Properties

- When `!n` runs, history records the **expanded** command, not the `!n` shorthand.
- Reverse-search (CTRL-R) and arrow-key history navigation are bash interactive features layered atop the same backing log (not covered in DIS App 2.11 but universally present).

## Connections

- [[HistoryCommand]] — the built-in itself.
- [[BangBang]] — the `!!` shortcut.
- [[Bash]] / [[UnixShell]] — host.
- [[BashRC]] — `HISTSIZE` / `HISTFILE` tuning lives here.
- [[dis-app2-11-history]] — source.
