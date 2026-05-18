---
title: "Jupyter"
type: concept
tags: [tool, notebook, python]
sources: [pydata-preliminaries, pydata-python-basics, d2l-preface, d2l-installation, d2l-appendix-tools]
last_updated: 2026-05-16
---

# Jupyter

Web-based interactive computing platform spun out of the [[IPython]] notebook in 2014. Documents are `.ipynb` JSON files containing executable code cells, Markdown / HTML cells, and rendered outputs (text, plots, HTML widgets). Architecture is *kernel-pluggable*: a notebook talks to a language-specific kernel over a ZMQ protocol; 40+ kernels exist. Python kernel = IPython.

## Variants
- **JupyterLab** — newer multi-panel IDE-like interface around the same notebook format.
- **JupyterHub** — multi-user server deployment.
- **VS Code / PyCharm / nbclassic / Voila** — alternate frontends consuming `.ipynb`.

## Connections
- [[IPython]] — origin and default Python kernel.
- [[FernandoPerez]] — co-founder.
- [[Quarto]] — publishing system that can render `.ipynb` to web/PDF (used for the open-access edition of Python for Data Analysis 3E).
- [[d2l-appendix-tools]] — D2L's operational reference for Jupyter: ssh `-L 8888:localhost:8888` port forwarding for remote kernels, the `notedown` plugin for editing markdown-source notebooks (`pip install d2l-notedown` + `c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'`), and the `ExecuteTime` nbextension for per-cell timing.
