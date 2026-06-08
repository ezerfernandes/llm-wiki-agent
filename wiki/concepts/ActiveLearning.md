---
title: "Active Learning"
type: concept
tags: [ml-method, data, efficiency, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch04-data-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Active Learning

A [[DataSelection|data-selection]] technique in which the learning system **chooses which examples to label**, querying an oracle (often a human annotator) for the most informative points rather than labeling data uniformly. Cited in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as one of the levers (alongside [[TransferLearning|transfer learning]] and curriculum design) that ensure every sample provides maximum learning value, reducing the operation count $O$ in the [[IronLawOfMLSystems|iron law]].

The data-engineering chapter ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) treats active learning as a [[DataLabeling|labeling]]-scalability strategy that achieves target accuracy with **50–90% fewer labels** than random sampling by querying highest-uncertainty examples. The critical systems caveat: **compute must be in the budget model** — scoring a full 10M-image pool at $0.01/image = $100K *before any labels*, exceeding a $50K labeling budget. Active learning is viable only if the candidate pool is pre-filtered, inference is cheaper, or compute is funded separately.

## Connections

- [[DataSelection]] — the parent efficiency dimension.
- [[TransferLearning]] / [[WeakSupervision]] / [[SemiSupervisedLearning]] — sibling label-efficiency strategies.
- [[AIAssistedLabeling]] — the labeling hierarchy active learning complements.
- [[InformationEntropy]] — active learning adds high-entropy examples (maximizing signal/byte).
- [[EfficiencyFramework]] — the framework it belongs to.
- [[DataEngineering]] — the pipeline context.
- [[DynamicDataSelection]] — [[mlsysbook-ch09-data-selection|Ch 9]] classes active learning as a dynamic-selection technique; [[UncertaintySampling]] is its dominant query strategy. Medical-imaging ROI: ~50K vs 1M labels = $4.75M saved, ~20× speedup, ~4× fewer samples to reach 90% accuracy. ROI also depends on annotation latency (model drifts between query rounds) — see [[SelectionInequality]].
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch04-data-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
