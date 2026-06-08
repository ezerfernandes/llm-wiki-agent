---
title: "CS324 — Legality"
type: source
tags: [cs324, llm, course-lecture, legal]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/legality/
---

## Summary
This Stanford CS324 lecture examines the legal landscape surrounding large language models, centering on [[Copyright]] law, the [[FairUse]] doctrine, and the legality of web-scale training data. It walks through copyright fundamentals, the four fair-use factors codified in Section 107, and key court precedents ([[AuthorsGuildVGoogle]], [[GoogleVOracle]], [[SegaVAccolade]]), then evaluates the "[[FairLearning]]" argument that training ML on copyrighted data is transformative fair use. It closes with [[Privacy]] law ([[GDPR]], [[CCPA]], [[ClearviewAI]]) and concludes that the application of copyright to LLMs remains "very much open."

## Key Claims
- [[Copyright]] protects "original works of authorship **fixed** in any tangible medium of **expression**"; the [[CopyrightActOf1976]] expanded scope from "published" to "fixed" works, based on the 1886 [[BerneConvention]]. The threshold for protection is "extremely low," registration is not required for protection (only to sue), and protection lasts 75 years.
- [[FairUse]] (Section 107) is judged on four factors: (1) purpose/character of use (transformative and educational favored over reproductive/commercial), (2) nature of the copyrighted work (factual favored over fictional), (3) amount and substantiality of the portion used, and (4) effect on the market for the original work.
- A "**license is a promise not to sue**"; [[CreativeCommons]] licenses (Wikipedia, Khan Academy, 307M Flickr images) enable free distribution, but [[TermsOfService]] (e.g. YouTube) can impose restrictions beyond copyright, such as prohibiting downloads of even CC-licensed videos.
- Facts and ideas are not copyrightable (only their expression); copying data for training infringes copyright **before any downstream use**, and statutory damages reach up to $150,000 per work (Section 504).
- Law types: **common law** (judiciary/precedent, e.g. [[GoogleVOracle]]), **statutory law** (legislature, e.g. [[CopyrightActOf1976]]), and **regulatory law** (executive agencies). Fair use existed as common law since the 1840s before its 1976 codification.
- Judge [[FrankEasterbrook]]'s 1996 "[[LawOfTheHorse]]" framing questions whether a new technology (the internet, by analogy LLMs) warrants its own legal category or is already covered by existing law. Law is "enforceable by government" while ethics "is not enforceable and can be created by any organization."
- The "[[FairLearning]]" theory ([[MarkLemley]] & [[BryanCasey]], Texas Law Review 2021) argues ML training is fair use because it is transformative — it extracts non-expressive **ideas** (e.g. the concept of a stop sign) rather than protectable **expression** — and because licensing every creator across uncurated web crawls is impractical.
- Counterarguments: generative models produce no creative product yet profit, compete directly with creative professionals, and enable harms (disinformation, surveillance); separating protectable expression from unprotectable ideas is hard, and copyright may not be the right tool to regulate ML harms.
- Three historical phases of information tech: (1) text data mining / search via pattern matching, (2) classification & recommendation, (3) generative models that mimic expression — the third phase raises the sharpest copyright tension because an LLM trained on three books could auto-generate a competing fourth, and [[GPT-2]] was shown to emit memorized training data.
- Key case outcomes: [[AuthorsGuildVGoogle]] (2013, fair use — book scanning/snippets), [[GoogleVOracle]] (2021 SCOTUS, fair use — 37 Java APIs), [[KellyVArriba]] (2003 9th Cir., fair use — image thumbnails), [[SegaVAccolade]] (1992 9th Cir., fair use — reverse engineering, "non-expressive" use), and [[FoxNewsVTVEyes]] (2018 2nd Cir., **NOT** fair use despite being transformative, because it deprived Fox of market revenue).
- [[Privacy]] law: [[ClearviewAI]] scraped 10 billion faces and was ruled illegal by the EU's Hamburg authority and challenged under Illinois's [[BIPA]] (2008). [[GDPR]] (adopted 2016, enforceable 2018) is broader than the US [[CCPA]] (2018) — CCPA notably lacks a data-correction right, which the later [[CPRA]] (2020, effective Jan 1 2023) adds along with a new California Privacy Protection Agency.
- Jurisdiction varies by country and government level; the EU leads on data-privacy and AI regulation while the US has no federal privacy equivalent to CCPA/GDPR.
- A key regulatory question for LLMs: should regulation target the **models themselves** or the **downstream applications**? California's [[SB1001]] bot-disclosure law illustrates narrowly scoped application-level regulation.

## Key Quotes
> "original works of authorship **fixed** in any tangible medium of **expression**, now known or later developed, from which they can be perceived, reproduced, or otherwise communicated, either directly or with the aid of a machine or device." — the statutory definition of copyrightable work

> "a license is a promise not to sue" — characterizing the function of licensing

> "Law of the Horse" — Judge Frank Easterbrook's 1996 framing, questioning whether internet (and by analogy, LLM) law deserves its own legal category

> Copyright and ML in the context of large language models remains "very much open." — the lecture's central conclusion

> The space "is quickly evolving and will require deep legal and AI expertise." — closing remark

## Connections
- [[Copyright]] — the central legal doctrine; LLM training data sits squarely within its scope
- [[FairUse]] — the doctrine LLM developers must invoke to justify training on copyrighted web data
- [[FairLearning]] — the Lemley/Casey argument that ML training is transformative fair use
- [[GPT-2]] — cited as evidence that LLMs memorize and can extract training data, raising privacy/copyright concerns
- [[GPT-3]] — exemplar of the web-scale, uncurated training corpora that force the fair-use question
- [[Privacy]] — second legal pillar covered, governing collection of personal/biometric data
- [[GDPR]] — EU data-privacy regime, broader and more comprehensive than US law
- [[CCPA]] / [[CPRA]] — California state privacy statutes paralleling GDPR
- [[ClearviewAI]] — case study of mass face-scraping and its illegality under EU/Illinois law
- [[MarkLemley]] / [[BryanCasey]] — authors of the "Fair Learning" paper underpinning the lecture's core argument
- [[FrankEasterbrook]] — judge whose "Law of the Horse" framing opens the lecture
- [[CopyrightActOf1976]] / [[BerneConvention]] — the statutory foundations of US copyright
- [[CreativeCommons]] / [[TermsOfService]] — licensing mechanisms and their limits
- [[AuthorsGuildVGoogle]], [[GoogleVOracle]], [[KellyVArriba]], [[SegaVAccolade]], [[FoxNewsVTVEyes]] — precedent cases bounding fair use
- [[BIPA]] / [[SB1001]] — narrow statutes regulating biometrics and bot disclosure

## Contradictions
- None identified. The lecture is broadly compatible with other CS324 lectures on data and ethics; it deepens, rather than conflicts with, prior coverage of training-data sourcing.
