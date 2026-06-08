---
title: "Training-Serving Skew"
type: concept
tags: [mlops, monitoring, serving, mlsysbook]
sources: [madewithml-monitoring, madewithml-serving, mlsysbook-ch04-data-engineering, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Training-Serving Skew

A mismatch between the data or transforms seen during training versus production serving. A leading cause of silent degradation; mitigated by shared [[Tokenizer]]s, feature stores, and [[ModelMonitoring]].

Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) calls it "the primary cause of ML system failure" and quantifies the cost: discrepancies as minor as a materialized view refreshed weekly in training vs daily in serving cause **10–15% accuracy drops** with no error messages, taking weeks to diagnose. The fix is the [[TrainingServingConsistency|consistency imperative]] — an architectural guarantee (shared code, persisted transform parameters), not copied code — operationalized by [[FeatureStore|feature stores]]. Uber found 30–40% of initial deployments suffered skew, motivating [[MichelangeloPlatform|Michelangelo]].

## Connections

- [[TrainingServingConsistency]] — the imperative that prevents it.
- [[FeatureStore]] / [[MichelangeloPlatform]] — the architectural fix.
- [[ModelMonitoring]] — runtime detection (shadow scoring).
- [[mlsysbook-ch04-data-engineering]] — source.
- [[mlsysbook-ch13-model-serving]] — Ch 13 focuses on the *serving-specific* manifestation, **preprocessing divergence** ($f_{\text{train}}(x) \neq f_{\text{serve}}(x)$): PIL vs OpenCV resize interpolation (0.5–1 pp), BGR vs RGB color ordering (≈ random predictions), wrong ImageNet normalization constants (out-of-distribution). Unlike data drift, it is a *deterministic, preventable engineering failure* — invisible to latency/exception monitoring. It is listed as a fallacy ("training accuracy guarantees serving accuracy") with a 95%→90% drop example; fix is identical preprocessing code paths or NVIDIA DALI.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 quantifies skew cost (1% error × 1M queries/day × $0.10 = $365K/yr) and gives the session_length 45-vs-12-min worked case; feature stores are the remedy.
- [[mlsysbook-ch16-conclusion]] — the conclusion formalizes this as the **Training-Serving Skew Law** (invariant #11 of the [[ThirteenQuantitativeInvariants|thirteen]]): $\Delta\text{Accuracy}\approx\mathbb{E}[|f_{serve}(x)-f_{train}(x)|]$; the opening MobileNetV2 failure is a skew × firmware-preprocessing interaction (4 pp accuracy drop), and skew is one of the five Deploy-phase signals that force the system back to its [[MLSystemLifecycle|Foundations]].

