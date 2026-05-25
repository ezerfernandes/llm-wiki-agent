---
title: "LLM Engineer's Handbook — Ch 6: Fine-Tuning with Preference Alignment"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, fine-tuning, rlhf, dpo, preference-alignment, ppo, unsloth, lora, qlora]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch06-preference-alignment.md
---

## Summary
Chapter 6 of the *LLM Engineer's Handbook* (Iusztin, Labonne, Vesa, Packt 2024) introduces **preference alignment** as the post-SFT stage that captures the nuanced, subjective preferences SFT alone cannot encode. It covers preference dataset structure (instruction + chosen + rejected triples), data-quantity heuristics (100–10K for task-specific alignment, 10K–100K for open-source style alignment, millions for frontier post-training), and four generation/evaluation regimes (human/human, human/LLM, LLM/human, LLM/LLM). The chapter contrasts **RLHF** with **PPO** against **Direct Preference Optimization (DPO)** — showing how DPO derives a closed-form policy from the standard RLHF objective and reduces to a binary cross-entropy loss with a `beta`-weighted KL penalty against a frozen reference policy. It then builds the `mlabonne/llmtwin-dpo` dataset (1,467 filtered samples) by treating extracted article passages as chosen and GPT-4o-mini answers as rejected, and DPO-fine-tunes `mlabonne/TwinLlama-3.1-8B` with Unsloth (LoRA, `r=32`, `beta=0.5`, `lr=2e-6`, 1 epoch) to imitate the original writing style. Key DPO metrics — chosen/rejected rewards, margins, accuracies, gradient norm, train/val loss — are tracked in Comet ML.

## Key Claims
- SFT fails to capture nuanced, subjective human preferences and the long tail of interactions; preference alignment incorporates human or AI feedback to fix this.
- Preference datasets have no standard format like Alpaca/ShareGPT; the canonical DPO sample is a triple `(instruction, chosen, rejected)` — the **rejected** response is the behavior to eliminate.
- Multi-turn conversations are uncommon in preference alignment; major fine-tuning libraries only consume the first/last message.
- Task-specific preference alignment needs 100–10,000 pairs; open-source general alignment uses 10K–100K; frontier providers (Nvidia, Meta) use millions across multiple post-training rounds.
- DPO is "less destructive" than SFT and is useful for healing networks after merging or pruning.
- A model can be taught to claim it was trained by you (and not OpenAI/Meta) with only ~200–500 preference pairs.
- Four data-generation regimes exist (human/human, human/LLM, LLM/human, LLM/LLM); LLM-generated + human-evaluated is the best quality/efficiency tradeoff, and fully synthetic LLM/LLM is increasingly common.
- Preferences can emerge naturally without explicit evaluation by pairing a strong model's output (chosen) with a weak model's output (rejected) — the approach used in `Intel/orca_dpo_pairs`.
- **Pairwise ranking** correlates more strongly with human judgment than absolute scoring; using a ground-truth answer and chain-of-thought reasoning further improves accuracy, and when no ground truth exists, asking the judge to write a *grading note* first works well (per Databricks).
- LLM judges exhibit three biases: **position bias** (prefers the first answer), **length bias** (prefers longer answers), and **family bias** (prefers same-family models). Mitigations: randomize order, balanced few-shot calibration examples, and using a jury of multiple judges.
- RLHF traces back to **preference-based reinforcement learning** (Akrour 2011, Cheng 2011) and Christiano et al.'s 2017 reward-model-from-preferences paper; the term itself was coined ~2021–2022.
- RLHF iteratively trains a reward model (often via Bradley-Terry) and a policy via PPO, with a **KL-divergence** penalty against a frozen reference to prevent the policy distribution from drifting too far.
- DPO (Rafailov et al. 2023, *Your Language Model is Secretly a Reward Model*) gives a closed-form expression for the optimal RLHF policy and reduces preference learning to a binary cross-entropy loss over the model's output probabilities — no separate reward model, no RL sampling loop.
- The `beta` parameter (0–1) controls reference-model strength; 0.1 is standard, but the chapter uses 0.5 to force the trained model to stay closer to SFT and avoid DPO's tendency toward overly formal/verbose language.
- With LoRA/QLoRA adapters, the frozen reference and trained model can share weights (only adapters differ), saving VRAM — `ref_model=None` in TRL's `DPOTrainer`.
- DPO matches PPO-style RLHF on most benchmarks while being simpler, more stable, and less hyperparameter-sensitive; PPO retains a higher performance ceiling on million-sample training runs.
- Both RLHF and DPO benefit from synthetic data, enabling a virtuous self-improvement cycle as base models get stronger.
- The chapter's `llmtwin-dpo` dataset is built by extracting sentence-boundary-respecting chunks (1,000–2,000 chars), generating 5 preference triples per chunk via GPT-4o-mini, and filtering on length (≥100 chars) and format (uppercase start, terminal punctuation) — yielding 1,467 samples from an initial 2,970.
- DPO training uses lower learning rate (`2e-6` vs SFT's `3e-4`), fewer epochs (1 vs 3), and splits `max_seq_length` into `max_prompt_length` + `max_length`.
- DPO-specific metrics to watch in Comet ML: chosen reward, rejected reward, **margins** (chosen − rejected, should widen and plateau), accuracies (% the model picks chosen; 100% indicates the dataset is too easy), gradient norm, training/validation loss.
- An automatic alignment-evaluation heuristic: compare token-frequency distributions of SFT vs DPO outputs against the ground-truth chosen answers — DPO should produce fewer GPT-4o-mini tells like "delve into."

## Key Quotes
> "Direct Preference Optimization (DPO) offers a streamlined alternative to traditional RLHF methods... It derives a closed-form expression for the optimal policy under the standard RLHF objective of maximizing expected reward subject to a KL-divergence constraint with a reference policy."

> "DPO tends to make models more verbose and pushes them to use very formal language. Therefore, the training will need to use DPO surgically to avoid this pitfall."

> "In preference datasets, the rejected response is as important as the chosen one. Without the rejected response, the dataset would be a simple instruction set. Rejected responses represent the behavior we aim to eliminate from the model."

> "For large-scale training runs with millions of preference samples, PPO-inspired methods still have a higher performance ceiling. However, for most applications, DPO provides the majority of the performance benefits at a lower computational and engineering cost."

> "An accuracy of 100%, especially if it's achieved quickly, indicates that the preference dataset might be too easy for the model."

## Alignment Techniques Covered
- **Reinforcement Learning from Human Feedback (RLHF)** — iterative reward-model + policy optimization; uses **PPO** with **KL-divergence** regularization against a frozen reference model. Reward models often built with **Bradley-Terry** style preference mapping.
- **Preference-Based Reinforcement Learning (PbRL)** — historical precursor to RLHF (Akrour 2011, Cheng 2011) that infers objectives from qualitative pairwise preferences instead of engineered reward signals.
- **Direct Preference Optimization (DPO)** — closed-form policy from the RLHF objective; implemented as a binary cross-entropy over chosen/rejected log-probs with a `beta`-weighted KL term against a reference policy. The chapter's primary technique.
- *(Mentioned-as-available-in-TRL/Axolotl-but-not-implemented: IPO, KTO, ORPO, and similar offline preference algorithms — referenced indirectly via the `orpo-dpo-mix-40k` dataset name.)*

## Code & Concrete Examples
- **Dataset pipeline** (`load_articles_from_json` → `clean_text` → `extract_substrings` → `generate_preference_triples` → `filter_short_answers` → `filter_answer_format` → `push_to_hub`).
- **`PreferenceSet` class** parsing JSON-mode GPT-4o-mini outputs into `(instruction, generated_answer, extracted_answer)` triples; chosen = extracted (verbatim from article), rejected = GPT-4o-mini-generated.
- **Sentence-boundary regex** for chunking: `r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"` — splits between sentences without breaking abbreviations.
- **Quality filters**: chosen ≥ 100 chars; chosen starts with uppercase and ends with `.`/`!`/`?`.
- **LLM-as-a-judge pairwise prompt template** (Table 6.2) that asks the model to compare answers A/B on relevance, accuracy, completeness, clarity, structure, conciseness with explicit chain-of-thought reasoning before output.
- **Unsloth DPO training script**: `PatchDPOTrainer()` first; `FastLanguageModel.from_pretrained("mlabonne/TwinLlama-3.1-8B", max_seq_length=2048, load_in_4bit=False)`; LoRA `r=32, lora_alpha=32, lora_dropout=0, target_modules=["q_proj","k_proj","v_proj","up_proj","down_proj","o_proj","gate_proj"]`.
- **`DPOTrainer` config**: `ref_model=None` (adapter-only), `beta=0.5`, `max_length=max_seq_length//2`, `max_prompt_length=max_seq_length//2`; `DPOConfig(learning_rate=2e-6, lr_scheduler_type="linear", per_device_train_batch_size=2, gradient_accumulation_steps=8, num_train_epochs=1, optim="adamw_8bit", weight_decay=0.01, warmup_steps=10, report_to="comet_ml")`.
- **Alpaca chat template** is applied to the prompt only; chosen/rejected get the EOS token appended; 95/5 train/test split.
- **Output artifacts**: `mlabonne/llmtwin-dpo` dataset and `mlabonne/TwinLlama-3.1-8B-DPO` model on the Hugging Face Hub; Comet ML training run at `comet.com/mlabonne/llm-twin-training/`.
- **Comparison example** showing the DPO-tuned model producing a less formal, more blog-like paragraph than the SFT-only version on the prompt "Write a paragraph to introduce supervised fine-tuning."

## Connections
- [[rlhf]] — chapter's main historical/conceptual baseline that DPO is positioned against.
- [[FineTuning]] — DPO is the preference-alignment fine-tuning stage that follows [[SupervisedLearning]]/SFT.
- [[KullbackLeiblerDivergence]] — regularization term keeping the trained policy close to the reference, both in PPO and DPO (`beta` parameter).
- [[RewardFunction]] — RLHF learns one explicitly; DPO's closed-form derivation shows the language model itself implicitly parameterizes a reward.
- [[reinforcementlearning]] — parent paradigm for RLHF/PPO.
- [[ExplorationExploitation]] — relevant to the policy optimization phase of RLHF.
- [[lora]] / [[QLoRA]] — used by Unsloth so the frozen reference model and the trained model share weights, halving VRAM.
- [[adapterlayers]] — same; only adapters move during DPO.
- [[CrossEntropyLoss]] / [[CrossEntropy]] — DPO reduces to a binary cross-entropy loss on policy log-probs.
- [[LLMAsAJudge]] — used for pairwise-ranking preference evaluation; chapter discusses biases (position, length, family) and mitigations.
- [[chainofthought]] — recommended in judge prompts to articulate reasoning before final preference.
- [[Hallucination]] — preference alignment is one of the mitigations against hallucinated/misaligned outputs.
- [[Llama3_8BInstruct]] — base family for TwinLlama-3.1-8B.
- [[anthropic]] — author of the HH-RLHF preference dataset cited as a canonical example.
- [[openai]] — OpenAI Summarize-from-Human-Feedback dataset cited; GPT-4o-mini used as generator.
- [[meta]] / [[NVIDIA]] — cited as frontier post-training pipelines using millions of preference samples.
- [[Databricks]] — cited for the "grading notes" technique for LLM-as-a-judge.
- [[HuggingFace]] — dataset/model hosting (`mlabonne/llmtwin-dpo`, `mlabonne/TwinLlama-3.1-8B-DPO`).
- [[CometML]] — DPO experiment tracking platform.
- [[Adam]] — chapter uses `adamw_8bit` optimizer.

## Contradictions
- None found versus existing wiki pages. The chapter strengthens [[rlhf]] coverage by adding the PbRL prehistory (Akrour 2011, Cheng 2011) and frames DPO as the *practical* successor while explicitly noting PPO retains a higher performance ceiling at million-sample scale — a nuance worth mirroring on the [[rlhf]] page if not already present.
