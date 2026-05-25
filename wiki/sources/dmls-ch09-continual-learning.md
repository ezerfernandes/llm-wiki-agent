---
title: "Designing ML Systems — Ch 9: Continual Learning and Test in Production"
type: source
tags: [book-chapter, dmls, continual-learning, mlops, deployment, ab-testing, bandits, streaming, monitoring]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch09-continual-learning.txt
last_updated: 2026-05-23
---

## Summary
Chapter 9 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly]], 2022) argues that adapting ML models to data distribution shifts is fundamentally an **infrastructural** problem rather than an algorithmic one. Huyen distinguishes **stateless retraining** (training from scratch each cycle) from **stateful training** (incremental fine-tuning that continues from the last checkpoint), and lays out a **four-stage maturity model** for moving from manual ad-hoc retraining to fully automated, trigger-driven continual learning. She then tackles the perennial question "how often should I retrain?" by reframing it as a measurable question about the value of data freshness, and devotes the second half of the chapter to **test in production** — shadow deployment, A/B testing, canary release, interleaving experiments, and multi-armed bandits — as the complement to passive monitoring. The chapter's central thesis is that continual learning is a superset of batch learning that unlocks use cases like sudden distribution shift, rare events (Black Friday), and the continuous cold-start problem, but its viability depends on streaming infrastructure, fresh-label pipelines, and a disciplined evaluation regime.

## Key Claims
- **Continual learning means stateful, micro-batch updates — not per-sample online learning.** Per-sample updates cause catastrophic forgetting and waste batch-oriented hardware; production systems update on micro-batches of 512–1,024 examples with task-dependent sizing.
- **Stateless retraining vs. stateful training is the load-bearing distinction.** Stateless retrains from scratch on a long window of data; stateful continues training from the last checkpoint on only the new data. Grubhub reported a **45× reduction in training compute and 20% lift in purchase-through rate** after switching from daily stateless retraining to daily stateful training.
- **Stateful training can eliminate the need to store training data.** Because each sample is used only once, this property has under-appreciated implications for privacy-constrained domains.
- **Model iteration ≠ data iteration.** Stateful training applies primarily to data iteration (same architecture/features, fresh data). Architecture or feature changes still require training from scratch, though *knowledge transfer* and OpenAI's *model surgery* hint at future bypasses.
- **The champion/challenger pattern.** Updated replicas (challengers) are evaluated against the deployed champion before any swap; real production systems run multiple challengers simultaneously.
- **Continual learning is justified by four scenarios:** sudden distribution shifts (Lyft surge pricing), rare events (Alibaba Singles Day, Black Friday), the **continuous cold-start problem** (Coveo: >70% of e-commerce shoppers visit fewer than three times a year), and intra-session personalization (TikTok adapting within minutes).
- **The three core challenges are infrastructural.** (1) Fresh-data access often requires streaming from [[ApacheKafka|Kafka]]/Kinesis rather than waiting for warehouse deposits; (2) fresh-label generation requires extracting natural labels from user behavior logs (label computation) via stream processing; (3) algorithm fit — matrix- and tree-based models adapt poorly to incremental updates compared to neural networks.
- **Hoeffding Tree and variants exist** for incremental tree-based learning but are not widely adopted; sklearn's `StandardScaler.partial_fit` and online quantile algorithms address feature-scaling statistics under streaming.
- **The four-stage maturity model.** Stage 1: manual, stateless retraining (the majority of non-tech companies). Stage 2: automated retraining via a script + scheduler ([[Airflow]]/[[ArgoWorkflows|Argo]]) + [[FeatureStore|feature store]] + [[ModelRegistry|model store]]. Stage 3: automated stateful training (mindset shift + model-and-data lineage tracking). Stage 4: continual learning with triggers (time, performance, volume, drift) and the "holy grail" of on-device continual learning at the edge.
- **"Log and wait"** reuses features already extracted by the prediction service for retraining, reducing compute and combating [[TrainingServingSkew|train-serving skew]]; Faire popularized the pattern.
- **Retraining frequency is an empirical question.** Train versions of the model on different past time windows and evaluate on today's data to quantify the gain from freshness. Facebook (2014) found a 1% loss reduction switching ad CTR retraining from weekly to daily.
- **Backtests on the most recent data are necessary but not sufficient.** Static test splits remain a sanity check; only deployment reveals real-world behavior — hence "test in production."
- **Five techniques for test in production.** (1) **Shadow deployment** — safest, doubles inference cost. (2) **A/B testing** — gold standard but requires truly random traffic and sufficient samples; Microsoft and Google each ran >10,000 A/B tests/year as of 2017. (3) **Canary release** — gradual traffic rollout, can implement A/B but doesn't require randomization. (4) **Interleaving experiments** — for ranking systems; team-draft interleaving fairly mixes recommendations from two models, identifying winners with much smaller sample sizes than A/B (Netflix). (5) **Multi-armed bandits** — stateful traffic routing that balances exploration and exploitation; in Greg Rafferty's experiment, Thompson Sampling needed <12,000 samples vs. >630,000 for A/B testing at the same confidence.
- **Contextual bandits** address the *partial feedback* problem in recommendations/ads — deciding which arms (items/ads) to expose given user context, balancing exploitation with the exploration needed to learn unseen items' value. They are harder to implement because the exploration strategy depends on model architecture.
- **Continual learning amplifies failure risk.** Tay (Microsoft, 2016) is the cautionary tale: trolls coordinated to poison an online-learning chatbot, forcing shutdown within 16 hours. More frequent updates mean more opportunities for catastrophic update + greater susceptibility to adversarial manipulation.
- **Evaluation latency is a bottleneck on update frequency.** A payment-fraud system Huyen worked with could only retrain every two weeks because that was how long A/B testing took to accumulate enough rare-event (fraud) samples for statistical significance.
- **Continual learning requires team ownership of the evaluation pipeline.** Ad-hoc, data-scientist-owned evaluation produces biased and variable results; pipelines should be codified, automated, and reviewed like CI/CD.

## Key Quotes
> "Continual learning isn't about the retraining frequency, but the manner in which the model is retrained." — Huyen's reframing that defuses the "every 5 minutes?" caricature; the real axis is stateless vs. stateful.

> "Going from daily stateless retraining to daily stateful training reduced their training compute cost 45 times and increased their purchase-through rate by 20%." — Grubhub's empirical case for [[StatefulTraining|stateful training]] (Alex Egg, "Online Learning for Recommendations at Grubhub," 2021).

> "The biggest challenge of continual learning isn't in writing a function to continually update your model — you can do that by writing a script! The biggest challenge is in making sure that this update is good enough to be deployed." — locates the actual difficulty in evaluation infrastructure, not training code.

> "As soon as Tay launched, trolls started tweeting the bot racist and misogynist remarks. The bot soon began to post inflammatory and offensive tweets, causing Microsoft to shut down the bot 16 hours after its launch." — the canonical adversarial-data failure mode for online learning.

> "The only way to know whether a model will do well in production is to deploy it. This insight led to one seemingly terrifying but necessary concept: test in production." — the chapter's pivot from offline to online evaluation.

> "A/B testing required over 630,000 samples to get a confidence interval of 95%, whereas a simple bandit algorithm (Thompson Sampling) determined that a model was 5% better than the other with less than 12,000 samples." — citing Greg Rafferty; the data-efficiency case for bandits.

> "The holy grail is when you combine continual learning with edge deployment. ... There will be no need for a centralized server, which means no centralized server cost. ... no need to transfer data back and forth between device and cloud, which means better data security and privacy!" — Huyen's forward-looking frame for stage 4+.

> "A good evaluation process involves not only what tests to run but also who should run those tests." — closing argument against data-scientist-owned, ad-hoc evaluation.

## Connections
- [[continuallearning]] — primary concept; this chapter is the canonical practitioner-oriented exposition. The existing wiki page is currently AI-Engineering-flavored; Ch 9 adds the stateful-vs-stateless distinction and four-stage maturity model.
- [[CatastrophicForgetting]] — the failure mode that rules out per-sample online learning for neural networks; Huyen cites this as the first reason for micro-batch updates.
- [[FineTuning]] — Huyen explicitly equates stateful training with fine-tuning / incremental learning.
- [[DistributionShift]] / [[DataDrift]] — continual learning is the response to these phenomena from Ch 8.
- [[Monitoring]] / [[ModelMonitoring]] — passive complement to test in production; both feed the trigger mechanisms in stage 4.
- [[ABTesting]] — covered in depth here; the default online-evaluation technique against which alternatives are measured.
- [[HypothesisTesting]] — A/B testing's statistical foundation (two-sample tests, p-values).
- [[ShadowDeployment]] — safest test-in-production technique; cost is doubled inference.
- [[CanaryDeployment]] — gradual rollout pattern; can implement A/B testing.
- [[MultiArmedBandits]] — Ch 9 introduces bandits-for-model-evaluation as a more data-efficient alternative to A/B testing.
- [[EpsilonGreedy]] — the simplest bandit exploration strategy named in the chapter.
- [[ExplorationExploitation]] — the foundational trade-off underlying bandits and contextual bandits.
- [[ThompsonSampling]] — named exploration algorithm; Rafferty's data-efficiency benchmark.
- [[UpperConfidenceBound]] — the sibling exploration algorithm Huyen pairs with Thompson Sampling.
- [[ContextualBandits]] — Ch 9's preferred terminology for exploration strategies that determine the payout of predictions/actions.
- [[InterleavingExperiments]] — Netflix-popularized ranker comparison via team-draft interleaving (Joachims 2002).
- [[ChampionChallengerPattern]] — production pattern for evaluating updated replicas before promotion.
- [[StatefulTraining]] / [[StatelessRetraining]] — the core dichotomy of the chapter.
- [[ModelIteration]] vs. [[DataIteration]] — Huyen's distinction between architecture/feature changes and data refresh.
- [[ContinuousColdStart]] — generalization of the cold-start problem to existing users (different device, infrequent visits).
- [[NaturalLabels]] — labels extracted from user behavior (clicks, ride completions), key to fresh-label pipelines.
- [[LabelComputation]] — the process of mining logs to construct labels from behavioral events.
- [[FeatureReuseLogAndWait]] — Faire's pattern for reusing prediction-time features at training time.
- [[TrainingServingSkew]] — what log-and-wait aims to reduce.
- [[ModelStore]] / [[ModelRegistry]] — required infrastructure for stage 2+; Huyen names [[AmazonSageMaker|SageMaker]] and [[MLflow]] as exemplars.
- [[ModelLineage]] / [[DataLineage]] — stage 3 prerequisite for reproducing checkpoints in a stateful retraining tree.
- [[FeatureStore]] — implicitly required for consistent online/offline feature serving.
- [[Airflow]] / [[ArgoWorkflows|Argo]] / [[Scheduler]] / [[Orchestrator]] — the schedulers that drive stage-2 retraining pipelines.
- [[ApacheKafka|Kafka]] / [[ApacheFlink|Flink]] / Kinesis — real-time transports for streaming-first ML.
- [[StreamProcessing]] — Huyen's preferred approach for fast label computation.
- [[Snorkel]] — named as a programmatic-labeling tool for accelerating fresh-label generation.
- [[HoeffdingTree]] — incremental tree-based learner Huyen names; foundational citation Domingos & Hulten 2000.
- [[CollaborativeFiltering]] / [[MatrixFactorization]] — examples of models that adapt poorly to continual updates.
- [[FeatureScaling]] — running statistics (mean, variance) must be computed online for streaming retraining; sklearn `StandardScaler.partial_fit` named.
- [[OnlineEvaluation]] / [[OfflineEvaluation]] — Ch 9 is the online-evaluation companion to Ch 6's offline-evaluation chapter.
- [[Backtest]] — Huyen's term for evaluating on the most recent data window.
- [[CTRPrediction]] — Facebook's data-freshness case study (2014).
- [[RecommenderSystems]] — the canonical home of natural labels, bandits, interleaving, and contextual bandits.
- [[EdgeML]] / [[OnDeviceLearning]] — the "holy grail" combination of continual learning with edge deployment.
- [[MLOps]] — the broader discipline within which Ch 9's infrastructure prescriptions sit.
- [[ChipHuyen]] — author entity; this chapter pairs naturally with her later *AI Engineering* (2024) coverage.
- [[OReilly]] — publisher of *Designing Machine Learning Systems* (2022).
- [[Grubhub]] — case study: 45× compute reduction via stateful training.
- [[Lyft]] — case study: dynamic-pricing shift response.
- [[TikTok]] — case study: within-session continual personalization.
- [[Alibaba]] — case study: Singles Day recommendations + Data Artisans / [[ApacheFlink]] acquisition.
- [[Coveo]] — case study source for the 70% infrequent-shopper statistic motivating continuous cold start.
- [[Netflix]] — case study: interleaving experiments + automated canary analysis.
- [[Microsoft]] — case study: Tay chatbot failure; A/B testing volume.
- [[Google]] — A/B testing volume; automated canary analysis; knowledge-transfer citation.
- [[OpenAI]] — *Neural Network Surgery* (2019) cited as a model-iteration bypass.
- [[Facebook]] — 2014 ad-CTR data-freshness study.
- [[Faire]] — log-and-wait pattern.
- [[StitchFix]] — Stefan Krawczyk quote on where engineering time goes in stage 2.
- [[Confluent]] — streaming infrastructure exemplar named by Huyen.
- [[Materialize]] — streaming SQL database named by Huyen.
- [[Snowflake]] — streaming team mentioned (2020).
- [[ApacheFlink]] / [[DataArtisans]] — Alibaba's $103M acquisition for streaming ML.
- [[ai-engineering-chip-huyen]] — Huyen's 2024 follow-up book; this chapter is the ML-systems predecessor's deepest coverage of online learning and continual training.
- [[1409.3215-seq2seq]] / [[1706.03762-attention-is-all-you-need]] — modern neural-network architectures that are amenable to stateful training because of their gradient-based, mini-batch nature (contrast with matrix/tree models in Ch 9).

## Contradictions
- **Definition of continual learning vs. existing `[[continuallearning]]` concept page.** The current wiki page (drawn from *AI Engineering* and Xu et al.) treats continual learning primarily as a weight-update paradigm in tension with in-context-learning-as-CL. Huyen's Ch 9 frames it more broadly as **infrastructure for fast model updates, whether stateless or stateful**, and explicitly distinguishes "online learning" (per-sample) as a special case. The two framings are compatible but emphasize different axes; the concept page should be expanded to include Huyen's stateless-vs-stateful and four-stage taxonomy.
- **Terminology: "continuous" vs. "continual" learning.** Huyen actively recommends abandoning "continuous learning" because it conflates the DevOps pipeline sense (continuous delivery of ML) with the ML training sense. No existing wiki page surfaces this distinction; ingesting this chapter introduces a potential terminology cleanup item rather than a contradiction with prior content.
