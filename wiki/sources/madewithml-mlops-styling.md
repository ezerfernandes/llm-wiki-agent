---
title: "Made With ML — Styling and Formatting Code"
type: source
tags: [mlops, made-with-ml, code-style, software-engineering]
date: 2026-05-15
source_file: raw/madewithml/mlops-styling.md
---

## Summary
Made With ML lesson on adopting consistent Python style and formatting. Uses Black for autoformatting, isort for import ordering, and flake8 for PEP8 linting, all configured in a single `pyproject.toml`. Demonstrates how to reconcile the three tools' conflicting defaults (isort `profile = "black"`, flake8 ignoring `E501/W503/E226`), and packages the commands into a `Makefile` with `style` and `clean` targets so consistent formatting is a single `make` invocation.

## Key Claims
- Style enforcement rests on two principles: consistency (everyone follows the same rules) and automation (effortless after one-time setup).
- [[Black]], [[isort]], and [[flake8]] each handle a distinct concern (formatting, imports, linting) and must be configured together to avoid mutual conflicts.
- `pyproject.toml` is the canonical config home, replacing `setup.py`/`setup.cfg` for modern Python tooling per PEP 518.
- isort must be configured with `profile = "black"` so import sorting agrees with Black's wrapping rules.
- flake8 should ignore `E501` (line too long), `W503` (line break before binary operator), and `E226` (whitespace around arithmetic) to coexist with Black's opinions.
- Line-by-line suppression with `# NOQA: <code>` is preferred over weakening global rules when only specific lines need an exception.
- A `Makefile` with `.PHONY` targets like `style` and `clean` reduces the cognitive load of running three tools.
- These checks are the foundation for the next layer — automatic enforcement via [[PreCommit]] hooks and [[CICD]].

## Key Quotes
> "Code is read more often than it is written." — Guido van Rossum, framing why style matters

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[Black]] — autoformatter
- [[isort]] — import sorter
- [[flake8]] — linter
- [[PEP8]] — base style spec
- [[PyprojectToml]] — config file format
- [[Makefile]] — task runner
- [[PreCommit]] — downstream automation
- [[CICD]] — downstream enforcement
- [[CodeStyle]] — primary concept
- [[PythonLanguage]] — host language
- [[MLOps]] — discipline

## Contradictions
- None identified.
