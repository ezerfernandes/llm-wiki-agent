---
title: "Made With ML — Evaluating Machine Learning Models"
type: source
tags: [mlops, made-with-ml, evaluation, testing]
date: 2026-05-15
source_file: raw/madewithml/mlops-evaluation.md
---

## Summary
Made With ML lesson on evaluating ML models beyond coarse-grained accuracy. Covers fine-grained per-class metrics, confusion-matrix sample analysis, confidence learning for label noise, slicing for bias detection, interpretability with SHAP/LIME, behavioral testing (invariance, directional, MFT), and online evaluation strategies (A/B, canary, shadow). Closes with the distinction between capability (loss) and alignment (accuracy) metrics.

## Key Claims
- Overall accuracy is insufficient; real-world ML requires per-class and per-slice metrics so you do not over-optimize one metric at the cost of another.
- Confusion-matrix false positives and false negatives should feed back into annotation pipelines, since many are actually labeling errors rather than model errors.
- Modern neural networks are systematically overconfident, so raw softmax probabilities must be calibrated (e.g. temperature scaling, Platt scaling) before being used to flag low-confidence predictions.
- Confident learning (cleanlab) can identify noisy labels by combining calibrated probabilities with class statistics, enabling relabel-and-retrain loops.
- Slice-based evaluation (via [[Snorkel]] slicing functions) exposes hidden bias such as algorithm-application correlations (CNNs always means computer-vision) that overall metrics hide.
- Behavioral testing from the CheckList paper decomposes model tests into invariance, directional, and minimum-functionality tests (MFT) that treat the model as a black box.
- Online evaluation needs three complementary strategies: [[ABTesting]] (control vs treatment), [[CanaryDeployment]] (small cohort), and [[ShadowDeployment]] (mirrored traffic, results not served).
- Shadow tests are safe but miss live user feedback signals and require replicating production dependencies, which is rarely fully possible.
- Capability (loss) and alignment (accuracy) can diverge: low accuracy with low loss signals misalignment; high accuracy with high loss signals skewed-distribution incorrect predictions.

## Key Quotes
> "It's a good to have our FP/FN samples feed back into our annotation pipelines in the event we want to fix their labels and have those changes be reflected everywhere." — on closing the labeling loop

> "Modern (large) neural networks result in higher accuracies but are over confident." — on the need for calibration before using probabilities as confidence signals

## Connections
- [[MadeWithML]] — source course
- [[GokuMohandas]] — author
- [[Anyscale]] — publisher / sponsor
- [[MLOps]] — overarching discipline
- [[ModelEvaluation]] — primary topic
- [[ConfusionMatrix]] — sample-level error analysis
- [[ConfidentLearning]] — cleanlab approach to label noise
- [[Cleanlab]] — library used
- [[Snorkel]] — slicing functions
- [[SHAP]] — interpretability
- [[LIME]] — interpretability
- [[BehavioralTesting]] — CheckList-style tests
- [[CheckList]] — landmark paper
- [[ABTesting]] — online experiment design
- [[CanaryDeployment]] — gradual rollout
- [[ShadowDeployment]] — mirrored traffic evaluation
- [[MultiArmedBandits]] — alternative to AB tests
- [[ModelCalibration]] — temperature/Platt scaling
- [[scikitlearn]] — `precision_recall_fscore_support`
- [[CapabilityVsAlignment]] — loss-vs-metric framing

## Contradictions
- None identified against existing wiki content.
