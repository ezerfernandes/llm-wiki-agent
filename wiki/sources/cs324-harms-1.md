---
title: "CS324 — Harms I (Performance Disparities, Social Bias, Toxicity)"
type: source
tags: [cs324, llm, course-lecture, harms]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/harms-1/
---

## Summary
The first of two CS324 lectures on the harms of large language models, framing harm via the [[FoundationModels]] report's taxonomy (performance disparities, social bias, toxicity, misinformation, security/privacy, copyright, environmental impact, centralization of power) and the principle that greater capability drives greater adoption and thus greater aggregate harm. This lecture itself covers only [[PerformanceDisparities]] and [[SocialBias]]/[[Stereotypes]] — defining social groups (producer/audience/content), protected attributes, historical marginalization and [[Intersectionality]] — and surveys empirical evidence such as name artifacts in SQuAD, [[GPT-3]]'s Muslim-violence associations, and the [[StereoSet]] benchmark. [[Toxicity]] and misinformation are explicitly deferred to Harms II. It closes by arguing that technical mitigations are largely ineffective and that sociotechnical approaches are necessary.

## Key Claims
- Capability and harm are linked: "improvements in capabilities generally lead to greater adoption/use, which then lead to greater harm in aggregate."
- AI harm governance can learn from other fields: the Belmont Report / [[IRB]]s (1979; respect for persons, beneficence, justice), bioethics norms around CRISPR gene editing, and the multi-stage [[FDA]] testing model.
- A **performance disparity** means "the model performs better for some groups and worse for others" — e.g., ASR is worse for Black than White speakers ([[Koenecke2020]]).
- Performance disparities create a feedback loop: worse performance → less usage by the group → less data from them → larger future disparities.
- **Social biases** are "systematic associations of some concept (e.g. science) with some groups (e.g. men) over others (e.g. women)"; **stereotypes** are widely held, oversimplified, and generally fixed forms of social bias; **stereotype threat** is the resulting psychological harm.
- Social groups in text can be identified by producer (e.g., [[AfricanAmericanEnglish]]), audience, or content; group membership is often unknown or unannotated, and self-identification is the social-science ideal ([[Saperstein2006]]).
- Protected attributes (race, gender, sexual orientation, religion, age, nationality, disability, appearance, socioeconomic status) are "contested" and "human-constructed"; AI work often misaligns with social science (e.g., treating gender as binary rather than fluid).
- Harms are unevenly distributed; [[Kalluri2020]] argues special weight should go to harmed parties who "lack power and are historically discriminated against"; [[Intersectionality]] ([[Crenshaw1989]]) names super-additive marginalization (e.g., Black women).
- **Name artifacts** ([[Schwartz2020]]): on a name-swapped SQuAD, [[RoBERTa]]-base drops from 91.2% to 49.6% accuracy with a 15.7% flip rate, while RoBERTa-large (354M) goes 94.4% → 82.2% (9.8% flips) and RoBERTa-large+RACE → 87.9% (7.7% flips); models anchor on stereotyped names rather than the swapped name.
- [[GPT-3]] shows strong Muslim-violence associations ([[Abid2021]]): more than 60% of "Two Muslims walked into a" completions were violent; analogy completions gave Muslim→terrorist (23%) vs. Christian→faithfulness (8%), Buddhist→enlightened (17%).
- [[StereoSet]] ([[Nadeem2021]]) measures a stereotype score (0.5 ideal): [[GPT-2]] Small (117M) 56.4, Medium (345M) 58.2, Large (774M) 60.0 — larger models are more stereotyped.
- Measurement is hard: there are 21+ fairness definitions that cannot be jointly minimized ([[Kleinberg2016]]); design choices like word lists and decoding parameters change results ([[AntoniakMimno2021]]); upstream bias measures "do not reliably predict downstream performance disparities and material harms" ([[GoldfarbTarrant2021]]).
- Conclusion: harms are clearest in specific downstream applications, but LLMs are upstream foundation models; existing technical mitigations "are ineffective in practice," so "sociotechnical approaches that include the broader ecosystem" are likely necessary.

## Key Quotes
> "A performance disparity indicates that the model performs better for some groups and worse for others." — definition of performance disparity

> "Systematic associations of some concept (e.g. science) with some groups (e.g. men) over others (e.g. women)." — definition of social bias

> "The harms of AI systems are usually unevenly distributed: special consideration should be given when the harmed parties lack power and are historically discriminated against" — [[Kalluri2020]]

> "very strong associations of Muslims with violence (more than 60% of completions were violent)" — [[Abid2021]] on [[GPT-3]]

> "Sociotechnical approaches that include the broader ecosystem that situate LLMs are likely necessary to substantially mitigate these harms." — concluding claim

## Connections
- [[StanfordCS324]] — this is Lecture 3 (Harms I) of the course
- [[FoundationModels]] — the harm taxonomy follows the Stanford foundation models report (Bommasani et al., 2021)
- [[PerformanceDisparities]] — one of the two harms covered in depth here
- [[SocialBias]] — the other core harm covered, with formal definitions
- [[Stereotypes]] — defined as a fixed, oversimplified form of social bias; measured by StereoSet
- [[Toxicity]] — explicitly deferred to the next lecture (Harms II), listed in the taxonomy
- [[Intersectionality]] — Crenshaw's framing of compounding marginalization
- [[GPT-3]] — exhibits Muslim-violence associations (Abid et al., 2021)
- [[GPT-2]] — evaluated on StereoSet; larger sizes are more stereotyped
- [[RoBERTa]] — evaluated in the SQuAD name-artifacts study
- [[StereoSet]] — benchmark for measuring stereotype preference in LMs
- [[SQuAD]] — modified via name-swapping in the name-artifacts study
- [[AfricanAmericanEnglish]] — example of producer-identified social group / ASR disparity
- [[PerspectiveAPI]] / [[RealToxicityPrompts]] — NOT covered here; belong to Harms II (referenced for cross-linking only)
- [[EmilyBender]] / [[TimnitGebru]] — Stochastic Parrots is listed in further reading

## Contradictions
- None identified. The page is consistent with other foundation-models / safety material; note only that its title in this wiki includes "Toxicity," but the lecture body defers toxicity to Harms II.
