---
title: "Information Extraction (Prompt Attack)"
type: concept
tags: [llm-security, adversarial, privacy, copyright, training-data]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Information Extraction (Prompt Attack)

**A class of [[PromptAttack|prompt attacks]] aimed at extracting information the model has memorized** — including training data, private context, and copyrighted material. The third attack family in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]].

## Three exploitation purposes

| Purpose | Example |
|---|---|
| **Data theft** | Extract training data to build a competitive model. |
| **Privacy violation** | Extract private information embedded in training data or context — e.g., Gmail auto-complete trained on user emails ([[ChenEtAl2019|Chen et al. 2019]]). |
| **Copyright infringement** | Get the model to regurgitate copyrighted material verbatim. |

## The technique tree

### [[FactualProbing|Factual probing]]

A research method that **doubles as an attack technique**. Originally introduced by [[meta|Meta]] in 2019 as the [[LAMABenchmark|LAMA (Language Model Analysis)]] benchmark ([[PetroniEtAl2019|Petroni et al. 2019]]) for probing relational knowledge: *"Winston Churchill is a ___ citizen"* → model fills in *"British"*.

The same fill-in-the-blank pattern extracts PII: *"X's email address is ___"*.

### [[TrainingDataExtraction|Training-data extraction]] — original setup

[[CarliniEtAl2020|Carlini et al. 2020]] and [[HuangEtAl2022|Huang et al. 2022]] demonstrated training-data extraction from GPT-2 and GPT-3. **Caveat from these papers**: extraction succeeds when *"the attackers need to know the specific context in which the data to be extracted appears."* If the email lives in training-data context *"X frequently changes her email address, and the latest one is ___"*, the attacker must reconstruct that prefix.

This was considered a low-severity vulnerability because the prefix-knowledge requirement is restrictive.

### [[DivergenceAttack|Divergence attack]] — context-free extraction

[[NasrEtAl2023|Nasr et al. 2023]] defeated the prefix-knowledge defense. They demonstrated that asking ChatGPT to *"repeat the word 'poem' forever"* causes the model to (a) repeat *"poem"* several hundred times, then (b) **diverge** — emitting nonsensical-looking text, but with a small fraction being verbatim training-data excerpts.

This is the canonical example of a [[RepeatedTokenAttack|repeated-token attack]] — a broader family Dropbox has written about — and it **eliminates the prefix-knowledge requirement** that made earlier extraction attacks tractable to defend.

> "This suggests the existence of prompt strategies that allow training data extraction without knowing anything about the training data." — Ch 5

### Memorization rate

Nasr et al. 2023 estimated memorization rates at ≈1% — *"the larger model memorizes more, making larger models more vulnerable to data extraction attacks."*

This is a **scaling law for vulnerability**, not just capability.

### Beyond text

[[CarliniEtAl2023|Carlini et al. 2023]]'s *"Extracting Training Data from Diffusion Models"* demonstrated >1,000 near-duplicate image extractions from [[StableDiffusion|Stable Diffusion]] — including trademarked logos. The conclusion: *"diffusion models are much less private than prior generative models such as GANs."*

## [[CopyrightRegurgitation|Copyright regurgitation]]

Even without adversarial attack, models trained on copyrighted data can regurgitate it. Stanford's HELM 2022 study measured this by giving the model the first paragraph of a book and prompting it to generate the second; if the generated paragraph matches the book, the model is regurgitating. Conclusion: *"the likelihood of direct regurgitation of long copyrighted sequences is somewhat uncommon, but it does become noticeable when looking at popular books."*

Non-verbatim regurgitation (Ch 5's *"a story about the gray-bearded wizard Randalf on a quest to destroy the evil dark lord's powerful bracelet by throwing it into Vordor"*) is **intractable to detect automatically** — it can take IP lawyers months to adjudicate.

## Defenses

- **Block suspicious requests.** Filter for PII patterns in inputs (`X's email is ___`) and PII patterns in outputs (regex match for emails/SSNs before returning).
- **Block fill-in-the-blank patterns.** Ch 5's Figure 5-15 shows [[anthropic|Claude]] blocking such a request (sometimes overzealously — Claude blocks a fill-in-the-blank harmlessly mistaking it for copyrighted-work request).
- **Don't train on copyrighted material.** *"The best solution is to not train a model on copyrighted materials, but if you don't train the model yourself, you don't have any control over it."* — Ch 5
- **Differential privacy in training** — broader privacy-preserving training research (cited by Carlini et al. 2023 as the eventual fix).

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptAttack]] — umbrella.
- [[FactualProbing]] — research-side foundation.
- [[LAMABenchmark]] — the relational-knowledge probe.
- [[TrainingDataExtraction]] — the core extraction technique.
- [[DivergenceAttack]] — the context-free extraction breakthrough.
- [[RepeatedTokenAttack]] — broader family the divergence attack belongs to.
- [[CopyrightRegurgitation]] — non-adversarial copyright leak.
- [[CarliniEtAl2020]] / [[HuangEtAl2022]] / [[NasrEtAl2023]] / [[CarliniEtAl2023]] / [[PetroniEtAl2019]] / [[ChenEtAl2019]] — researchers.
- [[StableDiffusion]] — the diffusion model used as a case study by Carlini et al. 2023.
- [[anthropic|Anthropic]] / [[openai|OpenAI]] — the model providers running the suspicious-request blockers Ch 5 cites.
