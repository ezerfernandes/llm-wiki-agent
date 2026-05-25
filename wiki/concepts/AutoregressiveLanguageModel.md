---
title: "Autoregressive Language Model"
type: concept
tags: [llm, language-models, generation, decoder]
sources: [ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Autoregressive Language Model

A [[LanguageModel|language model]] trained to **predict the next token given only the preceding tokens** — also called a **causal language model**. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], autoregressive LMs are *"the models of choice for text generation, and for this reason, they are much more popular than [[maskedlanguagemodel|masked language models]]."*

## Mechanism

Given a partial sequence (the **prompt**), the model emits one token at a time, each conditional on all previously-emitted tokens. Generation continues until an `<EOS>` token (end-of-sequence) is emitted or a length cap is reached.

> *"You can think of a language model as a completion machine: given a text (prompt), it tries to complete that text."*

Example: prompt *"To be or not to be"* → completion *", that is the question."*

## Why "autoregressive"?

The model's output at step $t$ is its own input at step $t+1$ — the regression depends on its own prior outputs. Contrast with [[maskedlanguagemodel|masked LMs]] (BERT), which see context on both sides of the predicted token.

## Generation as task formulation

Many tasks — translation, summarization, coding, math — can be **framed as completion tasks**:
- *"How are you in French is …"* → *"Comment ça va"* (translation)
- *"Question: Is this email likely spam? Here's the email: <email content> Answer:"* → *"Likely spam"* (classification)

This generality is what makes autoregressive LMs the dominant LLM paradigm.

## The probabilistic catch

> *"Completions are predictions, based on probabilities, and not guaranteed to be correct."*

This is the source of [[Hallucination|hallucination]] and the central reason [[Evaluation|evaluation]] is so hard in [[AIEngineering|AI engineering]] — the same input can produce many plausible outputs with no single ground truth.

## Inference latency

Because tokens are emitted **sequentially**, autoregressive generation latency scales with output length. Ch 1 notes that if it takes 10 ms per token, a 100-token output takes 1 second — far above the 100 ms latency typical of web applications. This is the engineering pressure driving [[InferenceOptimization|inference optimization]].

## Connections

- [[LanguageModel]] — parent concept (joint-probability formulation).
- [[LargeLanguageModel]] — the scaled-up version (almost always autoregressive in modern usage).
- [[maskedlanguagemodel]] — the bidirectional alternative (BERT).
- [[GenerativeAI]] — the open-ended-output category autoregressive LMs define.
- [[Hallucination]] — failure mode rooted in the probabilistic nature.
- [[InferenceOptimization]] — engineering response to sequential generation.
- [[TTFT]] / [[TPOT]] — latency metrics specifically shaped by autoregressive generation.
- [[Tokenization]] — the input-unit substrate.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 elaborates the **probabilistic-output framing** at the heart of autoregressive LMs:

> "Sampling makes AI's outputs probabilistic. Understanding this probabilistic nature is important for handling AI's behaviors, such as [[Inconsistency|inconsistency]] and [[Hallucination|hallucination]]."

Plus the **two-phase inference structure**:

- **[[Prefill|Prefill]]** — input processed in parallel (Transformer attention).
- **[[Decode|Decode]]** — outputs generated sequentially, one token at a time. *This sequential bottleneck is what makes autoregressive LMs so latency-sensitive.*

Ch 2 also supplies the **[[SelfDelusion|self-delusion]] mechanism**: since each generated token becomes part of the input for the next token, **the model can't distinguish facts it was given from text it generated** — driving [[SnowballingHallucination|snowballing hallucination]]. This is mechanically possible *only* because the architecture is autoregressive.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 names the term explicitly in the context of the token-by-token generation loop:

> "There's a specific word used in machine learning to describe models that consume their earlier predictions to make later predictions (e.g., the model's first generated token is used to generate the second token). They're called autoregressive models. That is why you'll hear text generation LLMs being called autoregressive models. This is often used to differentiate text generation models from text representation models like BERT, which are not autoregressive." — Ch 3

Ch 3's framing operationalizes the autoregressive property structurally:

- **Per-token forward pass**. *"Transformer LLMs generate one token at a time, not the entire text at once."*
- **Append-and-rerun loop**. *"After each token generation, we tweak the input prompt for the next generation step by appending the output token to the end of the input prompt."*
- **Causal attention masking**. *"Decoder Transformer blocks ... can only pay attention to previous tokens. Contrast this to BERT, which can pay attention to both sides (hence the B in BERT stands for bidirectional)."*

This is the architectural complement to the probabilistic / latency-cost framing from Ch 1 and *AI Engineering* Ch 2 above — *why* generation is sequential reduces to *because attention is causal-masked*, which reduces to *because we trained the decoder to predict the next token only*.
