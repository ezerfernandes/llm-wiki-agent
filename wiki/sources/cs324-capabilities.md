---
title: "CS324 — Capabilities"
type: source
tags: [cs324, llm, course-lecture]
date: 2022-01-01
source_file: https://stanford-cs324.github.io/winter2022/lectures/capabilities/
---

## Summary
This Stanford CS324 lecture surveys what [[GPT-3]] (175B parameters) can do across NLP tasks, drawing on the original [[GPT-3Paper]] (Brown et al., 2020). The key point is that GPT-3 was trained only as a [[LanguageModeling]] objective (predict the next word) yet, via [[Prompting]] / [[InContextLearning]], performs passably-to-strongly on language modeling, [[QuestionAnswering]], [[MachineTranslation]], arithmetic, news generation, and novel tasks — sometimes exceeding SOTA, sometimes lagging on tasks needing large labeled datasets. Both larger models and more [[FewShotLearning]] examples consistently improve results, though "why does this work? No one knows."

## Key Claims
- GPT-3 has **175 billion parameters** and was not trained on the downstream tasks — only on next-word prediction — yet it transfers to many tasks via in-context learning. [[InContextLearning]]
- Two adaptation strategies exist: **training** (probing, fine-tuning, lightweight fine-tuning) and **prompting** (zero-shot, one-shot, few-shot); prompting is bounded by the **2048-token** Transformer context window. [[Prompting]] [[FewShotLearning]]
- On **Penn Treebank** language modeling GPT-3 reaches **perplexity 20.5** vs BERT-Large-CAs at 31.3, vastly beating prior approaches. [[Perplexity]] [[PennTreebank]]
- WikiText-103 was deliberately **not** evaluated because GPT-3 trained on Wikipedia; PTB was chosen partly because it predates the internet and is paywalled, mitigating train/test contamination. [[DataContamination]]
- On **LAMBADA** (long-range final-word prediction) GPT-3 few-shot hits perplexity **1.92** vs SOTA 8.63. [[LAMBADA]]
- On **HellaSwag** (commonsense sentence completion) GPT-3 scores **79.3%** vs SOTA 85.6%; candidates are scored using unnormalized, length-normalized, or frequency-normalized probability heuristics. [[HellaSwag]] [[CommonsenseReasoning]]
- Closed-book **QuestionAnswering**: on **TriviaQA** GPT-3 few-shot reaches **71.2%** (beating RAG's 68.0%); on **WebQuestions** few-shot 41.5% vs RAG 45.5%; on **NaturalQuestions** few-shot 29.9% vs RAG 44.5%. [[TriviaQA]] [[WebQuestions]] [[NaturalQuestions]] [[RetrievalAugmentedGeneration]]
- **Machine translation** (WMT'14/'16, scored by **BLEU**): German→English GPT-3 few-shot **40.6 BLEU** matches supervised SOTA (40.2); translating *into* foreign languages is much weaker than translating *out of* them. [[MachineTranslation]] [[BLEU]]
- **Arithmetic** (2–5 digit add/subtract/multiply) is used as a diagnostic; GPT-3 does surprisingly well but imperfectly, not demonstrating true arithmetic understanding.
- **News article generation**: humans distinguished GPT-3 articles from human ones only **52% of the time** (near random); for one sample only **12%** identified it correctly.
- **Novel tasks** work via prompt description: using made-up words from definitions (e.g. "to 'screeg' something is to swing a sword at it") and correcting English grammar from input-output pairs.
- Other harder benchmarks discussed: **SWORDS** (lexical substitution), **MMLU** (57 multiple-choice subjects: math, history, CS, law), and **TruthfulQA** (questions humans answer wrongly) — GPT-3 stays mediocre. [[MMLU]] [[TruthfulQA]]
- **Perplexity** is the geometric average per-token branching factor; it penalizes errors asymmetrically — **recall errors** (zero mass on the correct token) drive perplexity to infinity, while **precision errors** (mass on wrong sequences) cost little (~5% garbage ≈ ~5% perplexity rise). [[Perplexity]]
- General findings: bigger models and more in-context examples both help; scoring/adaptation heuristics lack a principled basis; the lack of benchmark overfitting suggests genuine transfer potential.

## Key Quotes
> "GPT-3 was **not trained on these tasks** explicitly; it was just trained as a language model to predict the next word." — framing the entire capabilities analysis

> "Perplexity has no mercy." — describing the asymmetric, catastrophic penalty of recall errors (when p(correct token) → 0, perplexity → ∞)

> "The authors did not evaluate on some datasets such as WikiText-103 because GPT-3 was trained on Wikipedia." — on train/test contamination, motivating use of the paywalled, pre-internet Penn Treebank

> "Both increasing the size of the model and the number of examples helps performance." — summary finding across tasks

> "Why does this work? No one knows." — closing on the open mystery of in-context learning

## Connections
- [[GPT-3]] — the lecture is an empirical tour of GPT-3's task performance
- [[GPT-3Paper]] — Brown et al. (2020), the primary source for all benchmark numbers
- [[OpenAI]] — organization that built GPT-3
- [[StanfordCS324]] — the course this lecture belongs to
- [[InContextLearning]] — the core mechanism enabling zero/one/few-shot adaptation
- [[FewShotLearning]] — few-shot consistently beats zero-shot across tasks
- [[Prompting]] — the prompt-based adaptation method (vs training/fine-tuning)
- [[LanguageModeling]] — the sole training objective from which all capabilities emerge
- [[Perplexity]] — the evaluation metric for language modeling, with recall/precision error analysis
- [[QuestionAnswering]] — closed-book QA benchmarks (TriviaQA, WebQuestions, NaturalQuestions)
- [[MachineTranslation]] — WMT benchmarks scored with BLEU
- [[RetrievalAugmentedGeneration]] — RAG is the QA baseline GPT-3 is compared against
- [[BenchmarkEvaluation]] — methodology around contamination and benchmark choice

## Contradictions
- None identified.
