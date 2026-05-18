---
title: "Made With ML — Working in Notebooks"
type: source
tags: [foundations, made-with-ml, notebooks, jupyter, colab, course]
date: 2026-05-15
source_file: raw/madewithml/foundations-notebooks.md
---

## Summary
Intro lesson covering interactive notebooks as the development substrate for the rest of the Foundations track. Walks through opening notebooks in [[GoogleColab]] (Copy to Drive flow, rename to drop "Copy of") and the local alternative via [[JupyterLab]] inside a Python venv. Explains the two cell types (code and text), the SHIFT+RETURN execution shortcut, and standard create/edit/move/delete cell operations. Mentions cmd/ctrl+M+D to delete cells. Closes by previewing that subsequent lessons will introduce more notebook tricks.

## Key Claims
- Notebooks are the right onboarding surface for ML work because they interleave executable code with prose, math, and visual output in a single document — well suited to the iterative, exploratory nature of ML.
- Colab is the default zero-setup option (Google account + Copy to Drive); JupyterLab is the local-first alternative inside a Python virtual environment.
- The two-cell model (code + text/markdown) and one execution shortcut (SHIFT+RETURN) is essentially the entire notebook API surface for a beginner.
- Setting up a venv (`python3 -m venv venv && source venv/bin/activate && pip install jupyterlab`) is the recommended local pattern for a clean per-project environment.

## Key Quotes
> "Learn how to use interactive notebooks for developing in Python."

> "Notebooks are made up of cells. There are two types of cells: code cell ... and text cell."

## Connections
- [[GokuMohandas]] — author.
- [[MadeWithML]] — parent course.
- [[Jupyter]] — notebook execution kernel and UI lineage.
- [[JupyterLab]] — local IDE-style notebook front-end recommended in the lesson.
- [[IPython]] — interactive Python shell underlying Jupyter.
- [[GoogleColab]] — cloud notebook environment used as the default.
- [[VirtualEnvironment]] — Python venv pattern for local setup.
- [[Markdown]] — text cell format.

## Contradictions
None — entry-level setup lesson, no conflicting claims.
