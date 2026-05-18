---
title: "Python for Data Analysis 3E — Ch.9: Plotting and Visualization"
type: source
tags: [book, matplotlib, seaborn, plotting, visualization, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/plotting-and-visualization.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/plotting-and-visualization.html
chapter: 9
---

## Summary
A focused tour of [[matplotlib]] (Figure / Axes / Subplots; colors / markers / line styles; ticks / labels / legends; annotations; saving; rc configuration) and the higher-level plotting interfaces built on top — pandas's `.plot` accessor and [[seaborn]] (line / bar / hist / scatter / facet-grid / categorical). Closes with a one-paragraph survey of [[Bokeh]] / [[Altair]] / other modern web-based libraries.

## Key Claims
- **Figure / Axes** — `fig = plt.figure(figsize=(W,H))`; `ax = fig.add_subplot(rows, cols, idx)`; the convenient `fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)` returns a grid of Axes.
- **Line styles** — `ax.plot(x, y, color="g", linestyle="--", marker="o", drawstyle="steps-post")` or shorthand `ax.plot(x, y, "go--")`.
- **Ticks / labels / legends** — `ax.set_xticks([...])`, `ax.set_xticklabels([...], rotation=30)`, `ax.set_xlabel`, `ax.set_title`; `ax.legend(loc="best")` after passing `label=` to each plot call.
- **Annotations** — `ax.annotate(text, xy=(x,y), xytext=(...), arrowprops={...})`; `ax.add_patch(Rectangle / Circle / Polygon)`.
- **Saving** — `plt.savefig("path.svg", dpi=400, bbox_inches="tight")`; supports PDF, SVG, PNG, JPG.
- **rcParams** — `plt.rc("figure", figsize=(10,6))` or via `matplotlibrc` file; configures default styles globally.
- **pandas plotting** — `s.plot()` / `df.plot(kind="line"/"bar"/"barh"/"hist"/"box"/"kde"/"density"/"scatter"/"hexbin"/"pie")`; uses index as x-axis by default; subplots via `subplots=True, layout=(rows,cols)`.
- **seaborn** — high-level statistical plotting; common API `sns.barplot(x=, y=, data=df, hue=)`, `sns.regplot`, `sns.pairplot`, `sns.boxplot`, `sns.histplot`, `sns.kdeplot`; `sns.catplot` / `sns.relplot` create facet grids by category.
- **Backend setup** — `%matplotlib inline` in Jupyter for static images; `%matplotlib notebook` for interactive; `%matplotlib widget` for ipywidgets.
- **Other tools surveyed** — Bokeh, Altair (interactive, web-native); plotly, holoviews. Author sticks to matplotlib + seaborn for teaching fundamentals.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[matplotlib]] — the foundational plotting library.
- [[seaborn]] — statistical visualization on top of matplotlib.
- [[pandas]] — `.plot` accessor delegates to matplotlib.
- [[JohnHunter]] — original matplotlib author (2002).
- [[pydata-data-aggregation]] — chapter 10 next: groupby & aggregation.

## Contradictions
- None.
