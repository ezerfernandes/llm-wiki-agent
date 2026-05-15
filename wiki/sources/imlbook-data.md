---
title: "Data and Models"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/data.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
freedman_diaconis <- function(x) {   iqr <- IQR(x)   n <- length(x)   bin_width <- 2 * iqr * n^(-1/3)   num_bins <- ceiling((max(x) - min(x)) / bin_width)   return(num_bins) }

## Key Claims
- **Bike rentals (regression)** — This dataset contains daily counts of rented bikes from the bike rental company [Capital-Bikeshare](https://www.capitalbikeshare.com/) in Washington, D.C., along with weather and seasonal information.
- **Normalized Mutual Information** — Mutual information between two categorical random variables $X_j$ and $X_k$ is given by:
- **Palmer penguins (classification)** — For classification, we will use the Palmer penguins data.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- **Cited works** (sample): `fanaeet2014event`, `freedman1981histogram`, `gorman2014ecological`, `horst2020allisonhorst`, `mahmoudi2024proof`.

## Contradictions
None noted in this chapter.
