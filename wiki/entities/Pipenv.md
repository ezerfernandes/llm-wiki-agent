---
title: "Pipenv"
type: entity
tags: [tool, python, dependency-management, virtualenv]
sources: [leh-ch02-tooling-and-installation]
last_updated: 2026-05-22
---

## What it is
Pipenv is a Python dependency-management tool that combines `pip` and `virtualenv` behind a `Pipfile` + `Pipfile.lock` interface, similar in spirit to [[PoetryPython|Poetry]].

## In LLM Engineer's Handbook
Ch. 2 ([[leh-ch02-tooling-and-installation]]) lists Pipenv as a comparable alternative to Poetry but notes it is slower; the authors prefer Poetry's mature ecosystem and lockfile semantics.

## Connections
- [[PoetryPython]] — chosen alternative.
- [[Conda]] / [[UV]] — peer / faster successor.
- [[VirtualEnvironment]] — what Pipenv manages.
- [[Python]] — language.
