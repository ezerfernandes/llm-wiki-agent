---
title: "System Entropy (Statistical Decay)"
type: concept
tags: [ml-systems, mlops, monitoring, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# System Entropy (Statistical Decay)

The principle that **every deployed ML model is in a state of unobserved decay from the moment it ships**, because its accuracy degrades as the live data distribution drifts away from its training distribution. The reason deployment is "the beginning of a new engineering challenge, not the end," in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Unlike a sorting algorithm (correct as long as the code is unchanged), an ML model's quality decays per the *degradation equation* — proportional to the divergence between training and live distributions, scaled by the model's sensitivity. The consequence: **reliability in ML systems is a property of the monitoring and retraining infrastructure, not of the code.**

**The [[Zillow]] Offers collapse (2021)** is the chapter's war-story evidence: home-price forecasting became "more unpredictable than expected," and scaling automated home-buying under that [[DistributionShift|distribution shift]] produced a $304M inventory write-down, 25% (2,000) layoffs, and the division's shutdown. The systems lesson: "distribution shift is not just a metric drop; it is a business risk" requiring rapid feedback loops and circuit breakers, not just accurate offline models.

## Connections

- [[DistributionShift]] / [[SilentDegradation]] — the mechanism behind statistical decay.
- [[Zillow]] — the war-story exemplar.
- [[MLOps]] — the monitoring/retraining infrastructure that addresses entropy.
- [[ComplexityTax]] — system entropy is what makes ML's operational cost recurring.
- [[MachineLearningSystems]] — entropy is what distinguishes ML systems from deploy-once software.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 models accuracy decay as System Entropy with a measurable half-life, feeding the square-root-law retraining economics.

