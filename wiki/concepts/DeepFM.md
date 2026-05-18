---
title: "DeepFM"
type: concept
tags: [recommender-systems, ctr, deep-learning, feature-interactions]
sources: [d2l-recommender-systems]
last_updated: 2026-05-16
---

# DeepFM

**Deep Factorization Machines** ([[HuifengGuo|Guo]], [[RuimingTang|Tang]], Ye & He 2017, *IJCAI*) — fuses a [[FactorizationMachines|FM]] component (for low-order interactions) with a deep [[MultilayerPerceptron|MLP]] component (for high-order interactions and nonlinearities) **in a parallel structure that shares the same embedding table**.

## Architecture

$$\hat{y} = \sigma(\hat{y}^{(\text{FM})} + \hat{y}^{(\text{DNN})})$$

Both branches read from a shared sparse-categorical embedding table $\mathbf{E}\in\mathbb{R}^{(\sum d_f)\times k}$. The FM branch computes the standard $w_0 + \sum w_i x_i + \frac{1}{2}\sum_l((\sum v_{i,l}x_i)^2 - \sum v_{i,l}^2x_i^2)$ score. The DNN branch flattens the per-field embeddings $[\mathbf{e}_1,\ldots,\mathbf{e}_f]$ and runs them through stacked dense + ReLU + dropout layers:

$$\mathbf{z}^{(0)} = [\mathbf{e}_1, \ldots, \mathbf{e}_f], \quad \mathbf{z}^{(l)} = \alpha(\mathbf{W}^{(l)}\mathbf{z}^{(l-1)} + \mathbf{b}^{(l)})$$

Outputs of both branches are summed and squashed via sigmoid.

## vs Wide & Deep

The chapter explicitly positions DeepFM against [[WideAndDeep|Wide & Deep]] ([[GoogleResearch|Cheng et al. 2016]]) — same parallel-fusion spirit (memorization × generalization), but **DeepFM eliminates the manual feature-crossing required for Wide & Deep's wide side** because FM learns the bilinear interactions automatically.

## D2L implementation

- 10-d embeddings, MLP $= [30, 20, 10]$ pyramid, dropout $=0.1$, Adam, $\eta=0.01$, 30 epochs.
- **Outperforms FM** on the chapter's CTR dataset and converges faster.

## Limitations / variants

- Bilinear FM term may be insufficient even with DNN augmentation; **NFM** ([[XiangnanHe|He]] & Chua 2017) instead applies an MLP *over* the FM pairwise interactions (sequential rather than parallel).
- xDeepFM, AutoInt, DCN add further explicit-cross / attention-based variants.

## Connections
- [[FactorizationMachines]] — the FM component.
- [[MultilayerPerceptron]] — the DNN component.
- [[CTRPrediction]] — primary application.
- [[WideAndDeep]] — predecessor architectural pattern.
- [[Embedding]], [[Dropout]] — building primitives.
- [[d2l-recommender-systems]] — source §deepfm.
