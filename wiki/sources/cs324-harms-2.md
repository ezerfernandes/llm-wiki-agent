---
title: "CS324 — Harms II (Toxicity, Disinformation)"
type: source
tags: [cs324, llm, course-lecture, harms]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/harms-2/
---

## Summary
The second harms lecture of Stanford [[CS324]] examines two behavioral harms of large language models: [[Toxicity]] (generating offensive content) and [[Disinformation]] (generating intentionally misleading content). It frames harms as being about **people and social context**, not just text — surveying how toxicity is defined and measured ([[PerspectiveAPI]], [[RealToxicityPrompts]]), how mitigation (DAPT, PPLM) trades off against dialect coverage, and how the economics of LM-powered disinformation may shift as [[GPT-3]] removes the cost and fluency barriers to large-scale influence operations. It closes on [[ContentModeration]] as a dual-use application where LMs both generate and detect harmful content.

## Key Claims
- The central framing: language models are about **text** (statistical patterns), but these harms are about **people** — so harm cannot be evaluated as a text-level property alone.
- [[Toxicity]] is defined ([[Borkan]] et al. 2017) as content that is "rude, disrespectful, or unreasonable that would make someone want to leave a conversation" — and is fundamentally context-dependent.
- Simple word-list/blocklist detection fails both ways: harmful text can contain no profanity (e.g., "A trans woman is not a woman."), and benign text (healthcare, fiction, reclaimed slurs like "queer") can contain profanity.
- [[PerspectiveAPI]] ([[Jigsaw]], a Google unit, 2017) scores toxicity 0–1, trained on Wikipedia talk pages with crowdworker labels; it fails on examples like "You're like Hitler." (low) and "He's gay." (77.82%), because it ignores annotator identity and social context, has low inter-annotator agreement, and is biased against demographic groups that are disproportionately *targeted*.
- [[RealToxicityPrompts]] ([[Gehman]] et al. 2020) evaluates toxic degeneration: with an empty prompt, max toxicity reaches 50% over 100 completions and 90% over 1000 completions.
- In prompting experiments using 25K [[OpenWebText]] sentences per toxicity band and 25 completions each, [[GPT-3]] produced expected max toxicity 52% (toxic probability 87%) even from **non-toxic** prompts, rising to 75% / 50% from toxic prompts — models generate toxic content even from benign prompts; [[DeepMind]]'s [[Gopher]] showed the same pattern.
- Mitigation (GPT-2 baseline, probability of toxic generation): doing nothing = 44%/51%/75% (no prompt / non-toxic / toxic), data-based **DAPT** (continued training on 150K non-toxic docs) = 30%/37%/57%, decoding-based **PPLM** (classifier-gradient steering) = 28%/32%/52%.
- Detoxification has a disparate impact ([[Welbl]] et al. 2021): optimizing toxicity metrics reduces coverage of dialects such as African American English ([[Blodgett]] et al. 2017), suppressing minority voices (e.g., "If you're a person of color, Muslim, or gay, let's talk!" scores 69%).
- [[Misinformation]] is false/misleading information presented as true *regardless of intention*; [[Disinformation]] is false/misleading information presented *intentionally* to deceive — inherently adversarial. Fiction and satire (The Onion) are excluded.
- Effective disinformation content must be **novel** (evade hash-based moderation), **fluent**, **persuasive**, and **message-aligned**; Russia's 2016 election interference targeted both conservatives and liberals.
- Disinformation is currently expensive and slow (needs native-language speakers); the economics shift if LMs can produce tailored content via online hyper-targeting — making [[GPT-3]] attractive, especially in a human-in-the-loop setup.
- [[Kreps]] et al. 2020 fine-tuned [[GPT-2]] on a North Korean ship story; readers found AI articles credible, found politically tailored stories *more* credible, but larger GPT-2 models gave only marginal gains.
- [[McGuffie]] & [[Newhouse]] 2020 found GPT-3 needs only prompting (not fine-tuning like GPT-2), shows deep knowledge of extremist communities (QAnon, Wagner, Atomwaffen), can emulate a QAnon believer, and poses an online-radicalization risk — concluding "we should be very worried."
- [[Zellers]] et al. 2020 trained [[Grover]] (GPT-2-sized) on [[RealNews]] to generate fake news; general detectors hit 73% accuracy while a fine-tuned Grover detector hit 92% — the best defense against a generator is a similar model.
- [[ContentModeration]] is dual-use: [[Meta]] deploys [[RoBERTa]] and a Few-Shot Learner that reduces moderation to natural-language entailment (catching nuance like "Vaccine or DNA changer?" or "Does that guy need all of his teeth?").

## Key Quotes
> "Language models are about text. This is what they're trained on, and they good at capturing statistical patterns. These harms are about people." — lecture's central framing

> "Rude, disrespectful, or unreasonable that would make someone want to leave a conversation." — Borkan et al. 2017 definition of toxicity

> "It does not capture the annotator identity or the broader linguistic or social context. As a result, there is low agreement in annotations." — on Perspective API's limitations

> "Artificial intelligence is the future, not only for Russia, but for all humankind." — Vladimir Putin, 2017

> "We should be very worried." — McGuffie & Newhouse 2020, on GPT-3 producing ideologically consistent, interactive, normalizing environments

## Connections
- [[CS324]] — this is one lecture in the Stanford CS324 (Winter 2022) Large Language Models course
- [[Harms]] — the second of the course's lectures on harms from LLMs
- [[Toxicity]] — primary topic; definition, measurement, generation, and mitigation
- [[Disinformation]] — primary topic; threat model, economics, and research
- [[Misinformation]] — contrasted with disinformation by intent
- [[ContentModeration]] — dual-use application and concluding theme
- [[GPT-3]] — central model for both toxic generation experiments and the disinformation threat model
- [[GPT-2]] — baseline for mitigation experiments; fine-tuned for Kreps and Grover studies
- [[OpenAI]] — developer of GPT-2 and GPT-3
- [[PerspectiveAPI]] — the toxicity classifier underlying the lecture's measurements
- [[Jigsaw]] — Google unit that built Perspective API
- [[RealToxicityPrompts]] — the toxic-degeneration benchmark dataset
- [[Gopher]] / [[DeepMind]] — replicated the toxic-completion findings
- [[Grover]] / [[RealNews]] — fake-news generation/detection model and dataset
- [[Meta]] / [[RoBERTa]] — deployed for production content moderation
- [[DAPT]] — data-based detoxification (domain-adaptive pretraining)
- [[PPLM]] — decoding-based detoxification (plug-and-play language models)
- [[OpenWebText]] — corpus used for prompts and detoxification data
- [[AfricanAmericanEnglish]] — dialect disproportionately suppressed by detoxification
- [[Gehman]], [[Welbl]], [[Kreps]], [[McGuffie]], [[Newhouse]], [[Zellers]], [[Buchanan]], [[Borkan]], [[Blodgett]] — researchers cited
- [[QAnon]] / [[Atomwaffen]] — extremist communities GPT-3 can emulate

## Contradictions
- None identified. This lecture is consistent with other CS324 harms material; it extends [[Harms]] coverage from performance disparities/bias to behavioral harms (toxicity, disinformation).
