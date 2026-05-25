---
title: "Designing ML Systems — Ch 8: Data Distribution Shifts and Monitoring"
type: source
tags: [book-chapter, dmls, mlops, monitoring, distribution-shift, observability, production-ml]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch08-distribution-shifts-monitoring.txt
last_updated: 2026-05-23
---

## Summary

Chapter 8 of [[ChipHuyen|Chip Huyen]]'s *[[DesigningMachineLearningSystems|Designing Machine Learning Systems]]* ([[OReilly|O'Reilly]], 2022) addresses what happens **after** a model is deployed: performance degrades over time and the system fails — often silently. The chapter taxonomizes ML system failures into **software system failures** (the majority, per a Google study of 96 outages: 60/96 were non-ML) and **ML-specific failures** (production-vs-training data mismatch, edge cases, and degenerate feedback loops). It then zooms into [[DistributionShift|data distribution shifts]] — formalized via the decompositions $P(X,Y) = P(Y\mid X)P(X) = P(X\mid Y)P(Y)$ — and explains [[CovariateShift]], [[LabelShift]], and [[ConceptShift|concept drift]] with concrete examples (breast cancer, COVID-era housing prices, English-French translation). The second half is a practitioner's playbook for [[Monitoring|monitoring]] and [[observability|observability]] of ML systems: operational metrics (uptime, SLA/SLO, latency, throughput), ML metrics across four artifacts (accuracy-related, predictions, features, raw inputs), [[DriftDetection|drift detection]] via summary statistics and [[HypothesisTesting|two-sample tests]] ([[KolmogorovSmirnovTest|KS]], [[MaximumMeanDiscrepancy|MMD]], Least-Squares Density Difference), and a tools section on logs, dashboards, and alerts.

## Key Claims

- **Deploying a model is not the end of the process** — model performance degrades in production and must be continually monitored. ML systems often fail *silently* because ML-performance violations (unlike operational ones) lack a 404/timeout/segfault to surface them.
- **Most ML failures are non-ML failures.** Papasian and Underwood's 2020 study of 96 broken Google ML pipelines over 15 years found 60/96 caused by distributed-systems and data-pipeline issues, not ML; *"ML engineering is mostly engineering, not ML."*
- **Three new ML-specific failure modes emerge post-deployment:** (1) production data differing from training data, (2) [[EdgeCase|edge cases]], and (3) [[DegenerateFeedbackLoop|degenerate feedback loops]]. Edge cases (performance) differ from [[Outlier|outliers]] (data): every edge-case outlier is an outlier, but not every outlier is an edge case.
- **Roughly 80% of "drifts" captured by monitoring are caused by internal human errors** (the CTO of a monitoring vendor's estimate) — pipeline bugs, missing-value imputation issues, feature-extraction mismatch between training and inference, wrong model version, app-interface bugs that change user behavior. Detecting a shift is hard; *determining its cause* is even harder.
- **Distribution shift has three formal subtypes** under the joint decompositions $P(X,Y) = P(Y\mid X)P(X) = P(X\mid Y)P(Y)$: **[[CovariateShift|covariate shift]]** ($P(X)$ changes, $P(Y\mid X)$ fixed), **[[LabelShift|label shift]]** ($P(Y)$ changes, $P(X\mid Y)$ fixed), and **[[ConceptShift|concept drift]]** ($P(Y\mid X)$ changes, $P(X)$ fixed). The fourth case ($P(X\mid Y)$ changes while $P(Y)$ fixed) is rarely studied.
- **Shifts are not rare.** They happen suddenly (competitor pricing changes, celebrity mentions, new-region launches, COVID-19), gradually (changing social norms, languages, industries), or seasonally (winter rideshares, holiday flight prices). Companies sometimes maintain separate models for weekday/weekend or seasonal regimes.
- **General distribution shifts include feature change and label-schema change** — adding/removing features, changing units (years → months), NaN-injecting pipeline bugs, expanding the class set (POSITIVE/NEGATIVE/NEUTRAL → adding ANGRY/SAD), or changing a credit-score range from 300–850 to 250–900. Label-schema change is especially common in high-cardinality tasks.
- **Degenerate feedback loops** occur when system outputs influence the same system's future inputs — endemic to [[RecommenderSystems|recommender systems]] and click-through-rate prediction. Detect via **popularity-diversity metrics** (aggregate diversity, long-tail coverage) and **hit-rate-vs-popularity** bucketing (Chia et al. 2021); correct via **randomization** (TikTok's initial-traffic-pool strategy) or **positional features** that encode the slot where a recommendation was shown.
- **Drift-detection methods.** Industry practice starts with summary statistics (min/max/mean/median/variance/quantiles/skewness/kurtosis), then escalates to [[HypothesisTesting|two-sample hypothesis tests]] like the **[[KolmogorovSmirnovTest|Kolmogorov–Smirnov test]]** (nonparametric, 1-D only, can produce false positives), **Least-Squares Density Difference**, and **[[MaximumMeanDiscrepancy|Maximum Mean Discrepancy]]** (kernel-based, multivariate; popular in research but rare in industry). [[AlibiDetect|Alibi Detect]] implements many of these. Reduce dimensionality before testing.
- **Heuristic for significance:** *"if you are able to detect the difference from a relatively small sample, then it is probably a serious difference. If it takes a huge number of samples to detect, then the difference is probably not worth worrying about."*
- **Time-scale windows matter.** Cumulative statistics can hide a sudden dip that sliding statistics expose (Figure 8-4). Shorter windows detect changes faster but yield more false alarms. Distinguish **spatial shifts** (new user group, new device) from **temporal shifts** (time-series).
- **Three approaches to adapt to new distributions:** (1) train on massive datasets hoping production data falls within, (2) unsupervised domain adaptation without target labels (research-heavy, rarely used in industry — Zhang et al. 2013, Zhao et al. 2020), (3) **retrain** on labeled data from the target distribution. Retraining decomposes into **stateless retraining** (from scratch) vs **stateful training** (fine-tune from last checkpoint), and into a data-window choice (last 24h vs last week vs last 6 months vs since drift started).
- **Operational metrics ≠ ML metrics.** Operational metrics (latency, throughput, request-count, 2xx %, CPU/GPU utilization, memory) measure system health; **[[ServiceLevelObjective|SLOs]] / [[ServiceLevelAgreement|SLAs]]** quantify uptime guarantees (AWS EC2 promises 99.99% — only ~4 minutes downtime/month). ML systems also need ML-specific metrics that measure *prediction quality*.
- **Four artifacts to monitor in ML, in order of pipeline depth:** raw inputs → features → predictions → accuracy-related metrics. Predictions are easiest because they are low-dimensional. **Prediction-distribution shift is a proxy for input-distribution shift** when the model weights are fixed. Predictions can also catch immediate anomalies (e.g., "all False for 10 minutes").
- **Feature monitoring** = **table testing** / unit tests for data (range checks, regex, set membership, ordering). Open-source tools: **[[GreatExpectations|Great Expectations]]** and **Deequ** (AWS). Four concerns with feature monitoring at scale: (a) compute/memory cost of summary statistics across hundreds of models × thousands of features; (b) most feature shifts are benign — alert fatigue; (c) feature extraction is multi-step, multi-library, hard to attribute a shift; (d) schemas drift unless versioned.
- **The monitoring toolbox is three tools, not three pillars:** **logs**, **dashboards**, **alerts**. Stream-process logs (via [[ApacheKafka|Kafka]] / [[Kinesis|Kinesis]] / KSQL / Flink SQL) for real-time anomaly detection rather than batch (Spark/Hadoop/Hive). Each alert needs a *policy* + *notification channel* + *actionable description / runbook*. *"Alert fatigue is a real phenomenon"* — desensitization causes critical alerts to be missed.
- **Observability strictly contains monitoring.** Monitoring tracks external outputs to detect when something is wrong; observability instruments the system so the internal state can be inferred from those outputs without shipping new code. In ML, **observability encompasses [[Interpretability|interpretability]]** — knowing *which feature* contributed most to last hour's wrong predictions, not just *that* the model is degrading.

## Key Quotes

> "Deploying a model isn't the end of the process. A model's performance degrades over time in production." — opening framing of the chapter

> "Sixty out of these 96 failures happened due to causes not directly related to ML… ML engineering is mostly engineering, not ML." — citing Papasian & Underwood (Google, 2020)

> "Outliers refer to data: an example that differs significantly from other examples. Edge cases refer to performance: an example where a model performs significantly worse than other examples." — disambiguating two often-confused terms

> "A degenerate feedback loop is created when a system's outputs are used to generate the system's future inputs, which, in turn, influence the system's future outputs." — the canonical definition, illustrated with song-ranking and resume-screening

> "In his estimate, 80% of the drifts captured by his service are caused by human errors." — a monitoring-vendor CTO, on the gap between alleged data shift and actual pipeline bugs

> "If you are able to detect the difference from a relatively small sample, then it is probably a serious difference. If it takes a huge number of samples to detect, then the difference is probably not worth worrying about." — practical heuristic for two-sample tests

> "Monitoring makes no assumption about the relationship between the internal state of a system and its outputs… Observability makes an assumption stronger than traditional monitoring: that the internal states of a system can be inferred from knowledge of its external outputs." — the monitoring-vs-observability distinction

> "If it moves, we track it." — Ian Malpass (Etsy), the logging maximalist credo Huyen quotes; Etsy "also track[s] things that haven't changed yet, in case they'll move later"

## Connections

- [[ChipHuyen]] — author of *Designing ML Systems*; later wrote *AI Engineering* (2024).
- [[OReilly]] — publisher.
- [[DesigningMachineLearningSystems]] — the parent book this chapter belongs to.
- [[DistributionShift]] — the umbrella concept this chapter formalizes; existing wiki page already cites the same $P(X,Y)$ decomposition.
- [[CovariateShift]] — $P(X)$ changes, $P(Y\mid X)$ fixed; chapter gives the breast-cancer-age and free-to-paid-conversion examples.
- [[LabelShift]] — $P(Y)$ changes, $P(X\mid Y)$ fixed; the chapter notes label-shift adaptation methods mirror covariate-shift methods.
- [[ConceptShift]] / [[ConceptDrift]] — $P(Y\mid X)$ changes; the chapter's COVID-era San Francisco housing-price example.
- [[DataDrift]] / [[TargetDrift]] / [[DriftDetection]] — operational sibling concepts for the production-monitoring side of distribution shift.
- [[TrainingServingSkew]] — the train-vs-serve divergence Huyen names as a common failure mode.
- [[EdgeCase]] / [[Outlier]] — the data-vs-performance distinction Huyen draws sharply.
- [[DegenerateFeedbackLoop]] / [[FeedbackLoop]] — chapter is the canonical pre-LLM treatment; complements the LLM-era treatment in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]].
- [[FirstPositionBias]] / [[PositionBias]] — the positional-feature mitigation the chapter proposes for recommender feedback loops.
- [[RecommenderSystems]] — primary domain for degenerate feedback loops, popularity bias, exposure bias.
- [[ExplicitFeedback]] / [[ImplicitFeedback]] — the feedback substrate that loops corrupt.
- [[HypothesisTesting]] — the inferential frame for two-sample drift tests.
- [[KolmogorovSmirnovTest]] — the canonical 1-D nonparametric two-sample test Huyen recommends with caveats.
- [[MaximumMeanDiscrepancy]] — kernel-based multivariate two-sample test; "popular in research, but… not aware of any company that is using it in the industry."
- [[KernelDensityEstimation]] / [[KernelFunction]] — mathematical machinery underpinning MMD and density-ratio importance weighting.
- [[ImportanceWeighting]] — the standard remedy for known covariate shifts; chapter describes the two-step density-ratio estimation procedure.
- [[KernelTrick]] — kernel embedding of conditional/marginal distributions in Zhang et al. (2013)'s unsupervised adaptation.
- [[DomainAdaptation]] / [[TransferLearning]] — chapter explicitly frames distribution-shift adaptation as a special case of these.
- [[ActiveLearning]] — Huyen notes active learning *induces* covariate shift as a by-product.
- [[UnsupervisedLearning]] / [[SupervisedLearning]] — chapter notes the unsupervised-domain-adaptation research thread.
- [[FineTuning]] — the "stateful retraining" half of the retraining-strategy decision.
- [[ContinualLearning]] — the active counterpart to passive monitoring (chapter explicitly hands off to Ch 9 on this).
- [[Monitoring]] / [[observability]] / [[ModelMonitoring]] / [[PromptMonitoring]] / [[UsagePatternMonitoring]] / [[DataObservability]] — the second half of the chapter is a foundational treatment for all of these.
- [[Logging]] / [[StructuredLogging]] / [[PythonLogging]] — the logs pillar of the monitoring toolbox.
- [[RootCauseAnalysis]] — chapter mentions advanced monitoring platforms attempting automatic RCA across time-window sizes.
- [[F1Score]] / [[Latency]] / [[InstructionThroughput]] / [[CostAndLatency]] — operational and ML metrics referenced.
- [[MicroservicesArchitecture]] — context for distributed tracing and the "20–30 hops per request" point.
- [[MLOps]] — the operational discipline this chapter materially defines, predating widespread "MLOps" usage.
- [[GoogleCloudMLOpsReference]] — adjacent ops-reference page in the wiki.
- [[DataPipeline]] / [[FeatureEngineering]] / [[FeatureStore]] — the artifacts Huyen describes monitoring.
- [[MapReduce]] / [[Hadoop]] / [[ApacheSpark]] / [[ApacheHive]] / [[ApacheFlink]] / [[ApacheKafka]] / [[Kinesis]] — the batch- and stream-processing infrastructures Huyen names for log analytics.
- [[AlibiDetect]] — chapter calls out as "a great open source package" implementing many drift-detection algorithms.
- [[GreatExpectations]] — feature-validation tool Huyen names as canonical.
- [[TensorFlow]] — TFX's data-validation is critiqued as relying only on summary statistics.
- [[AmazonCloudWatch]] / [[AmazonEC2]] — referenced for SLA examples and alerting endpoints.
- [[Slack]] — example notification channel.
- [[google]] / [[Amazon]] — vendors whose internal/external systems the chapter draws on.

## Contradictions

None. The chapter aligns with the wiki's existing [[DistributionShift]] page (same $P(X,Y)$ decomposition and same three-subtype taxonomy) and with [[DegenerateFeedbackLoop]] (the *AI Engineering* Ch 10 treatment is a foundation-model-era restatement of this chapter's pre-LLM material — Huyen is the same author). A subtle terminology nuance: this chapter uses **"concept drift"** as the label for $P(Y\mid X)$ change, while the wiki has separate [[ConceptDrift]] and [[ConceptShift]] pages; both terms refer to the same phenomenon and Huyen treats them as synonyms ("Concept drift, also known as posterior shift").
