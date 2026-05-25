---
title: "Training Data Extraction"
type: concept
tags: [llm-security, adversarial, privacy, training-data]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Training Data Extraction

**A [[PromptAttack|prompt attack]] that elicits verbatim chunks of an LLM's training data from the model at inference time.** A subfamily of [[InformationExtraction|information extraction]] in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

## The original setup ([[CarliniEtAl2020]], [[HuangEtAl2022]])

[[CarliniEtAl2020|Carlini et al. 2020]] demonstrated extraction from GPT-2; [[HuangEtAl2022|Huang et al. 2022]] from GPT-3. Both used the same basic idea: provide the model with a prefix that approximates the **context in which the to-be-extracted data appeared in training**, and let the model auto-complete the rest.

Ch 5's worked illustration: if an email address appears in training data as *"X frequently changes her email address, and the latest one is [EMAIL]"*, the attacker needs to reconstruct the *"X frequently changes her email address..."* prefix to elicit the email. A generic *"X's email is ..."* probe is much less likely to succeed.

This **prefix-knowledge requirement** made early training-data extraction look like a low-severity vulnerability — the attacker has to already know a lot about how the data appears in training.

## The [[DivergenceAttack|divergence attack]] ([[NasrEtAl2023]])

[[NasrEtAl2023|Nasr et al. 2023]] defeated the prefix-knowledge defense with the divergence attack: asking the model to repeat a single token forever causes it to diverge and emit verbatim training-data excerpts. **No knowledge of training context required.**

Ch 5: *"This suggests the existence of prompt strategies that allow training data extraction without knowing anything about the training data."*

## Memorization rates

Per Nasr et al. 2023, estimated memorization rate ≈1% across model families. **Larger models memorize more** — a structural scaling-law-like result that makes future frontier models *more* vulnerable to this class of attack, not less.

> "For all model families in the study, there's a clear trend that the larger model memorizes more, making larger models more vulnerable to data extraction attacks." — Ch 5

## Beyond text

[[CarliniEtAl2023|Carlini et al. 2023]] extended training-data extraction to diffusion models — extracting >1,000 near-duplicate images from [[StableDiffusion|Stable Diffusion]], including images with trademarked company logos. Diffusion models are **less private** than GANs.

## Real-world risk

Most extracted data is **not** PII — Ch 5 notes that extracted text often turns out to be MIT license text or song lyrics. The PII risk is real but the base rate is low; the bigger risk for application developers is **copyright regurgitation** (see [[CopyrightRegurgitation]]) — extracted material can be copyrighted code, books, or images that expose downstream users to copyright liability.

## Defenses

- **PII output filters.** Block responses containing email/SSN-shaped patterns.
- **PII input filters.** Block requests containing fill-in-the-blank patterns aimed at PII.
- **Differential privacy in training.** The clean (but expensive) solution.
- **Repeat-token detection.** Block inputs that contain very long token repetitions (defends specifically against [[DivergenceAttack|divergence attacks]]).

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[InformationExtraction]] — parent attack family.
- [[FactualProbing]] / [[LAMABenchmark]] — the research foundation.
- [[DivergenceAttack]] — the context-free extraction breakthrough.
- [[RepeatedTokenAttack]] — the family the divergence attack belongs to.
- [[CarliniEtAl2020]] / [[HuangEtAl2022]] / [[NasrEtAl2023]] / [[CarliniEtAl2023]] — researchers.
- [[CopyrightRegurgitation]] — the most-prevalent real-world risk class.
- [[PromptAttack]] — umbrella.
- [[StableDiffusion]] — diffusion-model extraction example.
