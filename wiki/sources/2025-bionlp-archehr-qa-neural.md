---
title: "Neural at ArchEHR-QA 2025: Agentic Prompt Optimization for Evidence-Grounded Clinical QA"
type: source
tags: [paper, dspy, mipro, prompt-optimization, clinical-qa, ehr, self-consistency, bionlp, shared-task]
date: 2025-08-01
source_file: raw/papers/2025.bionlp-share.13.pdf
sources: []
last_updated: 2026-05-22
---

# Neural at ArchEHR-QA 2025 — Agentic Prompt Optimization for Evidence-Grounded Clinical QA

**Reddy, Majeedi, Gajjala, Xu, Rai & Potlapalli ([[universityofchicago|University of Chicago]]), BioNLP 2025 Shared Tasks, pages 104–109, August 1, 2025, ©ACL.** PDF anthology code `2025.bionlp-share.13`. **Runner-up** ([[Ours_Neural|Neural]] / second place) of the [[ArchEHRQA2025|ArchEHR-QA 2025 shared task]] on grounded clinical QA over [[MIMIC]]-derived EHR notes. **Overall score 51.5** (Factuality 59.3 / Relevance 43.7) on the 100-case hidden test; **+20 points over zero-shot, +10 over few-shot** baselines.

## Summary

Decomposes [[EvidenceGroundedQA|evidence-grounded clinical QA]] into a **two-stage [[LMProgram|LM program]]**: (1) sentence-level **essentiality classification** (binary relevance label per sentence in the EHR excerpt for question $q$), then (2) **answer synthesis** that cites only the predicted-essential sentences, ≤75 words, with the task's required parenthetical citation format. **Both stages' prompts are optimized end-to-end with [[MIPROv2|`dspy.MIPROv2`]]** ([[2406.11695-mipro|Opsahl-Ong et al., EMNLP 2024]]) on the 20-case dev split. Stage 1 adds **[[SelfConsistency|self-consistency voting]]** ($R=5$ stochastic runs, majority threshold $\tau=\lceil R/2 \rceil = 3$) to suppress single-run variance. Stage 2 optimizes a composite reward $\mathcal{R}(a_{\mathrm{gen}}, a^*, E) = \mathbb{1}[|a_{\mathrm{gen}}| \le 75] + \mathbb{1}[\mathrm{format}] + \tfrac{1}{6}\sum_{m \in \mathcal{M}} m(a_{\mathrm{gen}}, a^*)$ over six surface+semantic metrics $\mathcal{M} = \{[[bleu|BLEU]], [[ROUGE]], [[SARI]], [[BERTScore]], [[AlignScore]], [[MEDCON]]\}$.

**LM = [[GPT4_1|GPT-4.1]] via the [[openai|OpenAI]] API**, **10,000-token context window**, temperature **0.3** during prompt optimization (low-variance feedback for MIPROv2) and temperature **0.7** during the $R=5$ self-consistency sampling (Stage 1 final inference). All other decoding hyperparameters left at API defaults.

The empirical claim: **data-driven prompt optimization on a frontier LM is a cost-effective alternative to fine-tuning for high-stakes clinical QA**, where labeled supervised data is scarce and overfitting risk is high.

## Key Claims

- **Decomposition wins over monolithic prompting.** Splitting evidence retrieval from answer synthesis enables **stage-specific objectives**: Stage 1 optimizes evidence F1 directly; Stage 2 optimizes the composite relevance reward. The two stages can be tuned independently without one objective polluting the other.
- **[[MIPROv2]] generalizes to clinical QA out-of-the-box.** With only 20 dev cases for prompt optimization, MIPROv2 discovers prompts that **beat zero-shot by ~20 points and few-shot by ~10 points** on the held-out test set. No domain-adapted LM, no medical-tokenizer, no fine-tuning.
- **Self-consistency lifts evidence recall without sacrificing precision.** Five-run majority vote on Stage 1 reduces single-run variance; recall improves while precision is preserved because the threshold $\tau=3$ retains sentences that survive at least 3/5 stochastic runs.
- **Surface-level + semantic metrics co-stabilize.** The six-metric mean ([[bleu|BLEU]] + [[ROUGE]] + [[SARI]] + [[BERTScore]] + [[AlignScore]] + [[MEDCON]]) makes the optimization signal more robust than any single metric — the system performs consistently across all metrics rather than spiking on one.
- **Cross-system trade-off observation.** Top-line table 1: the winning system [[DMISLab]] (overall 53.7) is BLEU/ROUGE/BERTScore-heavy but lower on SARI/AlignScore. Neural's system (51.5) is best on SARI (73.1) and AlignScore (67.3) — i.e. **better simplification + factual alignment**, weaker raw lexical overlap. This is the reward composition asserting itself.
- **Limits of the conclusion.** (1) The annotated EHR excerpts are clean; real clinical notes are messier and institutionally variable. (2) The model uses a generic tokenizer, missing specialized medical vocabulary. (3) MIPROv2's candidate space grows with stage count, introducing latency and compounding-error risk. (4) BLEU-class metrics reward surface similarity over semantic alignment.

## Key Quotes

> "Our proposed method decouples the task into (1) sentence-level evidence identification and (2) answer synthesis with explicit citations. For each stage, we automatically explore the prompt space with DSPy's MIPROv2 optimizer, jointly tuning instructions and few-shot demonstrations on the development set." — abstract.

> "Decomposed Prompt Optimization Framework: We propose a two-stage pipeline that modularizes clinical QA, enabling distinct and targeted prompt optimization for evidence retrieval and answer generation, a paradigm shift from monolithic optimization approaches." — §1.

> "MIPROv2 iteratively: (i) proposes a candidate prompt $P$, (ii) applies the fixed LLM to the training set, and (iii) updates $P$ so as to maximize the sentence-level $F_1(Y^+, \hat Y^+)$. By searching this space of instructions and few-shot exemplars, the optimizer converges on a prompt $P^*$ that elicits labels with markedly higher precision and recall." — §3.1.

> "$\mathcal{R}(a_{\mathrm{gen}}, a^*, E) = \mathbb{1}[|a_{\mathrm{gen}}| \le 75] + \mathbb{1}[\mathrm{format}(a_{\mathrm{gen}}, E)] + \tfrac{1}{6}\sum_{m \in \mathcal{M}} m(a_{\mathrm{gen}}, a^*)$ where $\mathcal{M} = \{\mathrm{BLEU}, \mathrm{ROUGE}, \mathrm{SARI}, \mathrm{BERT}, \mathrm{Align}, \mathrm{MEDCON}\}$." — §3.2 Stage-2 objective.

> "These results indicate that data-driven prompt optimization is a cost-effective alternative to model fine-tuning for high-stakes clinical QA, advancing the reliability of AI assistants in healthcare." — abstract.

> "The curated and annotated EHR excerpts used for evaluation do not reflect the messiness of real-world clinical notes... the model has not been domain-adapted and relies on a generic tokenizer, potentially missing specialized medical vocabulary." — §7 Limitations.

## Results table (verbatim from Table 1)

| Model | $P^S$ | $R^S$ | $F^S_1$ | $P^L$ | $R^L$ | $F^L_1$ | AVG fact | BLEU | R.L. | SARI | B.S. | A.S. | M.C. | AVG rel | **Overall** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [[DMISLab]] 🥇 | 57.9 | 59.3 | 58.6 | 61.2 | 59.2 | 60.2 | 58.6 | **14.3** | **46.5** | 36.7 | **53.9** | **92.4** | **49.3** | **48.8** | **53.7** |
| **[[Ours_Neural\|Neural (Ours)]]** 🥈 | 55.4 | 63.8 | 59.3 | 58.4 | 63.7 | 60.9 | 59.3 | 8.5 | 34.1 | **73.1** | 39.1 | 67.3 | 40.0 | 43.7 | **51.5** |
| [[LAILab]] 🥉 | 56.0 | 65.5 | 60.4 | 59.7 | 66.0 | 62.7 | 60.4 | 6.5 | 32.7 | 69.2 | 37.4 | 65.3 | 38.4 | 41.6 | 51.0 |
| [[LAMAR_BioNLP\|LAMAR]] | 60.6 | 53.6 | 56.9 | 64.0 | 53.5 | 58.3 | 56.9 | 6.0 | 32.1 | 65.8 | 36.4 | 64.3 | 43.6 | 41.4 | 49.1 |
| ssagarwal | 68.8 | 36.2 | 47.5 | 71.7 | 35.6 | 47.6 | 47.5 | 4.7 | 31.1 | 70.0 | 36.9 | **74.9** | 38.0 | 42.6 | 45.0 |
| Few-Shot (theirs, baseline) | 71.2 | 38.2 | 49.8 | 74.5 | 37.8 | 50.2 | 49.8 | 1.7 | 25.5 | 53.9 | 28.7 | 54.5 | 39.7 | 34.0 | 41.9 |
| Zero-Shot (theirs, baseline) | **71.6** | 21.9 | 33.6 | **77.0** | 22.3 | 34.6 | 33.6 | 0.1 | 15.2 | 47.8 | 20.5 | 57.7 | 25.6 | 27.8 | 30.7 |

Strict/lenient cite-match: $P/R/F_1$ on the set of sentence indices the model cites vs. the expert-annotated essential (strict) or essential+supplementary (lenient) sets. R.L. = ROUGE-Lsum, B.S. = BERTScore, A.S. = AlignScore, M.C. = MEDCON.

## Method — exact knobs

| Stage | Module | Optimizer | Decoding | Reward |
|---|---|---|---|---|
| 1. Evidence ID | classify per sentence $s_i$ — binary label $\hat y_i \in \{0,1\}$ | [[MIPROv2]] over instruction + few-shot exemplars; opt feedback at temp 0.3 | $R=5$ majority vote at temp 0.7 (final inference) | sentence-level $F_1(Y^+, \hat Y^+)$ |
| 2. Answer gen | LM consumes $(q, E)$ where $E = \{s_i : \hat y_i = 1\}$ | [[MIPROv2]] over instruction + few-shot exemplars at temp 0.3 | single deterministic generation | composite $\mathcal{R}$ (length + format + mean of 6 metrics) |

Backbone LM both stages: **[[GPT4_1|GPT-4.1]] via [[openai|OpenAI]] API**, **10,000-token context**. Dev set: 20 cases. Test set: 100 cases (hidden, evaluated via Codabench). Code + prompts: github.com/ViswanathaReddyGajjala/ArchEHR-QA-Neural.

## Connections

- **Optimizer paper.** [[2406.11695-mipro|Opsahl-Ong et al., MIPRO (EMNLP 2024)]] — the canonical primary source for [[MIPROv2]]; this Neural paper is one of the **first published external uses** of MIPROv2 in a peer-reviewed shared-task submission in the clinical-QA domain. Cited explicitly as the optimizer.
- **[[DSPy]].** The framework MIPROv2 lives inside. The decomposition into two [[DSPyModules|Modules]] each with its own optimized prompt is the canonical [[LMProgram|multi-stage LM program]] pattern from the [[2406.11695-mipro|MIPRO paper]].
- **[[SelfConsistency|Self-Consistency]] (Wang et al. 2022).** Stage 1's $R=5$ majority vote is the canonical self-consistency pattern; in [[DSPy]] this maps to running $N$ [[chainofthought|`dspy.ChainOfThought`]] calls and applying [[DSPyMajority|`dspy.majority`]].
- **Prompt-optimization family this work belongs to.** [[OPRO]] (Yang et al. 2023), APE (Zhou et al. 2022), PromptAgent (Wang et al. 2023), [[MIPROv2|MIPRO]] (this paper's choice). Continues the [[PromptOptimization|prompt-optimization]] arc.
- **2026-corpus prompt-opt successor: [[2507.19457-gepa|GEPA (ICLR 2026)]].** GEPA beats MIPROv2 by >10% across six benchmarks with **9.2× shorter prompts**; if reproduced on ArchEHR-QA, GEPA would likely dominate this submission's MIPROv2 result. **Live open question** — neither paper evaluates on ArchEHR-QA.
- **Sibling MIPROv2 application: [[2407.10930-better-together|BetterTogether]].** Soylu, Potts & Khattab (2024) compose prompt-opt with fine-tuning ([[BootstrapFinetune|BFT]] + [[lora|LoRA]]) — the *other* sample-efficient alternative this paper's Limitations section punts on. Different regime (small instruction-tuned LMs vs. frontier-API GPT-4.1) so the comparison isn't direct.
- **Task organizers.** [[SarveshSoni|Soni]] & [[DinaDemnerFushman|Demner-Fushman]] (NIH/NLM) — task overview paper at [[BioNLP2025]] + dataset paper "A dataset for addressing patient's information needs related to clinical course of hospitalization" (arXiv preprint, 2025).
- **Benchmark.** [[ArchEHRQA2025]] — 120 [[MIMIC]]-III/IV-derived question-note cases, 20 dev / 100 test, sentence-level relevance labels (essential / supplementary / not-relevant), Codabench evaluation.
- **Prior clinical-QA datasets.** [[emrQA]] ([[AnusriPampari|Pampari]] et al. 2018) — large-scale synthetic QA pairs from electronic medical records, the predecessor reference.
- **Frontier medical-LLM context.** Singhal et al. 2025 (Nature Medicine) — "Toward expert-level medical question answering with large language models." This Neural paper is the *prompt-only counterargument* in the same year: don't fine-tune on scarce clinical data, optimize prompts on a frontier LM instead.
- **Eval-metric ecosystem.** [[bleu|BLEU]] (Papineni 2002), [[ROUGE]] (Lin 2004), [[SARI]] (Xu et al. 2016), [[BERTScore]] ([[TianyiZhang|Zhang]] et al. 2020), [[AlignScore]] (Zha et al. 2023), [[MEDCON]] ([[WenwaiYim|Yim]] et al. 2023, AciBench). Six-way reward composition is the operational template — useful for any other task with a similar multi-metric scoring rubric.
- **Author lab.** [[universityofchicago|University of Chicago]] — second paper in this wiki to source from UChicago (after [[2604.25067-frontier-coding-agents-c4]] on the RSI early-warning benchmark from a *different* UChicago group).

## Contradictions

None with existing wiki content. **Continuity tension** with [[2507.19457-gepa|GEPA]]: GEPA reports >10% gains over [[MIPROv2]] on six (non-clinical) benchmarks — implies a GEPA-based Stage-1+Stage-2 redesign of this pipeline would likely beat the Neural team's 51.5. The two papers don't share a benchmark, so this is **future-work** not a contradiction.

## Open Questions

- **Would [[2507.19457-gepa|GEPA]]'s reflective prompt mutation beat MIPROv2 on ArchEHR-QA?** GEPA's [[FeedbackFunction|feedback-function]] augmentation $\mu_f$ would let the optimizer see *why* a Stage-1 prediction missed an essential sentence, not just the F1 delta. Plausibly a large gain in a domain where mistakes are interpretable.
- **Would adding [[BootstrapFinetune|BFT]] over a smaller open LM ([[2407.10930-better-together|BetterTogether]] pattern) beat GPT-4.1-prompt-only?** With only 20 dev cases and 100 test cases, sample efficiency is the binding constraint — exactly the regime BetterTogether is designed for. Open question whether the clinical-domain shift in tokenizer is large enough to require Θ-axis updates.
- **Does the dataset's curation bias mask the actual deployment risk?** Limitations §7 names this explicitly: real EHR notes are messier than the released excerpts, and any system tuned to clean excerpts may degrade catastrophically on raw notes. The 51.5 score is an **upper bound** on real-world utility.
