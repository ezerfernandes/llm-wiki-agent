---
title: "SciPy"
type: concept
tags: [library, python, scientific-computing]
sources: [pydata-preliminaries]
last_updated: 2026-05-15
---

# SciPy

Collection of scientific-computing sub-packages built on top of [[NumPy]]: `scipy.integrate` (quadrature + ODE), `scipy.linalg` (linear algebra extending `numpy.linalg`), `scipy.optimize` (minimization + root-finding), `scipy.signal` (signal processing), `scipy.sparse` (sparse matrices + solvers), `scipy.special` (SPECFUN wrappers), `scipy.stats` (distributions + statistical tests). Pair with NumPy for most scientific work in Python; together they cover roughly the functionality of MATLAB plus toolboxes.

## Connections
- [[NumPy]] — depends on; uses ndarray as the data substrate.
- [[scikitlearn]] / [[statsmodels]] — depend on SciPy for many routines.
