---
title: "δ-mem"
type: concept
tags: [concept, memory, attention, online-learning]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# δ-mem

Lightweight memory mechanism introduced in [[2605.12357-delta-mem]] that augments a **frozen** Transformer backbone with an [[onlinestateofassociativememory|online state of associative memory (OSAM)]] $\mathbf{S}_t \in \mathbb{R}^{r \times r}$, updated via [[gateddeltarule|gated delta-rule learning]] as tokens arrive. At each position, δ-mem (1) **reads** the previous state with a learned query, (2) generates [[lowrankattentioncorrection|low-rank corrections]] $\Delta\mathbf{q}_t, \Delta\mathbf{o}_t$ added to the frozen backbone's attention query and post-attention output, then (3) **writes** the new key–value pair back into the state.

## Key properties
- **Backbone is frozen.** No parameters of the original Transformer are updated.
- **Memory is non-textual.** The state never re-enters as context tokens; the readout is a continuous vector projected into attention-space corrections.
- **Same projection parameters, different steering.** $\mathbf{W}_q^\Delta, \mathbf{W}_o^\Delta$ are static post-training, but the readout $\mathbf{r}_t = \mathbf{S}_{t-1}\mathbf{q}_t^m$ varies with history — so identical parameters yield different attention adjustments under different histories. This is the main technical distinction from a static [[adapterlayers|LoRA adapter]].
- **Tiny.** $r=8$ ⇒ 4.87M trainable params (0.12% of a Qwen3-4B backbone); $8\times 8$ matrix state.
- **Three [[writinggranularity|writing strategies]]:** Token-State (TSW), Sequence-State (SSW), Multi-State (MSW).

## Position in the memory taxonomy
δ-mem proposes a fourth category alongside the [[memgpt|TMM]] / OMM ([[2604.27707-agentic-memory-is-a-memo|Memorizing Transformers, LongMem]]) / [[parammem|PMM]] split: a runtime-evolving auxiliary state directly coupled with attention computation. Whether this collapses into "OMM with attention fusion" or is genuinely a fourth locus is an open question; see [[2605.12357-delta-mem]] Contradictions section for the tension with the Ω(k²) compositional bound in [[2604.27707-agentic-memory-is-a-memo]].

## Empirical highlights
On Qwen3-4B-Instruct: 1.10× over frozen backbone average, 1.31× on MemoryAgentBench, 1.20× on LoCoMo. Recovers ~6-15% of multi-hop signal on HotpotQA even when the explicit context is removed.
