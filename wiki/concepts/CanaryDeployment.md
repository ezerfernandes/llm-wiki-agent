---
title: "Canary Deployment"
type: concept
tags: [deployment, mlops]
sources: [mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Canary Deployment

Rolling out a new model version to a small slice of production traffic (named for coal-mine canaries), monitoring health metrics, and gradually expanding if signals stay green. Often paired with [[ABTesting]] for statistical confirmation; native primitive in [[AnyscaleServices]] and [[KNative]].

In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]), canary is the third stage of progressive [[ModelValidation|validation]] — offline → [[ShadowDeployment|shadow]] → canary (1–5% traffic, catches scaling issues) → A/B test — a staged path that catches 70–80% of production issues before full rollout.
