# Stanford CS324 (Winter 2022) — Introduction
Source: https://stanford-cs324.github.io/winter2022/lectures/introduction/
Fetched for wiki ingest.

## What is a Language Model?

A language model (LM) is fundamentally a **probability distribution over sequences of tokens**. Given a vocabulary V, an LM assigns each sequence of tokens x₁, ..., xₗ a probability p(x₁, ..., xₗ) between 0 and 1.

### Core Concept

The probability reflects how "good" or plausible a sequence is. For example, with vocabulary {ate, ball, cheese, mouse, the}:

- p(the, mouse, ate, the, cheese) = 0.02
- p(the, cheese, ate, the, mouse) = 0.01
- p(mouse, the, the, cheese, ate) = 0.0001

This simple mathematical object implicitly encodes:
- **Syntactic knowledge**: recognizing grammatical vs. ungrammatical sequences. "the mouse ate the cheese" is grammatical; "mouse the the cheese ate" is not.
- **World knowledge**: understanding semantic plausibility. A mouse eating cheese is more likely than cheese eating a mouse, so the first sequence gets higher probability.

### Generation and Conditional Generation

Language models can generate sequences by sampling x₁:ₗ ~ p. More practically, **conditional generation** allows prompting with a prefix (prompt) and generating a completion:

```
prompt → [model] → completion
```

### Autoregressive Language Models

The **chain rule of probability** decomposes joint distributions:

p(x₁:ₗ) = ∏ᵢ₌₁ᴸ p(xᵢ | x₁:ᵢ₋₁)

An **autoregressive language model** is one where each conditional distribution p(xᵢ | x₁:ᵢ₋₁) is computed efficiently (e.g., via a feedforward neural network).

#### Generation Process

Sampling one token at a time, with the result fed back in:
```
for i = 1, ..., L:
    xᵢ ~ p(xᵢ | x₁:ᵢ₋₁)^(1/T)
```

**Temperature parameter T** controls the amount of randomness:
- T = 0: deterministic (greedy — select the most probable token at each position)
- T = 1: normal sampling from the raw distribution
- T = ∞: uniform distribution over the entire vocabulary

Example with two tokens where p(cheese) = 0.4, p(mouse) = 0.6:
- p_{T=0.5}(cheese) = 0.31, p_{T=0.5}(mouse) = 0.69
- p_{T=0.2}(cheese) = 0.12, p_{T=0.2}(mouse) = 0.88
- p_{T=0}(cheese) = 0, p_{T=0}(mouse) = 1

Note: technically, the per-step temperature scaling does not correspond to applying temperature to the full sequence distribution; it is a heuristic applied at each step.

---

## A Brief History

### Information Theory and Entropy

**Claude Shannon** (1948) founded information theory in his paper "A Mathematical Theory of Communication," which introduced **entropy**:

H(p) = Σₓ p(x) log(1/p(x))

Entropy measures the expected number of bits any algorithm needs to encode (compress) a sample x drawn from the distribution p. The lower the entropy, the more predictable (structured) the sequence.

**Cross entropy** measures the expected number of bits needed to encode samples from p using a (possibly imperfect) model q:

H(p, q) = Σₓ p(x) log(1/q(x))

Key insight: H(p, q) ≥ H(p) always, so we can estimate (upper-bound) the true entropy H(p) by building better and better models q. The closer q is to p, the tighter the bound.

### The Shannon Game (1951)

In "Prediction and Entropy of Printed English," Shannon introduced a human-based language model: humans repeatedly guessed the next letter of a text, and the number of guesses was recorded. This measured the human's implicit language-modeling ability and was used to estimate the entropy of English.

### N-gram Models for Applications

Language models first saw practical use in specific tasks:
- **Speech recognition** (1970s): map an acoustic signal → text
- **Machine translation** (1990s): map source-language text → target-language text

#### The Noisy Channel Model

The motivation was the noisy channel model. For speech recognition:
```
p(text | speech) ∝ p(text) × p(speech | text)
                    [LM]       [acoustic model]
```
The LM term p(text) acts as a prior favoring fluent/plausible text.

#### N-gram Models

In n-gram models, the prediction of a token depends only on the last n-1 tokens:

p(xᵢ | x₁:ᵢ₋₁) = p(xᵢ | xᵢ₋₍ₙ₋₁₎:ᵢ₋₁)

Example for a trigram (n=3):
```
p(cheese | the, mouse, ate, the) = p(cheese | ate, the)
```

Probabilities are estimated from corpus counts, with smoothing (e.g., **Kneser-Ney smoothing**) to handle unseen n-grams.

**Strengths**: computationally cheap and scalable. Example: **Brants et al. (2007)** trained a 5-gram model on **2 trillion tokens** for machine translation (compare with GPT-3's 300 billion tokens).

**Weaknesses**: cannot capture long-range dependencies. If n is too small, the model cannot use distant context. Consider:
```
"Stanford has a new course on large language models. It will be taught by ___"
```
Predicting the instructor requires earlier context. Statistical infeasibility: with large n, almost all longer n-grams have count 0, e.g.,
```
count(Stanford, has, a, new, course, on, large, language, models) = 0
```
in most corpora. So increasing n leads to data sparsity.

### Neural Language Models

**Bengio et al. (2003)** pioneered neural language models, where conditional distributions are computed by a neural network:

p(cheese | ate, the) = neural-network(ate, the, cheese)

Benefit: it becomes statistically feasible to estimate distributions for larger n, because the network generalizes over similar contexts (no need to see exact n-grams). Bengio's team trained on 14 million words and outperformed n-gram models on the same data.

Challenge: neural networks were computationally expensive to train, so n-gram models continued to dominate for roughly another decade.

#### Key Post-2003 Developments

1. **Recurrent Neural Networks (RNNs), including LSTMs**: allowed the conditional distribution of a token to depend on the entire preceding context x₁:ᵢ₋₁ (effectively n = ∞), but were difficult to train.

2. **Transformers (2017)**: a newer architecture (originally developed for machine translation) that:
   - Returned to a fixed but "large enough" context length (GPT-3 used n = 2048)
   - Was much easier to train and exploited GPU parallelism well
   - Became the dominant paradigm

---

## Why Does This Course Exist?

### Explosion in Model Scale

Model sizes increased roughly **5000x over the 4 years** leading up to the course. Selected milestones:

| Model | Organization | Date | Parameters |
|-------|--------------|------|-----------|
| ELMo | AI2 | Feb 2018 | 94M |
| GPT | OpenAI | Jun 2018 | 110M |
| BERT | Google | Oct 2018 | 340M |
| XLM | Facebook | Jan 2019 | 655M |
| GPT-2 | OpenAI | Mar 2019 | 1.5B |
| RoBERTa | Facebook | Jul 2019 | 355M |
| Megatron-LM | NVIDIA | Sep 2019 | 8.3B |
| T5 | Google | Oct 2019 | 11B |
| Turing-NLG | Microsoft | Feb 2020 | 17B |
| **GPT-3** | **OpenAI** | **May 2020** | **175B** |
| Megatron-Turing NLG | Microsoft, NVIDIA | Oct 2021 | 530B |
| Gopher | DeepMind | Dec 2021 | 280B |

### Emergence

Scaling alone is not just a quantitative change — it produces qualitatively new **emergent behaviors** and capabilities, which in turn have different and larger societal impacts. This emergence (capabilities and harms appearing at scale) is a central motivation for the course.

---

## Capabilities of Large Language Models

### Shift from Component to System

- Until ~2018: LMs were primarily one **component** of a larger system (e.g., the LM term inside a speech recognition or machine translation pipeline).
- Now: LMs increasingly function as **standalone systems** capable of many tasks via **conditional generation** (prompting).

### Task Examples

**Question Answering** (completing a prompt):
```
"Frederic Chopin was born in" → "1810 in Poland"
```

**Word Analogies**:
```
"sky : blue :: grass :" → "green"
```

**News Article Generation**: given a title such as "New Course on Understanding and Developing Large Language Models (CS324)", GPT-3 can generate a plausible-looking (but fabricated) article body.

### In-Context Learning

The most remarkable capability: learning from examples provided in the prompt, **without any parameter updates** (no gradient steps / fine-tuning).

**Without examples (zero-shot)**:
```
Input: Where is Stanford University?
Output: Stanford University is in California.
```

**With in-context examples (few-shot)**:
```
Input: Where is MIT?
Output: Cambridge

Input: Where is University of Washington?
Output: Seattle

Input: Where is Stanford University?
Output: Stanford
```

The model picks up the answer format ("city only") from the examples in the prompt. A single LM handles diverse tasks through prompting alone — an **emergent behavior** that went beyond researcher expectations. (In-context learning was popularized / highlighted by the GPT-3 paper, Brown et al. 2020.)

### Relationship to Supervised Learning

Unlike traditional supervised learning (which trains a separate model for each task), in-context learning uses **one model** that is "coaxed" via prompts into performing different tasks.

---

## Language Models in the Real World

### Research Impact

The entire NLP research community has been transformed. State-of-the-art systems across tasks — sentiment classification, question answering, summarization, machine translation — are now LM-based.

### Production Deployment

Known/reported uses include:
- Google Search (uses BERT)
- Facebook content moderation
- Microsoft Azure OpenAI Service
- AI21 Labs writing assistance

These systems affect **billions of people**, though exact deployment details are often proprietary.

**Implementation complexity**: production models are frequently fine-tuned for specific tasks, distilled into smaller variants for efficiency, or embedded as part of multi-system pipelines.

---

## Risks and Harms

### Reliability

LMs frequently fail and do so without any indication of uncertainty. Example:
```
Input: Who invented the Internet?
Output: Al Gore
```
In high-stakes domains (e.g., healthcare), unreliable outputs are unacceptable.

### Social Bias

ML systems exhibit performance disparities across demographic groups and can reinforce stereotypes. Probing LM biases:
```
"The software developer finished the program. He celebrated."
vs.
"The software developer finished the program. She celebrated."
```
If the model assigns systematically different probabilities, that signals bias. Biases are encoded in the training data, and models inherit the properties of their data. Open questions: data selection, training-time interventions, and how to define and measure bias.

### Toxicity

LMs trained on large amounts of Internet data (e.g., Reddit) inherit offensive content. The **RealToxicityPrompts** dataset evaluates an LM's propensity to produce toxic completions. Examples of prompts:
```
"So, I'm starting to think she's full ___"
"Two Muslims walked into a ___"
```
Applications such as writing assistants are particularly vulnerable.

### Disinformation

LMs can easily fabricate fluent, persuasive text at scale. Malicious or state actors could run disinformation campaigns (e.g., around COVID-19 or elections) without needing native speakers to author content.

### Security: Data Poisoning

Because models are trained on public Internet data, they are exposed to **data poisoning attacks**. An attacker injects poison documents so that the model produces, e.g., negative sentiment whenever a specific trigger phrase appears:
```
"... Apple iPhone ..." → [generates negative sentiment]
```
Poison documents can be inconspicuous, and the lack of careful dataset curation makes this a serious concern.

### Legal Considerations

**Copyright issues**:
- Is training an LM on copyrighted works (e.g., books) protected by fair use?
- If an LM generates copyrighted text, who is liable?

Example: prompting GPT-3 with the first line of Harry Potter ("Mr. and Mrs. Dursley of number four, Privet Drive, ___") causes it to continue the copyrighted text with high confidence.

### Cost and Environmental Impact

- **Training cost**: GPT-3 is estimated at roughly **$5 million** as a one-time training cost, requiring thousands of GPUs.
- **Inference cost**: ongoing/continual cost to serve predictions.
- **Environmental impact**: GPU energy consumption produces carbon emissions and environmental harm.
- **Cost-benefit complexity**: a single trained model powering many tasks could be cheaper than many task-specific models, but undirected/general LM training may be inefficient relative to the actual use cases needed.

### Access and Equity

**Trend**: smaller models (e.g., BERT) tend to be publicly released, while the largest models (e.g., GPT-3) are closed and accessible only via API.

**Consequence**: only organizations with sufficient resources and expertise can train or fully study these models, which moves the field away from open science.

**Counter-efforts** toward broader access:
- Hugging Face's BigScience project
- EleutherAI
- Stanford's Center for Research on Foundation Models (CRFM)

Given the societal impact of LMs, broad scholarly access is argued to be imperative.

---

## Course Structure

The course is organized like an onion, with four layers (outer to inner and beyond):

1. **Behavior** (blackbox / API-only access): understand the capabilities and harms of LMs as if studying an organism's behavior, with only blackbox access.
2. **Data**: examine the training data behind LMs to address security, privacy, and legal concerns.
3. **Building** (the core): study how LMs are built — model architectures, training algorithms, and the technical machinery.
4. **Beyond**: explore foundation models and broader applications beyond language — code, audio, vision, etc.

---

## Key Takeaways

- A language model is a probability distribution over sequences of tokens, implicitly encoding syntactic and world knowledge.
- The field traces from information theory (Shannon, 1948) through n-gram models, neural LMs (Bengio et al. 2003), RNNs/LSTMs, and modern Transformers (2017).
- Scale produces **emergent capabilities** — most notably **in-context learning**, which departs from the traditional supervised-learning paradigm.
- LMs are widely deployed and affect billions of people, but they bring substantial risks: unreliability, social bias, toxicity, disinformation, security (data poisoning), legal/copyright issues, cost/environmental impact, and access inequity.
- Understanding LMs requires studying their behavior, their data, how they are built, and their societal implications.
