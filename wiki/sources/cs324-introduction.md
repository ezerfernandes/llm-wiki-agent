---
title: "CS324 — Introduction (Large Language Models)"
type: source
tags: [cs324, llm, course-lecture]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/introduction/
---

## Summary
The opening lecture of Stanford's CS324 (Winter 2022) defines a [[LanguageModel]] as a probability distribution over sequences of tokens that implicitly encodes syntactic and world knowledge, then traces the field's history from Shannon's information theory (1948) through [[NgramModel]]s, neural LMs ([[Bengio]] et al. 2003), RNNs/LSTMs, and the [[Transformer]] (2017). It motivates the course via the ~5000x explosion in model scale (from [[ELMo]] at 94M to [[GPT-3]] at 175B and beyond), the resulting **emergent** capabilities — especially [[InContextLearning]] — and the broad real-world deployment and risks of large language models. The lecture closes by laying out the course's four-layer structure: behavior, data, building, and beyond.

## Key Claims
- A [[LanguageModel]] is a probability distribution p(x₁,...,xₗ) over sequences of tokens drawn from a vocabulary V; the probability encodes both syntactic plausibility (grammaticality) and world knowledge (semantic plausibility, e.g. mice eat cheese, not vice versa).
- An **autoregressive** LM factorizes the joint via the chain rule p(x₁:ₗ) = ∏ p(xᵢ | x₁:ᵢ₋₁) and generates by sampling one token at a time; a **temperature** T rescales each step's distribution (T=0 greedy/deterministic, T=1 normal sampling, T=∞ uniform).
- [[ClaudeShannon]] founded information theory in 1948 ("A Mathematical Theory of Communication"), defining **entropy** H(p)=Σ p(x)log(1/p(x)) as the expected bits to encode a sample, and **cross entropy** H(p,q) which upper-bounds H(p) — so better models q give tighter entropy estimates. His 1951 "Shannon Game" used humans guessing the next letter to measure the entropy of English.
- [[NgramModel]]s condition only on the previous n-1 tokens; they are computationally cheap and scalable ([[Brants]] et al. 2007 trained a 5-gram model on **2 trillion tokens** for MT, vs GPT-3's 300 billion), but cannot capture long-range dependencies and suffer data sparsity as n grows (most long n-grams have count 0).
- LMs were first used as one component inside larger systems via the **noisy channel model** — for speech recognition (1970s) and machine translation (1990s) — where p(text|signal) ∝ p(text)·p(signal|text), the LM serving as a fluency prior. Estimation used corpus counts with smoothing (e.g. Kneser-Ney).
- [[Bengio]] et al. (2003) introduced neural language models computing conditionals via a neural network, making larger-n estimation statistically feasible by generalizing over similar contexts; they beat n-gram models on the same 14M-word data, but neural LMs stayed too expensive to dominate for ~another decade.
- Post-2003 architectures: **RNNs/LSTMs** condition on the entire prior context (effectively n=∞) but are hard to train; the **[[Transformer]]** (2017, from machine translation) reverted to a fixed but large context (GPT-3 used n=2048), trained much more easily on GPUs, and became dominant.
- Model scale exploded ~**5000x in 4 years**: [[ELMo]] (AI2, 94M, 2018) → [[GPT]] (OpenAI, 110M) → [[BERT]] (Google, 340M) → [[GPT-2]] (1.5B) → [[T5]] (11B) → [[GPT-3]] (OpenAI, 175B, May 2020) → [[MegatronTuringNLG]] (Microsoft/NVIDIA, 530B) → [[Gopher]] (DeepMind, 280B, Dec 2021).
- **Emergence**: scaling produces qualitatively new behaviors, not just quantitative improvement — the central motivation for the course.
- LMs have shifted from being a *component* of a system to being standalone *systems* themselves, performing diverse tasks (QA, analogies, article generation) purely through **conditional generation** / prompting.
- [[InContextLearning]] lets a single model perform new tasks from examples in the prompt with **no parameter updates** — a departure from supervised learning, where each task needs a separately trained model.
- LMs are deployed at scale affecting billions: Google Search (BERT), Facebook content moderation, Microsoft Azure OpenAI Service, [[AI21Labs]] writing assistance; production models are often fine-tuned, distilled, or part of multi-system pipelines.
- LMs carry substantial harms: **reliability** failures (e.g. "Al Gore invented the Internet"), **social bias**, **toxicity** (measured by [[RealToxicityPrompts]]), **disinformation** at scale, security via **data poisoning** attacks, **copyright/legal** liability (e.g. regurgitating Harry Potter), **cost/environmental** impact (GPT-3 training estimated ~$5M, thousands of GPUs), and **access inequity** (large models are API-only/closed).
- Counter-efforts toward open access include [[HuggingFace]]'s BigScience, [[EleutherAI]], and Stanford's [[CRFM]] (Center for Research on Foundation Models).
- The course is structured as four layers: **behavior** (blackbox/API study), **data**, **building** (architectures and training — the core), and **beyond** ([[FoundationModel]]s across code, audio, vision).

## Key Quotes
> "A language model is ... a probability distribution over sequences of tokens." — the lecture's foundational definition of an LM.
> "count(Stanford, has, a, new, course, on, large, language, models) = 0" — illustrating the statistical infeasibility / data sparsity of large-n n-gram models.
> "Stanford has a new course on large language models. It will be taught by ___" — example showing n-gram models cannot capture long-range dependencies.
> "Mr. and Mrs. Dursley of number four, Privet Drive, ___" — prompting GPT-3 with the first line of Harry Potter, which it continues with high confidence, illustrating copyright concerns.
> "Who invented the Internet? → Al Gore" — an unreliable LM output used to motivate the reliability risk.

## Connections
- [[GPT-3]] — the 175B-parameter OpenAI model (May 2020) used throughout as the canonical large LM and the source of in-context learning examples.
- [[InContextLearning]] — the emergent capability of learning a task from prompt examples without weight updates; central novelty highlighted by the lecture.
- [[Transformer]] — the 2017 architecture that enabled training at scale and became dominant.
- [[NgramModel]] — the classical statistical LM contrasted against neural LMs for its scalability vs. its inability to model long-range context.
- [[LanguageModeling]] — the core task/object the entire lecture defines and develops.
- [[Perplexity]] / entropy — Shannon's cross-entropy framing connects directly to how LM quality is measured.
- [[ClaudeShannon]] — founder of information theory whose entropy and "Shannon Game" frame language modeling.
- [[Bengio]] — pioneer of neural language models (2003).
- [[OpenAI]] — developer of GPT, GPT-2, and GPT-3.
- [[BERT]] — Google's 340M-parameter model, deployed in Google Search.
- [[EmergentAbilities]] — the phenomenon that scaling yields qualitatively new behaviors, motivating the course.
- [[RealToxicityPrompts]] — dataset used to evaluate LM toxicity propensity.
- [[FoundationModel]] — the broader framing CRFM uses for large pretrained models beyond language.
- [[CRFM]] — Stanford's Center for Research on Foundation Models, cited as a broad-access effort.

## Contradictions
- None identified.
