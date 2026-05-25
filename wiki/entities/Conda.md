---
title: "Conda"
type: entity
tags: [tool, python, package-manager, environment-manager]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
Conda is an open-source package and environment manager originally for Python that handles non-Python binary dependencies as well. Distributed via Anaconda or Miniconda.

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Conda among the virtualenv alternatives the authors compared against [[PoetryPython|Poetry]], noting that Conda (like Venv) lacks proper dependency-locking semantics and relies on the weaker `requirements.txt` pattern. The book therefore chooses Poetry instead.

## Connections
- [[PoetryPython]] — chosen alternative.
- [[Pipenv]] — peer.
- [[UV]] — faster successor.
- [[VirtualEnvironment]] — what Conda manages.
- [[Python]] — language.
