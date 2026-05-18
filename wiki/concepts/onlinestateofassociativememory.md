---
title: "Online State of Associative Memory (OSAM)"
type: concept
tags: [concept, memory, associative-memory, online-learning]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# Online State of Associative Memory (OSAM)

Fixed-size matrix $\mathbf{S}_t \in \mathbb{R}^{r \times r}$ that compactly stores key→value associations from streaming history, introduced as the memory substrate of [[deltamem|δ-mem]] in [[2605.12357-delta-mem]].

## Definition
Given a memory key $\mathbf{k}_t \in \mathbb{R}^r$ and value $\mathbf{v}_t \in \mathbb{R}^r$ at position $t$, $\mathbf{S}_t$ stores the association $\mathbf{k}_t \mapsto \mathbf{v}_t$ such that the prediction by the previous state is $\hat{\mathbf{v}}_t = \mathbf{S}_{t-1}\mathbf{k}_t$. Updated via [[gateddeltarule|gated delta-rule learning]] — viewable as SGD on the online regression loss $\mathcal{L}_t(\mathbf{S}) = \frac{1}{2}\|\mathbf{S}\mathbf{k}_t - \mathbf{v}_t\|^2$.

## Properties
- **Read cost independent of history length.** Querying $\mathbf{S}_{t-1}$ is a single $r \times r$ matvec regardless of how many tokens were absorbed.
- **Lossy by design.** Multiple writes overwrite/superpose along key directions; the gated forget term $\boldsymbol{\lambda}_t$ controls retention.
- **Continuous, not text.** The state is never serialized back into the context window — it is read as a vector and projected into [[lowrankattentioncorrection|attention corrections]].

## Relationship to other "memory states"
- vs **KV cache.** A KV cache grows with sequence length; OSAM is fixed-size and lossy.
- vs **[[lstm|LSTM]] hidden state.** Both are fixed-size recurrent; OSAM's update is the matrix delta-rule, not a gated nonlinear cell.
- vs **prefix / [[parammem|LoRA]].** Those are static post-training; OSAM evolves per-position at inference.
- vs **vector store / [[rag|RAG]].** OSAM is associative recall on a single matrix; RAG is exact-text top-k retrieval.

## Scale used in practice
$r = 8$ in [[2605.12357-delta-mem]] (matrix is $8 \times 8$), yielding < 0.5% backbone parameter overhead. The fact that such a small state suffices is the paper's signature empirical claim.
