---
title: "Designing ML Systems — Ch 4: Training Data"
type: source
tags: [book, dmls, designing-ml-systems, training-data, sampling, labeling, class-imbalance, data-augmentation, weak-supervision, semi-supervision, transfer-learning, active-learning, oreilly, chip-huyen]
date: 2022-05-17
sources: []
source_file: raw/books/designing-ml-systems/dmls-ch04-training-data.txt
last_updated: 2026-05-23
---

# Designing ML Systems Ch 4 — Training Data

## Summary

Chapter 4 of [[ChipHuyen|Chip Huyen]]'s *Designing Machine Learning Systems* ([[OReilly|O'Reilly Media]], 2022) is the data-science counterpart to Chapter 3's systems view: it covers how to **obtain, sample, label, balance, and augment** the data that ML models learn from, deliberately using "training data" rather than "training dataset" because production data is "neither finite nor stationary." The chapter is organized around four problems — choosing the right **[[Sampling|sampling]]** strategy, dealing with the **lack of labels**, dealing with **[[ClassImbalance|class imbalance]]**, and dealing with the **lack of data** via [[DataAugmentation|augmentation]] — and treats each through both classical statistical methods and modern alternatives such as [[WeakSupervision|weak supervision]], [[SemiSupervisedLearning|semi-supervision]], [[TransferLearning|transfer learning]], and [[ActiveLearning|active learning]]. Huyen repeatedly returns to a single warning — "data is full of potential biases ... use data but don't trust it too much" — and frames hand-labeling not as an auxiliary task but as "a core function of many ML teams in production," citing an anecdote where [[AndrejKarpathy|Andrej Karpathy]] kept an in-house [[Tesla]] labeling team "as long as we need an engineering team for." The chapter's signature empirical claim is that, in a Stanford Medicine study, a single radiologist writing eight hours of labeling functions produced [[WeakSupervision|weakly supervised]] labels comparable to a year of hand labeling on chest- and extremity-X-ray tasks.

## Key Claims

- **"Training data" ≠ "training dataset".** Production data is neither finite nor stationary, so the term *dataset* is misleading; the chapter treats data creation as an iterative process that evolves with [[DistributionShift|data distribution shifts]] across the model lifecycle.
- **Convenience drives ML data selection more than statisticians admit.** Language models are not trained on text representative of all possible texts but on what is easy to collect — [[Wikipedia]], [[CommonCrawl]], [[Reddit]] — and sentiment datasets are pulled from sources with natural labels (IMDb, [[Amazon]] reviews) that systematically over-represent users willing to leave reviews online.
- **Self-driving data was geographically biased to sunny weather** (Phoenix, Bay Area) until [[Waymo]] expanded to Kirkland, Washington in 2016 specifically to collect rain data — a concrete example of how [[Sampling|non-probability sampling]] embeds [[SelectionBias|selection bias]] into safety-critical models.
- **[[SimpleRandomSampling|Simple random sampling]] under-samples rare classes** by design — a class present in 0.01% of the population may simply not appear in a 1% sample; this motivates [[StratifiedSampling|stratified sampling]], which becomes hard or impossible for [[MultiLabelClassification|multi-label]] tasks where a sample belongs to multiple strata.
- **[[WeightedSampling|Weighted sampling]] and [[SampleWeights|sample weights]] are different things.** Weighted sampling biases *which* examples are drawn (e.g. more recent data); sample weights re-weight the *loss* contribution of each example. Both can shift the decision boundary, but they act at different stages of the pipeline.
- **[[ReservoirSampling|Reservoir sampling]] solves the stream-with-unknown-length problem.** A reservoir of size *k* with the "replace with probability *k/n* on the *n*th item" rule guarantees that every item ever seen has probability *k/n* of being in the reservoir, and the algorithm can be stopped at any time and remain correctly sampled — useful for streaming tweets, logs, or production events.
- **[[ImportanceSampling|Importance sampling]] lets you sample from P(x) using a cheaper proposal Q(x)** by re-weighting by P(x)/Q(x); used in [[ReinforcementLearning|policy-based RL]] when the old policy is the proposal distribution for evaluating a new policy.
- **Hand labeling is expensive, slow, privacy-hostile, and non-adaptive.** Phonetic transcription takes ~400× the utterance duration (1 hour audio → ~3 months work); a lung-cancer X-ray study waited "almost a year" for enough labels; relabeling for a new class (NEGATIVE/POSITIVE → +ANGRY) means waiting on humans before the model can update.
- **[[LabelMultiplicity|Label multiplicity]] (a.k.a. label ambiguity) is the rule, not the exception.** Three annotators on the same NER sentence produced 3, 4, and 6 entities respectively — a single sentence can yield three different training distributions. Mitigation requires explicit annotation guidelines (e.g. "pick the longest substring entity") *and* training on those guidelines.
- **[[DataLineage|Data lineage]] — tracking the origin and labeler of every sample — is required to debug "more data made the model worse" failures**, which Huyen has seen happen when a fresh million-sample crowdsourced batch had lower labeling accuracy than the original 100K.
- **63% of companies in Huyen's survey work on tasks with [[NaturalLabel|natural labels]]** (recommender clicks, ETA, stock prices, ad CTR), suggesting companies *select* into these problems because they're cheaper to evaluate. Labels inferred from user behavior are called **[[BehavioralLabel|behavioral labels]]**.
- **[[ImplicitLabel|Implicit labels] are presumed from absence** (no click within N minutes → NEGATIVE), in contrast to **[[ExplicitLabel|explicit labels]]** like downvotes. Implicit labels systematically *underestimate* the positive rate: a 2021 [[Twitter]] Ads study found that the majority of ad clicks happen within 5 minutes but a long tail extends hours later.
- **[[FeedbackLoopLength|Feedback loop length]] is a first-class design parameter.** Short loops (minutes — recommender clicks) enable rapid detection of model drift; long loops (months — fraud disputes, a typical 1–3 month dispute window) mean errors compound for months before being caught.
- **Four techniques handle the lack of hand labels: [[WeakSupervision|weak supervision]], [[SemiSupervisedLearning|semi-supervision]], [[TransferLearning|transfer learning]], and [[ActiveLearning|active learning]].** Weak supervision needs no ground truth (but a small set is recommended); semi-supervision needs a seed set; transfer learning needs none for [[ZeroShotLearning|zero-shot]] use, some for fine-tuning; active learning needs labels but chooses *which* unlabeled examples to label.
- **[[Snorkel]]-style [[LabelingFunction|labeling functions]] (LFs) operationalize weak supervision.** LFs encode keyword/regex/database-lookup/model-output heuristics; outputs are noisy and conflicting, so a combine-denoise-reweight model produces final labels. Huyen calls this **[[ProgrammaticLabeling|programmatic labeling]]** — versionable, shareable, privacy-friendly, and adaptive (relabel by re-running LFs).
- **Stanford Medicine case study**: a single radiologist writing LFs for **8 hours** matched models trained on **~1 year of hand labels** on CXR/EXR tasks, and 6 LFs transferred between the two tasks ([[JaredDunnmon|Dunnmon]] et al. 2020).
- **Semi-supervision methods include [[SelfTraining|self-training]] (label your unlabeled data with the model's own high-confidence predictions, retrain) and [[PerturbationBasedSemiSupervision|perturbation-based methods]]** that assume small noise additions preserve the label. These have reached supervised-level performance "even when a substantial portion of the labels has been discarded" (Oliver et al. 2018).
- **Larger pretrained base models give better downstream performance**, but [[GPT3|GPT-3]]-scale training "is in the tens of millions USD" — Huyen predicts that "only a handful of companies will be able to afford to train large pretrained models" and the rest will fine-tune. (2022 prediction; broadly borne out.)
- **[[ActiveLearning|Active learning]] (a.k.a. query learning) trades random labeling for *uncertainty-based* labeling.** A toy two-class Gaussian example reaches 70% accuracy with 30 random labels but 90% with 30 uncertainty-sampled labels. Variants: [[QueryByCommittee|query-by-committee]] (ensemble disagreement), expected-gradient-update sampling, and expected-loss-reduction sampling.
- **Class imbalance hurts learning for three reasons**: (1) insufficient signal — minority class becomes a [[FewShotLearning|few-shot]] problem or invisible; (2) models exploit "always predict majority" as a 99.99%-accurate local optimum that gradient descent struggles to escape; (3) asymmetric error cost — false-negative cancer is worse than false-positive cancer, but symmetric losses ignore this.
- **Accuracy is the wrong metric under imbalance.** Two models with identical 90% accuracy on a 90/10 cancer task can have F1 of 0.17 vs 0.64 on the positive class. Huyen recommends per-class accuracy, [[F1Score|F1]], [[Precision]]/[[Recall]], the [[ROCCurve|ROC curve]] / [[AUC]], and especially the **[[PrecisionRecallCurve|Precision-Recall curve]]** (Davis & Goadrich 2006) for heavily imbalanced tasks.
- **Data-level fixes (resampling) and algorithm-level fixes (loss reweighting) are complementary.** [[SMOTE]] synthesizes minority samples via convex combinations (works only in low-dim); [[TomekLinks|Tomek links]] remove majority samples near class boundaries; [[TwoPhaseLearning|two-phase learning]] (resample, fine-tune on original) and [[DynamicSampling|dynamic sampling]] (oversample low-performing classes mid-training) avoid the overfit/discard tradeoffs.
- **Never evaluate on resampled data** — doing so causes the model to overfit to the resampled distribution and produces misleadingly good metrics.
- **Three algorithm-level loss modifications**: **[[CostSensitiveLearning|cost-sensitive learning]]** (Elkan 2001 — a cost matrix C_ij weights misclassification class i→j); **[[ClassBalancedLoss|class-balanced loss]]** (weight inversely proportional to class size, optionally adjusted by effective number of samples per Cui et al. 2019); **[[FocalLoss|focal loss]]** (Lin et al. 2017 — down-weight easy examples so the model focuses on hard ones).
- **Data augmentation falls into three families**: **label-preserving transformations** (rotate/flip/crop images; synonym replacement in NLP), **[[Perturbation|perturbation]]** (adversarial-style noise — [[OnePixelAttack|one-pixel attacks]] flip 67.97% of CIFAR-10 / 16.04% of ImageNet), and **data synthesis** (templates for chatbots; [[Mixup|mixup]] for vision; [[CycleGAN]] for medical CT — Sandfort et al. 2019).
- **AlexNet's GPU-overlapping augmentation is "computationally free"** (Krizhevsky et al. 2012); [[BERT|BERT]]'s 15%-tokens-masked-of-which-10%-random-word policy means ~1.5% of all tokens get nonsense replacements and this produced a small accuracy boost.

## Key Quotes

> "Data is messy, complex, unpredictable, and potentially treacherous. If not handled properly, it can easily sink your entire ML operation." — Ch 4 opening, on why training data deserves its own chapter

> "Data is full of potential biases. ... Use data but don't trust it too much!" — Ch 4 standing warning, echoed every section

> "How long do we need an engineering team for?" — [[AndrejKarpathy|Andrej Karpathy]] (then [[Tesla]] director of AI), quoted by Huyen on why labeling is permanent rather than an auxiliary task

> "Disagreements among annotators are extremely common. The higher the level of domain expertise required, the higher the potential for annotating disagreement. ... If human experts can't agree on a label, what does human-level performance even mean?" — Ch 4, on [[LabelMultiplicity|label multiplicity]]

> "In theory, you don't need any hand labels for weak supervision. However, to get a sense of how accurate your LFs are, a small number of hand labels is recommended." — Ch 4, on [[Snorkel]]-style [[ProgrammaticLabeling|programmatic labeling]]

> "Models trained with weakly supervised labels obtained by a single radiologist after eight hours of writing LFs had comparable performance with models trained on data obtained through almost a year of hand labeling." — Ch 4, summarizing [[JaredDunnmon|Dunnmon]] et al. (2020) on CXR/EXR weak supervision

> "If your model learns to always output the majority class, its accuracy is already 99.99%. ... This heuristic can be very hard for gradient descent algorithms to beat because a small amount of randomness added to this heuristic might lead to worse accuracy." — Ch 4, on why imbalanced classes trap gradient descent

> "When you resample your training data, never evaluate your model on resampled data, since it will cause your model to overfit to that resampled distribution." — Ch 4, the canonical resampling pitfall

> "The transformed images are generated in Python code on the CPU while the GPU is training on the previous batch of images. So these data augmentation schemes are, in effect, computationally free." — Krizhevsky et al. (2012) on [[AlexNet]], quoted in Ch 4 to justify routine augmentation

## Connections

- [[ChipHuyen]] — author; this book precedes her 2024 *AI Engineering* and overlaps with [[ai-engineering-ch08-dataset-engineering]] on data quality, augmentation, and synthesis.
- [[OReilly]] — publisher.
- [[DesigningMachineLearningSystems]] — the parent book this chapter belongs to.
- [[Sampling]] — chapter's first major topic; foundation for the [[NonProbabilitySampling|non-probability]] vs [[RandomSampling|random sampling]] dichotomy.
- [[NonProbabilitySampling]] — [[ConvenienceSampling|convenience]] / [[SnowballSampling|snowball]] / [[JudgmentSampling|judgment]] / [[QuotaSampling|quota]] sub-types.
- [[SimpleRandomSampling]] — baseline probability sampling; rare-class blind spot.
- [[StratifiedSampling]] — sample-per-stratum fix; fails on multi-label.
- [[WeightedSampling]] — selection probability via per-sample weights.
- [[SampleWeights]] — loss-weighting cousin of weighted sampling.
- [[ReservoirSampling]] — streaming, unknown-length population.
- [[ImportanceSampling]] — sample from cheap Q(x), reweight to expensive P(x); used in policy-based [[ReinforcementLearning|RL]].
- [[SelectionBias]] / [[SamplingBias]] — root cause of biased datasets; Heckman 1979 cited.
- [[Waymo]] / [[Tesla]] — self-driving examples of geographic sampling bias.
- [[Wikipedia]] / [[CommonCrawl]] / [[Reddit]] — convenience-sampled corpora that dominate language modeling.
- [[Amazon]] / [[IMDb]] — sentiment-analysis sources biased toward review-leaving users.
- [[LabelMultiplicity]] — multiple conflicting labels per instance; needs annotation guidelines.
- [[AnnotationGuidelines]] — mitigation for label multiplicity; harder than the labeling itself.
- [[DataAnnotation]] — umbrella process.
- [[DataLineage]] — origin tracking for samples & labels; needed to debug "more data made it worse" failures.
- [[AndrejKarpathy]] — quoted on permanent in-house labeling teams at [[Tesla]].
- [[HandLabel]] / [[GroundTruth]] — the expensive baseline this chapter argues against relying on exclusively.
- [[AmazonMechanicalTurk]] / [[Crowdsourcing]] — adjacent practice for cheap hand labels.
- [[NaturalLabel]] — labels the system can verify automatically (ETA, click, stock price).
- [[BehavioralLabel]] — natural labels inferred from user behavior (clicks, ratings, purchases).
- [[ImplicitLabel]] / [[ExplicitFeedback]] / [[ImplicitFeedback]] — presumed-from-absence vs user-supplied feedback.
- [[FeedbackLoopLength]] — minutes (recommenders) to months ([[FraudDetection|fraud]] dispute window).
- [[RecommenderSystems]] — canonical natural-label tasks.
- [[CTRPrediction]] — click-through prediction framed as recommendation.
- [[FraudDetection]] — long-feedback-loop class-imbalance archetype.
- [[WeakSupervision]] — heuristic-driven labeling via [[LabelingFunction|LFs]].
- [[ProgrammaticLabeling]] — synonym; the practitioner term for weak supervision in production.
- [[LabelingFunction]] — keyword/regex/db-lookup/model-output rules combined via Snorkel-style denoisers.
- [[Snorkel]] — Stanford AI Lab tool; [[AlexanderRatner|Ratner]] et al. VLDB 2017.
- [[JaredDunnmon]] — first author of the Stanford Medicine CXR/EXR weak-supervision study.
- [[ChristopherRe]] — senior author of Snorkel and the Stanford Medicine study.
- [[StanfordAILab]] — origin of Snorkel.
- [[SemiSupervisedLearning]] — leverages structural assumptions on top of seed labels.
- [[SelfTraining]] — classic semi-supervision; pseudo-label high-confidence predictions.
- [[PerturbationBasedSemiSupervision]] — perturb sample, assume label invariance.
- [[KNearestNeighbors]] / [[Cluster|clustering]] — semi-supervision similarity heuristics.
- [[TransferLearning]] — base task + downstream task framing.
- [[FineTuning]] — adapt a pretrained model to downstream data.
- [[ZeroShotLearning]] — use base model directly without task labels.
- [[LanguageModel|Language models]] / [[pretraining]] — the canonical transfer-learning base task.
- [[BERT]] / [[GPT3]] — examples Huyen cites of transfer-learning enablers.
- [[ImageNet]] / [[AlexNet]] — object-detection's pretrained-backbone analog.
- [[ActiveLearning]] — model picks which examples to label.
- [[QueryByCommittee]] — ensemble-disagreement active-learning heuristic.
- [[UncertaintySampling]] — label-the-least-certain heuristic.
- [[ClassImbalance]] — the chapter's third major topic; rare-event detection.
- [[ConfusionMatrix]] — TP/FP/FN/TN structure for binary classification.
- [[F1Score]] / [[Precision]] / [[Recall]] — asymmetric metrics on the positive class.
- [[ROCCurve]] / [[AUC]] — threshold sweep visualization.
- [[PrecisionRecallCurve]] — Davis & Goadrich 2006; preferred over ROC for heavy imbalance.
- [[Oversampling]] / [[Undersampling]] / [[Resampling]] — data-level imbalance fixes.
- [[SMOTE]] — convex-combination minority oversampling; low-dim only.
- [[TomekLinks]] — undersampling by removing majority-class points near boundaries.
- [[TwoPhaseLearning]] — train on resampled, fine-tune on original.
- [[DynamicSampling]] — oversample low-performing classes during training.
- [[CostSensitiveLearning]] — Elkan 2001; explicit per-class cost matrix.
- [[ClassBalancedLoss]] — Cui et al. 2019; weight ∝ 1/class size (or effective number of samples).
- [[FocalLoss]] — Lin et al. 2017; downweights easy examples.
- [[CrossEntropyLoss]] — baseline loss the above modify.
- [[ModelEnsemble]] / [[adversarialensemble]] — ensembles help with imbalance but deferred to Ch 6.
- [[DataAugmentation]] — chapter's fourth major topic; three families.
- [[Perturbation]] — adversarial-style label-preserving noise.
- [[AdversarialAttack]] / [[OnePixelAttack]] — Su et al. 2017; 67.97% CIFAR-10 / 16.04% ImageNet misclassified by 1 pixel.
- [[AdversarialAugmentation]] / [[DeepFool]] — Moosavi-Dezfooli et al. 2016; minimum-perturbation adversarial example.
- [[Mixup]] — Zhang et al. 2018; convex combinations of (x, y) pairs.
- [[CycleGAN]] — Sandfort et al. 2019; GAN-augmented CT segmentation.
- [[DataSynthesis]] — template-based and model-generated training data.
- [[CIFAR10]] / [[ImageNet]] — vision benchmarks referenced in perturbation results.
- [[AlexNet]] — Krizhevsky et al. 2012; "computationally free" CPU/GPU-overlapped augmentation.
- [[BERT]] — Devlin et al. 2018; 1.5% random-token-replacement perturbation in pretraining.
- [[DistributionShift]] — chapter motivates the term by rejecting "dataset" in favor of "training data."
- [[MultiLabelClassification]] — stratified-sampling failure mode.
- [[FewShotLearning]] — what extreme class imbalance degenerates into.
- [[ObjectDetection]] — surprising class-imbalance example (most bounding boxes are background).
- [[SentimentAnalysis]] — running example for the NEGATIVE/POSITIVE/ANGRY relabeling story.
- [[IntentClassifier|Intent detection]] / [[QuestionAnswering]] — downstream tasks for transfer learning.
- [[MachineTranslation]] — example of soliciting community feedback (Google Translate) to bootstrap natural labels.
- [[StitchFix]] — multi-week feedback-loop example (clothing recommendations).
- [[Twitter]] / [[Reddit]] / [[Amazon]] — recurring data sources / examples.
- [[ai-engineering-ch08-dataset-engineering]] — Huyen's later, expanded treatment of dataset engineering; this chapter is the predecessor and overlaps on augmentation, synthesis, data quality, and lineage.

## Contradictions

- None directly contradicting existing wiki content. Chapter 4 is the **2022 predecessor** of [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]] (2024); where they overlap, the 2024 treatment refines but does not reverse the 2022 framing (e.g. augmentation vs. synthesis distinction in Ch 8 is stricter; both books endorse [[WeakSupervision|weak supervision]], [[Mixup]], [[OnePixelAttack|one-pixel attacks]], and [[DataLineage|data lineage]]). The 2022 prediction that "only a handful of companies will be able to afford to train large pretrained models" is consistent with the post-[[GPT3|GPT-3]] industry trajectory documented elsewhere in the wiki.
