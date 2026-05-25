---
title: "pyenv"
type: entity
tags: [tool, python, version-manager, open-source]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
pyenv is a Unix command-line tool for installing and switching between multiple Python interpreter versions, including per-directory selection via a checked-in `.python-version` file.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) uses pyenv as the official Python version manager for the book. Readers run `pyenv install 3.11.8` and `pyenv local 3.11.8` to pin all examples to Python 3.11.8 inside the repo, so that opening the project directory automatically selects the correct interpreter.

## Connections
- [[Python]] — interpreter pyenv manages.
- [[PoetryPython]] — used alongside pyenv (pyenv picks the interpreter, Poetry creates the virtualenv).
- [[VirtualEnvironment]] — adjacent concept.
- [[Reproducibility]] — pinning the Python version is a reproducibility lever.
