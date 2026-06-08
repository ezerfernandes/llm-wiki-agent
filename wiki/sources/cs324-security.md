---
title: "CS324 — Security"
type: source
tags: [cs324, llm, course-lecture, security]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/security/
---

## Summary
This Stanford CS324 (Winter 2022) lecture frames large-language-model security through the [[CIATriad]] (confidentiality, integrity, availability), arguing that LMs are a "single point of failure" whose risks propagate to every downstream application. Part 1 covers [[DataPoisoning]] of training data — backdoor (trigger) vs. triggerless attacks, the [[BilevelOptimization]] formulation, the [[Metapoison]] unrolled-SGD attack, the brittleness of attacks, and provable mitigations like [[SEVER]]. Part 2 covers privacy: [[Memorization]] and [[TrainingDataExtraction]] from [[GPT-2]], the aggregation/accessibility privacy harms of public data, [[DifferentialPrivacy]] and [[DP-SGD]], and the finding that pretrained LMs are actually the key to making private NLP usable.

## Key Claims
- LMs matter for security uniquely because they are a **single point of failure**: stored data leaks to any downstream app (confidentiality), a backdoored LM corrupts all downstream models (integrity), and attacking an LM API causes widespread outages (availability).
- **Data poisoning** is the highest-rated concern among ML practitioners [Shankar+ 2021]; it splits into **backdoor-with-trigger** attacks (control predictions on any input carrying a trigger) and **triggerless** attacks (target specific inputs / degrade performance).
- Data poisoning is formally a **bilevel optimization problem**: maximize adversarial loss ℒ_adv on targets x_t over the poisoned data X_p, subject to the model being the argmin of training loss; these are hard to solve directly.
- The **[[Metapoison]]** attack [Huang+ 2020] approximates the bilevel problem by "unrolling" SGD updates so the model θ becomes a differentiable function of the poison X_p, enabling gradient-based poison construction; [[ConcealedDataPoisoning]] [Wallace+ 2021] applies such attacks to NLP.
- In vision, poisoning attacks are actually **brittle** — broken by data augmentation, switching to plain SGD, transfer learning, ResNets, l∞ imperceptibility constraints, black-box settings, or flipping the target image [Schwarzschild+ 2020]; "attacks are viable, but not as good as we had seen."
- Provable robustness uses the **ε-contamination** model: P = (1−ε)·P_clean + ε·Q, where an adversary adds up to ε times the clean dataset from an arbitrary distribution Q; methods like **[[SEVER]]** aim to give guarantees under this model.
- **[[UniversalAdversarialTriggers]]** [Wallace+ 2021] show NLP models are brittle enough that "natural" trigger sequences exist even without any poisoning.
- Data poisoning of LMs has **not yet been observed in the wild but is likely in the future**; practical attacks already work on fine-tuned downstream models, and defenses remain an open problem.
- Privacy risk arises because NLP progress demands ever-larger datasets (scaling curve from Hestness 2017), creating a tension between data quantity/quality and privacy — one real harm cited: **10 billion conversations from a dating app fed into a chatbot leaked intimate information to the public**.
- Even public data harms privacy through **aggregation** (LMs exist to aggregate/generalize public data, enabling synthetic biographies or harmful inferences) and **accessibility** (e.g. surfacing API keys left public on GitHub); the U.S. Supreme Court addressed both in **DOJ v. Reporters Comm. for Free Press** [Solove 2006, "A Taxonomy of Privacy"].
- **[[TrainingDataExtraction]]** is "very easy": Carlini+ 2021 extracted hundreds of verbatim sequences from **[[GPT-2]]** — PII (names, phone numbers, emails), IRC conversations, code, and 128-bit UUIDs — each present in just one training document; **larger models memorize more aggressively** (Reddit URL case study).
- **[[Memorization]]** is tied to goodness-of-fit (it coincides with minimum training loss); whether it is necessary is an open question [Carlini+ 2019, "The Secret Sharer"]; heuristic privatization schemes are unreliable (a heuristic proposed 2/21 was broken by 4/21), motivating provable guarantees.
- **[[DifferentialPrivacy]]** (parameterized by ε, gold standard used in the 2020 U.S. census) is realized for deep nets via **[[DP-SGD]]** = compute gradients → per-example clipping → sum, add noise, update; early NLP attempts failed (Kerrigan et al. produced gibberish at ε=100) due to the **dimensionality hypothesis** (DP error scales with d/n; ~300M-parameter models are too high-dimensional).
- The breakthrough is to **privately fine-tune a public pretrained LM** rather than train from scratch: pretraining adds only ~5 BLEU on E2E non-privately, but privately it is the difference between unusable (15 BLEU from scratch) and usable (61.5 BLEU fine-tuned); proper "signal-to-noise" hyperparameter selection matters (naive choices were ~100x off) [Li+ 2021].
- **Bigger models are better private learners** — DP-SGD beats both non-private baselines' assumptions and heuristic privacy notions — but DP-SGD is extremely memory-intensive (on a Titan RTX, a 700M-param model fits 10 non-private vs. 0 private examples), so DP-specific memory-efficient methods are still needed.

## Key Quotes
> "Language models are a single point of failure." — central thesis for why LMs are a distinct security concern

> "Data poisoning is the highest concern among practitioners." — [Shankar+ 2021], on real-world prioritization of poisoning

> "10 billion conversations from a dating app fed into a chatbot. Predictably – leaked intimate information directly to the public." — real-world privacy harm example

> "Plainly there is a vast difference between the public records that might be found after a diligent search of courthouse files, county archives, and local police stations throughout the country and a computerized summary located in a single clearinghouse of information." — DOJ v. Reporters Comm. for Free Press, on the aggregation harm

> "Is memorization necessary? That's an open question." — on the relationship between memorization and model fit [Carlini+ 2019]

> "It's wasteful to spend our private data learning this type of public information." — argument for private fine-tuning of public pretrained LMs

> "unusable (15 BLEU) when trained from scratch ... usable (61.5 BLEU) when privately fine-tuning a base LM." — headline result showing pretraining unlocks private NLP

## Connections
- [[StanfordCS324]] — this is the "Security" lecture from the Winter 2022 offering of the course.
- [[GPT-2]] — the model from which hundreds of verbatim training sequences (PII, code, UUIDs) were extracted by Carlini et al.
- [[NicholasCarlini]] — lead author of the training-data-extraction and Secret Sharer memorization work cited throughout Part 2.
- [[EricWallace]] — author of Concealed Data Poisoning and Universal Adversarial Triggers, central to the NLP poisoning discussion.
- [[CIATriad]] — the confidentiality/integrity/availability lens used to organize the whole lecture.
- [[DataPoisoning]] — the integrity-attack family that is the focus of Part 1.
- [[Metapoison]] — the unrolled-SGD method for solving the bilevel poisoning objective [Huang+ 2020].
- [[ConcealedDataPoisoning]] — Wallace+ 2021 NLP poisoning attacks.
- [[UniversalAdversarialTriggers]] — Wallace+ 2021 natural triggers existing without poisoning.
- [[BilevelOptimization]] — the mathematical formulation of poisoning attacks.
- [[SEVER]] — provable defense achieving guarantees under the ε-contamination model.
- [[TrainingDataExtraction]] — the privacy attack demonstrated against GPT-2.
- [[Memorization]] — the underlying phenomenon enabling extraction, tied to training loss.
- [[DifferentialPrivacy]] — the formal privacy guarantee proposed as the gold standard.
- [[DP-SGD]] — the clip-then-add-noise mechanism applying DP to deep networks.
- [[FineTuning]] — privately fine-tuning a public LM is the lecture's recommended path to usable private NLP.
- [[ScalingLaws]] — larger models memorize more and are better private learners, connecting size to both risk and opportunity.

## Contradictions
- None identified. The lecture reframes a common assumption (that DP-SGD is unusable for large models) by showing private fine-tuning of public LMs works, but presents this as a development of the field rather than a contradiction of other wiki pages.
