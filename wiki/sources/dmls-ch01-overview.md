---
title: "Designing ML Systems — Ch 1: Overview of Machine Learning Systems"
type: source
tags: [book, dmls, mlops, ml-systems, production, chip-huyen, oreilly]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch01-overview.txt
last_updated: 2026-05-23
---

## Summary
Chapter 1 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly Media]], 2022) frames an ML system as far more than the algorithm: business requirements, the user/developer interface, the data stack, the model development/monitoring/update logic, and the underlying infrastructure are all first-class components. The chapter defines [[MLOps|MLOps]] as the operational descendant of DevOps, and ML systems design as the holistic-systems approach to MLOps. It enumerates the conditions under which ML is the right tool — learnable patterns, available data, predictive framing, repetitive tasks, tolerable wrong-prediction costs, scale, and shifting distributions — and surveys consumer and enterprise use cases. It closes by contrasting ML in research vs. ML in production along five axes (stakeholders, computational priority, data, fairness, interpretability) and contrasting ML with traditional software engineering, where the assumption that code and data are separate breaks down.

## Key Claims
- **An ML system is not just the algorithm.** The "algorithm" (e.g. [[LogisticRegression|logistic regression]] or a neural network) is only one component; the production system also includes business requirements that motivated the project, the user/developer interface, the data stack, the develop/monitor/update logic, and the infrastructure that delivers all of it.
- **MLOps = DevOps for ML; ML systems design = holistic-systems view of MLOps.** "Ops" in [[MLOps|MLOps]] comes from DevOps; operationalizing means deploying, monitoring, and maintaining. ML systems design ensures all components and stakeholders work together toward the specified objectives.
- **ML is "an approach to (1) learn (2) complex patterns from (3) existing data and use these patterns to make (4) predictions on (5) unseen data."** This five-keyphrase framing structures the chapter's "when to use ML" discussion.
- **ML needs patterns to learn.** A fair die has no pattern to predict; a lookup table from zip code to state needs no ML. ML is justified only when the pattern is complex enough that manual specification is infeasible — hence Andrej Karpathy's framing of ML as [[SoftwareTwo|"Software 2.0"]], where patterns are learned from data instead of hand-coded.
- **What is complex differs for humans vs. machines.** Raising a number to the 10th power is trivial for a machine and hard for humans; detecting a cat in a picture is the reverse. [[ObjectDetection|Object detection]] and [[SpeechRecognition|speech recognition]] are canonical "complex-for-machines" wins.
- **"Existing data" can be relaxed via zero-shot or continual learning, but data is still required somewhere.** [[ZeroShotLearning|Zero-shot learning]] (a.k.a. zero-data learning) makes predictions for a task without task-specific data — but only because the model was trained on related tasks. [[continuallearning|Continual learning]] lets a model be deployed with no prior training and learn from incoming production traffic, at the cost of poor early customer experience. A common workaround is the "fake-it-til-you-make-it" approach: serve human predictions first, then train on the generated data.
- **Reframing problems as prediction is a general lever.** Any question can be cast as "what would the answer to this question be?" Even compute-intensive deterministic problems (image denoising, screen-space shading) can be approximated by ML models for cheap, approximate predictions at scale.
- **Unseen data must share the training distribution.** Out-of-distribution behavior is the dominant failure mode in production; a 2008-trained app-download model fails on 2020 traffic. Monitoring and testing-in-production are the production-side defenses ([[Monitoring|monitoring]], covered in DMLS Ch 8; testing in production in DMLS Ch 9).
- **ML especially shines when the task is repetitive, wrong-prediction cost is cheap, scale is large, and patterns shift.** [[RecommenderSystems|Recommender systems]] dominate ML usage precisely because bad recs are cheap. Self-driving cars are the cost-tolerant counterexample: catastrophic individual mistakes but a path to net safety gain at population scale. Spam classification is the canonical shifting-distribution example.
- **When NOT to use ML: unethical, simpler-solution-suffices, or not cost-effective.** Even when ML can't solve the whole problem, it can often solve a subproblem (e.g. an FAQ-matcher routing easy queries before customer service).
- **Enterprise ML use cases outnumber consumer ones.** Survey of Algorithmia's 2020 State of Enterprise ML lists [[FraudDetection|fraud detection]] / [[AnomalyDetection|anomaly detection]], [[PriceOptimization|price optimization]], [[DemandForecasting|demand forecasting]], [[CustomerAcquisitionCost|customer-acquisition]] optimization, [[ChurnPrediction|churn prediction]], [[SupportTicketClassification|support-ticket classification]], [[BrandMonitoring|brand monitoring]] / [[SentimentAnalysis|sentiment analysis]], and health-care diagnostics (skin cancer, diabetes) as flagship enterprise applications.
- **Enterprise vs. consumer ML have inverted requirement profiles.** Enterprise tolerates higher latency but demands tighter accuracy (a 0.1% efficiency gain at Google or General Motors is worth millions); consumers are highly latency-sensitive but tolerate lower accuracy (a 95.0 → 95.5% [[SpeechRecognition|speech recognition]] bump is imperceptible). Consumer apps are easier to distribute but harder to monetize.
- **ML in research vs. production differs on five axes.** (1) **Requirements**: SOTA on a benchmark vs. heterogeneous stakeholder requirements. (2) **Computational priority**: fast training / high throughput vs. fast inference / low [[Latency|latency]]. (3) **Data**: static benchmark vs. constantly shifting, noisy, biased, sparsely / imbalancedly labeled. (4) **Fairness**: often ignored in research, must be considered in production. (5) **Interpretability**: often ignored in research, must be considered in production.
- **Stakeholders have conflicting objectives.** The recommended-restaurant example pits ML engineers (model complexity), the sales team (high-fee restaurants), product team (sub-100ms latency), the platform team (no new model updates), and the manager (margin, possibly via layoffs) against each other. Resolution: develop one model per objective and combine predictions (decoupling objectives, covered later in the book).
- **Leaderboards / [[Kaggle|Kaggle]]-style competitions misalign with production.** Many hard steps are pre-done for competitors; multiple-hypothesis testing on shared hold-out sets means a winner may win by chance (Oakden-Rayner 2019); Ethayarajh & Jurafsky (EMNLP 2020) argue NLP benchmarks incentivize accuracy at the expense of compactness, fairness, and energy efficiency. [[ModelEnsemble|Ensembling]], popular in the $1M [[NetflixPrize|Netflix Prize]] and Kaggle, is rarely deployed in production because of complexity and inference cost.
- **Latency is a distribution, not a number.** Use [[Percentile|percentiles]] (p50/p90/p95/p99), not means. The slowest-percentile users at Amazon are often the most valuable (highest data, most purchases). A 100ms delay hurt conversion 7% (Akamai 2017); ~30% latency increase at Booking.com cost 0.5% in conversion (Bernardi et al. 2019); >3s page load loses half of mobile users (Google 2016).
- **Throughput-latency trade-off changes with batching.** Serially, higher latency = lower throughput. With [[BatchInference|batching]], higher per-query latency can co-exist with higher aggregate throughput; batching online queries requires waiting, which adds latency. Research prioritizes throughput via aggressive batching; production prioritizes latency.
- **ML systems break the SWE assumption that code and data are separate.** ML applications are part code, part data, part artifacts; "the application with the most/best data wins." [[DataVersioning|Data must be versioned and tested]] alongside code, and not all data samples are equal — a cancerous lung scan is more valuable than the millionth normal one, and indiscriminate ingestion exposes systems to [[DataPoisoning|data poisoning]] attacks.
- **Model size is a production constraint.** As of 2022, hundreds of millions to billions of parameters are routine; deploying these to [[EdgeDeployment|edge devices]] and serving them with usable latency is a major engineering problem. [[bert|BERT]]-large (340M params, 1.35 GB) was called impractical at release in 2018; two years later it was used in nearly every English Google Search query.
- **Algorithmic bias is bias at scale.** "ML algorithms don't predict the future, but encode the past." A 2019 Berkeley study found 1.3M creditworthy Black and Latino applicants were rejected from 2008–2015; removing race identifiers caused the applications to be accepted. McKinsey 2019: only 13% of large companies are mitigating algorithmic bias risks; only 19% are working on [[Interpretability|interpretability]].

## Key Quotes
> "Machine learning is an approach to (1) learn (2) complex patterns from (3) existing data and use these patterns to make (4) predictions on (5) unseen data." — the chapter's operational definition of ML; each italicized keyphrase anchors a subsection.

> "ML algorithms don't predict the future, but encode the past, thus perpetuating the biases in the data and more. When ML algorithms are deployed at scale, they can discriminate against people at scale." — on fairness as a production-grade concern.

> "Research usually prioritizes fast training, whereas production usually prioritizes fast inference." — the inversion of computational priority between phases.

> "Suppose you have cancer and you have to choose between a black box AI surgeon that cannot explain how it works but has a 90% cure rate and a human surgeon with an 80% cure rate. Do you want the AI surgeon to be illegal?" — Geoffrey Hinton (Feb 2020), opening the interpretability discussion; in Huyen's informal survey of 30 non-tech-company executives, only half chose the AI surgeon.

> "In SWE, there's an underlying assumption that code and data are separated… On the contrary, ML systems are part code, part data, and part artifacts created from the two." — why traditional software-engineering best practices don't transfer cleanly.

> "The vast majority of ML-related jobs will be, and already are, in productionizing ML." — Huyen's framing of why ML systems design (vs. ML research) deserves its own book.

> "ML is also called Software 2.0." — citing Karpathy: instead of hand-specifying patterns, ML solutions learn them from input/output pairs.

## Connections
- [[ChipHuyen]] — author; this chapter is the opening of her 2022 [[OReilly|O'Reilly]] book and a precursor to her later *AI Engineering* (2024).
- [[OReilly]] — publisher of both *Designing Machine Learning Systems* (2022) and *AI Engineering* (2024).
- [[ai-engineering-chip-huyen]] — Huyen's 2024 successor book; same systems-thinking lens applied to foundation-model applications instead of bespoke ML models.
- [[MLOps]] — the chapter's framing concept; ML systems design is the holistic-systems take on MLOps.
- [[MachineLearning]] — the chapter's working definition (learn complex patterns from existing data → predict on unseen data) belongs on this page.
- [[SoftwareTwo]] — Karpathy's "Software 2.0" framing of ML; chapter cites this directly.
- [[SupervisedLearning]] — the chapter's first illustrative learning paradigm (Airbnb rental-price prediction).
- [[ZeroShotLearning]] — discussed as a way to relax the "existing data" requirement.
- [[continuallearning|ContinualLearning]] — discussed as a way to deploy models without prior training data; revisited in DMLS Ch 9.
- [[FewShotLearning]] — contrasted with humans' few-example learning vs. most ML algorithms' many-example requirement.
- [[RecommenderSystems]] — canonical low-wrong-prediction-cost ML use case.
- [[FraudDetection]] — oldest enterprise ML application; anomaly-detection driven.
- [[AnomalyDetection]] — underlying technique for fraud detection in the chapter.
- [[PriceOptimization]] — enterprise ML use case; example domains: ads, flights, accommodations, ride-sharing.
- [[DemandForecasting]] — enterprise ML use case (grocery-store inventory example).
- [[CustomerAcquisitionCost]] — chapter cites $86.61 avg in-app purchase user cost (2019) and $158/rider for Lyft.
- [[ChurnPrediction]] — predicting when customers/employees will leave; chapter cites 5–25× retention/acquisition cost ratio.
- [[SupportTicketClassification]] — ML-driven ticket routing as a customer-service use case.
- [[BrandMonitoring]] — sentiment-tracking of brand mentions, explicit and implicit.
- [[SentimentAnalysis]] — underlying technique for brand monitoring.
- [[MachineTranslation|machinetranslation]] — Huyen's gateway use case; Google Neural Machine Translation (Nov 2016) cited as a watershed deep-learning production deployment.
- [[GoogleTranslate]] — concrete example of the latency/throughput discussion.
- [[ObjectDetection]] — example of an ML-solvable complex-pattern task.
- [[SpeechRecognition]] — example of an ML-solvable complex-pattern task; also used to illustrate enterprise-vs.-consumer accuracy sensitivity.
- [[ModelEnsemble|Ensembling]] — discussed as a research/Kaggle technique rarely useful in production due to complexity and inference cost.
- [[NetflixPrize]] — $1M Kaggle-style competition where ensembling won; chapter's go-to example of leaderboard-vs.-production misalignment.
- [[Kaggle]] — concrete leaderboard example criticized for misalignment with real ML practice.
- [[ImageNet]] — benchmark cited alongside GLUE as a leaderboard example.
- [[Leaderboard]] — generalized concept being critiqued in the chapter.
- [[Latency]] — chapter discusses the term, distinguishes it from response time (per Kleppmann), and gives p50/p90/p95/p99 percentile-based guidance.
- [[Percentile]] — argued as the correct way to report latency.
- [[BatchInference]] — batching as the lever that converts the latency-throughput trade-off.
- [[InferenceOptimization]] — production constraint introduced as the dominant computational priority.
- [[Monitoring]] — production-side defense against distribution shift; DMLS Ch 8.
- [[DistributionShift]] — the failure mode when unseen data deviates from training distribution.
- [[DataDrift]] — closely related to distribution shift; relevant to "constantly shifting" production data.
- [[Interpretability]] — research-vs.-production axis; framed via Hinton's AI-surgeon question.
- [[Fairness]] — research-vs.-production axis; Berkeley 2019 lending bias study cited.
- [[ResponsibleAI]] — chapter forward-references DMLS Ch 11 on fairness and responsible AI.
- [[AlgorithmicBias]] — Huyen's term for the bias-at-scale phenomenon; loan/resume/mortgage examples.
- [[DataPoisoning]] — risk of indiscriminately ingesting all available production data.
- [[EdgeDeployment|EdgeDevice]] — billion-parameter models on edge devices flagged as a major engineering challenge; DMLS Ch 7.
- [[bert|BERT]] — the chapter's worked example of an "impractical" 2018 model that became ubiquitous in Google Search by 2020.
- [[Google]] — sponsor of Google Neural Machine Translation (2016 launch), Google Translate, Google Assistant, Google Search (BERT deployment), and the source of two cited latency/conversion datapoints.
- [[Amazon]] — cited for the "slowest requests come from highest-value customers" observation (Kleppmann).
- [[Netflix]] — cited via the $1M Netflix Prize ensembling story.
- [[Tesla]] — Andrej Karpathy was director of AI at Tesla; the data-in-research-vs.-production figure is adapted from his Spark+AI Summit 2018 talk.
- [[GeoffreyHinton]] — quoted on the AI-surgeon interpretability dilemma (Feb 2020 tweet).
- [[AndrejKarpathy]] — author of the "Software 2.0" framing and the data-in-research-vs.-production figure; ex-Tesla AI director.
- [[MartinKleppmann]] — *Designing Data-Intensive Applications* author cited twice (latency/response-time terminology; slow-request-vs.-valuable-customer observation).
- [[Algorithmia]] — source of the 2020 State of Enterprise ML survey driving the enterprise-use-case taxonomy.
- [[CathyONeil]] — *Weapons of Math Destruction* recommended as further reading on algorithmic bias.
- [[Lyft]] — $158/rider customer-acquisition-cost data point.
- [[Airbnb]] — running example for both the supervised-learning rental-price problem and the lookup-table-vs.-ML zip-code-to-state contrast.
- [[1706.03762-attention-is-all-you-need]] — the architectural progenitor of [[bert|BERT]] (which is the chapter's worked example of a production-deployed Transformer model at scale).

## Contradictions
- **Latency vs. response-time terminology.** The chapter explicitly notes that it overloads "latency" to mean "response time" (per Kleppmann's stricter *Designing Data-Intensive Applications* definition), to align with ML-community usage. Any existing wiki pages that use Kleppmann's stricter definition should cross-reference this convention. No other contradictions with existing wiki content noted.
