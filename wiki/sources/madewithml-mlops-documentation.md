---
title: "Made With ML — Documenting Code"
type: source
tags: [mlops, made-with-ml, documentation, software-engineering]
date: 2026-05-15
source_file: raw/madewithml/mlops-documentation.md
---

## Summary
Made With ML lesson on producing self-documenting Python code and auto-generating a docs site. Distinguishes comments (why), typing (input/output shapes), docstrings (full function contract), and rendered docs. Demonstrates type hints with `typing.List`/`int`/`np.ndarray`, Google-style docstrings with Args/Raises/Returns blocks, and how to wire up [[MkDocs]] + `mkdocstrings` to auto-render docstrings for every module under `madewithml/`. Concludes by publishing to GitHub Pages with optional custom domain.

## Key Claims
- Documentation has four distinct artifacts: comments, typing, docstrings, and rendered docs — each addresses a different reader.
- Type hints are explicit contracts: `def some_function(a: List, b: int = 0) -> np.ndarray` is a one-line spec readable by humans, IDEs, and static checkers.
- Python 3.9+ removes the need to import `List`/`Dict`/`Tuple` from `typing` — use built-in generics instead.
- Docstrings should include a summary, a runnable example, Args, Raises, and Returns; this enables both reader comprehension and automated rendering.
- `mkdocs new .` + `mkdocstrings` plugin scaffolds an auto-generated docs site whose structure mirrors the code repo.
- Per-module markdown files containing only `::: madewithml.<module>` populate themselves from the source's docstrings — there is no duplication.
- GitHub Pages serves the resulting site for free, with optional private hosting and custom domains, making docs publishing a one-config step.
- Docs publishing should be wired into CI/CD so every commit refreshes the site.

## Key Quotes
> "Code tells you how, comments tell you why." — Jeff Atwood, on the role of comments

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher
- [[MkDocs]] — static-site docs framework
- [[Mkdocstrings]] — docstring-to-docs plugin
- [[GitHubPages]] — hosting
- [[GitHubActions]] — CI to rebuild docs
- [[PythonLanguage]] — host language
- [[TypeHints]] — primary technique
- [[Docstrings]] — primary technique
- [[Documentation]] — overarching concept
- [[MLOps]] — discipline
- [[VSCode]] — referenced for autodocstring extension

## Contradictions
- None identified.
