---
title: "IIR Ch. 13: Text Classification and Naive Bayes"
type: source
tags: [iir, information-retrieval, textbook, text-classification, naive-bayes, feature-selection]
date: 2026-05-23
source_file: "https://nlp.stanford.edu/IR-book/html/htmledition/text-classification-and-naive-bayes-1.html"
---

## Summary

Chapter 13 of Manning, Raghavan, and Schütze's *Introduction to Information Retrieval* (Cambridge, 2008) opens the classification half of the book. It motivates supervised [[TextClassification]] as the principled successor to ad hoc retrieval whenever the same information need recurs ("standing queries") or whenever automated decisions must be made on a continuous stream of documents — spam filtering, language identification, sentiment scoring, vertical-search routing, and topic indexing. The chapter develops two probabilistic models — the multinomial and Bernoulli variants of [[NaiveBayes]] — derives their MAP parameter estimates with add-one ([[LaplaceSmoothing]]) smoothing, analyzes their training and test complexity, and explains why a model whose probability estimates are notoriously poorly calibrated can still produce competitive classification decisions. The second half of the chapter is devoted to [[FeatureSelection]]: it formalizes [[MutualInformation]] I(U;C), introduces the χ² statistic ([[ChiSquareTest]]) for term–class independence, contrasts both against frequency-based selection, and finally lays out the evaluation machinery — precision, recall, F1, accuracy, and the distinction between [[MicroAveraging]] and [[MacroAveraging]] over multi-class contingency tables. Benchmarks are reported on the classical [[Reuters21578]] ModApte split and on the newer RCV1 collection.

## Key Claims

- Text classification is the supervised mapping γ: 𝕏 → ℂ from a document space 𝕏 to a fixed finite class set ℂ = {c₁, …, c_J}, learned from a labeled training set 𝔻 of (document, class) pairs.
- The literature distinguishes the **one-of (single-label)** problem from the **any-of (multi-label)** problem; the any-of case is conventionally decomposed into J independent two-class classifiers.
- "High accuracy on the training set in general does not mean that the classifier will work well on new data" — generalization, not memorization, is the goal; this is the foundational supervised-learning caveat.
- The **multinomial Naive Bayes** model treats a document as an ordered sequence of token positions, each independently generated from a class-conditional unigram distribution; it is "formally identical to the multinomial unigram language model" of Chapter 12, with documents in the role of queries.
- The **Bernoulli Naive Bayes** model treats a document as a binary M-vector recording term presence/absence and explicitly factors in non-occurring vocabulary terms, which the multinomial model does not.
- Both variants are bag-of-words models: the **conditional independence assumption** P(d|c) = ∏ᵢ P(tᵢ|c) and (for multinomial) the **positional independence assumption** P(X_k = t | c) = P(X_k′ = t | c) are demonstrably false yet empirically tolerable.
- "Even though the probability estimates of NB are of low quality, its classification decisions are surprisingly good" — *correct estimation implies accurate prediction, but accurate prediction does not imply correct estimation* (Domingos & Pazzani 1997).
- **Add-one (Laplace) smoothing** resolves the sparse-data zero-probability pathology that would otherwise force any product containing an unseen (term, class) pair to zero out the entire posterior.
- Training the multinomial NB classifier runs in Θ(|𝔻|·L_ave + |ℂ|·|V|) and test classification in Θ(|ℂ|·M_a), where L_ave is average training-document length, |V| is vocabulary size, and M_a is the number of distinct tokens in the test document — this is **optimal** because the data must be scanned at least once.
- The Bernoulli model "typically makes many mistakes when classifying long documents" because the binary indicator ignores term frequency.
- **Feature selection** serves two ends: it shrinks the effective vocabulary (memory/time) and it raises accuracy by stripping out noise terms; the Bernoulli model is "particularly sensitive to noise features" and benefits most.
- Three greedy ranking utilities dominate: **mutual information (MI / information gain)**, **χ² independence test**, and **frequency-based selection** (document frequency for Bernoulli, collection frequency for multinomial).
- On Reuters-RCV1, MI-based selection at a few hundred features matches or beats using the full vocabulary by 0.1–0.2 F₁; the Bernoulli model peaks at ≈10 selected features per class, the multinomial at ≈100.
- χ² "selects more rare terms (which are often less reliable indicators) than mutual information," but MI and χ² achieve comparable downstream accuracy.
- **Multiple-testing caveats** apply to χ² as a statistical test, but "as long as χ² feature selection only ranks features … and is not used to make statements about statistical dependence or independence of variables, we need not be overly concerned that it does not adhere strictly to statistical theory."
- The standard 2008 benchmark is **Reuters-21578**, 21,578 newswire stories across 118 topic categories with the **ModApte split** of 9,603 training and 3,299 test documents; **Reuters-RCV1** is the larger successor.
- **Macroaveraging** averages per-class metrics (equal weight to each class) while **microaveraging** pools per-document decisions across all classes before computing the metric (equal weight to each decision); the two diverge sharply when class sizes are skewed.

## Section Notes

### 13.1 The text classification problem
Formalizes supervised learning of γ: 𝕏 → ℂ from a labeled training set. Introduces the role of the human "supervisor" who defines ℂ and labels documents, and warns explicitly that **training accuracy ≠ test accuracy**. Distinguishes one-of (mutually exclusive classes) from any-of (overlapping classes) problems and shows that any-of can be solved as J binary problems. Establishes the convention that γ is evaluated on a held-out test set drawn from the same distribution as 𝔻.

### 13.2 Naive Bayes text classification
Develops the multinomial NB classifier. The posterior P(c|d) ∝ P(c) · ∏_{1≤k≤n_d} P(t_k|c) is reduced via Bayes' rule, dropping the document evidence P(d) since it is constant across classes. To avoid floating-point underflow on long documents, classification proceeds in log space:

  c_map = argmax_{c∈ℂ} [ log P̂(c) + Σ_{1≤k≤n_d} log P̂(t_k|c) ]

MAP estimates use empirical priors P̂(c) = N_c / N and class-conditional term probabilities P̂(t|c) = T_{ct} / Σ_{t′∈V} T_{ct′}. The **zero-probability problem** is patched with Laplace (add-one) smoothing:

  P̂(t|c) = (T_{ct} + 1) / (Σ_{t′∈V} T_{ct′} + B′)

where B′ = |V| for the multinomial model. Worked example: the four-document toy collection with classes "China"/"not-China" and the test document "Chinese Chinese Chinese Tokyo Japan" is classified as "China" once smoothing pulls the otherwise-zero probabilities away from the boundary.

### 13.3 The multinomial NB / unigram-LM correspondence
Shows the multinomial NB model is **formally identical** to the multinomial unigram language model of Chapter 12 with roles swapped: in classification, the *document* indexes the model and the *class* is the latent variable; in language modeling, the *query* is the observation and the *document* is the latent. Add-one smoothing here mirrors the add-½ smoothing seen in probabilistic relevance feedback.

### 13.4 The Bernoulli model
Each document is encoded as a binary M-vector e(d) = (e₁, …, e_M) where e_t = 1 iff term t appears in d at least once, 0 otherwise. The likelihood becomes:

  P(d|c) = ∏_{t∈V} [ P̂(t|c)^{e_t} · (1 − P̂(t|c))^{1−e_t} ]

The product runs over the **entire vocabulary**, so non-occurring terms contribute (1 − P̂(t|c)) factors — Bernoulli explicitly models absence. Smoothing uses the same add-one form but with B′ = 2: P̂(t|c) = (N_{ct} + 1) / (N_c + 2). Document frequency, not term frequency, drives the estimate. The model's blindness to repetition makes it brittle on long documents but acceptable on short ones (titles, snippets, short emails).

### 13.5 Properties of Naive Bayes
The two violated independence assumptions — conditional independence of features given the class, and positional independence in the multinomial case — are quantitatively wrong. NB compensates by being **resistant to overconfidence harming the argmax**: even when P̂(c|d) is wildly off from the true posterior, the *ordering* of classes by score is often preserved, so the argmax remains correct. NB is fast to train, fast to apply, easy to implement, robust to concept drift, and serves as the canonical baseline.

### 13.6 A variant of the multinomial model
Recasts the multinomial document representation as a fixed M-dimensional vector of term-frequency counts. Equation 129 in the book shows P(d|c) ∝ ∏_{tᵢ∈V} P(t_i|c)^{tf(t_i,d)}, equivalent to the sequence formulation because absent terms (tf=0) contribute neutral factors (x⁰ = 1) and repeated terms multiply factors accordingly.

### 13.7 Feature selection
Defines feature selection as choosing A ⊂ V with |A| ≪ |V| to feed the classifier. Two motivations: (a) **computational** — smaller A means faster training, less memory; (b) **statistical** — pruning rare or noise-correlated features raises accuracy, particularly for the Bernoulli model. The three rankings discussed (MI, χ², frequency) are all **greedy and univariate**: they score each term independently and may pick mutually redundant features that together carry less information than a smaller diverse set.

### 13.7.1 Mutual information
For binary U_t (term t present/absent) and binary C_c (document in class c / not), the **expected mutual information** between U_t and C_c is:

  I(U_t; C_c) = Σ_{e_t ∈ {0,1}} Σ_{e_c ∈ {0,1}} P(U_t=e_t, C_c=e_c) · log₂ [ P(U_t=e_t, C_c=e_c) / ( P(U_t=e_t) · P(C_c=e_c) ) ]

(also called **information gain**, per Yang & Pedersen 1997). MI on Reuters-RCV1 with the "UK" class surfaces terms like *london, uk, british, stg, britain, plc, england, pound, english, ireland* — semantically obvious, statistically validated.

### 13.7.2 χ² feature selection
The χ² statistic on the 2×2 contingency table of (term occurrence) × (class membership) tests the null hypothesis that the two are independent. With observed counts N_{e_te_c} and expected counts E_{e_te_c} = N · P(U=e_t) · P(C=e_c):

  X²(t, c) = Σ_{e_t ∈ {0,1}} Σ_{e_c ∈ {0,1}} (N_{e_te_c} − E_{e_te_c})² / E_{e_te_c}

Equation 137 collapses this to an arithmetically simpler closed form using just N₁₁, N₁₀, N₀₁, N₀₀ without explicit expected-count computation. In the worked Reuters example for *export*/*poultry*, X² ≈ 284 — far above the 0.001-significance critical value of 10.83 (1 df), letting us reject independence and rank the term as highly informative.

### 13.7.3 Assessing χ² as a feature-selection method
With one degree of freedom, Yates' continuity correction applies in principle. The **multiple-testing problem** also matters: at α = 0.05 over |V| ≈ 10⁵ candidate terms one expects thousands of false rejections by chance alone. The book argues that since χ² here is used only as a *ranker* — not as a basis for asserting genuine statistical (in)dependence — these concerns are mostly academic for the IR task.

### 13.7.4 Frequency-based feature selection
Document frequency (Bernoulli) or collection frequency (multinomial) is the cheapest possible signal: keep the k most-frequent terms per class. Performs surprisingly well at *large* feature counts (thousands) but lags MI and χ² substantially in low-feature regimes because it does not weigh class discrimination.

### 13.7.5 Feature selection for multiple classifiers
Two strategies for J binary classifiers: (a) **per-classifier** — pick top-k for each c independently (J·k terms total); (b) **shared** — pick one common pool by combining per-class scores (averaging, max, etc.). Per-classifier is more accurate but uses more memory; shared scales better at the cost of accuracy.

### 13.7.6 Comparison of feature-selection methods
Empirically, MI and χ² are roughly tied; χ² favors rarer terms; frequency-based wins at high k. All three are greedy/univariate and can select redundant features. The independence of term and class "can sometimes be rejected with high confidence even if the term carries little information about membership," which is exactly the failure mode where χ² rankings can mislead.

### 13.8 Evaluation of text classification
Defines precision = TP/(TP+FP), recall = TP/(TP+FN), F₁ = 2PR/(P+R), and accuracy. For multi-class evaluation, **macroaverage** computes F₁ per class then averages (equal weight per class — surfaces poor performance on small classes), while **microaverage** sums TP/FP/FN across all classes into a single contingency table then computes F₁ (equal weight per decision — dominated by large classes). On Reuters-21578 ModApte: NB achieves ≈80% microaveraged F₁ on the top-10 categories; SVMs and boosted trees outperform it; kNN and Rocchio are mixed. χ² and MI-based selection are noted not to distinguish positively from negatively correlated features.

### 13.9 References and further reading
Foundational attribution: **Maron and Kuhns (1960)** built one of the first NB text classifiers (Bayes' theorem itself due to **Thomas Bayes**, 18th century, published posthumously 1763). **Lewis (1998)** surveys the history of NB classification and the multinomial/Bernoulli divide. **McCallum and Nigam (1998)** is the canonical empirical comparison of the two models. **Yang and Pedersen (1997)** review feature-selection methods including MI/information gain. **Lewis and Ringuette (1994)** and **Schütze et al. (1995)** are early χ² applications. **Snedecor and Cochran (1989)** is the recommended statistical reference for χ². The **ModApte split** of Reuters-21578 is curated by David D. Lewis from **Apté et al. (1994)**. **Lewis et al. (2004)** benchmark SVM > kNN > Rocchio on RCV1. **Perkins et al. (2003)** and **Joachims (2006a)** discuss the super-linear training cost of methods that beat NB — the very price one pays to leave the NB baseline behind. **Domingos and Pazzani (1997)** explain why NB classifies well despite biased probability estimates.

## Algorithms & Formulas

### Multinomial NB — MAP classification rule

  c_map = argmax_{c∈ℂ} [ log P̂(c) + Σ_{1≤k≤n_d} log P̂(t_k | c) ]

with empirical estimates

  P̂(c) = N_c / N
  P̂(t|c) = (T_{ct} + 1) / ( Σ_{t′∈V} T_{ct′} + |V| )       ← add-one (Laplace) smoothing

Training:  Θ( |𝔻| · L_ave + |ℂ| · |V| )
Testing:   Θ( |ℂ| · M_a )        ← M_a = distinct tokens in test document

### Bernoulli NB — MAP classification rule

  c_map = argmax_{c∈ℂ} [ log P̂(c) + Σ_{t∈V} ( e_t · log P̂(t|c) + (1−e_t) · log(1 − P̂(t|c)) ) ]

with

  P̂(t|c) = (N_{ct} + 1) / (N_c + 2)        ← Laplace smoothing, B′ = 2

### Mutual information (information gain)

  I(U; C) = Σ_{e_u ∈ {0,1}} Σ_{e_c ∈ {0,1}} P(U=e_u, C=e_c) · log₂ [ P(U=e_u, C=e_c) / ( P(U=e_u) · P(C=e_c) ) ]

Closed form using observed counts N_{e_te_c} with N = N₁₁ + N₁₀ + N₀₁ + N₀₀:

  I(U; C) = (N₁₁/N) log₂(N·N₁₁ / ((N₁₁+N₁₀)(N₁₁+N₀₁)))
          + (N₀₁/N) log₂(N·N₀₁ / ((N₀₁+N₀₀)(N₁₁+N₀₁)))
          + (N₁₀/N) log₂(N·N₁₀ / ((N₁₁+N₁₀)(N₁₀+N₀₀)))
          + (N₀₀/N) log₂(N·N₀₀ / ((N₀₁+N₀₀)(N₁₀+N₀₀)))

### χ² independence test for term t and class c

  X²(t, c) = Σ_{e_t ∈ {0,1}} Σ_{e_c ∈ {0,1}} (N_{e_te_c} − E_{e_te_c})² / E_{e_te_c}

Simplified form (Eq. 137):

  X²(t,c) = ( (N₁₁+N₁₀+N₀₁+N₀₀) · (N₁₁ · N₀₀ − N₁₀ · N₀₁)² )
            / ( (N₁₁+N₀₁) · (N₁₁+N₁₀) · (N₁₀+N₀₀) · (N₀₁+N₀₀) )

Critical thresholds (1 df): 3.84 at α=0.05, 6.63 at α=0.01, 10.83 at α=0.001.

### Micro- vs. macro-averaging

Macro-averaged F₁:        F₁_macro = (1/J) Σ_{c∈ℂ} F₁(c)
Micro-averaged F₁:        compute (TP, FP, FN) summed over all classes, then
                          P_micro = ΣTP / Σ(TP+FP),  R_micro = ΣTP / Σ(TP+FN),
                          F₁_micro = 2·P_micro·R_micro / (P_micro + R_micro)

## Key Quotes

> "Even though the probability estimates of NB are of low quality, its classification decisions are surprisingly good." — §13.5 Properties of Naive Bayes

> "Correct estimation implies accurate prediction, but accurate prediction does not imply correct estimation." — §13.5

> "High accuracy on the training set in general does not mean that the classifier will work well on new data in an application." — §13.1

> "As long as χ² feature selection only ranks features with respect to their usefulness and is not used to make statements about statistical dependence or independence of variables, we need not be overly concerned that it does not adhere strictly to statistical theory." — §13.7.3

> "Macroaveraging gives equal weight to each class, whereas microaveraging gives equal weight to each per-document classification decision." — §13.8

> "Using a carefully selected subset of the features results in better effectiveness than using all features." — §13.7, on Reuters-RCV1 MI selection

## Connections

- [[InformationRetrieval]] — Ch. 13 begins the supervised-learning half of IR; classification complements ad hoc ranking by addressing recurring/standing information needs.
- [[NaiveBayes]] — chapter is the canonical NB-for-text reference; introduces the two textbook variants.
- [[TextClassification]] — the chapter is the foundational textbook treatment; defines γ: 𝕏 → ℂ, one-of vs any-of, training/test split.
- [[MultinomialNaiveBayes]] — Eq. 122–128: sequence-of-tokens generative model, MAP rule, Laplace smoothing with B′ = |V|, Θ(|𝔻|L_ave + |ℂ||V|) training.
- [[BernoulliNaiveBayes]] — §13.3 / Fig. 13.3: binary presence-vector model, smoothing with B′ = 2, models term *absence* explicitly, weaker on long documents.
- [[LaplaceSmoothing]] — add-one MAP estimator used by both NB variants to neutralize zero-count terms; relates to add-½ in probabilistic relevance feedback.
- [[MutualInformation]] — also known as information gain; primary univariate feature-selection criterion; closed form over a 2×2 contingency table.
- [[ChiSquareTest]] — alias of [[ChiSquaredTest]]; statistical independence test repurposed as feature ranker, sensitive to rare terms.
- [[FeatureSelection]] — chapter §13.5 frames the noise-vs-signal trade-off; greedy, univariate methods (MI, χ², frequency).
- [[MicroAveraging]] — pooling-then-metric multi-class evaluation; equal weight per document decision.
- [[MacroAveraging]] — metric-per-class-then-averaging multi-class evaluation; equal weight per class.
- [[Reuters21578]] — 21,578 newswire articles, 118 topic categories, ModApte split = 9,603 train / 3,299 test; standard 2008 benchmark.
- [[BernoulliDistribution]] — underlying random variable model for the Bernoulli NB variant.
- [[InformationTheory]] — Shannon-style MI definition borrowed wholesale for the feature-ranking task.
- [[LanguageModel]] — §13.2.1 shows multinomial NB ≡ multinomial unigram LM with documents/queries roles swapped.
- [[ThomasBayes]] — 18th-century namesake; theorem published posthumously 1763.

## Contradictions

No direct contradictions detected with existing wiki pages. Two tensions worth flagging:

- The chapter's claim that NB classification decisions are "surprisingly good" despite poor probability calibration sits alongside any wiki pages that present NB as a *probabilistically sound* model — both can be true, but pages should distinguish *estimation quality* from *argmax-decision quality* (Domingos & Pazzani 1997).
- The chapter uses **"mutual information"** in the binary-term/binary-class sense (also called information gain) — slightly different in spirit from the continuous Shannon MI definition that may appear elsewhere in [[MutualInformation]] or [[InformationTheory]]. The formula is consistent; only the random-variable domain differs.
