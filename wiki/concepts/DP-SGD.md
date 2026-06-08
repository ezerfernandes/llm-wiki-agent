---
title: "DP-SGD"
type: concept
tags: [cs324, llm]
sources: [cs324-security]
last_updated: 2026-06-04
---

DP-SGD (differentially private stochastic gradient descent) modifies standard SGD by clipping each example's gradient to a fixed norm and then adding calibrated random noise to the aggregated gradient. This provides a formal differential-privacy guarantee for the trained model.

## Connections
- [[DifferentialPrivacy]] — the guarantee DP-SGD provides
- [[cs324-security]] — discussed in this CS324 lecture
