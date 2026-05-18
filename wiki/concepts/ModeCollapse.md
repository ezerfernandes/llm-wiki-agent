---
title: "Mode Collapse"
type: concept
tags: [generative-model, gan, failure-mode, deep-learning]
sources: [d2l-generative-adversarial-networks]
last_updated: 2026-05-16
---

# Mode Collapse

The dominant pathology of [[generativeadversarialnetwork|GAN]] training: the [[Generator]] $G$ learns to produce only a small subset of data modes — often just one — rather than matching the full data distribution. The discriminator is fooled on the chosen mode, the generator's loss is low, and yet the model has learned almost nothing useful.

## Why it happens

The [[MinMaxGame|minimax objective]] $\min_D \max_G \{\cdots\}$ does not directly require $G$ to *cover* the data distribution — it only requires $G(\mathbf{z})$ to fool $D$. If $G$ can find *one* point that fools $D$, it has solved its local optimization problem regardless of whether the rest of the data distribution is represented. The structural fix would be to optimize a divergence that explicitly penalizes mode dropping (Wasserstein, MMD, energy-based) — most modern GAN variants modify the objective for exactly this reason.

## D2L's framing

[[d2l-generative-adversarial-networks]] §`gan` flags this with the exercise: *"Does an equilibrium exist where the generator wins, i.e. the discriminator ends up unable to distinguish the two distributions on finite samples?"* The question gestures at the gap between the *theoretical* Nash equilibrium ($D \equiv 1/2$, $p_g \equiv p_{\textrm{data}}$) and the *practical* training trajectory where $G$ can fool $D$ on finite-sample two-sample tests without matching the full distribution.

## Diagnostic signs

- Generated samples look fine individually but exhibit very low *diversity*.
- $G$'s loss is low and stable while $D$'s loss oscillates.
- The generator output collapses to a single image or a tiny cluster of nearly-identical images.

## Mitigations (literature; not in D2L §`gan`)

- **Minibatch discrimination** (Salimans et al. 2016) — let $D$ examine relationships *between* samples in a batch, not just individual samples.
- **Unrolled GANs** (Metz et al. 2016) — backpropagate through $k$ future $D$ updates to discourage $G$ from exploiting a stale $D$.
- **Wasserstein loss** (Arjovsky et al. 2017) — replace the BCE objective with an Earth-Mover-distance proxy that has better gradients far from the data manifold.
- **Architectural fixes** — [[BatchNormalization|BN]] (already in [[DCGAN]]), [[Spectral Normalization]] for the discriminator, learning-rate balancing.

## Connections

- [[generativeadversarialnetwork|GAN]] — the framework whose training this pathology defines.
- [[Generator]] / [[Discriminator]] / [[MinMaxGame]] — the structural primitives that admit this failure mode.
- [[DCGAN]] — the architecture where the mitigations (BN + LeakyReLU + Adam $\beta_1=0.5$) make mode collapse rare-but-not-impossible.
- [[d2l-generative-adversarial-networks]] — canonical source (exercise hints at the concept).
- [[DiffusionModel]] — the successor generative-model family whose training is *not* a minimax game and therefore does not exhibit mode collapse (a structural advantage often cited as one reason diffusion replaced GANs in production).
