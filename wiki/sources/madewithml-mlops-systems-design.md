---
title: "Made With ML — Machine Learning Systems Design"
type: source
tags: [mlops, made-with-ml, systems-design, ml-canvas]
date: 2026-05-15
source_file: raw/madewithml/mlops-systems-design.md
---

## Summary
The systems-design lesson is the *How* counterpart to product design. It walks through data sources (training + production batch/stream), labeling, metric selection (precision/recall/F1 for a multiclass task), offline vs. online evaluation, modeling principles, and the choice between [[BatchInference]] and [[OnlineInference]]. The running example optimizes weighted F1 for content tagging, plans canary/A-B rollouts for online evaluation, and builds in human-in-the-loop feedback for low-confidence predictions.

## Key Claims
- Tying qualitative business objectives to quantitative ML metrics is "one of the hardest challenges with ML systems."
- Five modeling principles: end-to-end utility, manual-before-ML, augment-vs-automate, internal-vs-external, and thorough testing/evaluation.
- Start with a rule-based baseline before reaching for ML; some early releases should be internal-only for feedback and data collection.
- Batch inference caches predictions in a database for low-latency lookup; ideal for recommendations based on stable history but predictions go stale on shifting interests.
- Online inference requires the model to be served as a separate API/microservice with real-time monitoring because the input space is unbounded.
- Offline evaluation uses a gold-standard holdout dataset; online evaluation uses real-world labels or proxy signals when labels are scarce.
- Feedback loops should combine human-in-the-loop checks on low-confidence cases with user-reported misclassifications.
- Releases need not all be external — internal canary rollouts and A/B tests on subsets gather UX/utility signal before full launch.

## Key Quotes
> "One of the hardest challenges with ML systems is tying our core objectives, many of which may be qualitative, with quantitative metrics that our model can optimize towards."

> "While it's important to iterate and optimize on our models, it's even more important to ensure that our ML systems are actually making an impact."

## Connections
- [[MadeWithML]] — parent course.
- [[GokuMohandas]] — author.
- [[Anyscale]] — publisher.
- [[MLCanvas]] — design template extended here.
- [[SystemsDesign]] — methodology this lesson teaches.
- [[MLOps]] — surrounding discipline.
- [[BatchInference]] — one of the two inference modes covered.
- [[OnlineInference]] — the other inference mode, used in the example.
- [[OfflineEvaluation]] — gold-standard holdout pattern.
- [[OnlineEvaluation]] — proxy-signal / labeled production evaluation.
- [[F1Score]] — chosen metric for the content-tagging task.
- [[PrecisionRecall]] — underlying metric pair.
- [[ConfusionMatrix]] — TP/FP/TN/FN framework referenced.
- [[CanaryRollout]] — staged release pattern mentioned.
- [[ABTesting]] — staged rollout method.
- [[humanintheloop]] — feedback mechanism for low-confidence predictions.
- [[DataLeakage]] — flagged as a risk during data splitting.
- [[DataDrift]] — implicit in "trust that this stream only has data consistent with what we've seen."

## Contradictions
- None identified.
