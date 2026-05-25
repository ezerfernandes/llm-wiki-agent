---
title: "RNN"
type: concept
tags: [neural-networks, sequence-models, deep-learning]
sources: [madewithml-baselines, madewithml-foundations-recurrent-neural-networks, d2l-recurrent-neural-networks, d2l-recurrent-modern, hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# RNN

**Recurrent Neural Network** — a neural network with [[HiddenState|hidden states]] that capture the dynamics of sequences via recurrent connections. The same parameters are applied at every time step (weight-tied across time), so the parameter count is *independent of sequence length* ([[d2l-recurrent-neural-networks]] §rnn).

## Recurrence

$$\mathbf{H}_t = \phi(\mathbf{X}_t \mathbf{W}_\textrm{xh} + \mathbf{H}_{t-1} \mathbf{W}_\textrm{hh} + \mathbf{b}_\textrm{h}), \quad \mathbf{O}_t = \mathbf{H}_t \mathbf{W}_\textrm{hq} + \mathbf{b}_\textrm{q}.$$

Identical (after concatenation) to a single matmul on $[\mathbf{X}_t, \mathbf{H}_{t-1}]$ with stacked weights — the trick frameworks use under the hood. The [[RecurrentLayer|recurrent layer]] implements this recurrence; the typical activation is $\tanh$.

## Training

- Inputs partitioned into length-$n$ subsequences; targets are the inputs shifted by one ([[TeacherForcing|teacher-forcing]]).
- Loss: per-step softmax + cross-entropy; tracked as [[Perplexity]] = $\exp(\text{avg-CE})$.
- Gradients via [[BPTT|backpropagation through time]] — chain rule on the unrolled graph, weight gradients summed across time steps.
- [[GradientClipping]] (project $\mathbf{g}$ onto $\|\mathbf{g}\|\leq\theta$ ball) is mandatory in practice.

## Pathologies

The BPTT gradient involves powers $(\mathbf{W}_\textrm{hh}^\top)^k$. Eigenvalues $|\lambda|<1$ vanish ([[VanishingGradient]]); $|\lambda|>1$ explode ([[ExplodingGradient]]). Mitigated by [[LSTM]] / [[GRU]] gating (cell-state additivity), and ultimately replaced by [[transformer|Transformers]] which avoid sequential dependence in the forward pass.

## History + status

Popularized by 2010s breakthroughs in handwriting recognition (Graves 2008), machine translation (Sutskever, Vinyals, Le 2014; [[1409.3215-seq2seq]]), and medical diagnoses (Lipton & Kale 2016). Per [[d2l-recurrent-neural-networks]]: "RNNs have recently ceded considerable market share to Transformer models" but remain staple models for sequential modeling.

## Connections

- [[d2l-recurrent-neural-networks]] — canonical pedagogical exposition.
- [[madewithml-foundations-recurrent-neural-networks]] — applied implementation with gated variants.
- [[HiddenState]] / [[RecurrentLayer]] — internal building blocks.
- [[LanguageModel]] / [[CharacterLevelLanguageModel]] — primary application surface.
- [[BPTT]] / [[TruncatedBPTT]] / [[GradientClipping]] — training mechanics.
- [[VanishingGradient]] / [[ExplodingGradient]] — pathologies.
- [[LSTM]] / [[GRU]] — gated successors ([[d2l-recurrent-modern]]).
- [[DeepRNN]] / [[BidirectionalRNN]] — depth and direction architectural axes.
- [[Transformer]] — modern replacement.
- [[1706.03762-attention-is-all-you-need]] — the architectural pivot away from RNNs.
