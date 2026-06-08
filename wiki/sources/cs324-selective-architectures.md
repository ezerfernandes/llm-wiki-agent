---
title: "CS324 — Selective Architectures (Mixture of Experts, Retrieval)"
type: source
tags: [cs324, llm, course-lecture, architecture]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/selective-architectures/
---

## Summary
This Stanford CS324 lecture surveys "selective" architectures that scale language models by having each input activate only a subset of parameters, motivated by network bandwidth becoming the bottleneck when dense Transformers (e.g. GPT-3's 175B params) are split across machines. It covers two families: Mixture-of-Experts (MoE) — sparse gating, top-k routing, load balancing, and trillion-parameter models like Switch Transformer, GLaM, and FacebookMoE — and retrieval-based models — RAG, RETRO — which offload knowledge to an external store. The throughline is the trade-off between FLOPs per input, total parameter count, training stability, and general-purpose capability.

## Key Claims
- Network bandwidth becomes a training bottleneck as models grow and are split across machines; dense Transformers use *all* parameters per input (175B for [[GPT-3]]), motivating architectures where each input activates only a parameter subset.
- [[MixtureOfExperts]] uses a softmax **gating function** g_e(x) = exp(w_e·x) / Σ exp(w_e'·x) over E experts and outputs f(x) = Σ g_e(x) h_θe(x); an **approximate (sparse) gating** g̃(x) zeros out most experts so only activated experts are computed in forward/backward passes, saving FLOPs.
- The **sparsely-gated MoE** (Lepikhin et al., 2021, the [[GShard]] line) replaces every other Transformer block's feed-forward layer with an MoE layer and uses **top-2 routing**: always keep the top expert, stochastically keep the second with probability p = min(2·g_{e₂}(x), 1).
- **Load balancing** is critical because unused experts get zero gradient: an **expert capacity** with capacity factor 2 drops tokens (residual bypass f(x)=x) when an expert exceeds 2·(B/E) tokens, and an **auxiliary loss** λ·Σ m_e c_e (e.g. λ = 0.01/B) penalizes imbalance.
- [[SwitchTransformer]] (Fedus et al., 2021) uses **top-1 routing** (maximum sparsity), reaches **1.6 trillion parameters**, and achieves a **4× pre-training speedup over T5-XXL** (11B params); it relies on FP32→FP16 selective casting, smaller init, expert dropout, and expert parallelism.
- **BASE Layers** (Lewis et al., 2021) assign each token exactly one expert by solving a balanced-assignment **linear program** over the whole batch (hard constraint Σ 𝟙[a_i=e] = B/E rather than a soft penalty); more stable but more compute for assignment.
- [[GShard]] (Lepikhin et al., ICLR 2020) trained a 600B-parameter MoE Transformer for neural machine translation across 100 languages using top-2 experts; Shazeer et al. (2017) introduced the original sparsely-gated MoE layer (137B params, 1000 experts).
- [[GLaM]] (Du et al., 2021) is a **1.2 trillion-parameter** MoE (64 experts, 64 layers, 32K hidden) where each token activates only **95B params (~8%)**, trained on 1.6T tokens at **~1/3 the training cost of GPT-3**, and beats GPT-3 on 0-shot/1-shot knowledge tasks while showing *less* WinoGender bias (71.7% vs GPT-3's 64.2%).
- FacebookMoE (Artetxe et al., 2021) is a 1.1T-parameter MoE (512 experts, 32 layers, 4096 hidden) trained on 112B tokens; unlike GLaM, its StereoSet stereotype bias *worsens* with model size.
- Decentralized MoE (Ryabinin & Gusev, 2020) targets crowdsourced training across 10³–10⁶ heterogeneous, failure-prone, low-bandwidth (~100 Mbps) nodes using Kademlia distributed hash tables; a related project trained an ALBERT-style Bengali masked LM with 40 volunteers.
- Retrieval-based models retrieve relevant passages z from a store S and generate y conditioned on (z, x); nearest-neighbor retrieval over the training set is a special case.
- [[RetrievalAugmentedGeneration]] (RAG, Lewis et al., 2020) models p(y|x) = Σ_{z∈S} p(z|x) p(y|z,x) (sum approximated by top-k), pairing a **DPR** dense retriever (dual [[BERT]] encoders, FAISS index) with a **BART-large (400M)** generator over concatenated (z, x).
- [[RETRO]] (Borgeaud et al., 2021) retrieves on **32-token chunks** from a **2-trillion-token store** using a **frozen BERT**, and with only **7B parameters (~25× fewer than GPT-3)** reaches strong LM results and 45.5% on NaturalQuestions.
- Retrieval models add interpretability and updatable knowledge stores, but it is unclear whether they match the general-purpose capabilities of dense Transformers; MoE enables far larger models with fewer FLOPs per input, though fair cross-model comparison at scale is hard.

## Key Quotes
> "As models get larger, they have to be split up across more machines, and network bandwidth becomes a bottleneck to training." — motivation for selective architectures

> "With the above tricks carefully implemented, we observe that the training of sparsely activated models at all scales becomes quite stable." — GLaM (Du et al., 2021), on MoE training stability

> "Switch Transformer ... 4x pre-training speedup vs. T5-XXL (11 billion parameters) ... 1.6 trillion parameters" — Switch Transformer scale and efficiency

## Connections
- [[MixtureOfExperts]] — the central paradigm: sparse gating activates only a subset of experts per input.
- [[SwitchTransformer]] — top-1-routed, 1.6T-param MoE; concrete instantiation of the MoE idea.
- [[GShard]] — sparsely-gated top-2 MoE for 600B-param multilingual translation; the line this lecture's MoE math is drawn from.
- [[GLaM]] — 1.2T-param Google MoE that beats GPT-3 on 0/1-shot knowledge tasks at 1/3 the cost.
- [[RETRO]] — retrieval-augmented 7B model with a 2T-token store; rivals much larger dense models.
- [[RetrievalAugmentedGeneration]] — RAG framework combining DPR retrieval with a BART generator.
- [[GPT-3]] — the 175B dense-Transformer baseline these selective architectures are compared against.
- [[BERT]] — backbone of DPR retrievers (RAG) and the frozen retriever in RETRO.
- [[T5]] — T5-XXL (11B) is the dense baseline Switch Transformer outpaces 4×.
- [[FAISS]] — similarity-search index used at RAG inference time.
- [[DenseRetrieval]] — DPR is the dense passage retriever underpinning RAG.
- [[Google]] — produced Switch Transformer, GShard, and GLaM.
- [[StanfordUniversity]] — institution offering CS324.
- [[Gopher]] — RETRO reuses Gopher's MassiveText dataset.
- [[LoadBalancing]] — expert-capacity and auxiliary-loss mechanisms keep MoE experts utilized.

## Contradictions
- Internal tension noted in the lecture (not a cross-page wiki contradiction): [[GLaM]] reports *reduced* gender bias at scale (WinoGender), whereas FacebookMoE reports stereotype bias *worsening* with model size (StereoSet).
- Otherwise None identified.
