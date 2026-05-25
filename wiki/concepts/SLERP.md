---
title: "SLERP — Spherical Linear Interpolation"
type: concept
tags: [model-merging, interpolation, geometry]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# SLERP — Spherical Linear Interpolation

A [[ModelMerging|model-merging]] primitive based on the **Spherical LinEar inteRPolation** operator from computer graphics. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]]:

> "Intuitively, you can think of each component (vector) to be merged as a point on a sphere. To merge two vectors, you first draw the shortest path between these two points along the sphere's surface. This is similar to drawing the shortest path between two cities along the Earth's surface. The merged vector of these two vectors is a point along their shortest path."

## How it differs from [[LinearCombinationMerging|linear combination]]

Linear interpolation moves in a **straight line** through Euclidean space between two vectors:
- Midpoint: `0.5·A + 0.5·B`.

SLERP moves along the **geodesic** (great-circle arc) on the unit hypersphere:
- Midpoint: the rotation halfway between A and B.

For high-dimensional weight vectors that approximately live on a hypersphere (Wortsman et al. observation), SLERP often preserves model behavior better than linear interpolation — the merged model is more likely to stay "in distribution" of the constituents.

## The interpolation factor

The user-controlled hyperparameter `t ∈ [0, 1]`:

- `t = 0` → result = vector A.
- `t = 0.5` → halfway point on the geodesic (most common default).
- `t = 1` → result = vector B.
- `t < 0.5` → result is closer to A.
- `t > 0.5` → result is closer to B.

## Limitations Ch 7 names

- **Defined for two vectors at a time.** To merge more than two, do SLERP sequentially: merge A with B → merge result with C → etc. The order matters; results aren't commutative.
- **The formula is "mathy"** — Ch 7 doesn't show it; model-merging libraries (`mergekit`, etc.) implement it for you.

## When to choose SLERP over linear

- The constituents are **finetunes of the same base** and you want a *blend* rather than an *average*.
- The vectors are far apart in angle (linear interpolation can underflow magnitudes on the sphere).
- Your community has empirical evidence SLERP works better on your model family.

When in doubt, try both — they're both cheap operations.

## Connections

- [[ModelMerging]] — parent operation.
- [[LinearCombinationMerging]] — the Euclidean alternative.
- [[TaskVector]] / [[TaskArithmetic]] — usable as operands for SLERP.
- [[ai-engineering-ch07-finetuning]] — primary source.
