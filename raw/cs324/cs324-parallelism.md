# Stanford CS324 (Winter 2022) — Parallelism
Source: https://stanford-cs324.github.io/winter2022/lectures/parallelism/
Fetched for wiki ingest.

> **Provenance note.** The public lecture page is a thin wrapper that links to two PDFs:
> `Parallelism.pdf` (the main lecture, delivered as hand-drawn whiteboard/slide scans) and
> `An_Ancient_Tale_of_Parallelism.pdf` (a supplementary slide deck on the history of
> parallel ML, drawn from Christopher Ré / Hazy Research group work c. 2017). The main
> lecture PDF is a *scanned/handwritten* document; automated OCR of it is noisy, so the
> technical detail below has been reconstructed faithfully from (a) the OCR-recoverable
> structure and concrete figures of the whiteboard notes, (b) the legible supplementary
> "Ancient Tale" deck, and (c) the four papers the lecture is explicitly built on
> (Megatron-LM 2019, GPipe 2018, Megatron-LM-at-scale / 3D parallelism SC'21, TeraPipe 2021).
> Numeric facts attributed to those papers are taken from the papers themselves.

---

## Further Reading (papers the lecture is built on)

- **Megatron-LM** — Shoeybi et al., 2019. *Training Multi-Billion Parameter Language Models Using Model Parallelism.* arXiv:1909.08053
- **GPipe** — Huang et al., NeurIPS 2018. *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism.* arXiv:1811.06965
- **Megatron-LM at scale (3D parallelism)** — Narayanan et al., SC 2021. *Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM.* arXiv:2104.04473
- **TeraPipe** — Li et al., ICML 2021. *TeraPipe: Token-Level Pipeline Parallelism for Training Large-Scale Language Models.* arXiv:2102.07988

---

## Lecture Framing / Goals

- Parallelism has arguably been the main goal of most systems research for the last decade
  (the lecturer cites Stanford's "Pervasive Parallelism Lab").
- The lecture surveys the **main trends from ~5 years ago** and shows **what a modern large
  training setup looks like** along the three axes: **data parallel, model parallel, pipeline parallel.**
- Stated goal: keep it high-level and "give you a taste" of distributed training.
- Disclaimer from the lecturer: they were active in this research area and have co-founded /
  funded companies in the space, so the slides are biased toward their own work.

---

## What a Modern Large Training Setup Looks Like (the hardware)

### Compute units and rough peak throughput
- A single modern accelerator delivers on the order of **~125 TFLOP/s** (low precision), up
  toward **~1000 TFLOP/s (≈1 PFLOP/s)** at the high end for newer chips.
- For scale comparison, the lecture notes that the **largest supercomputer in Canada was ~3.6 PF**
  and **in Germany ~44 PF** at the time — with the caveat that these numbers are **not directly
  comparable** (different precisions, benchmarks like LINPACK vs. ML-relevant throughput).
- **Specialization is growing rapidly**: accelerators increasingly contain **multiple chips/dies**
  per package and **large amounts of high-bandwidth memory (HBM)** (e.g. tens of GB per device).

### How the hardware is wired (the memory/communication hierarchy)
The lecture sketches the datacenter hierarchy from small to large:
- **Chip / die** → multiple dies per **box (server)**.
- Within a box, accelerators connect to each other over a fast interconnect
  (**NVLink, ~hundreds of GB/s class**, e.g. ~200 GB/s order), and the box plugs into the
  host over **PCIe**.
- **Boxes** are grouped (e.g. a handful per rack), **racks** connect into larger fabrics, and
  the whole thing forms the **datacenter**.
- Bandwidth gets **looser (slower / more contended) at every level you go up** the hierarchy —
  intra-chip ≫ intra-box (NVLink) ≫ inter-box ≫ inter-rack. This is the central constraint that
  every parallelism strategy must respect.

### The two questions that drive every design decision
1. **Memory**: does your model (parameters + activations + optimizer state) **fit**? If not you
   must spread it out.
2. **Network / communication**: communication is "loose" (relatively slow) at all levels, so the
   strategy that minimizes communication relative to the available bandwidth wins.

### Co-design of models and hardware
- "We've co-designed models to extract performance."
- Example: a **matrix multiply is highly parallel** and can reach **~80% of peak utilization** or more.
- By contrast, more irregular kernels (e.g. attention, before specialized engineering) can land at
  only **~10–15% utilization "out of the box."** Teams of engineers work specifically to speed up
  attention. The gap between matmul efficiency and full-model efficiency is what parallelism +
  kernel engineering try to close.

---

## The Three (Major) Parallelism Techniques

The lecture organizes everything around three orthogonal strategies that are combined in practice:
**Data parallelism, Model (tensor) parallelism, Pipeline parallelism.**

---

### 1. Data Parallelism

**Setup.** Take a model (toy example: a model with **3 layers**, each layer `l` computing
`a = f(W·x)` for weights `W`). Replicate the *entire model* onto each of several workers
(toy example: **3 nodes / chips**). Split the input mini-batch `B` across the workers so each
worker sees a different shard of the data.

**The data-parallel training step (the loop):**
1. **Send batches** — distribute distinct sub-batches of data to each worker.
2. **Each worker computes in parallel** — forward + backward on its own data shard against its
   local copy of the weights, producing local gradients.
3. **Send back the gradients** — each worker sends its gradient to one node / the host
   (or all-reduces them).
4. **Update the (global) weights** — take an optimizer step.
5. **Broadcast the updated weights back** to every worker for the next iteration.

**Properties / tradeoffs.**
- **Utilization is very high** as long as nobody is left idle / waiting (no straggler in the barrier).
- **Communication cost**: each gradient/weight is communicated proportional to the model size.
  In the toy example the model is effectively "sent ~3 times" (broadcast weights, gather gradients)
  per step — communication scales with **the number of replicas × the model size**.
- **Requirement / limitation**: the **entire model must fit on a single device.** Data parallelism
  scales throughput but does **nothing** to fit a model that is too big for one accelerator's memory.
- This is the historical home of asynchronous-SGD ideas (see "Ancient Tale" below): relaxing the
  synchronization (locking) between workers can buy hardware efficiency at some statistical cost.

---

### 2. Model Parallelism (Tensor / Intra-layer Parallelism)

**Motivation.** When a model — or even a *single layer* — is too big to fit on one device, you must
split the layer itself across devices. "Only one layer (and its weights) needs to fit" per device.

**Mechanics.** Recall forward and backward for a stack of layers:
```
z1 = f(W1 · x)
z2 = f(W2 · z1)
z3 = f(W3 · z2)
```
Tensor model parallelism splits the **weight matrices `W` (and the matrix multiplications) across
devices** — e.g. partition `W` by columns/rows so each device holds a slice and computes a partial
result, then combine the partials with a collective communication. The Megatron approach partitions
the matmuls inside the Transformer's MLP and self-attention blocks.

**Key Megatron-LM facts (Shoeybi et al. 2019).**
- An **intra-layer model-parallel** approach for Transformers with billions of parameters.
- **No new compiler or library changes** required; **orthogonal and complementary to pipeline
  parallelism**; implemented with just a few added communication ops in **native PyTorch**.
- Trained an **8.3-billion-parameter** model on **512 GPUs**.
- Sustained **15.1 PetaFLOP/s** across the application; **76% scaling efficiency** relative to a
  strong single-GPU baseline (single GPU = **39 TeraFLOP/s**, **~30% of peak**).

**Tradeoffs.**
- Communication happens **within every layer's forward and backward pass** (to stitch partial
  products together), so tensor parallelism is **communication-heavy** and is best confined to
  devices with the fastest interconnect — i.e. **within a single box over NVLink**, not across boxes.
- The forward pass is *not* freely commutable across the split — the partitioned matmuls must be
  reduced in the right order, which is why the collective communication is unavoidable each layer.

---

### 3. Pipeline Parallelism

**Motivation.** Split the model **by layers (stages)** across devices: device 1 holds layers 1..k,
device 2 holds the next group, etc. A forward activation flows from stage to stage; the backward
gradient flows back. This lets a model far larger than one device's memory be trained.

**The naive problem — the pipeline "bubble".** Because stage `i+1` cannot start until stage `i`
finishes (a dependency chain), a naive layer-split leaves most devices **idle** most of the time:
while stage 1 computes the first batch, stages 2..N wait. This idle "white space" in the
time-vs-device diagram is the **bubble**, and it kills utilization (the lecture sketches per-device
utilization landing around **~60–70%** depending on configuration, and far worse for a naive split).

**The fix — micro-batches (GPipe's idea).** Split each mini-batch into many smaller **micro-batches**
and feed them through the pipeline staggered, so that while stage 2 works on micro-batch 1, stage 1
is already working on micro-batch 2, etc. Notation from the lecture: `F(i, j)` = forward pass on
**node/stage `i` with micro-batch `j`**. More micro-batches → more overlap → smaller bubble → **more
efficient.** The bubble fraction shrinks roughly as the number of micro-batches grows relative to the
number of pipeline stages.

**Key GPipe facts (Huang et al., NeurIPS 2018).**
- A library for **pipeline parallelism**: pipelines different **sub-sequences of layers on separate
  accelerators**; works for any network expressible as a **sequence of layers**.
- A **novel batch-splitting (micro-batch) pipelining algorithm** that yields **almost linear speedup**
  when a model is partitioned across multiple accelerators.
- Uses **re-materialization (gradient checkpointing)** to cut activation memory: recompute activations
  in the backward pass instead of storing them all, trading compute for memory.
- Demonstrations: a **557M-parameter AmoebaNet** reaching **84.4% top-1 on ImageNet-2012**, and a
  **6-billion-parameter, 128-layer Transformer** for multilingual NMT across **>100 languages**.

**Improving the pipeline further.** Ways to reduce the bubble / improve throughput discussed:
- More / smaller micro-batches (basic GPipe lever).
- **Interleaved pipeline schedules** (Megatron SC'21) — assign multiple non-contiguous stages per
  device to shrink the bubble.
- **Reduced precision** and other systems tricks.
- **TeraPipe (Li et al., ICML 2021)** — see below.

---

### TeraPipe — Token-Level (Sequence-Dimension) Pipeline Parallelism

- Identifies a **new, orthogonal dimension** to existing model-parallel approaches: for
  Transformer-based language models, you can do **pipeline parallelism *within a single training
  sequence*** thanks to the **autoregressive property** (token `t` only attends to tokens `< t`).
- This gives a **more fine-grained pipeline** than layer-level pipelining (pipeline along the **token
  / sequence dimension**), filling the bubble better.
- Result: **5.0× training speedup for the largest GPT-3 model (175B parameters)** on an AWS cluster of
  **48 × p3.16xlarge** instances, versus state-of-the-art model-parallel methods.

---

## Combined / "3D" Parallelism (Megatron-LM at scale, SC 2021)

In practice the three strategies are **composed**, matched to the bandwidth hierarchy:
- **Tensor (model) parallelism within a server/box** (fastest NVLink interconnect),
- **Pipeline parallelism across boxes** (slower inter-node links carry only stage-boundary activations),
- **Data parallelism across the resulting model-parallel groups** (replicate the whole pipeline and
  all-reduce gradients).

**Key facts (Narayanan et al., SC 2021).**
- Combines **tensor, pipeline, and data parallelism** to train models up to **1 trillion parameters**.
- Scaled to **3,072 GPUs**, achieving an **aggregate throughput of 502 PetaFLOP/s**.
- Achieved **~52% of theoretical peak per-GPU** throughput at that scale.
- Introduced a **novel interleaved pipeline-parallelism schedule** that improves throughput by
  **10%+** with memory footprint comparable to existing approaches.

> The lecture also gestures at **ZeRO**-style optimizer-state / gradient / parameter **sharding**
> across data-parallel workers (partitioning the optimizer state instead of replicating it) as the
> memory-saving complement to these compute-parallel strategies, alongside **gradient accumulation**
> (accumulate gradients over micro-steps before a single optimizer update to emulate large batches).

---

## Supplementary Deck: "An Ancient Tale of Parallelism" (verbatim-faithful summary)

This older deck (slides ~2017, drawn from Christopher Ré / Hazy Research work) supplies the historical
motivation. Core thesis: **statistical algorithms have relaxed notions of correctness, which creates
new opportunities for algorithms, systems, and hardware.**

**The key balance — Statistical vs. Hardware efficiency.**
- *Statistical efficiency*: how many steps you take (to converge).
- *Hardware efficiency*: how efficiently you take each of those steps.
- Citing: *Ce Zhang & C. Ré, "DimmWitted: A Study of Main-Memory Statistical Analytics," VLDB 2014.*

**Three driving trends in hardware:**
1. **Lots of smaller cores** (single cores stopped getting faster; throughput rises only if you
   rewrite the algorithms).
2. **Non-Uniform Memory Access (NUMA)** — thousands of cores with nearby **high-bandwidth memory (HBM)**.
3. **Single-Instruction Multiple Data (SIMD), and SIMT** — fine-grained data parallelism; SIMD
   bandwidth doubled in each of the last four generations ("good old days of Moore's Law").
- Across all three, **approximation allows major performance improvements.**

**Statistical analytics crash course.**
- A staggering amount of ML/stats is `min_x  Σ_{i=1..N} f(x, y_i)`, with `N` (number of data points
  `y_i`) typically in the **billions** (classification, recommendation, deep learning).
- The de-facto solver is **SGD**: `x^{k+1} = x^k − α·N·∇f(x^k, y_j)` — select one term `j`, estimate
  the gradient. SGD = **billions of tiny iterations / tiny jobs.**

**Multicore communication scaling.**
- *Independent jobs* with little communication: 2 cores → ~2× faster.
- *Dependent jobs* need a "whose turn" protocol called **locking** (~**100 cycles** each).
- **Communication scales quadratically**: if 2 cores take 1 s to communicate, 4 cores take 4 s,
  8 cores take 16 s — `k` cores take `(k/2)^2` seconds. Servers may have **100+ cores**.
- Consequence: implemented classically (with locking), **SGD gets *slower* with more cores.**

**Hogwild! — the heresy that works.**
- **Just ignore the locking protocol** ("go Hogwild!"). Computer-science heresy.
- **Theorem (Hogwild!, NIPS 2011, Niu, Recht, Ré, Wright):** with no locking, SGD still converges to
  the correct answer at essentially the same rate.
- Follow-ons: **AsySCD** (Liu, Wright et al., ICML/JMLR 2014), **Buckwild!** (De Sa, Olukotun, Ré,
  NIPS 2015). Adopted in industry — Microsoft's Project Adam / Cortana used "a technology called, of
  all things, Hogwild!".
- General lesson: **relaxing consistency to be architecture-aware can be a big performance win** (a
  regularizer is a sane statistical penalty; bugs in your implementation are *not* helpful).

**Model & data replication tradeoffs (DimmWitted).** Three design axes, each with a hardware/statistical
tradeoff:
1. **Access methods** — {Row, Column, Row-col}.
2. **Model replication** — {Per-Core (low cache-coherence stalls, infrequent comm), Per-Node (in
   between), Per-Machine / Hogwild! (high coherence traffic, stalls)}.
3. **Data replication** — {Full, Importance, Shard}.
- Choosing well can be **100× faster** than the classical choices.

**Precision vs. parallelism (low-precision training).**
- Trade SIMD precision for SIMD parallelism. A hardware model for precision (ISCA 2017; De Sa, Olukotun).
- **Four classes of numbers** — the **DMGC** model — quantize each class independently:
  - **D**ataset numbers (store the immutable input data),
  - **M**odel numbers (the vector being updated),
  - **G**radient numbers (intermediates in gradient computation),
  - **C**ommunication numbers (used to communicate among workers).
- Example DMGC signature `D8 M16 G32f C16`: 8-bit dataset, 16-bit model, 32-bit-float gradients,
  16-bit communication. Quantizing gradients improves compute throughput but barely affects memory;
  prior work often quantizes some classes but ignores others.
- **Warning:** your learning hyperparameters (e.g. momentum, delay) depend on the hardware and these
  precision choices — they are coupled.

**Closing reflection.** "Optimization is a leaky abstraction for deep learning" — some approaches make
the loss go down *more slowly* (worse optimization) yet *generalize better* (better test performance).
