---
title: "CS324 — Scaling Laws"
type: source
tags: [cs324, llm, course-lecture, scaling]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/scaling-laws/
---

## Summary
Week 6 of Stanford's CS324 (Winter 2022, "Large Language Models") on [[ScalingLaws]] — simple, predictive power-law rules that map data, model size, and compute to model loss/error. The lecture is organized simple-to-complex across three themes: (1) **data scaling** (loss is linear in log-log against dataset size, with a conceptual grounding that estimation error decays polynomially as 1/n^α, where the exponent is tied to the data's *intrinsic dimensionality*); (2) **model engineering** (use scaling laws fit on small models to choose optimizers, depth, and architecture, and to make compute/data tradeoffs before paying for huge runs); and (3) **forecasting** (extrapolating per-task scaling curves from [[GPT-3]] to ask which capabilities can be "brute-forced" by more compute). It reproduces the [[2001.08361-scaling-laws|Kaplan et al. 2020]] exponents and motivates the field's scale-up trajectory while flagging phase transitions as the "big unknown."

## Key Claims
- **Scaling laws are simple, predictive power laws.** The pitch: instead of the "old and unpleasant" practice of tuning hyperparameters on big models, "tune on small models, extrapolate to large ones." A [[PowerLaw]] is linear on a log-log plot ("scale-free").
- **Three headline language-model power laws** (from [[2001.08361-scaling-laws|Kaplan et al. 2020]]): loss vs dataset size `L = (D / 5.4·10^13)^(-0.095)`; loss vs non-embedding parameters `L = (N / 8.8·10^13)^(-0.076)`; loss vs compute `L = (C_min / 2.3·10^8)^(-0.050)`. The teaser compute-vs-loss fit (from [[GPT-3|Brown et al. 2020]]) is `L = 2.57·C^(-0.048)` over PetaFLOP/s-days.
- **Data scaling laws hold across domains:** machine translation (Hestness 2017, `ε(m)=3.87 m^(-0.13)`), speech (attention `ε(m)=0.95 m^(0.30)`), language modeling (Kaplan 2020), and object recognition (Rosenfeld 2020). Known since at least Kolachina+ 2012 (MT) and [[Hestness2017|Hestness+ 2017]] (neural).
- **Why power laws appear — the theory.** Estimation error naturally decays polynomially. Toy proof: estimating a Gaussian mean gives `E[(μ̂−μ)²] = σ²/n`, i.e. `log(Error) = −log n + 2 log σ` — already a 1/n scaling law. Any rate `1/n^α` is a scaling law.
- **Neural exponents are mysteriously shallow.** Classical models (regression) scale as `1/n` (slope −1), so we'd expect `y = −x + C`; observed neural slopes are much shallower. Explanation via nonparametric learning: partitioning d-dimensional space yields `Error = n^(−1/d)`, so the slope is `−1/d` — flexible learning has **dimension-dependent** scaling.
- **Intrinsic-dimensionality theory:** the slope α is tied to the *intrinsic dimensionality* of the data (Bahri+ 2021 verify this empirically; `4/α_D` scales roughly linearly with dimension across CIFAR-10/100, SVHN, MNIST, FashionMNIST).
- **Data composition shifts the offset, not the slope.** Distribution-shift scaling laws (Kaplan+ 2021 across WebText2, Books, Wikipedia, Common Crawl; Hashimoto 2021) argue for collecting diverse data; minority-subgroup performance also follows a scaling law (Rolfe+ 2021), so scaling laws can optimize data collection for fairness.
- **Hyperparameters can be chosen before training the big model** via the procedure: (1) train a few smaller models, (2) establish a scaling law, (3) pick the optimal hyperparameter from the law's prediction — applied to optimizer choice, model depth, and architecture.
- **[[Transformer|Transformers]] asymptotically beat [[LSTM|LSTMs]].** On test-loss-vs-parameters, Transformers keep a sustained, steeper slope while 1/2/4-layer LSTMs plateau — so you don't need to "spend tens of millions to train an LSTM GPT-3" to know the answer.
- **Optimizer and depth findings:** Adam slightly beats SGD on depth-10 RHNs (`5.25 m^(-0.095)` vs `5.37 m^(-0.094)`, Hestness 2017). 1-vs-2 layers matters a lot; beyond ~6 layers there are diminishing returns below 10^7 params. Scaling laws can also "lead us astray" — depth-efficiency arguments (Levine+ 2021) drove [[Jurassic-1]]'s architecture (J1-Jumbo: 178B, 76 layers, d_model 13824, vs GPT-3 175B: 96 layers, d_model 12288).
- **Joint data–model scaling laws.** Rosenfeld+ 2020: `Error = n^(−α) + m^(−β) + C`; Kaplan+ 2021: `Error = [m^(−α) + n^(−1)]^β`. Both extrapolate accurately from small-data/small-model fits (e.g. ImageNet, WikiText-103). Optimize `n^(−α)+m^(−β)+C` against your costs to trade off data vs model size.
- **Data adequacy and compute-optimal allocation.** Fitted laws suggest a 22B-token WebText can support ~10^9 parameters; model size should scale as `O(m^0.74)`. For a fixed compute budget, **"properly undertrained models are better"** — i.e. train big models and stop short of convergence. Compute-optimal allocation: `N = (1.3·10^9)·C_min^0.73` and steps `S_min = (5.4·10^3)·C_min^0.03` (steps barely grow → favorable for data-parallel / huge batches). Cross-reference [[ComputeEfficientTraining]].
- **Not all parameters are equal (effective dimensionality).** Counting parameters *with* embeddings distorts the trend; the clean laws hold for *non-embedding* parameters. Related: scaling laws for [[MixtureOfExperts]].
- **Forecasting capabilities by extrapolation.** Build a per-capability scaling law and extend the line. [[GPT-3]] hits 77% on Winograd after 50 examples; extrapolating Winogrande suggests roughly **64× more parameters** for human-level. SAT analogies show clean log-linear scaling; **WiC** (word-in-context, a pairwise-comparison task) scales near-zero.
- **Phase transitions are the "big unknown."** Few-shot arithmetic in GPT-3 shows sudden discontinuous jumps (e.g. around 13B–175B) rather than smooth log-linear gains. Some tasks improve continually with scale; others show emergent jumps — see [[EmergentAbilities]].

## Key Quotes
> "Old and unpleasant: tune hyperparameters on big models. New and exciting: tune on small models, extrapolate to large ones." — framing of the whole lecture

> "Scaling laws tell us: properly undertrained models are better." — compute-tradeoffs slide, the compute-optimal-training takeaway

> "The effect of hyperparameters on big LMs can be predicted before training!" — surprising-takeaways slide

> "If the scaling law holds.. Roughly 64 times more parameters will get us to human-level." — Winogrande forecasting slide

> "Do we expect to see more phase transitions? This is probably the 'big unknown' in LM scaling!" — phase-transitions slide

## Connections
- [[ScalingLaws]] — the central concept; this lecture is the course's teaching of it, spanning data, model, and compute scaling plus forecasting.
- [[2001.08361-scaling-laws]] — the Kaplan et al. 2020 paper whose exponents (α_N=0.076, α_D=0.095, etc.) and compute-optimal findings the lecture reproduces; this page is the lecture, not a duplicate of the paper.
- [[PowerLaw]] — the functional form underlying every law discussed (linear in log-log).
- [[ComputeEfficientTraining]] — the "train big, stop short of convergence" / compute-optimal allocation conclusion.
- [[GPT-3]] — source of the capability-forecasting curves (Winogrande, SAT analogies, WiC, few-shot arithmetic phase transitions); Brown+ 2020 supplies the compute-vs-loss teaser fit.
- [[Transformer]] — shown to asymptotically dominate LSTMs on the scaling curve.
- [[LSTM]] — the recurrent baseline that plateaus relative to Transformers.
- [[EmergentAbilities]] — the lecture's "phase transitions" (sudden, discontinuous capability jumps) are the precursor framing for emergent abilities.
- [[MixtureOfExperts]] — flagged as related work on scaling laws beyond dense parameter counts.
- [[Jurassic-1]] — AI21's models (Levine+ 2021) cited as a case where depth-efficiency scaling arguments shaped architecture vs GPT-3.
- [[Hestness2017]] — foundational neural data-scaling work cited for MT, speech, and Adam-vs-SGD curves.
- [[OpenAI]] — origin of the Kaplan et al. and GPT-3 scaling results that anchor the lecture.
- [[Stanford]] — CS324 is a Stanford course (Winter 2022).

## Contradictions
- **Tension with the [[Chinchilla]] / Hoffmann et al. 2022 line (not yet published at lecture time).** This lecture, following Kaplan, concludes that under a fixed compute budget you should train **very large models and undertrain them** (model size `~C^0.73`, steps `~C^0.03`), and that ~22B tokens suffice for ~10^9 params. The later Chinchilla result argues compute-optimal training scales **parameters and tokens roughly equally** (~1:1), implying Kaplan-style models were *over-parameterized and under-trained on data*. The lecture predates Chinchilla and does not address this; the existing paper page [[2001.08361-scaling-laws]] already notes this forthcoming revision in its caveats. No contradiction with any other current wiki page.
