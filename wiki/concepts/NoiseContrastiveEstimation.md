---
title: "Noise Contrastive Estimation (NCE)"
type: concept
tags: [nlp, embeddings, approximate-training, estimation]
sources: [d2l-nlp-pretraining]
last_updated: 2026-05-16
---

# Noise Contrastive Estimation (NCE)

A general estimation principle (Gutmann & Hyvärinen 2010) for training **unnormalized probabilistic models** by recasting density estimation as binary classification: distinguish samples from the data distribution $P_{\textrm{data}}$ from samples drawn from a known **noise distribution** $P_{\textrm{noise}}$. Under mild conditions NCE is consistent — the model's normalization constant becomes a free parameter that the classifier learns alongside the model — sidestepping the partition-function intractability that plagues maximum-likelihood training of softmax-over-vocabulary or energy-based models.

In NLP, NCE was the key enabler of large-vocabulary [[Word2Vec|word2vec]] / language-model training before [[NegativeSampling]] simplified it further. [[NegativeSampling]] is **NCE with the noise-probability term dropped** in the loss — fast but no longer a consistent estimator of $\log P(w\mid c)$; it instead learns a discriminator-like score that empirically works well for embedding tasks even if not for density estimation.

See [[d2l-nlp-pretraining]] §approx-training (frames negative sampling as the practical descendant of NCE).
