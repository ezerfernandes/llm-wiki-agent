---
title: ".bashrc"
type: concept
tags: [unix, shell, bash, configuration]
sources: [dis-app2-14-dotfiles, dis-app2-4-editors]
last_updated: 2026-05-18
---

# `.bashrc`

`~/.bashrc` is the per-interactive-shell [[Bash]] configuration file — read every time a non-login interactive bash starts. Its purpose: customize the shell environment with [[EnvironmentVariable|environment variables]], [[BashAlias|aliases]], shell options, prompt strings, and shell functions.

## Typical contents

```bash
# Environment variables
export PATH=$PATH:/home/user/mybin
export EDITOR=vim
export VISUAL=vim

# Aliases — safety
alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"

# Aliases — convenience
alias gt31="cd ~/classes/CS31"
alias ll="ls -la"
alias gs="git status"

# Prompt
export PS1="\u@\h:\w$ "
```

## Activation

Changes to `.bashrc` apply on next shell start — or immediately via:

```bash
source ~/.bashrc       # or: . ~/.bashrc
```

## `.bashrc` vs `.bash_profile`

- `.bash_profile` runs for **login** shells (SSH session start, console login).
- `.bashrc` runs for **interactive non-login** shells (every new terminal tab).
- Common pattern: `.bash_profile` sources `.bashrc` so both regimes pick up the same config.

## Connections

- [[DotFile]] — umbrella category.
- [[BashAlias]] — `alias name="value"` syntax.
- [[EnvironmentVariable]] / [[PathVariable]] — most common `.bashrc` content.
- [[Bash]] — host shell.
- [[VimEditor]] — `export EDITOR=vim` is the canonical example from [[dis-app2-4-editors|App 2.4]].
- [[dis-app2-14-dotfiles]] — source.
