---
title: "matplotlib"
type: concept
tags: [library, python, plotting, visualization]
sources: [pydata-preliminaries, pydata-plotting-and-visualization, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# matplotlib

The foundational Python plotting library. Started by [[JohnHunter]] in 2002 to bring a MATLAB-style plotting interface to Python. Designed for *publication-quality* static figures; exports to PDF, SVG, PNG, JPG, BMP, GIF. Now the substrate beneath most higher-level Python visualization tools.

## API
- Object-oriented: `fig, ax = plt.subplots(...)` then `ax.plot(...)`, `ax.set_xlabel(...)`, etc.
- Pyplot state machine: `plt.plot(...)`, `plt.title(...)` (modeled on MATLAB).
- Standard import: `import matplotlib.pyplot as plt`.
- Backends: agg (default raster), svg, pdf; interactive: Qt5Agg, TkAgg, MacOSX, WebAgg, ipympl (Jupyter widget).
- Configuration via `rcParams` or a `matplotlibrc` file.

## Higher-level wrappers
- [[seaborn]] — statistical plotting (uses matplotlib under the hood).
- [[pandas]] `.plot` accessor — convenient DataFrame plotting.

## Connections
- [[JohnHunter]] — original author.
- [[seaborn]] — built on top of matplotlib.
- [[pandas]] — `.plot` delegates here.
- [[pydata-plotting-and-visualization]] — chapter 9 covers the API primer.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — used to plot 2D UMAP-projected HDBSCAN clusters (outliers vs assigned points) as a static scatter alongside [[Plotly]]'s interactive view.
- [[Plotly]] / [[Datamapplot]] — sibling visualization libraries used in Ch 5.
