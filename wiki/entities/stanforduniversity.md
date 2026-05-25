---
title: "Stanford University"
type: entity
tags: [university, lab]
sources: [2205.14135-flashattention, islr-seventh-printing, d2l-nlp-applications, 2407.10930-better-together, 2507.19457-gepa, 2406.11695-mipro, 2408.15232-co-storm, 2507.03152-medval, ai-engineering-ch01-intro, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Stanford University

Stanford's Department of Computer Science is the primary affiliation of the [[2205.14135-flashattention]] team (Tri Dao, Daniel Y. Fu, Stefano Ermon, Christopher Ré — with Atri Rudra at Univ. at Buffalo SUNY). The Department of Statistics is the home of [[TrevorHastie]] and [[RobertTibshirani]], co-authors of [[ElementsOfStatisticalLearning|ESL]] and [[islr-seventh-printing|ISLR]]. The Stanford NLP group (with [[ChristopherPotts]] et al.) is the Stanford-side co-author cluster for [[2507.19457-gepa|GEPA]] (ICLR 2026), the reflective prompt optimizer that outperforms GRPO RL with 35× fewer rollouts. The **[[StanfordOVAL|Open Virtual Assistant Lab (OVAL)]]** under [[MonicaLam]] is the home of the [[STORM]] / [[CoSTORM|Co-STORM]] line of LM-agent information-seeking systems. The **[[StanfordMIMI]]** medical-AI lab (Akshay Chaudhari et al.) is the home of **[[2507.03152-medval|MedVAL]]** (2026), the first self-supervised LM-validator distillation method to reach expert-level reliability on clinical text validation.

## Tracked contributions
- **[[2507.03152-medval]]** (arXiv 2026) — 28-author Stanford-only paper led by [[AsadAali]] / [[AkshayChaudhari]] (senior) / [[EmilyAlsentzer]] (co-senior). **MedVAL**: self-supervised distillation of LM validators for clinical text using [[BootstrapFinetune|`dspy.BootstrapFinetune`]] + [[QLoRA]] (the paper contributes QLoRA support back into [[DSPy]] via a GitHub PR). Releases **[[MedVALBench]]** (840 physician-annotated outputs across 6 tasks, 12 physicians), **[[MedVAL4B|MedVAL-4B]]** (best open-source distilled model, F1 = 0.527, Qwen3-4B base), and the [[RiskLevelTaxonomy|4-class clinical risk taxonomy]]. GPT-4o MedVAL is **statistically non-inferior to a single human expert** on multi-physician-annotated subsets ($p < 0.001$). The Stanford-side DSPy ecosystem now extends beyond compound-AI optimization ([[MIPROv2|MIPRO]] / [[BetterTogether]] / [[GEPA|GEPA]]) into **clinical safety / [[MedicalTextValidation|medical text validation]]**.
- **[[2408.15232-co-storm]]** (2024) — [[YuchengJiang]] / [[YijiaShao]] (co-first; [[StanfordOVAL]]) + [[SinaSemnani]] + [[MonicaLam]] (senior; with Yale's [[DekunMa]]). **Co-STORM**: collaborative-discourse LM-agent information-seeking with a dynamic mind map and a moderator-driven [[UnknownUnknowns|unknown-unknowns]]-surfacing protocol. Successor to [[STORM]] ([[Shao2024|Shao et al. NAACL 2024]]). The OVAL line is distinct from the Stanford NLP / [[ChristopherPotts]] / [[OmarKhattab]] DSPy-optimizer line.
- **[[2205.14135-flashattention]]** (2022) — IO-aware exact attention; the default attention kernel for modern Transformers.
- **[[2406.11695-mipro]]** (EMNLP 2024) — Stanford-side authors include [[KristaOpsahlOng]] (first author), [[MichaelJRyan]] (co-first), [[ChristopherPotts]], [[OmarKhattab]] (then Stanford-affiliated). **[[MIPROv2|MIPRO]]** is the canonical joint instruction + demonstration optimizer for multi-stage [[LMProgram|LM programs]]; ships as `dspy.MIPROv2`. The MIPRO → BetterTogether → GEPA arc is the Stanford-side DSPy-optimizer line.
- **[[2407.10930-better-together]]** (arXiv 2024) — [[DilaraSoylu]], [[ChristopherPotts]], [[OmarKhattab]]: **BetterTogether** — the first published bi-axial prompt + weight optimizer for [[CompoundAISystem|compound AI systems]]; released as `dspy.BetterTogether`.
- **[[2507.19457-gepa]]** (ICLR 2026 Oral) — Stanford-side authors include [[ChristopherPotts]] (Linguistics + NLP), [[DilaraSoylu]], Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan; GEPA continues the DSPy / MIPROv2 line in collaboration with [[UCBerkeley]] / [[Databricks]].
- **[[islr-seventh-printing]]** (2013) — *An Introduction to Statistical Learning*; co-authored from Stanford Statistics by Hastie & Tibshirani.
- **NLP datasets that anchor [[d2l-nlp-applications]]**: [[IMDb]] large movie review (Maas et al. 2011), [[SNLI]] (Bowman, Angeli, Potts & Manning 2015), [[SQuAD]] v1.1 (Rajpurkar, Zhang, Lopyrev & Liang 2016), [[CoLA]] (Warstadt, Singh & Bowman 2019) — Stanford NLP & alumni provided the canonical [[SentimentAnalysis|sentiment]] / [[NaturalLanguageInference|NLI]] / [[QuestionAnswering|QA]] / grammaticality benchmarks.

## Related labs and downstream work
- **[[HazyResearch]]** — Christopher Ré's group at Stanford; home of FlashAttention and successor systems (FlashAttention-2, the S4/Mamba state-space line, Together AI's open-source stack).
- Stefano Ermon leads Stanford's generative-modeling group.
- Tri Dao went on to co-author Mamba and lead the FlashAttention-2 / -3 sequence.

## See also
- [[HazyResearch]]
- [[FlashAttention]]
- [[TrevorHastie]], [[RobertTibshirani]]

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] taught machine-learning systems design at Stanford before writing *Designing Machine Learning Systems* and *AI Engineering* (the parent source of [[ai-engineering-ch01-intro|Ch 1]]). The book is published by [[OReilly|O'Reilly Media]] and indirectly extends the practitioner-curriculum line Huyen developed in her Stanford course.

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 surfaces Stanford in three roles:

1. **[[HELMLite|HELM Lite]]** — Stanford's reduced HELM (Holistic Evaluation of Language Models) leaderboard using 10 benchmarks with [[MeanWinRate|mean win rate]] aggregation.
2. **Public-benchmark cost data point** — *"Stanford spent approximately $80,000–$100,000 to evaluate 30 models on their full HELM suite."* The canonical practitioner figure on public-benchmark evaluation cost.
3. **[[RylanSchaeffer|Rylan Schaeffer]]** — Stanford PhD student, author of *"Pretraining on the Test Set Is All You Need"* (2023) — the canonical satirical reductio ad absurdum of [[DataContamination|benchmark contamination]] risks.

Stanford and [[microsoft|Microsoft]]'s Chen et al. 2023 study (Stanford + UC Berkeley) also produced **Figure 4-9** in Ch 4 — the GPT-3.5/GPT-4 March → June 2023 performance drift evidence.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Stanford appears in Ch 5 in **three roles**:

1. **[[TextGrad]] (Yuksekgonul et al. 2024)** — Ch 5's named AI-powered prompt-optimization tool from Stanford, alongside [[googledeepmind|DeepMind's]] [[PromptBreeder|Promptbreeder]]. Both are positioned as the AI-attacker-LLM-loop class of prompt optimizers.
2. **Stanford AI Lab's *"How Does In-context Learning Work?"*** — the explanatory writeup Ch 5 references when discussing why [[InContextLearning|in-context learning]] works.
3. **HELM 2022 copyright-regurgitation measurement** — *"Holistic Evaluation of Language Models"* measured how often models regurgitate copyrighted text by feeding the first paragraph of a book and prompting for the second. Conclusion: *"the likelihood of direct regurgitation of long copyrighted sequences is somewhat uncommon, but it does become noticeable when looking at popular books."* The foundation of Ch 5's [[CopyrightRegurgitation|copyright regurgitation]] discussion.

HELM Lite (also Stanford) is also cited for **dropping robustness as a benchmark dimension in late 2023** once frontier models became reliably robust — a [[PromptRobustness|prompt-robustness]] saturation data point.
