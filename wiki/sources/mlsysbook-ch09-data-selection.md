---
title: "Machine Learning Systems (mlsysbook Vol 1) — Ch 9: Data Selection"
type: source
tags: [book, ml-systems, mlsysbook, data-selection, data-efficiency, coreset, active-learning, curriculum-learning, self-supervised, synthetic-data, data-wall]
date: 2026-06-05
sources: []
source_file: raw/mlsysbook-vol1/mlsysbook-ch09-data-selection.qmd
last_updated: 2026-06-05
---

# Machine Learning Systems (mlsysbook Vol 1) — Ch 9: Data Selection

## Summary

Chapter 9 opens the **Optimize** part (Ch 09–12) of [[VijayJanapaReddi|Vijay Janapa Reddi]]'s *Machine Learning Systems* ([[Harvard]], mlsysbook.ai, 2026) by arguing that the highest-leverage optimization runs *upstream of any gradient*: on the data itself. Its thesis is that large datasets are massively heterogeneous — a tiny fraction of examples supplies most of the gradient signal while the rest is redundant, noisy, or misaligned — so [[DataSelection|data selection]] is the "D" pillar of the [[DAMTaxonomy|D·A·M taxonomy]] (Data → Algorithm → Machine) and the only lever that shrinks the *total operations* $(O)$ term of the [[IronLawOfMLSystems|iron law]] at its source. The motivating force is the **[[DataWall|Data Wall]]**: GPU compute grows ~10× / 3 years while high-quality web text grows only ~2× / 5 years (labels ~1.5× / 5 years), so the field has become *compute-rich and data-poor*, inverting the priority from "get more data" to "get more from existing data." The chapter formalizes value with the **[[InformationComputeRatio|Information-Compute Ratio]] (ICR = ΔI/ΔFLOPs)** and shows that in redundant data $I(D)\sim\log D$ while cost is linear, so past the "ICR frontier" data becomes a **data tax**.

The engineering content is a three-stage pipeline that each raises ICR by a different mechanism: **(1) [[StaticDataPruning|static pruning]]** before training ([[CoresetSelection|coresets]] via [[EL2N]]/[[GraNd]]/[[ForgettingEvents|forgetting events]]/k-Center/Herding; [[DataDeduplication|deduplication]] via [[MinHash]]/[[LocalitySensitiveHashing|LSH]]/[[CLIP]] embeddings; quality pruning via [[Cleanlab]]-style label-error and [[Perplexity|perplexity]] filtering), **(2) [[DynamicDataSelection|dynamic selection]]** during training ([[CurriculumLearning|curriculum learning]], [[ActiveLearning|active learning]], [[SemiSupervisedLearning|semi-supervised]] [[PseudoLabeling|pseudo-labeling]]/[[ConsistencyRegularization|consistency regularization]]/[[FixMatch]]), and **(3) [[SyntheticDataGeneration|synthetic generation]]** on demand ([[DataAugmentation|augmentation]] incl. [[MixUp]]/[[CutMix]]/[[Cutout]]/[[RandAugment]]/[[AutoAugment]]/[[BackTranslation|back-translation]]; generative synthesis via [[GenerativeAdversarialNetwork|GANs]]/[[DiffusionModel|diffusion]]/simulators; [[KnowledgeDistillation|distillation]] as enriched soft labels). It crowns the progression with **[[SelfSupervisedLearning|self-supervised learning]]** and the **[[FoundationModel|foundation-model]] paradigm**, framing them economically via *cost amortization* ("pretrain once, fine-tune many").

The chapter is unusually systems-honest about the *cost of selection itself*. It introduces the **[[SelectionInequality|Selection Inequality]]** $(T_{\text{selection}}+T_{\text{train}}(\text{subset})<T_{\text{train}}(\text{full}))$, the **random-access I/O penalty**, **[[DataEchoing|data echoing]]**, a full **[[DataSelectionCostModel|cost model]]** ($C_{\text{total}}=C_{\text{acquire}}+C_{\text{label}}+C_{\text{store}}+C_{\text{process}}$) with ROI / break-even / amortization analysis, **distributed selection** (centralized vs hierarchical vs approximate; the "coordination tax"), cross-layer interactions with [[ModelCompression|compression]]/hardware/distributed training, a measurement framework (PPD, AULC, DCR, the [[ChinchillaScalingLaw|Chinchilla]] compute-optimal frontier and D/P-ratio diagnostic), and a dense Fallacies & Pitfalls section. It closes by handing off to Ch 10 (model compression).

## Key Claims

- **Data selection is the only iron-law lever that reduces the total-operations term at its source.** [[ModelCompression|Model compression]] reduces $O$ per forward/backward pass; hardware acceleration raises peak throughput $R_{\text{peak}}$ and utilization $\eta_{\text{hw}}$; data selection reduces the *number of passes through the entire equation*. Effects are **multiplicative**: 2× dataset reduction × 2× compression × 2× hardware = **8× total cost reduction, not 6×**.
- **The Data Wall is a supply constraint, not an economic one.** GPU compute grows ~10× / 3 yr; training web text ~2× / 5 yr; labeled data ~1.5× / 5 yr; synthetic data is "unbounded" but bounded by generator quality (risk of [[ModelCollapse|model collapse]]). [[EpochAI|Epoch AI]] projected high-quality public text exhaustion on a near-term (years, not decades) horizon. Marked corpus milestones: GPT-3 (~3×10¹¹ tokens, 2020), Chinchilla (~1.4×10¹² , 2022), Llama 2 (~2×10¹², 2023), Llama 3 (~1.5×10¹³, 2024).
- **Training on *less* data often matches the full dataset.** On CIFAR-10, gradient-based selection ([[EL2N]], [[GraNd]]; Paul et al. 2021) matches full accuracy with **50%** of samples; aggressive pruning to **10–30%** retains 90%+ performance. [[ImageNet|ImageNet-1K]] is less redundant: a self-supervised prototype metric discards only ~20% without loss (Ganguli et al. 2022). Web corpora ([[ThePile|The Pile]], [[C4]]) show **10–30% near-duplicate ratios** (Lee et al. 2022).
- **The Data Quality Multiplier: one clean label ≈ 100 noisy ones.** Clean-data convergence scales $\mathcal{O}(1/N)$, noisy $\mathcal{O}(1/\sqrt N)$; to reach 1% error, clean needs ~100 samples and noisy ~10,000 — a **100× compute accelerator** from cleaning.
- **Coreset trade-off is selection-quality vs scoring cost.** Geometry methods (k-Center $\mathcal{O}(D^2)$/$\mathcal{O}(DK)$, Herding $\mathcal{O}(DK)$) need no training but ignore labels; gradient methods (GraNd/EL2N $\mathcal{O}(\text{epochs}\times D)$, Forgetting Events $\mathcal{O}(\text{full training})$) target the decision boundary but need a **proxy model**. Crucially, scores **transfer across architectures** (ResNet-18 → ResNet-50), so a 5-epoch proxy curates data for a 90-epoch run. Worked EL2N coreset on ImageNet: 50% coreset → **~1.8× higher ICR** (~nearly 2× learning per FLOP) for ~0.5 pp accuracy.
- **Deduplication is the highest-ROI, lowest-risk technique.** Exact dedup via MD5/SHA-256 hashing is $\mathcal{O}(D)$ and trivially parallel; near-dup via [[MinHash]]+[[LocalitySensitiveHashing|LSH]] approximates [[JaccardSimilarity|Jaccard]] (threshold ~0.8 catches near-dups, <0.5 collapses diversity); images use perceptual hashing or [[CLIP]] embeddings (CLIP ~100× costlier/sample). Dedup yields both fewer wasted FLOPs and **better generalization via less memorization**. DLRM variant: 20% fewer unique interactions → **30–40% smaller embedding tables** (memory-capacity bound, not compute).
- **Curriculum learning's gains are inversely proportional to data quality.** Easy-to-hard ordering acts as a continuation method smoothing the nonconvex loss landscape; measured epoch reductions: CIFAR-10 (115 vs 150, ~23%), CIFAR-100 self-paced (180 vs 220, ~18%), **ImageNet only 80 vs 90 (~11%)** because it's less redundant; MentorNet noisy ~22%. Gains manifest as *faster convergence*, not higher final accuracy. Anti-curriculum and self-paced often match hand-designed curricula.
- **Active learning is a financial optimization: 10–100× labeling-cost reduction.** It chooses which unlabeled samples are *worth labeling at all* (uncertainty sampling, query-by-committee, expected model change, diversity sampling). Medical-imaging ROI: 1M scans at $5/label = $5M (10× over a $500K budget); active learning needs ~50K labels = $250K, a **$4.75M saving and ~20× speedup**; ~4× fewer *samples* to hit 90% accuracy than random.
- **Semi-supervised learning reaches 80–95% of supervised accuracy with 10–20% of labels** by pushing decision boundaries into low-density regions of $p(x)$. [[FixMatch]] on CIFAR-10: 250 labels (25/class) → 94.9% (within ~1.2 pp of 96.1% full supervision) = **200× label efficiency**, at ~5× more compute; 40 labels still → 88.6%. Failure modes: OOD unlabeled data, severe class imbalance (pseudo-labels amplify majority bias), uncovered classes.
- **Self-supervised pretraining breaks the label asymptote and restructures economics.** Pretext tasks (masked LM, next-token, contrastive, masked autoencoding, CLIP alignment) derive supervision from data structure. Pretraining can cost **>10,000× a single fine-tune** but is amortized across thousands of tasks: 10-task example → labeling drops **100×**, per-task marginal compute **20×**, deployment 20–50× faster; crossover ~11 tasks. [[FoundationModel|Foundation models]] create a single point of failure — pretraining-data defects propagate to thousands of downstream deployments (homogenization risk).
- **Synthetic data is a supplement, not a replacement.** Augmentation is cheapest ([[Cutout]] ~1–2 pp on CIFAR; [[CutMix]] ~1% ImageNet top-1; [[AutoAugment]] cost **15,000 GPU-hours**, displaced by [[RandAugment]]'s 2 hyperparameters; [[BackTranslation|back-translation]] 100–1000× slower, precomputed offline). Generative synthesis ([[GenerativeAdversarialNetwork|GANs]], [[DiffusionModel|diffusion]]/[[StableDiffusion]] ~2–5 s/image ≈1000× slower, simulators like [[CARLA]]). Best mixes are **50–80% synthetic + 20–50% real**; pure synthetic fails via the **[[DomainGap|domain gap]]** (webcam→DSLR loses 20–40% accuracy) and **[[ModelCollapse|model collapse]]** (Shumailov et al. 2024: diversity <50% by generation 5).
- **Selection isn't free — the Selection Inequality gates every technique.** Scoring 1M images with a full ResNet-50 (~2.8 hr) can negate a 10% coreset; a ResNet-18 proxy (~0.6 hr) preserves ~90% savings. Rule: **selection time should stay below ~10% of full-training time** and must be smaller than the compute saved.
- **The random-access penalty is the hidden cost.** Dynamic selection jumps across the dataset; sequential reads enjoy readahead/page-cache, random reads collapse throughput — extreme on HDD and cloud S3. Mitigations: small proxy models, [[FAISS]] ANN indices, sharded formats (WebDataset/FFCV), and shuffle buffers.
- **[[DataEchoing|Data echoing]] recovers idle GPU cycles** when the CPU pipeline is the bottleneck (ratio $R=T_{\text{pipeline}}/T_{\text{GPU}}>1$): reuse each batch $e$ times with fresh augmentations (upstream echoing). Choi et al. 2020 measured a **3.25× speedup** on ResNet-50/ImageNet over network; echoed samples are worth ~70–90% of fresh ones; above ~4× the model memorizes.
- **Data costs often dominate compute.** $C_{\text{total}}=C_{\text{acquire}}+C_{\text{label}}+C_{\text{store}}+C_{\text{process}}$; labeling spans **$0.10–$100/sample** (crowd vs expert) — three orders of magnitude. ImageNet-scale supervised example: ~81% data vs ~19% compute (inverts for SSL on web data). Deduplication infra ($55K) is a net loss at 1 run but **highly profitable across 50 runs**; high-reuse, broad-transfer techniques amortize best.
- **Compute-optimal frontier & Chinchilla diagnostic.** [[ChinchillaScalingLaw|Chinchilla]] (70B params, 1.4T tokens) beat GPT-3 (175B, 300B tokens) — prescribing ~**20 tokens/parameter**. D/P-ratio diagnostic: <10 = data-starved, ~20 = optimal, >40 = diminishing; GPT-3 ≈ 1.7 (chronically undertrained), Llama-2-70B ≈ 28.6. Because $D_{\text{opt}}\propto\sqrt C$, doubling compute needs only ~41% more tokens — yet even that outpaces human-text supply. Quick test: train 2× longer; improvement ⇒ compute-starved, plateau ⇒ data-starved.
- **Cross-layer multiplicative effect & sparsity trap.** Models trained on 50% EL2N coresets quantize to INT4 with **2% less accuracy loss** (cleaner weight distributions). But the **sparsity latency trap**: a 99% FLOP reduction can yield 0% latency reduction on dense-optimized GPUs/TPUs — *FLOPs are not latency* (Hooker 2020).
- **War story — the benchmark replication gap (Recht et al. 2019).** New CIFAR-10/ImageNet test sets built with the original methodology dropped accuracy **3–15 pp (CIFAR-10)** and **11–14 pp (ImageNetV2)**; inflated benchmark accuracy inflates ROI projections, so evaluation data must be deduplicated against training data too.

## Key Quotes

> "Why can a carefully selected 10 percent of your data match the accuracy of 100 percent?" — the chapter's opening question (Purpose)

> "The shift is paradigmatic: from accumulating data as a massive liability to curating it as a precise resource, where every sample earns its place." — Purpose

> "Data selection is the only technique that reduces the total operations term at its source." — on the iron law

> "Beyond the frontier, adding more data yields near-zero learning but still costs linear compute. In this regime, data is no longer an asset; it is a data tax." — on the ICR frontier

> "Cleaning the dataset (removing label noise) is a 100× compute accelerator." — the Data Quality Multiplier

> "Data selection is not free. It introduces a new term to the iron law." — the Selection Inequality checkpoint

> "FLOPs are not latency. A 99 percent reduction in operations can yield a 0 percent reduction in time if the remaining operations are memory bound." — the sparsity latency trap (after Hooker 2020)

> "GPT was trained to predict the next token in a sequence. BERT was trained to fill in masked tokens. Neither task required a single human label." — opening the self-supervised section

> "Curate, do not accumulate." — chapter takeaways title

## Connections

- [[VijayJanapaReddi]] — author; [[Harvard]] — host institution / mlsysbook.ai publisher.
- [[DataSelection]] — the parent concept this chapter most fully develops; extends the Ch 1 / Ch 4 framing into a full engineering discipline and three-stage pipeline.
- [[IronLawOfMLSystems]] — data selection reduces the $O$ term; multiplicative with compression and hardware.
- [[DAMTaxonomy]] — data selection is the "D" pillar, applied first ("highest leverage first").
- [[DataWall]] — the supply-side constraint motivating the chapter (NEW).
- [[InformationComputeRatio]] — the central metric ICR = ΔI/ΔFLOPs and its diminishing-returns frontier (NEW).
- [[StaticDataPruning]] / [[DynamicDataSelection]] — stages 1 and 2 of the pipeline (NEW).
- [[CoresetSelection]] — k-Center, Herding, GraNd, EL2N, Forgetting Events; proxy-model transfer (NEW).
- [[EL2N]] / [[GraNd]] / [[ForgettingEvents]] — gradient/training-dynamics scoring methods (NEW).
- [[DataDeduplication]] — exact + near-duplicate removal; elevated here from a pipeline stage to an optimization lever.
- [[MinHash]] / [[LocalitySensitiveHashing]] / [[JaccardSimilarity]] — near-duplicate detection machinery (LSH, Jaccard NEW).
- [[DataPruning]] — quality pruning (label-error detection, outlier removal, perplexity filtering).
- [[CurriculumLearning]] — easy-to-hard ordering, pacing functions, self-paced / anti-curriculum (NEW).
- [[ActiveLearning]] — uncertainty/diversity querying; this chapter adds the medical-imaging ROI and the selection-cost caveat.
- [[UncertaintySampling]] — the dominant active-learning query strategy (NEW).
- [[SemiSupervisedLearning]] — pseudo-labeling, consistency regularization, label propagation.
- [[PseudoLabeling]] / [[ConsistencyRegularization]] / [[FixMatch]] — semi-supervised techniques (NEW).
- [[SelfSupervisedLearning]] — pretext tasks that break the label asymptote.
- [[FoundationModel]] / [[FoundationModels]] — the amortization paradigm; homogenization risk.
- [[Pretraining]] / [[FineTuning]] / [[TransferLearning]] — the cost-amortization mechanism ("pretrain once, fine-tune many").
- [[CostAmortization]] — pretraining cost spread across downstream tasks (NEW).
- [[ContrastiveLearning]] / [[MaskedLanguageModeling]] — SSL pretext tasks (SimCLR/MoCo, BERT-style).
- [[SyntheticData]] / [[SyntheticDataGeneration]] — stage 3; supplement-not-replacement framing.
- [[DataAugmentation]] — transformation-based synthesis.
- [[MixUp]] / [[CutMix]] / [[Cutout]] / [[RandAugment]] / [[AutoAugment]] / [[BackTranslation]] — augmentation methods (most NEW; BackTranslation exists).
- [[GenerativeAdversarialNetwork]] / [[DiffusionModel]] / [[StableDiffusion]] — generative synthesis engines.
- [[CARLA]] — simulator for autonomous-driving synthetic data with perfect ground truth.
- [[DomainGap]] / [[DomainRandomization]] / [[DomainAdaptation]] — bridging synthetic↔real distributions (Gap & Randomization NEW).
- [[ModelCollapse]] — recursive synthetic-training degradation (Shumailov et al. 2024).
- [[KnowledgeDistillation]] — "dark knowledge"; here a *data-selection* technique that raises information density per sample; complements its Ch 10 compression treatment.
- [[GeoffreyHinton]] — coined "dark knowledge"; distillation originator.
- [[SelectionInequality]] — the systems gate on every dynamic technique (NEW).
- [[DataEchoing]] — amortizing CPU-bound pipeline stalls by reusing batches (NEW).
- [[FAISS]] — ANN index that makes embedding-based selection tractable at web scale.
- [[CLIP]] — semantic deduplication and image-text alignment pretext task.
- [[DataSelectionCostModel]] — total-cost / ROI / break-even / amortization framework (NEW).
- [[SamplesPerDollar]] — the cost-efficiency sibling metric from earlier chapters.
- [[ChinchillaScalingLaw]] — compute-optimal frontier and the D/P-ratio data-starvation diagnostic.
- [[ScalingLaws]] — power-law loss ($\mathcal{L}\propto D^{-\alpha}$, α≈0.095) underpinning the data-compute asymmetry.
- [[ModelCompression]] / [[Quantization]] / [[Pruning]] — downstream stages; coresets improve compressibility; the sparsity latency trap.
- [[DistributedTraining]] / [[DataParallelism]] — distributed selection challenges and the coordination tax.
- [[DataEngineering]] — the upstream chapter (quality) that data selection (value) builds on.
- [[InformationEntropy]] — the signal-per-byte view of informative samples.
- [[ThePile]] / [[C4]] / [[ImageNet]] / [[CIFAR10]] — corpora/benchmarks used as redundancy and replication evidence.
- [[Cleanlab]] — confident-learning label-error detection for quality pruning.
- [[UCBerkeley]] — Recht et al. benchmark-replication study.
- [[EpochAI]] — data-exhaustion projections (Villalobos et al. 2022).
- [[DataLeakage]] — train/test contamination motivating joint deduplication.
- [[GreenAI]] — halving the dataset halves training energy/CO₂; data selection as the most direct Green-AI lever (NEW).
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch04-data-engineering]] — sibling chapters that seeded [[DataSelection]], [[ActiveLearning]], [[InformationEntropy]].

## Contradictions

- **No direct contradiction with earlier mlsysbook chapters.** Ch 1 and Ch 4 introduced [[DataSelection]] and [[ActiveLearning]] as efficiency levers; this chapter *deepens* rather than revises them, adding the ICR metric, the Selection Inequality, the three-stage pipeline, and the cost model. The [[ActiveLearning]] "compute must be in the budget model" caveat from Ch 4 is reinforced and quantified here.
- **"More data is always better" is explicitly refuted.** The chapter's first Fallacy directly contradicts the folk wisdom (also echoed loosely in some older wiki pages) that scaling data yields proportional gains: 10× data may add only ~4 pp accuracy, and a curated 100K set at 92% can beat a raw 1M set at 88%. Reconcile by treating data value as ICR-dependent, not volume-dependent.
- **Tension with naive [[KnowledgeDistillation]] framing.** Elsewhere in the wiki distillation is a *compression* technique (smaller student); this chapter reframes it as a *data-selection* technique (soft labels carry more information per sample). Both views are correct — the chapter notes Ch 10 covers the compression perspective — but pages should make the dual role explicit.
- **FLOPs-as-proxy-for-speedup caution.** The sparsity latency trap warns that the chapter's own FLOP-savings numbers do not translate one-to-one into wall-clock latency on dense-optimized hardware; quantization/pruning latency claims elsewhere should be read as hardware-dependent.
