# Stanford CS324 (Winter 2022) — Training
Source: https://stanford-cs324.github.io/winter2022/lectures/training/
Fetched for wiki ingest.

## Overview

This lecture discusses how to train large language models, building on prior coverage of model architectures. The content focuses on two main areas: **objective functions** and **optimization algorithms**.

---

## Objective Functions

### Introduction

Language models map token sequences into contextual embeddings using models like LSTMs or Transformers:

$$\phi : \mathcal{V}^L \to \mathbb{R}^{d \times L}$$

The lecture covers three model types with different training objectives:
1. **Decoder-only** (e.g., GPT-3)
2. **Encoder-only** (e.g., BERT)
3. **Encoder-decoder** (e.g., T5)

### Decoder-Only Models (Autoregressive Language Modeling)

**Conditional Distribution Definition:**

Autoregressive language models define:

$$p(x_i \mid x_{1:i-1})$$

The process involves:
- Mapping $x_{1:i-1}$ to contextual embeddings $\phi(x_{1:i-1})$
- Applying embedding matrix $E \in \mathbb{R}^{V \times d}$ to obtain token scores
- Exponentiating and normalizing to produce the distribution

**Formal Definition:**

$$p(x_{i+1} \mid x_{1:i}) = \text{softmax}(E \phi(x_{1:i})_i)$$

**Maximum Likelihood Objective:**

Let $\theta$ denote all model parameters and $\mathcal{D}$ the training data (a set of sequences). The negative log-likelihood objective is:

$$\mathcal{O}(\theta) = \sum_{x_{1:L} \in \mathcal{D}} -\log p_\theta(x_{1:L}) = \sum_{x_{1:L} \in \mathcal{D}} \sum_{i=1}^L -\log p_\theta(x_i \mid x_{1:i-1})$$

This factorization decomposes the sequence probability into conditional probabilities for each token given its context.

### Encoder-Only Models

**Motivation for Bidirectional Embeddings:**

Decoder-only models produce *unidirectional* contextual embeddings. Encoder-only models like BERT provide stronger *bidirectional* embeddings since they don't need to generate tokens.

#### BERT (Bidirectional Encoder Representations from Transformers)

**Architecture:**

$$\text{BERT}(x) = \text{TransformerBlock}^{24}(\text{EmbedTokenWithPosition}(x) + \text{SentenceEmbedding}(x)) \in \mathbb{R}^{d \times L}$$

Where $\text{SentenceEmbedding}(x)$ returns:
- $e_A \in \mathbb{R}^d$ for tokens left of [SEP]
- $e_B \in \mathbb{R}^d$ for tokens right of [SEP]

**Model Specifications (BERT-large):**
- 24 Transformer blocks (layers)
- 16 attention heads
- 1024-dimensional model
- Total: 355M parameters

**Special Tokens:**
- **[CLS]**: Contains embeddings used for classification tasks
- **[SEP]**: Separates the first and second sequences

**Training Objective:**

BERT combines two loss terms — masked language modeling and next sentence prediction:

$$\mathcal{O}(\theta) = \sum_{(x,c) \in \mathcal{D}} \underbrace{\mathbb{E}_{I, \tilde{x} \sim A(\cdot \mid x, I)}\left[\sum_{i \in I} -\log p_\theta(\tilde{x}_i \mid x)\right]}_{\text{masked language modeling}} + \underbrace{-\log p(c \mid \phi(x)_1)}_{\text{next sentence prediction}}$$

##### Masked Language Modeling

**Task Definition:**

Maps noisy/incomplete sequences to original sequences:

$$\tilde{x} \Rightarrow x$$

Example:

$$[\text{the}, \text{[MASK]}, \text{ate}, \text{[MASK]}, \text{cheese}] \Rightarrow [\text{the}, \text{mouse}, \text{ate}, \text{the}, \text{cheese}]$$

**Model:**

Predicts each token independently given the contextual embedding:

$$p(x_i \mid \tilde{x}) = \text{softmax}(E \phi(\tilde{x})_i)$$

**Masking Function $A(\tilde{x} \mid x)$:**

1. Select a random 15% of token positions $I \subset \{1, \dots, L\}$
2. For each $i \in I$:
   - With probability **0.8**: set $\tilde{x}_i \leftarrow \text{[MASK]}$
   - With probability **0.1**: set $\tilde{x}_i \leftarrow x_i$ (unchanged)
   - With probability **0.1**: set $\tilde{x}_i \leftarrow$ random word from vocabulary $\mathcal{V}$

**Distribution Shift Mitigation:**

If all masked positions were replaced with [MASK]:
- During training: the model only sees [MASK] tokens
- At test time: no [MASK] tokens are present
- Solution: replace with real words 20% of the time (probability 0.1 unchanged + 0.1 random) so train and test distributions match

##### Next Sentence Prediction

**Task:**

Binary classification predicting whether the second sentence follows the first.

Examples:
- $[\text{[CLS]}, \text{the mouse ate the cheese}, \text{[SEP]}, \text{it was full}] \Rightarrow 1$
- $[\text{[CLS]}, \text{the mouse ate the cheese}, \text{[SEP]}, \text{hello world}] \Rightarrow 0$

Uses the [CLS] token embedding for the binary classification.

**Dataset Construction:**

For each example $(x, c)$:
1. Let $A$ be a sentence from the corpus
2. With probability 0.5: let $B$ be the next sentence
3. With probability 0.5: let $B$ be a random sentence
4. Construct $x = [\text{[CLS]}, A, \text{[SEP]}, B]$
5. Label $c$ indicates whether $B$ is the next sentence

**Key Insights on BERT:**

- BERT, ELMo, and ULMFiT demonstrated that a uniform architecture (Transformer) could be applied to multiple NLP classification tasks.
- Shifted the NLP community toward the "pre-training + fine-tuning" paradigm.
- Demonstrated the importance of deeply bidirectional contextual embeddings.
- Evidence suggests that model size and fine-tuning strategies (e.g., p-tuning) may compensate for unidirectional approaches.

#### RoBERTa (Robustly Optimized BERT)

**Improvements over BERT:**

- Removed the next sentence prediction objective (found it didn't help)
- Trained on more data: 16GB → 160GB text
- Trained for longer duration
- Performance improvement: SQuAD benchmark **81.8 → 89.4**

### Encoder-Decoder Models

**Task Example (Table-to-Text Generation):**

$$[\text{name:Clowns|eatType:coffee shop}] \Rightarrow [\text{Clowns is a coffee shop}]$$

**Architecture:**

- Encode the input bidirectionally (like BERT)
- Decode the output autoregressively (like GPT-2)

#### BART (Bidirectional Auto-Regressive Transformers)

**Architecture (Lewis et al., 2019):**
- Transformer-based encoder-decoder model
- Same encoder as RoBERTa: 12 layers, 1024 hidden dimension
- Trained on 160GB text (same as RoBERTa)

**Noise/Corruption Transformations $A(\tilde{x} \mid x)$:**

Based on BERT-scaled experiments, the final model uses:
- Mask 30% of tokens in the document
- Permute all sentences

Achieved strong results on both classification and generation tasks via fine-tuning.

#### T5 (Text-to-Text Transfer Transformer)

**Model (Raffel et al., 2020):**

Transformer-based encoder-decoder treating all tasks as text-to-text.

**Unsupervised Objective:**

Given a span of text, randomly split into input and output:

$$[\text{the mouse}] \Rightarrow [\text{ate the cheese}]$$

The paper experimented with multiple unsupervised objectives and found that "i.i.d. noise, replace spans" worked well (though many objectives performed similarly).

**Supervised Task Formulation:**

All classical NLP tasks are recast as text-to-text:
- **Classification approach difference:**
  - BERT: uses the [CLS] token embedding
  - T5, GPT-2, GPT-3: cast classification in natural language space
  - Example: predict entailment in a text-generation format

**Model Specifications:**
- 11B parameter model
- A thorough empirical study across: datasets, model size, training objectives, etc.

---

## Optimization Algorithms

The focus is optimizing the autoregressive language modeling objective:

$$\mathcal{O}(\theta) = \sum_{x \in \mathcal{D}} -\log p_\theta(x)$$

### Key Optimization Concerns

When optimizing large language models, three objectives often conflict:

1. **Speed:** Convergence to good solutions quickly
2. **Stability:** Numerically stable training
3. **Memory Efficiency:** Especially critical for large models

There is tension: fast convergence and cutting down on memory via low precision tends to produce less stable training.

### Optimization Levels

Different scales of optimization challenges:

1. **Classic optimization:** Second-order methods, constrained optimization
2. **Machine learning:** Stochastic methods, implicit regularization + early stopping
3. **Deep learning:** Initialization, normalization, architectural changes
4. **Large language models:** Stability issues, unusual learning rate schedules

Much of large language model training remains "fairly ad-hoc and poorly understood."

### Stochastic Gradient Descent (SGD)

**Algorithm:**

1. Initialize parameters $\theta_0$
2. Repeat:
   - Sample a mini-batch $B_t \subset \mathcal{D}$
   - Perform the gradient step:

$$\theta_t \leftarrow \theta_{t-1} - \eta \frac{1}{|B_t|} \sum_{x \in B_t} \nabla_\theta (-\log p_\theta(x))$$

### ADAM (Adaptive Moment Estimation)

**Key Ideas:**

- **Momentum:** Continue moving in the same direction
- **Adaptive step sizes:** A different step size per dimension of $\theta$ (inspired by second-order methods)

**Initialization:**
- Parameters: $\theta_0$
- Moments: $m_0, v_0 \leftarrow 0$

**Update Procedure:**

**Compute gradient:**

$$g_t \leftarrow \frac{1}{|B_t|} \sum_{x \in B_t} \nabla_\theta (-\log p_\theta(x))$$

**Update first- and second-order moments:**

$$m_t \leftarrow \beta_1 m_{t-1} + (1 - \beta_1) g_t$$
$$v_t \leftarrow \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$

**Bias correction:**

$$\hat{m}_t \leftarrow m_t / (1 - \beta_1^t)$$
$$\hat{v}_t \leftarrow v_t / (1 - \beta_2^t)$$

**Parameter update:**

$$\theta_t \leftarrow \theta_{t-1} - \eta \, \hat{m}_t / (\sqrt{\hat{v}_t} + \epsilon)$$

**Memory Considerations:**

- Standard SGD: $2 \times (\text{num-params})$ storage ($\theta_t, g_t$)
- Adam: $4 \times (\text{num-params})$ storage ($\theta_t, g_t, m_t, v_t$)

### AdaFactor

(Shazeer & Stern, 2018)

**Memory Reduction Strategy:**

- Store row and column sums instead of full moment matrices
- For an $O(m \times n)$ matrix: $O(m + n)$ memory instead of $O(m \times n)$
- Removes the momentum term
- Used to train T5

**Caveat:**

Can be difficult to train with AdaFactor (see Twitter discussions and blog posts).

### Mixed-Precision Training

(Narang et al., 2018)

**Problem:**

Default FP32 (32-bit floating point) uses significant memory. FP16 (16-bit) is memory-efficient but values below $2^{-24}$ become 0.

**Solution:**

1. Store master weights in FP32
2. Perform computations in FP16
3. Use loss scaling: scale up the loss to prevent vanishingly small gradients
4. Result: halves memory usage

**Process:**
- Compute the forward/backward pass in FP16
- Scale the loss by a large factor before backprop
- Unscale gradients before the optimizer step
- Update the master weights in FP32

---

## Training Dynamics and Stability

### Learning Rate Schedules

**Standard practice:** Learning rate decreases over time.

**Transformer requirement:** Must *increase* the learning rate initially (warmup).

**Rationale (Huang et al., 2020):**

A potential cause: vanishing gradients from layer normalization create instability in the Adam optimizer. A warmup phase prevents this.

### Initialization

**Standard (Xavier initialization):**

$$W_{ij} \sim \mathcal{N}(0, 1/n)$$

where $n$ is the fan-in.

**GPT-2 and GPT-3 modification:**

Scale weights by an additional factor $1/\sqrt{N}$, where $N$ is the number of residual layers.

**T5 modification:**

Scale attention matrices by an additional $1/\sqrt{d}$ factor.

---

## GPT-3 Training Specification

**Optimizer Parameters (Adam):**
- $\beta_1 = 0.9$
- $\beta_2 = 0.95$
- $\epsilon = 10^{-8}$

**Data and Batch Configuration:**
- Batch size: 3.2 million tokens (~1500 sequences)
- Gradient clipping: $g_t \leftarrow g_t / \min(1, \|g\|_2)$

**Learning Rate Schedule:**
- Linear warmup over the first 375 million tokens
- Cosine annealing decay to 10% of the peak value
- Gradually increase the batch size during training

**Regularization:**
- Weight decay: 0.1

---

## Further Reading

The lecture references the following resources:

- [Mixed precision training](https://lilianweng.github.io/lil-log/2021/09/24/train-large-neural-networks.html#mixed-precision-training)
- "Fixing Weight Decay Regularization in Adam" (Loshchilov & Hutter, 2017) — introduces AdamW
- "ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators" (Clark et al., ICLR 2020)
- "DeBERTa: Decoding-enhanced BERT with Disentangled Attention" (He et al., ICLR 2020)
