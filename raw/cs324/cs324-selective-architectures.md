# Stanford CS324 (Winter 2022) — Selective architectures
Source: https://stanford-cs324.github.io/winter2022/lectures/selective-architectures/
Fetched for wiki ingest.

---

## Overview / Motivation

This lecture explores **"selective" architectures** that enable training larger
language models by having each input activate a different *subset* of the model's
parameters. The motivation is a scaling bottleneck:

- As models get larger, they have to be split up across more machines, and
  **network bandwidth becomes a bottleneck** to training.
- For **dense Transformers**, each input uses the same (all) parameters of the
  language model — e.g. 175B parameters for GPT-3.
- Example of parallelization across devices (model/pipeline parallelism):
  GPU1 = [layer1, layer2], GPU2 = [layer3, layer4], GPU3 = [layer5, layer6].
  Splitting layers across machines means activations must cross the network.

Two main approaches are discussed:

1. **Mixture-of-Experts (MoE)**: Create a set of experts; each input activates
   only a sparse subset of them. This reduces FLOPs per input while letting the
   total parameter count grow very large.
2. **Retrieval-based models**: Retrieve relevant data from a store, then generate
   outputs conditioned on the retrieved data. This offloads "knowledge" to an
   external store rather than packing it all into model weights.

---

## Part 1 — Mixture of Experts (MoE)

### Foundational concepts (Jacobs et al., 1991)

**Basic setup.** Problem: map x ∈ ℝ^d → y ∈ ℝ^d. A single feedforward network

    h_θ(x) = W₂ max(W₁ x, 0)

may lack expressiveness.

**MoE components:**

- E experts, each with an embedding w_e ∈ ℝ^d.
- **Gating function** — a probability distribution over experts:

      g_e(x) = exp(w_e · x) / Σ_{e'=1}^E exp(w_{e'} · x)

- **Expert functions** with parameters θ^(e) = (W₁^(e), W₂^(e)):

      h_{θ_e}(x) = W₂^(e) max(W₁^(e) x, 0)

- **Final output** (mixture over experts):

      f(x) = Σ_{e=1}^E g_e(x) h_{θ_e}(x)

**Training via backpropagation.** Gradient:

    ∇f(x) = Σ_{e=1}^E g_e(x) ( ∇(log g_e(x)) h_{θ_e}(x) + ∇h_{θ_e}(x) )

The gradient is proportional to g_e(x), and updates both the gating function and
the experts.

**Computational savings via approximate (sparse) gating.**

- The full gating function is dense, e.g. g(x) = [0.04, 0.8, 0.01, 0.15].
- **Approximate gating** g̃(x) zeros out most experts, e.g. g̃(x) = [0, 0.84, 0, 0.16].
- The forward and backward passes only evaluate the nonzero experts → savings.

**Expert balancing.** It is critical that all experts pitch in. Unused experts
receive zero gradients, so the main consideration is ensuring all experts are
utilized across inputs.

**Parallelism.** Each expert can live on a different machine. The approximate
gating is computed centrally, and only the machines holding the *activated*
experts process input x.

### Sparsely-Gated Mixture of Experts (Lepikhin et al., 2021 — GShard line)

**Application to language modeling.** Turn the feed-forward networks of a
Transformer into MoE feed-forward networks:

    MoETransformerBlock(x) = AddNorm(MoEFeedForward, AddNorm(SelfAttention, x))

Every *other* Transformer block uses the MoE variant.

**Top-2 experts gating:**

1. Compute top expert: e₁ = arg max_e g_e(x)
2. Compute second expert: e₂ = arg max_{e ≠ e₁} g_e(x)
3. Always keep the top expert; stochastically keep the second:
   - Let p = min(2 g_{e₂}(x), 1).
   - With probability p (keep both, renormalized):
         g̃_{e₁}(x) = g_{e₁}(x) / (g_{e₁}(x) + g_{e₂}(x))
         g̃_{e₂}(x) = g_{e₂}(x) / (g_{e₁}(x) + g_{e₂}(x))
         g̃_e(x) = 0 for e ∉ {e₁, e₂}
   - With probability 1 − p (keep only top):
         g̃_{e₁}(x) = 1, g̃_e(x) = 0 for e ≠ e₁

**Notation:**

- B = number of tokens in a batch (typically millions).
- E = number of experts (typically thousands).

**Load balancing mechanisms:**

- Count of times expert e is selected:

      c_e = Σ_{i=1}^B 𝟙[ g̃_e(x_i) > 0 ]

  After a batch: Σ_e c_e = B. Balanced state: c_e = B/E.

- **Overflow / expert capacity.** If c_e > 2(B/E), bypass with the residual:
  set f(x) = x. The **capacity factor = 2**.

- **Auxiliary load-balancing loss.** Define a soft version of c_e:

      m_e = Σ_{i=1}^B g_e(x_i)

  Total loss:

      loss = negative-log-likelihood + λ · load-balancing-loss
      load-balancing-loss = Σ_{e=1}^E m_e c_e

  Example: λ = 0.01 / B.

**Worked example** (B = 2 tokens, E = 4 experts):

- g(x₁) = [0.2, 0.6, 0.1, 0.1] → g̃(x₁) = [0.25, 0.75, 0, 0]
- g(x₂) = [0.1, 0.6, 0.2, 0.1] → g̃(x₂) = [0, 0.75, 0.25, 0]
- c = [1, 2, 1, 0], m = [0.3, 1.2, 0.3, 0.2]

### Switch Transformer (Fedus et al., 2021)

- Approximate gating g̃(x) uses only the **top-1 expert** (maximum sparsity).
- Techniques:
  - Selective FP32 → FP16 casting.
  - Smaller initialization parameters.
  - Expert dropout.
  - Expert parallelism.
- **Model scale: 1.6 trillion parameters.**
- **Performance: 4× pre-training speedup vs. T5-XXL (11 billion parameters).**

### BASE Layers — Balanced Assignment of Sparse Experts (Lewis et al., 2021)

- Approximate gating g̃(x) is obtained by **joint optimization over all tokens in
  the batch**.
- Each token is assigned exactly 1 expert; load balancing is enforced as a hard
  **constraint** (not a soft penalty).
- Assignment vector a = [a₁, …, a_B] ∈ {1, …, E}^B.
- Optimization problem:

      maximize   Σ_{i=1}^B w_{a_i} · x_i
      subject to ∀e:  Σ_{i=1}^B 𝟙[a_i = e] = B/E

- This is an efficient **linear program** solvable in practice with parallelization.
- At test time: choose top-1 expert.

**Experimental comparison (same architecture, ~52.5B parameters):**

- Sparsely-gated MoE (top-2): 52.5B parameters
- Switch Transformer (top-1): 52.5B parameters
- BASE (1 jointly optimized expert): 44.4B parameters
  (1.3B shared parameters + 335M × 128 experts)
- BASE requires more compute for the assignment step but is more stable.

**Summary note.** Switch Transformer (Google, top-1) and BASE (Facebook, 1
expert/token, jointly optimized) did **not** outperform GPT-3. Subsequent
high-performing MoE models returned to **top-2 experts**: GLaM (Google),
FacebookMoE (Facebook).

### GLaM — Generalist Language Model (Du et al., 2021)

**Specifications:**

- **1.2 trillion parameters** (vs. GPT-3's 175 billion).
- 64 experts, 64 layers, 32K hidden units.
- Each token activates **95B parameters (~8% of 1.2T)**.

**Training improvements:**

- New dataset (GLaM dataset): **1.6 trillion tokens** (webpages, forums, books, news).
- Relative positional embeddings.
- Gated linear units.
- GeLU activation.
- RMSNorm (instead of LayerNorm).
- Skip weight updates / checkpoint rollback on NaN/Inf.
- Quote: "With the above tricks carefully implemented, we observe that the training
  of sparsely activated models at all scales becomes quite stable."

**Results:**

- **1/3 the training cost vs. GPT-3.**
- Same benchmarks as GPT-3 (open-domain QA, reading comprehension, SuperGLUE).
- Better 0-shot and 1-shot performance than GPT-3, especially on
  knowledge-intensive tasks.
- Note: did not evaluate the few-shot regime, where GPT-3 is stronger.

**WinoGender bias results:**

- Example sentence: "The nurse notified the patient that {her/his, their} shift
  would be ending in an hour."
- GPT-3: 64.2%
- GLaM: 71.7% overall
  - "he" examples: 70.8%
  - "she" examples: 72.5%
  - Stereotypical: 71.7%
  - Anti-stereotypical ("gotcha"): 71.7%
- GLaM shows **less** gender bias.

### FacebookMoE (Artetxe et al., 2021)

**Setup:**

- **1.1T parameter model.**
- 512 experts (more than GLaM).
- 32 layers, 4096 hidden units.
- Trained on **112 billion tokens** (webpages, forums, books, news).
- Strong gains for smaller models; diminishing returns for larger ones.

**StereoSet results:**

- Example: "The assistant went to work. {She brought her boss coffee., She was
  valued for her input.}"
- Stereotype bias **worsens** with model size (contrasts with the GLaM finding).

### Decentralized Mixture-of-Experts (Ryabinin & Gusev, 2020)

**Motivation:**

- Move beyond centralized organizations toward a decentralized architecture.
- The Azure supercomputer used for GPT-3 cost ~$250 million.
- Folding@Home volunteer-computing analogy: in April 2020, 700,000 volunteers
  produced 2.43 exaFLOPs (GPT-3 requires ~350 gigaFLOPs).
- Key difference: molecular dynamics is compute-heavy, not bandwidth-dependent.

**Main considerations:**

- Many nodes (10³ to 10⁶ heterogeneous PCs).
- Frequent failures (5–20% of nodes have ≥1 failure/day).
- Home-internet bandwidth (~100 Mbps vs. ~400 Gbps for Azure).

**Technical approach:**

- Distributed hash tables (DHTs): N nodes, each node talks to O(log N) others.
- Uses the **Kademlia DHT protocol** (as in BitTorrent, Ethereum).

**Experiments:**

- Top-4 experts (256 experts total).
- Each expert = a Transformer layer.
- Small Transformer LM trained on 4 GPUs.

**Related work (Diskin et al., 2021):**

- 40 volunteers trained an ALBERT-style masked LM for Bengali.
- "Training Transformers Together" project: anyone can join.

### MoE summary

- Mixture-of-experts: classic idea of allocating different experts across inputs.
- **Scale:** enables training much larger models (1.1–1.2 trillion parameters).
- **Efficiency:** fewer FLOPs per input than dense Transformers.
- **Comparison challenge:** direct apples-to-apples comparisons are difficult at scale.
- **Decentralization implications:** strong fit for distributed/crowdsourced training.

---

## Part 2 — Retrieval-Based Models

**Problem setting.** Sequence-to-sequence tasks in an encoder-decoder framework:
input x → output y.

Example (open-book QA):
- Input: "What is the capital of Canada?"
- Output: "Ottawa"

**Encoder-decoder models:** BART, T5 trained on denoising objectives, modeling
p(y | x). Example denoising: Input "Thank you me to your party week." → Output
"for inviting last".

**Retrieval framework.** Given a store S = {documents/passages}:

1. **Retrieve** relevant sequence(s) z based on input x.
2. **Generate** output y given z and x.

Example:
- Input: "What is the capital of Canada?"
- Retrieved z: "Ottawa is the capital city of Canada."
- Output: "Ottawa"

**Nearest neighbors as a special case.** Let S = the training set. Retrieve
(x', y') ∈ S whose x' is most similar to x, and generate y = y'.

### RAG — Retrieval-Augmented Generation (Lewis et al., 2020)

**RAG-Sequence model:**

    p(y | x) = Σ_{z ∈ S} p(z | x) p(y | z, x)

In practice the sum Σ is replaced by a **top-k** sum (analogous to top-1/top-2
experts in MoE).

**Retriever — Dense Passage Retrieval (DPR)** (Karpukhin et al., 2020):

    p(z | x) = exp(BERT_d(z) · BERT_q(x)) / Σ_{z' ∈ S} exp(BERT_d(z') · BERT_q(x))

- Passages: 100 words each, prefixed with the Wikipedia article title.
- Training data: tuples (q, p⁺, p⁻₁, …, p⁻ₙ) from QA datasets:
  - Positive p⁺: the correct passage.
  - Negatives p⁻: random passages + BM25-retrieved passages that do not contain
    the answer.
- Inference uses **FAISS** (Facebook AI Similarity Search) for fast retrieval.

**Generator:**

    p(y | z, x) = p(y | concat(z, x))

- **BART-large (400M parameters).**
- Input: the retrieved passage z concatenated with x.
- BART pre-trained with a denoising (masking) objective on web, news, books, stories.

**Training:**

- Initialize with BART (generator) and DPR (retriever, itself initialized from BERT).
- Fine-tune BART and BERT_q (the query encoder).

**Results:**

- Jeopardy generation (input "Hemingway"): RAG outperforms non-retrieval methods.
- Open-domain QA comparison to GPT-3 (few-shot) — GPT-3 reference numbers:
  - NaturalQuestions: GPT-3 = 29.9%
  - WebQuestions: GPT-3 = 41.5%
  - TriviaQA: GPT-3 = 71.2%
  (The lecture states RAG outperforms non-retrieval methods; the explicit RAG
  benchmark numbers are not stated on the page beyond this comparison.)

### RETRO (Borgeaud et al., 2021)

- Retrieves based on **chunks of 32 tokens**.
- Store: **2 trillion tokens**.
- Model: **7 billion parameters** (~25× fewer than GPT-3).
- Uses a **frozen BERT** for retrieval (no retriever updates).
- Dataset: **MassiveText** (the same dataset used for Gopher).

**Performance:**

- Strong language-modeling results.
- NaturalQuestions accuracy: **45.5%** (vs. SOTA at the time: 54.7%).

### Retrieval-based models — discussion

- Highly geared toward knowledge-intensive QA.
- Beyond scalability, they provide **interpretability** and the ability to update
  the store (knowledge) without retraining the model.
- It is unclear whether they achieve the same general-purpose capabilities as
  dense Transformers.

---

## General Summary

**Scaling challenge.** Dense Transformers hit network-bandwidth bottlenecks when
split across machines. Example pipeline parallelization:
GPU1 = [layer1, layer2], GPU2 = [layer3, layer4], GPU3 = [layer5, layer6].

**Solutions explored:**

- **MoE:** Each input activates a different sparse parameter subset; enabled
  training 1.1–1.2T-parameter models.
- **Retrieval:** Retrieve relevant data before generation; a 7B-parameter model
  with a 2T-token store (RETRO) is effective.

**Key trade-off.** Designing optimal, scalable architectures remains an open
question.

---

## Further Reading References

**Mixture-of-Experts papers:**

- "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts
  Layer" (Shazeer et al., ICLR 2017) — 137B-parameter model, 1000 experts.
- "GShard: Scaling Giant Models with Conditional Computation and Automatic
  Sharding" (Lepikhin et al., ICLR 2020) — 600B parameters, neural machine
  translation across 100 languages, top-2 experts.
- "Switch Transformers: Scaling to Trillion Parameter Models with Simple and
  Efficient Sparsity" (Fedus, Zoph, Shazeer, 2021).
- "GLaM: Efficient Scaling of Language Models with Mixture-of-Experts"
  (Du et al., 2021).
- "BASE Layers: Simplifying Training of Large, Sparse Models" (Lewis et al.,
  ICML 2021) — 110B parameters.
- "Efficient Large Scale Language Modeling with Mixtures of Experts"
  (Artetxe et al., 2021).
- "Towards Crowdsourced Training of Large Neural Networks using Decentralized
  Mixture-of-Experts" (Ryabinin & Gusev, NeurIPS 2020).
- "Distributed Deep Learning in Open Collaborations" (Diskin et al., 2021).
- "Dense-to-Sparse Gate for Mixture-of-Experts" (Nie et al., 2021).

**Retrieval-based papers:**

- "REALM: Retrieval-Augmented Language Model Pre-Training" (Guu et al., 2020).
- "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
  (Lewis et al., NeurIPS 2020).
- "Improving language models by retrieving from trillions of tokens"
  (Borgeaud et al., 2021) — RETRO.

---

_Note: The lecture does **not** cover kNN-LM (k-nearest-neighbor language models);
that topic is not present on this page despite being a related retrieval method._
