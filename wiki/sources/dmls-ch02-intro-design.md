---
title: "Designing ML Systems — Ch 2: Introduction to Machine Learning Systems Design"
type: source
tags: [book, dmls, ml-systems-design, mlops, oreilly, designing-ml-systems]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch02-intro-design.txt
last_updated: 2026-05-23
---

# Designing ML Systems — Ch 2: Introduction to Machine Learning Systems Design

## Summary

Chapter 2 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly Media]], 2022) lays the conceptual foundation for the rest of the book by walking through four pillars of [[MLOps|ML systems design]]: (1) translating **business objectives** into **ML objectives**, (2) the four cross-cutting **system requirements** — reliability, scalability, maintainability, and adaptability, (3) the **iterative six-step process** for building production ML systems, and (4) **framing ML problems** in terms of inputs, outputs, and objective functions. The chapter closes with the "mind vs data" philosophical debate — whether progress comes from cleverer architectures or simply more data — and lands on the practitioner's verdict that, for now, [[DataQuality|data quality and quantity]] dominate (citing [[AlexNet]], [[bert|BERT]], and [[GPT|GPT]] as evidence). Huyen repeatedly emphasizes that most ML projects fail not because the model is wrong but because the **problem framing**, **metric mapping**, or **organizational requirements** were wrong. The chapter functions as the design-level scaffolding for everything from data engineering (Ch 3-4) through deployment (Ch 7) and continual learning (Ch 9).

## Key Claims

- **Business metrics — not ML metrics — decide an ML project's fate.** Companies don't care about moving accuracy from 94% to 94.2% unless that move maps to revenue, conversion, retention, or cost savings; data scientists who optimize ML metrics in isolation see their projects killed by managers who only see [[BusinessMetric|business metrics]].
- **Click-through-rate prediction and fraud detection dominate industrial ML adoption** precisely because each marginal ML improvement maps cleanly to dollars (ad revenue, money saved on prevented fraud) — see [[CTRPrediction]].
- **Companies invent intermediate metrics to bridge ML and business.** [[Netflix]] uses **take-rate** (quality plays / recommendations shown), then verifies that take-rate correlates with total streaming hours and lower cancellation rates — a worked example of metric-laddering.
- **Returns on ML investment compound with maturity.** Per a 2020 Algorithmia survey, ~75% of companies with 5+ years of production ML can deploy a new model in under 30 days, versus 60% of newcomers needing more than 30 days; the payoff curve is years-long, not overnight.
- **Four cross-cutting requirements define a good ML system**: [[Reliability]], [[Scalability]], [[Maintainability]], and [[Adaptability]]. These are borrowed from software-systems thinking but specialized: e.g., "correctness" for ML is hard to verify without ground-truth labels, and ML systems can **fail silently** (a mistranslation looks fine to a user who doesn't know the target language).
- **Scalability has two distinct axes**: **resource scaling** (autoscaling GPUs/CPUs up and down with traffic) and **artifact management** (managing 1 model vs. 1,000 models — one startup managed 8,000 per-customer models). Autoscaling is hard: Amazon's Prime Day autoscaling failure cost an estimated $72-99M per downtime hour.
- **Maintainability is fundamentally an organizational concern** — ML engineers, DevOps engineers, and subject-matter experts (SMEs) bring different languages and tools; infrastructure must let each contributor work in their preferred stack while keeping code, data, and artifacts versioned and reproducible.
- **Adaptability requires online updateability.** ML systems are "part code, part data," and data drifts ([[DataDrift]], [[LabelShift]]); the system needs hooks for [[continuallearning|continual learning]] and update-without-service-interruption.
- **The ML development workflow is a cycle, not a pipeline.** Huyen's worked ad-targeting example shows 13 steps with multiple loops back to step 1 (relabeling, fixing class imbalance, model staleness, switching the optimization target from impressions to click-through rate).
- **Six canonical lifecycle steps**: project scoping → data engineering → ML model development → deployment → monitoring & continual learning → business analysis (which feeds back to scoping). Each maps to subsequent chapters of the book.
- **An ML problem is defined by three components**: inputs, outputs, and an objective function. A business request ("speed up customer support") is **not** an ML problem until those three are specified — the engineer's job is to do the framing.
- **Problem framing dominates difficulty.** The "next-app prediction" example: framed as multiclass classification, adding a new app requires retraining the model; reframed as regression (input = user + environment + app features, output = a single likelihood scalar), new apps are zero-cost additions.
- **High-cardinality classification (thousands of classes)** suffers a data-collection bottleneck — ML models typically need ≥100 examples per class to learn it, so 1,000 classes implies ≥100k examples, with rare classes especially starved. **Hierarchical classification** (classify into a coarse group first, then a sub-classifier within that group) is the standard mitigation.
- **Multilabel classification is the trickiest task type** — it amplifies label-multiplicity disagreements between annotators and makes converting raw probabilities into predicted label sets non-obvious (no fixed top-k rule).
- **Most ML engineers don't design loss functions** — they pick standard ones: [[CrossEntropy]] for multiclass classification, log loss for binary, [[MeanSquaredError|RMSE]] or MAE for regression. Designing a loss requires algebra-level fluency.
- **Decouple competing objectives into separate models when possible.** Ranking news-feed posts for "quality_score" and "engagement_score" should be two models whose outputs are linearly combined (α·quality + β·engagement) — this lets product teams retune α and β without retraining. The alternative ([[ParetoOptimization|Pareto optimization]] over a single weighted loss) requires retraining on every reweighting and conflates maintenance schedules (spam filters need weekly updates; quality models need monthly).
- **The "mind vs data" debate is unresolved but data is currently winning.** [[JudeaPearl|Pearl]] and [[ChristopherManning|Manning]] argue for structure and inductive biases; [[RichardSutton|Sutton]]'s "Bitter Lesson" and [[PeterNorvig|Norvig]] ("we don't have better algorithms, we just have more data") argue for scale. Dataset sizes for language models grew from ~0.8B tokens (One Billion Word Benchmark, 2013) to 10B ([[GPT2]], 2019) to 500B ([[GPT3]], 2020).
- **More data does not always help — quality matters.** Outdated data or data with incorrect labels can actively hurt model performance; the right framing is finite-but-high-quality data, not infinite data.

## Key Quotes

> "Most companies don't care about the fancy ML metrics. They don't care about increasing a model's accuracy from 94% to 94.2% unless it moves some business metrics." — on the business-vs-ML metric gap

> "Magically: possible. Overnight: no." — Huyen's verdict on ML hype and realistic timelines for ROI

> "With traditional software systems, you often get a warning, such as a system crash or runtime error or 404. However, ML systems can fail silently." — the [[SilentModelUpdate|silent-failure]] thesis for ML reliability

> "Slow customer support is a problem, but it's not an ML problem. An ML problem is defined by inputs, outputs, and the objective function that guides the learning process." — the framing manifesto

> "Data is profoundly dumb." — [[JudeaPearl|Judea Pearl]], quoted from *The Book of Why*, representing the mind-over-data camp

> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin." — [[RichardSutton|Rich Sutton]], "The Bitter Lesson," quoted as the data-over-mind position

> "We don't have better algorithms. We just have more data." — [[PeterNorvig|Peter Norvig]], on why Google Search works

> "Developing an ML system is like writing — you will never reach the point when your system is done. But you do reach the point when you have to put your system out there." — on deployment as the only finish line

## Connections

- [[ChipHuyen]] — author of the book; this chapter is the design-level scaffolding for her later [[ai-engineering-chip-huyen|AI Engineering book]].
- [[DesigningMachineLearningSystems]] — parent book; *new* page needed.
- [[OReilly]] — publisher.
- [[MLOps]] — the umbrella discipline; this chapter is the design-thinking layer of MLOps.
- [[BusinessMetric]] — the business-side metrics ML must move; this chapter is the canonical reference for how to map ML metrics to business metrics.
- [[Reliability]] — *new* concept page needed; one of the four requirements.
- [[Scalability]] — *new* concept page needed; covers both resource scaling and artifact management.
- [[Maintainability]] — *new* concept page needed; organizational and reproducibility concerns.
- [[Adaptability]] — *new* concept page needed; tied to [[continuallearning]] and [[DataDrift]].
- [[Autoscaling]] — directly referenced; the Prime-Day failure anecdote.
- [[DistributedTraining]] — chapter forward-references this as a resource-scaling technique.
- [[Reproducibility]] — required for maintainability when scaling to many models.
- [[Versioning]] — code/data/artifact versioning as maintainability prerequisite.
- [[ExperimentTracking]] — artifact-management aspect of scalability.
- [[DevOps]] — one of the three contributor roles in ML maintainability.
- [[continuallearning|Continual Learning]] — adaptability requirement; tied to [[DataDrift]] and [[LabelShift]].
- [[Monitoring]] — production-side requirement of adaptability; deferred to Ch 8.
- [[SilentModelUpdate]] — related to the silent-failure thesis for ML reliability.
- [[FeatureEngineering]] — step 3 of the iterative process; covered in Ch 5.
- [[ModelSelection]] — step 3 of the iterative process; covered in Ch 6.
- [[DataAnnotation]] / [[AnnotationGuidelines]] — label-multiplicity problem in multilabel classification.
- [[DataQuality]] — the "more data can hurt" warning; ties into the mind-vs-data debate.
- [[Classification]] — the dominant task type in industrial ML.
- [[Regression]] — alternative framing that often makes problems easier (next-app example).
- [[BinaryClassification]] — *new* concept page needed.
- [[MulticlassClassification]] — *new* concept page needed.
- [[MultilabelClassification]] — *new* concept page needed; the trickiest task type per Huyen.
- [[HierarchicalClassification]] — *new* concept page needed; mitigation for high-cardinality classification.
- [[HighCardinalityClassification]] — *new* concept page needed; the ≥100 examples/class heuristic.
- [[ProblemFraming]] — *new* concept page needed; inputs/outputs/objective triple.
- [[ObjectiveFunction]] — *new* concept page needed; aka loss function in ML.
- [[CrossEntropy]] — standard loss for multiclass classification per Huyen.
- [[CrossEntropyLoss]] — the loss-function formulation.
- [[MeanSquaredError]] — RMSE/MAE for regression problems.
- [[LossFunction]] — *new* concept page needed; synonym for objective function in ML.
- [[ParetoOptimization]] — multi-objective optimization framing for the news-feed example.
- [[DecoupleObjectives]] — *new* concept page needed; the practitioner pattern of training separate per-objective models.
- [[CTRPrediction]] — canonical example of clean ML-to-business mapping.
- [[FraudDetection]] — *new* concept page needed; the other canonical clean-mapping example.
- [[SpamDetection]] — *new* concept page needed; binary-classification archetype.
- [[ContentModeration]] — *new* concept page needed; the NSFW / misinformation filtering layer.
- [[RecommenderSystems]] — Netflix take-rate, news-feed ranking examples.
- [[ABTesting]] — how companies test whether ML metrics actually move business metrics.
- [[BatchInference]] / [[OnlineInference]] — the ecommerce-recommender framing example.
- [[F1Score]] — easier to compute for binary than multiclass classification.
- [[Accuracy]] — the canonical ML metric used in the 94%→94.2% anecdote.
- [[Latency]] — inference latency as one of the standard ML metrics.
- [[GPU]] — resource-scaling unit; the 10-vs-100 GPU example.
- [[LanguageModel]] — the One Billion Word Benchmark→GPT-3 data-size growth example.
- [[AlexNet]] — cited as proof that data-scale wins; the data-camp evidence.
- [[bert|BERT]] — cited alongside AlexNet and GPT as the data-camp evidence.
- [[GPT2]] — 10B-token dataset milestone in the dataset-size growth curve.
- [[GPT3]] — 500B-token dataset milestone.
- [[NetflixPrize]] — Netflix is the take-rate case study source.
- [[google|Google]] — Norvig's "more data, not better algorithms" quote; decades of ML investment.
- [[Amazon]] — Prime Day autoscaling failure anecdote.
- [[OpenAI|openai]] — GPT-2 and GPT-3 dataset-size milestones.
- [[googledeepmind|DeepMind]] — Richard Sutton's affiliation.
- [[PeterNorvig]] — quoted in the data-over-mind camp.
- [[JudeaPearl]] — *new* entity page needed; mind-over-data champion; Turing Award winner; author of *The Book of Why*; causal inference and Bayesian networks pioneer.
- [[RichardSutton]] — *new* entity page needed; "The Bitter Lesson" author; University of Alberta + DeepMind.
- [[ChristopherManning]] — *new* entity page needed; director of Stanford AI Lab; structure-over-scale advocate.
- [[MonicaRogati]] — *new* entity page needed; former VP of Data at Jawbone; author of "The AI Hierarchy of Needs."
- [[MiltonFriedman]] — *new* entity page needed; quoted on "sole purpose of business is to maximize shareholder profits."
- [[Algorithmia]] — *new* entity page needed; 2020 State of Enterprise ML survey source.
- [[stanforduniversity|Stanford University]] — Manning's institutional home; Huyen previously taught here.
- [[UniversityOfAlberta]] — *new* entity page needed; Sutton's institutional home.

## Contradictions

- **None** with the existing wiki corpus. The chapter sets up the design framework on which later DMLS chapters (and the spiritual successor *AI Engineering*) build; existing wiki entries on [[MLOps]], [[BusinessMetric]], [[continuallearning]], [[DataDrift]], [[ABTesting]], [[CTRPrediction]], and [[ParetoOptimization]] all align with Huyen's treatment here. The chapter sharpens (but does not contradict) the [[ChipHuyen]] entity page's positions, which were derived from her later *AI Engineering* book.
- **Internal tension flagged, not a wiki contradiction**: Huyen presents the mind-vs-data debate as live and undecided, then explicitly lands on "data is essential, for now" — practitioners reading this chapter alongside the [[ChinchillaScalingLaw]] / [[scalinglaws]] entries should note that the data-camp position has been further refined post-2022 (compute-optimal, not just maximum, data is now the consensus).
