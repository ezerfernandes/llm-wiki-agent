---
title: "seaborn"
type: concept
tags: [library, python, plotting, visualization, statistics]
sources: [pydata-plotting-and-visualization]
last_updated: 2026-05-15
---

# seaborn

High-level statistical visualization library built on top of [[matplotlib]]. Author: Michael Waskom. Designed for tidy ([[pandas]]) DataFrames: most functions take `data=`, `x=`, `y=`, `hue=`, `style=`, `size=` and produce statistically-meaningful plots (regression, distribution, categorical relationships, facet grids).

## Common API
- `sns.relplot(x=, y=, hue=, kind="line"/"scatter", data=df)` — relational plots.
- `sns.catplot(x=, y=, kind="bar"/"box"/"violin"/"strip"/"swarm", data=df)` — categorical relationships.
- `sns.histplot(data=df, x=, hue=, kde=True)`, `sns.kdeplot`, `sns.ecdfplot` — distributions.
- `sns.regplot` / `sns.lmplot` — regression overlay.
- `sns.pairplot(df)` / `sns.heatmap(df.corr())` — exploratory grids.
- `sns.set_theme(style="whitegrid")` — defaults.

## Connections
- [[matplotlib]] — substrate; returns / accepts matplotlib Axes.
- [[pandas]] — tidy DataFrames are the expected input.
