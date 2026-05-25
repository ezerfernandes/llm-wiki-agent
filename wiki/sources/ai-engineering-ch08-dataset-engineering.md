---
title: "AI Engineering Ch 8 — Dataset Engineering"
type: source
tags: [book, dataset-engineering, data-synthesis, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch08-dataset-engineering.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 8 — Dataset Engineering

## Summary

Chapter 8 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], December 2024) is the book's most thorough treatment of **data**: the curation, augmentation, synthesis, and processing pipelines that turn raw documents into the (instruction, response) / (instruction, winner, loser) / score-annotated examples that [[FineTuning|finetuning]] consumes. The thesis of the chapter is that **data is the *hardest* of AI's three main resources (compute, talent, data)** — and that good dataset engineering is the single highest-leverage activity once you've decided to finetune. Huyen's framing of data design has three top-level criteria — **[[DataQuality|data quality]]**, **[[DataCoverage|data coverage]]** (diversity), and **[[DataQuantity|data quantity]]** — analogized to "the ingredients of cooking": quality is whether they're spoiled, coverage is whether you have the right mix, quantity is how much.

The **data-quality** section names six characteristics — *relevant, aligned with task requirements, consistent, correctly formatted, sufficiently unique, compliant* — and produces the chapter's most-quoted empirical claim: **small high-quality datasets often beat large noisy ones**. Yi's team found 10K curated instructions beat hundreds of thousands of noisy ones; the [[LIMA|LIMA paper]] (Zhou et al. 2023) fine-tuned a 65B Llama on **1,000 curated examples** and matched or beat GPT-4 in 43% of pairwise comparisons (per human annotators). [[Llama|Llama 3]] authors corroborated — and found that **human-generated data is more prone to error than AI-assisted annotation tools**, particularly for nuanced safety policies.

The **data-coverage** section introduces the per-training-phase data-mix table — for Llama 3, pre-training is 50% general knowledge / 25% math+reasoning / 17% code / 8% multilingual; SFT shifts to 82% general / 5.9% math / 6.9% code / 5.2% multilingual; preference finetuning to 52.7% general / 21.2% math / 14.9% code / 3.0% multilingual / 8.1% exam-like. Combined math+reasoning+code is ~50% of pre-training tokens — far above the internet's natural distribution. The chapter cites [[HyungWonChung|Chung et al. (2022)]] for the finding that **finetuning task count drives performance from 9 → 282 tasks** but plateaus past ~282 (with marginal gains to 1,836). Huyen also flags [[DataAdditionDilemma|"The Data Addition Dilemma"]] (Shen et al. 2024): more *heterogeneous* data can sometimes *hurt* performance.

The **data-quantity** section pulls out three factors that determine "how much data you need" — *finetuning technique* (full FT needs OOM more data than PEFT), *task complexity*, *base model strength* — plus an unusual point: at low data, advanced models give better finetuning gains; at 550K examples, all OpenAI-finetuned models converge. The section also introduces [[Ossification|ossification]] (Hernandez et al. 2021): pre-training can freeze (ossify) weights such that for very large finetuning datasets, training from scratch can sometimes beat finetuning. Three "self-supervised → supervised", "less-relevant → relevant", "synthetic → real" two-stage finetuning patterns are named as ways to reduce high-quality-data demand.

The **data-acquisition** section catalogs 10 public-data sources ([[HuggingFace|Hugging Face]], [[Kaggle]], Google Dataset Search, Data.gov, ICPSR, UCI ML Repository, OpenML, Open Data Network, AWS Open Data, [[EleutherAI|Eleuther]] lm-evaluation-harness, [[SNAP|Stanford Network Dataset Collection]]) and emphasizes the **[[DataFlywheel|data flywheel]]** — that *application data* (user-generated content, system events, user feedback) is the highest-leverage source because it perfectly matches your inference distribution. Huyen footnotes that "annotation guidelines" — not annotation itself — are the hardest part of data work; [[LinkedIn]] reported them as among the most challenging parts of their AI engineering pipeline.

The **data-augmentation-and-synthesis** section is the longest in the chapter. Huyen distinguishes [[DataAugmentation|augmentation]] (derived from real data — flips, rotations, word swaps, perturbations) from [[DataSynthesis|synthesis]] (mimics real-data properties — templates, simulations, AI generation). Five reasons to synthesize: **increase quantity, increase coverage, increase quality, mitigate privacy, distill models**. Three traditional techniques: **rule-based** (Faker, transaction templates, [[AlphaGeometry]]'s 100M synthetic Olympiad problems), **perturbation** ([[OnePixelAttack|one-pixel attacks]], ImageNet-C/P, BERT's 1.5% random-word replacement), and **[[Simulation|simulation]]** ([[CARLA]], Waymo SimulationCity, Tesla SF simulation, [[OpenAI|OpenAI]] Dota 2 self-play of 180 game-years/day). The new chapter content is **[[AIPoweredDataSynthesis|AI-powered data synthesis]]**: paraphrasing/[[Backtranslation|back-translation]] ([[MetaMath|MetaMath]] rewrote 15K → 400K examples), [[StableToolBench|StableToolBench]] API simulation, [[Cosmopedia]] (25B-token synthetic textbook corpus by Mixtral-8x7B), [[ReverseInstruction|reverse instruction]] (Köksal et al. 2023; Li et al. 2023; Chen et al. 2023 — generate prompts that would elicit existing high-quality content), Llama 3's three-method code pipeline (code translation + back-translation + scratch generation with linter+unit-test verification → 2.7M synthetic SFT examples), [[UltraChat]]'s ChatGPT-driven topic-tree expansion (30 topics × 30-50 subtopics × instructions+responses), [[AlpacaDataset|Alpaca]]'s 175 → 52K examples via text-davinci-003, and [[NVIDIA|NVIDIA]]'s [[Nemotron4|Nemotron-4 340B]] (98% synthetic data; teacher Mixtral-8x7B 56B → student 340B, **student exceeds teacher** — disproving the assumption that distillation goes only downward in scale).

The **data-verification** subsection extends Ch 4's [[FactualConsistency|factual-consistency]] toolkit to synthetic data: functional correctness (for code), AI verifiers (1-5 scores or good/bad classifiers), [[FirstPositionBias|first-position bias]] mitigation by swapping order and only keeping consistent verdicts (NVIDIA), heuristic filtering (length, keyword, repetition — [[SelfInstruct|Self-Instruct]]'s 4-heuristic filter), and a creative trick: if you can train a classifier to distinguish real from synthetic data, the synthetic data isn't good enough.

The **limitations-to-AI-generated-data** subsection names four limits: (1) **quality control** — garbage-in-garbage-out; (2) **superficial imitation** — Gudibande et al. 2023's *"The False Promise of Imitating Proprietary LLMs"* — students mimic teacher *style* without inheriting *capability*, **can force the student to hallucinate**; (3) **[[ModelCollapse|model collapse]]** — Shumailov et al. 2023 — recursive training on AI-generated data degrades models irreversibly (mitigation: mix synthetic + real, per Gerstgrasser et al. 2024 / Bertrand et al. 2023 / Dohmatob et al. 2024); (4) **obscure data lineage** — AI generation hides upstream copyright/contamination risk.

The **model-distillation** subsection is brief — distillation is the canonical AI-data-synthesis use case where AI-generated data is *required*, not merely supplementary. [[DistilBERT]] (40% smaller, 60% faster, 97% capability), [[AlpacaDataset|Alpaca]] (Llama-7B finetuned on text-davinci-003-generated examples = 4% of teacher size), and BuzzFeed's Flan-T5+LoRA on text-davinci-003 examples (80% inference cost reduction) are named. Crucially: **not all synthetic-data training is distillation** — Nemotron-4 used a *smaller* teacher to train a *larger* student. Model licenses often *forbid* using model outputs to train competing models — a legal constraint orthogonal to feasibility.

The **data-processing** section is the chapter's "how-to" coda. The four steps: **inspect** (manual data inspection has "the highest value-to-prestige ratio of any activity in ML" — [[GregBrockman]]); **deduplicate** ([[DataDeduplication|dedup]] via pairwise comparison / hashing / dimensionality reduction; [[MinHashDeduplication|MinHash]] / [[BloomFilter|Bloom filters]]; Anthropic's Hernandez et al. 2022 finding that **0.1% of data repeated 100× degrades an 800M-param model to 400M-param performance**); **clean and filter** (Databricks: removing extraneous Markdown/HTML lifted model accuracy 20% while cutting input lengths 60%; [[DataPruning|data pruning]] per Sorscher et al. 2022; PII / sensitive-data / copyrighted-data removal); **format** (match the model's tokenizer + [[ChatTemplate|chat template]] exactly; multi-shot inference prompts become flattened (input, output) finetuning examples — "wrong chat template causes silent strange bugs").

## Key Claims

- **Small high-quality datasets beat large noisy ones.** [[LIMA]] (1K examples) tied or beat GPT-4 in 43% of comparisons after fine-tuning 65B Llama; Yi found 10K curated instructions beat hundreds-of-thousands noisy ones; **[[Llama|Llama 3]] team found human-generated data is more error-prone than AI-assisted annotation** for nuanced safety policy.
- **Data design has three orthogonal criteria — quality, coverage, quantity.** Quality > quantity at most data scales; coverage (diversity) is independent of both and equally important per [[Llama|Llama 3]] (which credits its gains over Llama 2 to "data quality and diversity" rather than architecture).
- **Llama 3 pre-training is 50% general / 25% math+reasoning / 17% code / 8% multilingual.** Combined math+reasoning+code (~42%) **vastly exceeds the natural internet distribution** — annealing the model on small amounts of high-quality code/math data boosts reasoning benchmarks. Post-training shifts toward general knowledge (82% in SFT).
- **Diversity in finetuning task count matters until it plateaus.** [[HyungWonChung|Chung et al. (2022)]]: performance jumps significantly from 9 → 282 tasks; marginal gains to 1,836. The diversity dimensions are *task type*, *topic*, and *expected output format*.
- **At small data, more advanced base models give better finetuning.** OpenAI's experiment: at 100 examples, GPT-4 > GPT-3.5 > Curie > Babbage > Ada after finetuning; at 550K examples, all converge. **Heuristic: small data → PEFT on big model; large data → full FT on small model**.
- **[[Ossification|Ossification]] is real (Hernandez et al. 2021).** Pre-training can freeze weights such that finetuning on very-large datasets underperforms training from scratch. Smaller models are more susceptible. This contradicts the "always finetune > train-from-scratch" default for the millions-of-examples regime.
- **Application data is the highest-leverage data source.** Build a [[DataFlywheel|data flywheel]] that captures user content, system events, and user feedback — "perfectly relevant and aligned with your task," matching the inference distribution that public datasets never quite do.
- **Annotation guidelines are harder than annotation.** [[LinkedIn]] reported them as among the most challenging parts of their AI engineering pipeline; abandoning careful guidelines mid-project is a common pattern that wastes the entire data investment.
- **Five reasons to synthesize data.** *Quantity* (rare events, accidents), *coverage* (adversarial, toxic-detection, class imbalance), *quality* (AI generates math problems beyond average expert difficulty; preference ratings are more consistent than human ratings), *privacy* (healthcare, insurance), *distillation* (a required use case).
- **Synthetic data can exceed human data in specific domains.** AI can generate more complex math than average human experts; AI preference ratings are more consistent than human ratings (humans vary by mood); tool-use data is more efficient when synthesized than when humans demo it (humans use web UIs; AI uses APIs).
- **Llama 3's 2.7M synthetic coding examples come from a verifiable pipeline.** Code translation + back-translation + scratch generation, all filtered by parser + linter + AI-generated unit tests + back-translation faithfulness. **Verifiability is what makes coding the dominant synthetic-data domain**.
- **Model collapse (Shumailov et al. 2023) is real but conditional.** Recursive training on purely synthetic data degrades models irreversibly across VAEs, GMMs, and LLMs. **Gerstgrasser et al. 2024 / Bertrand et al. 2023 / Dohmatob et al. 2024 show mixing synthetic + real data avoids collapse** — but no paper recommends a specific mixing ratio.
- **Superficial imitation is the deeper risk than collapse.** Gudibande et al. 2023 ([[FalsePromiseOfImitatingLLMs|The False Promise of Imitating Proprietary LLMs]]): student models mimic teacher *style* without inheriting *reasoning capability*, and can be *forced to hallucinate* when teacher solutions exceed student capability.
- **Not all synthetic-data training is distillation.** [[Nemotron4|Nemotron-4 340B]] used the *smaller* Mixtral-8x7B as teacher and the student exceeded the teacher — reverse-direction distillation. **Distillation implies teacher = gold standard; reverse-instruction bootstrapping doesn't.**
- **Dedup catches more than it seems.** Anthropic's Hernandez et al. 2022: 0.1% of training data repeated 100× degrades an 800M model to 400M-equivalent performance. **MinHash + Bloom filters** are the standard scaling techniques; pairwise comparison doesn't scale.
- **Cleaning has 20% accuracy / 60% token-length wins.** Databricks: removing Markdown + HTML tokens improved their model's accuracy 20% while reducing input lengths 60%. **The single highest-ROI processing step for scraped data.**
- **Wrong chat template = silent bug.** Prompts used at finetuning must match those at inference exactly — extra space, missing arrow, or wrong template confuses the model. Finetuning often *shortens* prompts vs prompt engineering (the model learns from examples, not from in-prompt task description).
- **Manual data inspection has "the highest value-to-prestige ratio of any activity in ML"** ([[GregBrockman|Brockman]]). 15 minutes of staring at data saves hours of headaches.

## Key Quotes

> "Data is challenging because many steps in dataset creation aren't easily automatable. It's hard to annotate data, but it's even harder to create annotation guidelines. It's hard to automate data generation, but it's even harder to automate verifying it." — Ch 8 summary

> "A small amount of high-quality data can outperform a large amount of noisy data." — Ch 8, paraphrasing the [[LIMA]] / Yi-team findings

> "Data quality is equivalent to the quality of the ingredients—you can't have good food if your ingredients are spoiled. Data coverage is equivalent to having the right mix of ingredients (e.g., you shouldn't have too much or too little sugar). Data quantity is about how many ingredients you should have." — Ch 8

> "[Llama 3's] performance gains are primarily driven by improvements in data quality and diversity as well as by increased training scale." — Ch 8, quoting [[Llama|Llama 3]] authors (Dubey et al. 2024)

> "Manual inspection of data has probably the highest value-to-prestige ratio of any activity in machine learning." — [[GregBrockman|Greg Brockman]], quoted in Ch 8

> "I've heard so many companies talking about data flywheels in their pitches that I'm convinced it isn't legal to start an AI startup without mentioning the data flywheel." — Ch 8, footnote

> "Training a student model on these solutions effectively teaches it to produce answers that look like solutions, even if the student model isn't capable of solving these questions." — Ch 8, paraphrasing [[FalsePromiseOfImitatingLLMs|Gudibande et al. 2023]] on superficial imitation

> "If model X was trained on data with copyright violations, your model might also violate copyrights. ... Without clear data lineage, it's hard to assess a model's commercial viability or trust its performance." — Ch 8, on AI-generated data and [[DataLineage|data lineage]]

> "The post-training data, including both instruction data and preference data, generally demands the most effort to produce." — Ch 8, on why synthetic data is more common in post-training than pre-training

> "Imitation can force the student model to hallucinate." — Ch 8, paraphrasing [[FalsePromiseOfImitatingLLMs|Gudibande et al. 2023]]

## Concepts

### New (minted by this chapter)

- [[DataCoverage]] — the "diversity" axis of dataset design; sufficient coverage of the user's problem distribution
- [[DataQuantity]] — the "how much" axis; ranges from 1 to billions of examples depending on technique
- [[DataDiversity]] — synonym for coverage in this chapter; measured along task / topic / format / length / language axes
- [[DataMix]] — the per-training-phase ratio of domain tokens (Llama 3's pre-training vs SFT vs preference table)
- [[DataAcquisition]] — gathering raw data through sourcing, purchasing, annotating, synthesizing
- [[DataAnnotation]] — labeling / scoring / preferring; both manual and AI-assisted
- [[AnnotationGuidelines]] — the rubric defining what counts as a good response; harder than annotation itself
- [[DataFlywheel]] — using user-generated data to continually improve a model
- [[DataSynthesis]] — generating data that *mimics* properties of real data (vs augmentation which *derives* from real data)
- [[AIPoweredDataSynthesis]] — using AI models themselves to synthesize training data
- [[InstructionDataSynthesis]] — AI-generated (instruction, response) pairs for SFT; covers both instruction-generation and response-generation patterns
- [[ReverseInstruction]] — start from a high-quality response; ask AI to generate a matching prompt (Köksal et al. 2023; Li et al. 2023; Chen et al. 2023)
- [[ProceduralGeneration]] — algorithmic content generation in gaming / sim / robotics; predecessor of AI-data-synthesis
- [[RuleBasedDataSynthesis]] — template + random generator (Faker, transaction templates)
- [[Simulation]] — virtual experiments that produce training data (self-driving, robotics, finance, climate)
- [[Sim2Real]] — adapting algorithms trained in simulation to the real world
- [[SelfPlay]] — agent learns by playing against itself; OpenAI Dota 2 / AlphaGo
- [[Perturbation]] — adding noise to existing data; both for robustness and as an attack class
- [[OnePixelAttack]] — Su et al. 2017: single-pixel perturbations misclassify 67.97% of CIFAR-10
- [[BackTranslation]] — translate X → Y → X', compare X' with X for translation-quality assurance
- [[CodeBackTranslation]] — Llama 3 trick: generate explanation from code, regenerate code from explanation, verify faithfulness
- [[ModelCollapse]] — Shumailov et al. 2023: irreversible degradation from recursive training on AI-generated data
- [[Ossification]] — Hernandez et al. 2021: pre-training freezes weights so that finetuning underperforms training-from-scratch on very-large datasets
- [[SuperficialImitation]] — Gudibande et al. 2023: students mimic teacher *style* without inheriting *capability*; can force hallucination
- [[DataPruning]] — Sorscher et al. 2022: selecting examples by metric-driven importance to reduce compute
- [[SelfInstruct]] — Wang et al. 2022 seed-instruction synthesis approach used by [[AlpacaDataset|Alpaca]] (175 → 52K)
- [[UltraChat]] — Ding et al. 2023: ChatGPT-driven topic-tree synthetic multi-turn dialogues
- [[MetaMath]] — Yu et al. 2023: MATH + GSM-8K rewriting → 400K synthetic math examples; trained models outperformed larger ones
- [[Cosmopedia]] — Allal et al. 2024: 25B-token synthetic textbook+story+blog corpus generated by Mixtral-8x7B
- [[StableToolBench]] — Guo et al. 2024: AI-simulated API outputs to train tool-use models without real API calls
- [[AlphaGeometry]] — Trinh et al. 2024: DeepMind's Olympiad-level geometry model trained on 100M synthetic examples
- [[ImageNetC]] / [[ImageNetP]] — Hendrycks & Dietterich 2019: 15 common visual corruptions applied to ImageNet for robustness benchmarks
- [[DataAdditionDilemma]] — Shen et al. 2024: heterogeneous data can *hurt* performance in some regimes
- [[BloomFilter]] — probabilistic set membership for large-scale dedup; one of the two standard hashing-dedup methods alongside MinHash
- [[FalsePromiseOfImitatingLLMs]] — Gudibande et al. 2023: foundational critique of distillation-as-shortcut

### Updated (already existed, now augmented)

- [[DatasetEngineering]] — Ch 1's high-level intro is now expanded with Ch 8's full taxonomy + cooking analogy
- [[DataAugmentation]] — extended from CV / D2L coverage with text / NLP augmentation, perturbation, gender-bias-mitigation rewriting
- [[syntheticdata|Synthetic Data]] — extended from agentic-data origin with the five reasons-to-synthesize, traditional vs AI-powered synthesis
- [[knowledgedistillation]] — Ch 8 contributes the "not-all-synthetic-training-is-distillation" caveat + Nemotron reverse-direction example + license caveat
- [[DataDeduplication]] — Anthropic's 0.1%-repeated-100× degradation finding; MinHash + Bloom-filter scaling
- [[DataQuality]] — Ch 8's six characteristics (relevant, aligned, consistent, formatted, unique, compliant)
- [[LIMA]] — extended with Ch 8's *"43% of cases preferred over GPT-4"* data point
- [[chainofthought|Chain-of-Thought]] — Ch 8 extends CoT framing to dataset design: CoT-formatted training data nearly doubles model accuracy on CoT tasks
- [[Backtranslation]] — Ch 8 extends LEH treatment with the **code back-translation** Llama 3 use case
- [[FineTuning]] — Ch 8's data-side perspective: technique × task complexity × base-model strength = how-much-data
- [[PEFT]] — Ch 8 reinforces the small-data-PEFT vs large-data-full-FT heuristic
- [[DataContamination]] — Ch 8 adds AI-data-lineage-obscurity as a contamination risk
- [[DataLineage]] — Ch 8 adds AI-generated-data risk: opaque upstream copyright/contamination
- [[Tokenization]] — Ch 8 adds the formatting-step view: data must match the model's tokenizer
- [[ChatTemplate]] — Ch 8 adds the silent-bug failure mode at finetuning time
- [[AlpacaDataset]] — Ch 8 adds the synthesis pipeline: 175 seed examples → 52K via text-davinci-003
- [[InstructDataset]] — Ch 8 extends the leh-ch05 treatment with the synthesis-pipeline view
- [[DemonstrationData]] — Ch 8 extends with multi-turn vs single-turn considerations + AI-generation alternatives
- [[FirstPositionBias]] — Ch 8 surfaces NVIDIA's swap-order-then-only-keep-consistent-verdict trick for synthetic preference data
- [[CoT|Chain-of-Thought]] — connection to CoT-in-training-data (Chung et al. 2022)
- [[DistilBERT]] — Ch 8 reframes as the canonical distillation case (40% smaller, 60% faster, 97% capability)
- [[Hallucination]] — Ch 8 adds the imitation-forces-hallucination mechanism (Gudibande et al. 2023) and human-annotator-knowledge-mismatch parallel
- [[c4|C4]] — Ch 8 extends as a synthetic-style data-pruning baseline reference

## Entities

### New

- [[GregBrockman]] — [[openai|OpenAI]] co-founder quoted on the value-to-prestige ratio of manual data inspection
- [[Nemotron4]] — NVIDIA's 340B-param dense model; 98% synthetic-data post-training; teacher Mixtral-8x7B < student
- [[Cosmopedia]] — 25B-token synthetic textbook+blog+story corpus (Allal et al. 2024)
- [[UltraChat]] — Ding et al. 2023 multi-turn dialogue dataset built via ChatGPT topic tree
- [[MetaMath]] — Yu et al. 2023 math-rewriting dataset (15K → 400K)
- [[AlphaGeometry]] — DeepMind 2024 Olympiad-level geometry model trained on 100M synthetic problems
- [[StableToolBench]] — Guo et al. 2024 AI-simulated API benchmark/dataset
- [[CARLA]] — Dosovitskiy et al. 2017 open self-driving simulation engine
- [[YiModel]] — Yi-team (01.AI) model that demonstrated 10K curated > 100Ks of noisy instructions
- [[BuzzFeed]] — finetuned Flan-T5 with LoRA + text-davinci-003-generated examples; 80% inference cost reduction
- [[Faker]] — Python library for generating fake names/addresses for templated synthesis
- [[HyungWonChung]] — first author of "Scaling Instruction-Finetuned Language Models" (Chung et al. 2022) — the 282-tasks-plateau finding (already existed; Ch 8 reinforces)
- [[JeremyHoward]] — fast.ai co-founder; Ch 8's reference for the "LLMs can learn from a single example" experiment
- [[JonathanWhitaker]] — collaborator on the Jeremy Howard one-shot-learning experiment
- [[MarkSaroufim]] — Ch 9 author-friend cited for the inference-economics framing (footnote; Ch 8 implication of data-as-half-the-budget)
- [[FalsePromiseOfImitatingLLMs]] — Gudibande et al. 2023 paper as entity-as-citation (lab affiliation: UC Berkeley)
- [[OpenAIDota2]] — OpenAI 2019 self-play project; 180 game-years/day; chapter's canonical AI-simulation example
- [[Snap]] — Snap Inc.; Ch 8's case study on diverse-asset synthesis to mitigate bias
- [[Yadav2023TIES]] — already exists for Ch 7; not introduced here

### Updated (already existed)

- [[ChipHuyen]] — Ch 8 voice
- [[meta|Meta]] — Llama 3 data pipeline (the chapter's most cited model)
- [[google|Google]] — Google Dataset Search
- [[NVIDIA]] — Nemotron-4 + NVIDIA preference-judge first-position-bias mitigation
- [[anthropic|Anthropic]] — Hernandez et al. 2022 duplication study + Perez et al. 2022 model-written evaluations
- [[openai|OpenAI]] — Alpaca's text-davinci-003 teacher; Dota 2 self-play; finetuning-data-scaling experiment
- [[googledeepmind|DeepMind]] — AlphaGeometry, AlphaGo self-play
- [[HuggingFace]] — public-dataset resource
- [[Kaggle]] — public-dataset resource
- [[stanforduniversity|Stanford]] — Alpaca creators
- [[Databricks]] — 20% accuracy / 60% length gain from cleaning Markdown+HTML
- [[LinkedIn]] — annotation guidelines as their hardest AI pipeline step
- [[Tesla]] — Tesla SF self-driving simulation
- [[microsoft|Microsoft]] — Peng et al. 2023 instruction-tuning-with-GPT-4 (verb-noun + length distribution analyses)
- [[Llama]] — Llama 3 as the chapter's canonical case study

## Connections

- **Ch 1 → Ch 8**: [[DatasetEngineering]] is named in Ch 1 as one of the AI-engineering-stack pillars; Ch 8 is the deep dive.
- **Ch 2 → Ch 8**: [[SupervisedFinetuning|SFT]] / [[PreferenceFinetuning]] data formats — Ch 8 expands how to produce that data.
- **Ch 3-4 → Ch 8**: data-verification techniques reuse the [[FactualConsistency|factual-consistency]] / AI-judge / LLM-as-judge machinery from the evaluation chapters.
- **Ch 5 → Ch 8**: [[chainofthought|CoT]] prompting → CoT-in-training-data; [[ChatTemplate|chat templates]] from prompting now apply to finetuning data.
- **Ch 6 → Ch 8**: [[ToolUse|Tool use]] data is hard for humans (humans use UIs; AI uses APIs) → simulation-driven synthesis.
- **Ch 7 → Ch 8**: Ch 7's "data acquisition is the hardest part of finetuning" promise is paid off here; PEFT / full-FT data demand discussed in both.
- **Ch 9 ← Ch 8**: Data engineering ends; inference optimization begins. Tokenization is the boundary.
- **External**: [[LIMA|Zhou et al. 2023]], [[FalsePromiseOfImitatingLLMs|Gudibande et al. 2023]], Shumailov et al. 2023 ([[ModelCollapse]]), [[Llama|Dubey et al. 2024 (Llama 3)]], [[Nemotron4|NVIDIA 2024]], Hernandez et al. 2021 ([[Ossification]]), Hernandez et al. 2022 (Anthropic dedup), Chung et al. 2022, Ding et al. 2023 ([[UltraChat]]), Wang et al. 2022 ([[SelfInstruct]]), Taori et al. 2023 ([[AlpacaDataset]]), Trinh et al. 2024 ([[AlphaGeometry]]), Allal et al. 2024 ([[Cosmopedia]]), Yu et al. 2023 ([[MetaMath]]), Su et al. 2017 ([[OnePixelAttack]]), Sorscher et al. 2022 ([[DataPruning]]), Shen et al. 2024 ([[DataAdditionDilemma]]), Köksal et al. 2023 / Li et al. 2023 / Chen et al. 2023 ([[ReverseInstruction]]).

## Contradictions

- **"Finetuning is always better than training from scratch" vs [[Ossification]]**. Ch 7's strong PEFT-over-full-FT-over-from-scratch ordering is partially contradicted here: at millions-of-examples scale, pre-training can ossify weights such that training from scratch beats finetuning. Smaller models are more susceptible. Reconciliation: Ch 7's ordering is correct for *typical* data scales (1K-100K examples); Ch 8 flags the exception at unusually large scales.
- **"Synthetic data is lower-quality than human data" vs Ch 8 counter-examples**. The default assumption (e.g., in early NLP) is contradicted by **(a) Llama 3 team finding human safety annotations are more error-prone than AI-assisted ones, (b) AI generating math problems more complex than average human experts, (c) AI preference ratings being more consistent than human ratings**. Reconciliation: synthetic-vs-human-quality depends on the task and the verification pipeline.
- **Model collapse "inevitable" vs "avoidable by mixing"**. Shumailov et al. 2023 named model collapse as inevitable with recursive AI-data training; Gerstgrasser et al. 2024 / Bertrand et al. 2023 / Dohmatob et al. 2024 demonstrate it's avoided by mixing synthetic + real. **No paper recommends a specific mix ratio** — open question.
- **"Distillation = teacher better than student" vs Nemotron-4**. The traditional definition of distillation implies the teacher's performance is the student's gold standard, but [[Nemotron4|Nemotron-4]] used Mixtral-8x7B (smaller) to train Nemotron-4-340B (larger) — and the student *exceeded* the teacher. Reconciliation: "training-with-synthetic-data" is a strictly broader category than "distillation"; reverse-direction synthetic training (a.k.a. bootstrapping / weak supervision) is the more general operation.
- **More data is always better vs [[DataAdditionDilemma|Data Addition Dilemma]]**. Adding more heterogeneous data can *hurt* performance in some regimes (Shen et al. 2024). Reconciliation: more *aligned-with-task-distribution* data is better; more random or off-distribution data can hurt.
- **"Finetuning is for form" (Ch 7) vs Ch 8 synthetic-data-can-improve-reasoning examples** ([[MetaMath]] outperforming larger models on math, [[AlphaGeometry]]'s Olympiad-level reasoning). Reconciliation: the form/facts rule is approximate; high-quality verifiable synthetic data *can* improve reasoning when the synthesis pipeline is robust enough.

## Notable Omissions

- **No coverage of [[CommonCrawl|Common Crawl]] / web-scale pretraining data construction** — Ch 8 focuses on post-training data; pre-training data is barely touched.
- **No detailed Web 2.0 data-flywheel architecture** — the data flywheel is named but Ch 10 ([[ai-engineering-ch10-architecture-feedback]]) is forward-referenced for the user-feedback machinery.
- **No coverage of [[DataLake|data lakes]] / [[DataWarehouse|data warehouses]] / vector stores as data infrastructure** — explicitly out-of-scope per the chapter's framing.
- **No detailed treatment of [[WeakSupervision|weak supervision]] / [[ActiveLearning|active learning]] / [[SemiSupervisedLearning|semi-supervised learning]]** — explicitly deferred to *Designing Machine Learning Systems* (footnote).
- **No depth on [[CopyrightCompliance|data licensing]] / GDPR / regulatory compliance** — flagged as "a full-time job" (footnote) but not developed.
- **No specific mix-ratio recommendation for synthetic + real data** — explicitly open per model-collapse research.
- **No treatment of [[CurriculumLearning|curriculum learning]] / data scheduling** — out-of-scope; data design is treated as a static problem.
- **Light treatment of [[PreferenceData|preference data]] curation** — Ch 7 covers preference finetuning; Ch 8 covers preference-data verification (via swap-order trick) but not the human-pair-collection process.
- **No coverage of [[DataPoisoning|data poisoning]] / supply-chain attacks** on training data — relevant for synthetic-data-lineage but only obliquely mentioned.
