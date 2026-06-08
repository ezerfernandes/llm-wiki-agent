---
title: "Expected Calibration Error"
type: concept
tags: [benchmarking, calibration, model-quality, compression, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Expected Calibration Error

**ECE** measures the gap between a model's predicted confidence and its actual accuracy, averaged across confidence bins — the quantitative test of [[ModelCalibration|model calibration]]. A well-calibrated model that says "90% confident" should be correct 90% of the time. Per [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]] interpretation thresholds:

- ECE < 0.05 — well-calibrated; confidence reliable for threshold-based decisions.
- 0.05 < ECE < 0.10 — moderate; use confidence with caution.
- ECE > 0.10 — poorly calibrated; confidence unreliable.

The systems significance: **compression degrades calibration even when it preserves accuracy.** Quantizing MobileNetV2 to INT8 holds top-1 accuracy (−0.9 pp) but raises **ECE 0.031 → 0.089** (borderline) — invisible to aggregate accuracy yet decisive for any pipeline that thresholds on confidence ("only act if confidence > 85%"). Quantization compresses the softmax distribution's mass toward the top prediction, causing overconfidence. The fix is post-hoc **temperature scaling** (learn scalar $T$≈1.5–2.5, divide logits before softmax); reliability diagrams visualize the correspondence. This is why compression validation must be **multi-dimensional**, not accuracy-only.

## Connections

- [[ModelCalibration]] — the property ECE quantifies (confidence matching empirical accuracy).
- [[Calibration]] — the related *quantization* calibration step (calibration dataset), a distinct sense of the term.
- [[Quantization]] — the compression technique that most often degrades calibration.
- [[ParetoFrontier]] — calibration is a hidden axis of the compression trade-off.
- [[ModelCompression]] — multi-dimensional validation includes ECE alongside accuracy and edge-case robustness.
- [[mlsysbook-ch12-benchmarking]] — source.
