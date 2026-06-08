# Stanford CS324 (Winter 2022) — Adaptation
Source: https://stanford-cs324.github.io/winter2022/lectures/adaptation/
Fetched for wiki ingest.

---

## Overview

This lecture examines methods for adjusting (adapting) pre-trained language
models to specific downstream tasks. Downstream tasks often differ substantially
in format, topic, or temporal scope from the original (task-agnostic) pre-training
data, so some form of adaptation is required to make a general-purpose language
model useful for a concrete application.

## Why Adapt Language Models?

Language models undergo **task-agnostic** training but must handle diverse
applications. A motivating example is **Natural Language Inference (NLI)**:
determining the entailment relationship between two sentences.

### NLI Example

- **Premise**: "I have never seen an apple that is not red."
- **Hypothesis**: "I have never seen an apple."
- **Correct output**: "Not entailment" (the reverse direction would be entailment).

This kind of task requires task-specific adjustment because it takes in two
sentences and produces a single binary output — unlike standard next-token
prediction or MASK-filling.

### Ways Downstream Tasks Differ From Pre-training

The lecture identifies three primary ways downstream tasks diverge from
pre-training:

1. **Formatting**: For example, NLI takes in two sentences and compares them to
   produce a single binary output. This is different from generating the next
   token or filling in MASKs.

2. **Topic shift**: The downstream task is focused on a new or very specific
   topic (e.g., medical records) that diverges from general pre-training corpora.

3. **Temporal shift**: The downstream task requires new knowledge that is
   unavailable during pre-training because (1) the knowledge is new (e.g., GPT-3
   was trained before Biden became President), or (2) the knowledge for the
   downstream task is not publicly available.

## General Adaptation Framework

Adaptation optimizes parameters γ ∈ Γ on a task-specific loss function:

```
γ_adapt = argmin_{γ ∈ Γ}  (1/n) Σ_i  ℓ_task(γ, θ_LM, x_i, y_i)
```

Variable definitions:
- **(x^(i), y^(i))** — the downstream dataset (inputs and labels).
- **θ_LM** — the pre-trained language model parameters (frozen or used as init).
- **γ** — the optimized parameters, drawn from a parameter family Γ.
- **ℓ_task** — the task-specific loss function.

The framework spans a spectrum: in some methods θ_LM is preserved (frozen) while
new parameters γ are introduced; in others θ_LM itself is updated.

The three main families of adaptation methods covered are: **Probing**,
**Fine-tuning**, and **Lightweight (parameter-efficient) Fine-tuning**.

---

## Probing

Probing introduces lightweight prediction heads — typically linear or shallow
feedforward networks — on top of **frozen** encoder representations. This
approach suits encoder-only architectures like BERT but extends to decoder-only
models (Liu et al., 2021, https://arxiv.org/pdf/2103.10385.pdf).

The language model encoder is frozen; only the task-specific prediction head is
optimized.

### Fixed-Length Representation Strategies

To get a single fixed-length vector from a variable-length sequence:

- **CLS token method** [Devlin et al., 2018]: "During both pre-training and
  fine-tuning, we prepend a special token called CLS to the prompt. We use the
  embedding vector corresponding to the CLS token as the 'sequence-level'
  embedding."

- **Token averaging**: "Another common way is to average over the L tokens."
  (Computing mean embeddings across all L positions.)

**Summary**: Probing freezes the language model encoder while optimizing
task-specific prediction heads. Limited expressivity (the underlying
representations are fixed).

---

## Fine-tuning

Fine-tuning initializes optimization from the pre-trained parameters θ_LM and
optimizes **all** model parameters plus any task-specific heads. It is more
expressive than probing but computationally expensive and requires storing a
separate full copy of the model per task.

### Applications

**Zero-shot enhancement (FLAN and T0)**: Both FLAN and T0 fine-tune the model
for better zero-shot performance and unify the prompt format of many downstream
tasks. By multi-task fine-tuning across many tasks cast into a unified prompt
format, they improve zero-shot generalization to unseen tasks.

**Instruction alignment (InstructGPT)**: InstructGPT aligns GPT-3 through three
stages:
1. Supervised fine-tuning on human demonstrations.
2. Preference data collection by sampling k outputs per instruction and having
   humans rank them.
3. Reinforcement learning optimization against a learned human-preference reward
   model.

**InstructGPT performance metrics (verbatim):**
- "A 1.3B InstructGPT model produces outputs that are preferred to 175B GPT-3
  85% of the time, and 71% when using few-shot prompts."
- "On closed-domain QA/summarization, InstructGPT hallucinates information 21% of
  the time vs 41% in GPT-3."
- "InstructGPT generates 25% fewer toxic outputs than GPT-3 when prompted to be
  respectful."
- "InstructGPT doesn't improve bias: not much benefit on Winogender and
  CrowSPairs."

**Summary**: Fine-tuning has no frozen parameters; it optimizes all language
model parameters plus any new prediction heads.

---

## Lightweight Fine-tuning (Parameter-Efficient Fine-Tuning)

Lightweight fine-tuning balances fine-tuning's expressivity against storage
efficiency by optimizing **less than 1%** of model parameters while keeping the
rest of the pre-trained model frozen.

### Prompt Tuning [Lester et al., 2021]

Developed for **T5** (encoder-decoder). The method prepends **k learnable,
continuous token embeddings** to the input, freezing the entire pre-trained
model. Only the prepended (soft) prompt embeddings are trained.

Scaling benefit: as the frozen model grows larger, prompt tuning becomes
increasingly competitive with full fine-tuning.

Initialization strategies for the prompt embeddings:
- Random embeddings from the vocabulary.
- Embeddings of class label strings.
- Pure random initialization (which underperforms).

### Prefix Tuning [Li and Liang, 2021]

Developed for **BART and GPT-2**. Rather than only modifying input vectors,
prefix tuning concatenates additional learnable key and value weights at **every
attention layer**.

For attention head i, prefix tuning extends the sequence length from L to
L' = L + k by concatenating learnable prefix matrices
P_key^(i), P_value^(i) ∈ ℝ^{d×k}:

```
K_prefix = [P_key^(i), K]
V_prefix = [P_value^(i), V]
head_i   = Attn-op(Q, K_prefix, V_prefix)
```

All-layer variant: "Prompt Tuning v2" / P-Tuning v2 (He et al., 2022) applies
learnable prefixes at all layers and shows benefits for both classification and
generation tasks.

### Adapter Tuning [Houlsby et al., 2019]

Inserts small bottleneck layers between frozen Transformer (sub)layers:

```
Adapter(x) = x + W_up · σ(W_down · x)
```

where:
- W_down ∈ ℝ^{r×d} projects down to a small bottleneck dimension r,
- σ is a nonlinearity,
- W_up ∈ ℝ^{d×r} projects back up to dimension d,
- the residual connection (+ x) preserves the original signal.

Adapters add < 1% of the total parameters.

### Other Lightweight Methods Mentioned

- **LoRA** (Low-Rank Adaptation).
- **BitFit** (training only bias terms).

### Parallelization / Personalized Deployment

Prefix tuning enables personalized deployment: one can store N user-specific
prefixes and, during minibatch processing, prepend the corresponding per-user
prefix to each example — serving many personalized "models" with a single shared
frozen backbone.

### Out-of-Distribution (OOD) Robustness

Lightweight methods tend to improve out-of-distribution performance relative to
full fine-tuning:

- **Prompt tuning**: Better F1 on out-of-domain MRQA 2019 tasks after training
  on **SQuAD** (i.e., train in-domain on SQuAD, test on out-of-domain MRQA 2019
  reading-comprehension tasks).
- **Prefix tuning**: Gains on **XSUM** summarization when trained on some news
  categories (e.g., world, UK, business) and tested on disparate categories
  (e.g., health, technology), evaluated using the **ROUGE-L** metric.
- **In-distribution** performance typically still favors full fine-tuning
  slightly.

**Summary**: Lightweight fine-tuning freezes most language model parameters and
optimizes minimal additions (< 1%). Methods include prompt tuning, prefix tuning,
adapter tuning, LoRA, and BitFit.

---

## Synthesis / Conclusion

We need to adapt large language models to the diverse array of downstream tasks,
which may differ in format, topic, or temporal scope from pre-training.
Adaptation bridges the divide between pure representation extraction (probing's
limited expressivity) and full model specialization (fine-tuning's storage
burden) through parameter-efficient techniques that optimize high-leverage
components of the model.

## Further Reading (referenced in lecture)

- FLAN — multi-task instruction fine-tuning for zero-shot generalization.
- T0 — multitask prompted training for zero-shot task generalization.
- InstructGPT — Training language models to follow instructions with human
  feedback.
- Prompt Tuning — Lester et al., 2021, "The Power of Scale for Parameter-Efficient
  Prompt Tuning."
- Prefix-Tuning — Li and Liang, 2021, "Prefix-Tuning: Optimizing Continuous
  Prompts for Generation."
- Adapters — Houlsby et al., 2019, "Parameter-Efficient Transfer Learning for NLP."
- P-Tuning v2 — He et al., 2022 (all-layer prefix/prompt tuning).
- LoRA, BitFit (parameter-efficient methods).
- Liu et al., 2021 — probing / prompting on decoder-only models
  (https://arxiv.org/pdf/2103.10385.pdf).
- BERT / CLS token — Devlin et al., 2018.
