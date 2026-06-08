---
title: "Shadow Deployment"
type: concept
tags: [deployment, mlops]
sources: [madewithml-serving, mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Shadow Deployment

Running a new model in parallel with the current one on live traffic without serving its outputs to users. A risk-free precursor to [[ABTesting]] and full rollout in [[ModelServing]].

In Reddi's *Machine Learning Systems* ([[mlsysbook-ch03-ml-workflow|Vol 1, Ch 3]]), shadow mode is the second stage of progressive [[ModelValidation|validation]] (offline → shadow → [[CanaryDeployment|canary]] → A/B), where it specifically catches *integration* issues that offline evaluation cannot.
