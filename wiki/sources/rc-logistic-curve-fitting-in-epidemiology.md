---
title: "Logistic curve fitting in epidemiology (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, curve-fitting, epidemiology]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Logistic_curve_fitting_in_epidemiology
---

## Summary
This task asks the programmer to fit a logistic growth curve to real cumulative Covid-19 case counts (96 daily world totals from December 31, 2019) using a least-squares method. The fitted curve has the form f(t) = n0·e^(rt) / (1 + n0·(e^(rt) − 1)/K), where K is the world population (~7.8 billion), n0 is the initial 27 cases, and r is the growth rate to be solved for. The key insight is converting the fitted growth rate r into the epidemiological basic reproduction number R0 via R0 ≈ e^(12r), using a generation time of roughly 12 days.

## Task Requirements
- Implement a least-squares fit of the logistic curve to the provided cumulative case data.
- Report the calculated growth rate r for the fitted logistic curve.
- Report the resulting R0 reproduction number derived from r using R0 ≈ e^(12r).

## Language Coverage
30 languages implement this task, spanning systems, numeric, and scripting ecosystems. Representative implementations include C, C++, D, Fortran, Go, Java, Julia, Python, R, Raku, and Wren.

## Connections
- [[LeastSquares]] — the core optimization method used to fit the curve.
- [[LogisticFunction]] — the sigmoidal growth model being fitted.
- [[CurveFitting]] — the general technique of estimating model parameters from data.
- [[NonlinearRegression]] — fitting the nonlinear logistic parameters minimizes squared residuals.
- [[BasicReproductionNumber]] — the epidemiological R0 derived from the fitted growth rate.

## Contradictions
- None — reference task page.
