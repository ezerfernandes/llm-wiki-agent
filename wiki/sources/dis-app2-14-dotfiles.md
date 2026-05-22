---
title: "Dive into Systems — App 2.14 Dotfiles"
type: source
tags: [book, unix, shell, configuration]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix2/dotfiles.html
---

## Summary
Fourteenth subchapter of [[DiveIntoSystems]] Appendix 2 *Using Unix*. Codifies [[DotFile|dotfiles]] — hidden configuration files (filenames starting with `.`) that customize program behavior. Anchors on [[BashRC|`.bashrc`]] for shell customization (aliases, [[EnvironmentVariable|environment variables]], the [[PathVariable|`PATH`]]) and surveys siblings like `.vimrc`, `.xsession`.

## Key Claims
- Files starting with `.` are **hidden** by default; `ls -a` reveals them.
- [[BashRC|`.bashrc`]] is read at bash startup; changes apply after `source .bashrc` or shell restart.
- [[PathVariable|`PATH`]] lists directories searched for executables: `PATH=$PATH:/home/user/mybin` adds a custom directory.
- Common aliases: `alias rm="rm -i"` (safety), `alias gt31="cd ~/classes/CS31"` (convenience).
- Editor configs like `.vimrc` parallel [[BashRC|`.bashrc`]] for [[VimEditor]] from [[dis-app2-4-editors|App 2.4]].

## Connections
- [[DotFile]] — minted here.
- [[BashRC]] — minted here.
- [[EnvironmentVariable]] / [[PathVariable]] — the variables `.bashrc` typically sets.
- [[BashAlias]] — the `alias` shell built-in.
- [[VimEditor]] / [[EmacsEditor]] — sibling editors with their own dotfiles (`.vimrc`, `.emacs`).
- [[DiveIntoSystems]] — Appendix 2.14.
