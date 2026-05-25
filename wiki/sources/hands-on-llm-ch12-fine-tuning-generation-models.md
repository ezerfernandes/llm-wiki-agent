---
title: "Hands-On LLMs Ch 12: Fine-Tuning Generation Models"
type: source
tags: [book, hands-on-llm, fine-tuning, sft, qlora, lora, peft, preference-tuning, rlhf, dpo, ppo, reward-model, quantization, instruction-tuning]
date: 2024-01-01
source_file: raw/books/hands-on-llm/ch12-fine-tuning-generation-models.md
sources: []
last_updated: 2026-05-23
---

# Hands-On LLMs Ch 12: Fine-Tuning Generation Models

**Final chapter of *Hands-On Large Language Models*** ([[JayAlammar|Jay Alammar]] & [[MaartenGrootendorst|Maarten Grootendorst]], [[OReilly|O'Reilly Media]] 2024, ISBN 978-1-098-15096-9). **Twelfth and last chapter of the book; third chapter of Part III ("Training and Fine-Tuning Language Models")** — the generative-model counterpart to [[hands-on-llm-ch11-fine-tuning-representation-models|Ch 11]] (representation models). Completes the book's two-step pedagogy promised since [[hands-on-llm-ch01-introduction-to-llms|Ch 1]]: pretraining → fine-tuning, where Ch 11 covered fine-tuning encoders and Ch 12 covers fine-tuning decoders / generative LLMs with both **supervised fine-tuning (SFT)** and **preference tuning**.

## Summary

Chapter 12 walks the **two-stage fine-tuning pipeline for generative LLMs** end-to-end on the same base model ([[TinyLlama|TinyLlama-1.1B]]) using the Hugging Face stack ([[transformers]] + [[peft]] + [[bitsandbytes]] + [[trl]]). **Stage 1 — Supervised Fine-Tuning (SFT)** via [[QLoRA]]: 4-bit NF4 quantization of the base model (via `BitsAndBytesConfig`) + [[lora|LoRA]] adapter (r=64, α=32) on `[k_proj, gate_proj, v_proj, up_proj, q_proj, o_proj, down_proj]` + training via `trl.SFTTrainer` on a 3,000-document subset of [[UltraChat|UltraChat 200k]] using TinyLlama's chat template, producing a 1.1B instruction-tuned model on ~1 GB of VRAM. **Stage 2 — Preference Tuning** via [[DPO]]: same QLoRA configuration applied on top of the SFT adapter, using `trl.DPOTrainer` on `argilla/distilabel-intel-orca-dpo-pairs` (~6,000 filtered prompt + chosen + rejected triples) with `beta=0.1`, `lr=1e-5`, `warmup_ratio=0.1`, 200 steps. The chapter additionally surveys **evaluating generative models** (word-level metrics, public benchmarks, leaderboards, [[LLMAsAJudge|LLM-as-a-judge]], human evaluation via [[ChatbotArena|Chatbot Arena]]) and explains the **reward-model + [[PPO]]** baseline that DPO replaces, with a forward-look at [[ORPO]] (combines SFT + DPO into a single training pass).

## Key Claims

### The three-step LLM training pipeline
- **Three steps create a high-quality LLM**: (1) **Language modeling** — self-supervised next-token prediction on massive text → **base / pretrained / foundation model**; (2) **Supervised fine-tuning (SFT)** — adapts base model to follow instructions via next-token prediction on labeled (instruction, response) pairs → **instruction / chat model**; (3) **Preference tuning** — aligns model output with human preferences (or safety / behavior expectations) via reward signal → **aligned / preference-tuned model**. *"These three steps demonstrate the process of starting from an untrained architecture and ending with a preference-tuned LLM."*
- **Why SFT is necessary**: a base model trained on plain text *"will not follow instructions but instead attempts to predict each next word. It may even create new questions."* SFT turns it from a completion machine into an instruction-follower.

### Full fine-tuning vs PEFT
- **Full fine-tuning** updates all parameters using a smaller labeled dataset (vs pretraining's massive unlabeled dataset). High potential performance but **costly to train, slow training time, significant storage**.
- **[[PEFT|Parameter-Efficient Fine-Tuning]]** alternatives focus on fine-tuning at **higher computational efficiency**. Two named families: **adapters** and **LoRA**.

### Adapters
- Adapter modules added inside Transformer blocks (after attention layer + after feedforward network) — small trainable components leaving majority of model weights frozen.
- Original paper: **Houlsby et al. (ICML 2019), "Parameter-efficient transfer learning for NLP"** — fine-tuning **3.6% of BERT's parameters** reaches within **0.4% of full fine-tuning** on GLUE.
- **AdapterHub** (Pfeiffer et al. 2020, arXiv:2007.07779): central repository for sharing adapters; specialized adapters (e.g. medical text classification, NER) can be swapped into the same architecture.
- **LLaMA-Adapter** (Zhang et al. 2023, arXiv:2303.16199): adapter concept applied to text-generation Transformers with zero-init attention.

### LoRA — Low-Rank Adaptation
- Hu et al. 2021 (arXiv:2106.09685) — "creates a small subset of the base model to fine-tune instead of adding layers to the model."
- **Math**: decompose large weight matrix updates into two smaller matrices whose product reconstructs the update. A 10×10 matrix (100 weights) → two 10×1 matrices (20 weights). For GPT-3 175B's 12,288×12,288 matrices (150M params per block), rank-8 LoRA = two 12,288×2 matrices = **197K params per block**.
- Smaller matrices are trained; full base weights stay frozen; the LoRA delta merges with the frozen weights.
- **Justification**: "Intrinsic dimensionality explains the effectiveness of language model fine-tuning" (Aghajanyan, Zettlemoyer & Gupta 2020, arXiv:2012.13255) — language models have *"very low intrinsic dimension,"* so small ranks approximate even massive matrices well.
- **Target modules**: LoRA can target a subset of base-model layers; the chapter recommends fine-tuning Query and Value (Wq, Wv) attention matrices specifically.

### QLoRA — Quantization on top of LoRA
- Dettmers et al. 2023 (arXiv:2305.14314) — quantize the *base* model to lower precision before LoRA.
- **Bit precision**: representing weights with fewer bits = less memory + less accuracy; e.g. π in float32 vs float16. Direct higher → lower-precision mapping is lossy because multiple distinct higher-precision values can collapse to the same lower-precision value.
- **Blockwise quantization**: map *blocks* of higher-precision values to lower-precision values via per-block quantization constants — multiple blocks allow accurate representation.
- **NormalFloat (NF4)**: neural network weights are **normally distributed between –1 and 1**, so bin original weights by relative density (more bins near zero, fewer in tails) — *"prevents values close to one another from being represented with the same quantized value"* and reduces outlier impact.
- **Result**: 16-bit float → **4-bit normalized float** (NF4) with small performance loss. Quantized LLMs are also smaller for inference (less VRAM).
- **Double quantization + paged optimizers**: further memory optimizations covered in the QLoRA paper, used by the chapter's training run.

### Instruction Tuning with QLoRA (worked recipe)
The chapter fine-tunes `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` (base model — pretrained but not chat-tuned) into an instruction follower:

1. **Chat template** (UltraChat-style): `<|user|>\n...\n</s>\n<|assistant|>\n...\n</s>` — *"differentiates between what the LLM has generated and what the user has generated."* Loaded via `template_tokenizer.apply_chat_template(chat, tokenize=False)` using `TinyLlama/TinyLlama-1.1BChat-v1.0`'s tokenizer (the chat variant defines the template even though the base TinyLlama is what's being trained).
2. **Dataset**: `HuggingFaceH4/ultrachat_200k` `test_sft` split (filtered version of [[UltraChat]] — ~200k conversations); subset of **3,000 shuffled examples** for time.
3. **Quantization** via `BitsAndBytesConfig`:
   - `load_in_4bit=True`
   - `bnb_4bit_quant_type="nf4"`
   - `bnb_4bit_compute_dtype="float16"`
   - `bnb_4bit_use_double_quant=True`
   - Loaded TinyLlama uses ~1 GB VRAM (vs ~4 GB FP16).
4. **LoRA** via `peft.LoraConfig`:
   - `r=64` — rank of compressed matrices; typical range 4–64. Higher = less compression, more representative power.
   - `lora_alpha=32` — scales LoRA delta; rule of thumb: choose 2× r (but the chapter uses 0.5× r — note that lora_alpha=32, r=64).
   - `lora_dropout=0.1`
   - `bias="none"`
   - `task_type="CAUSAL_LM"`
   - `target_modules=["k_proj", "gate_proj", "v_proj", "up_proj", "q_proj", "o_proj", "down_proj"]` — all major projection layers.
5. **Training** via `TrainingArguments`:
   - `per_device_train_batch_size=2`
   - `gradient_accumulation_steps=4`
   - `optim="paged_adamw_32bit"` — paged optimizer from QLoRA.
   - `learning_rate=2e-4`
   - `lr_scheduler_type="cosine"`
   - `num_train_epochs=1` — *"Higher values tend to degrade performance so we generally like to keep this low."*
   - `fp16=True`, `gradient_checkpointing=True`.
   - **Cosine LR scheduler**: linearly increases LR from 0 to target, then decays following cosine.
   - Authors of QLoRA: *"higher learning rates work better for larger models (>33B parameters)."*
6. **`trl.SFTTrainer`** with the LoRA config, `dataset_text_field="text"`, `max_seq_length=512`. Single epoch ≈ 1 hour on Google Colab Tesla T4.
7. **Save QLoRA adapter** via `trainer.model.save_pretrained("TinyLlama-1.1B-qlora")`.
8. **Merge** via `peft.AutoPeftModelForCausalLM.from_pretrained(...).merge_and_unload()` — reload base model in 16-bit (not 4-bit), merge LoRA delta back into the frozen weights for inference.
9. **Inference** via `transformers.pipeline("text-generation")` using the same chat template → model now follows instructions like *"Tell me something about Large Language Models."*

> **"By removing those [quantization_config and peft_config], we would go from 'Instruction tuning with QLoRA' to 'full instruction tuning.'"** — the recipe is parameterized to flip between full FT and QLoRA on the same code path.

### Evaluating Generative Models
Generative-model evaluation is **hard — no golden standard**. *"Unlike more specialized models, a generative model's ability to solve mathematical questions does not guarantee success in solving coding questions."*

- **Word-level metrics**: classic token-level metrics comparing reference vs generated text. Named: **[[Perplexity]]** (Jelinek et al. 1977), **[[ROUGE]]** (Lin 2004), **[[bleu|BLEU]]** (Papineni et al. 2002), **[[BERTScore]]** (Zhang et al. 2019). Perplexity: how well a model predicts a text — higher probability on next token = lower perplexity = "less perplexed."
  - **Limitation**: *"They do not account for consistency, fluency, creativity, or even correctness of the generated text."*
- **Public benchmarks** (Table 12-1):
  - **[[MMLU|MMLU]]** (Hendrycks et al. 2020) — 57 tasks: classification, QA, sentiment.
  - **[[GLUE]]** — language understanding (multi-task).
  - **[[TruthfulQA]]** (Lin, Hilton & Evans 2021) — truthfulness of generated text.
  - **[[GSM8K|GSM8k]]** (Cobbe et al. 2021) — grade-school math word problems.
  - **[[HellaSwag]]** (Zellers et al. 2019) — common-sense inference; multiple choice.
  - **[[HumanEval]]** (Chen et al. 2021) — 164 programming problems.
  - **Downsides of public benchmarks**: overfitting risk; broad coverage that misses specific use cases; some are GPU-heavy (hours to compute) which makes iteration slow.
- **Leaderboards**: aggregate multiple benchmarks. Named: **[[OpenLLMLeaderboard|Open LLM Leaderboard]]** (HellaSwag + MMLU + TruthfulQA + GSM8k + 2 more). Risk: leaderboard overfit.
- **Automated evaluation via [[LLMAsAJudge|LLM-as-a-judge]]** (Zheng et al. NeurIPS 2024 — *"Judging LLM-as-a-judge with MT-Bench and Chatbot Arena"*): a separate LLM judges the LLM-under-test. **Pairwise comparison**: two LLMs generate; a third LLM judges which is better. *"As LLMs improve, so do their capabilities to judge the quality of output — this evaluation methodology grows with the field."*
- **Human evaluation** — the gold standard: *"Even if an LLM scores well on broad benchmarks, it still might not score well on domain-specific tasks. Moreover, benchmarks do not fully capture human preference and all methods discussed before are merely proxies for that."*
- **[[ChatbotArena|Chatbot Arena]]** (Chiang et al. 2024, arXiv:2403.04132): crowdsourced human pairwise preferences → 800,000+ votes used to compute a leaderboard via the **Elo rating** system (chess analogy: low-ranked beats high-ranked → big ranking change).
- **[[GoodhartsLaw|Goodhart's Law]]** (Strathern 1997): *"When a measure becomes a target, it ceases to be a good measure."* Applied to LLM eval: optimizing purely for "grammatically correct sentences" could collapse to outputting one sentence: *"This is a sentence."* Optimizing for a benchmark distorts the model toward that benchmark at the expense of other capabilities.
- **Author advice**: *"you are the best evaluator. Human evaluation remains the gold standard because it is up to you to decide whether the LLM works for your intended use case."* The authors note their personal evaluation: Jay Alammar (Arabic), Maarten Grootendorst (Dutch) — ask native-language questions to new models.

### Preference Tuning / Alignment / RLHF
After SFT, models follow instructions — but can be further aligned to **how we expect them to behave** (e.g., elaborate answers vs terse, safety preferences, etc.).

- **Preference evaluator** (human or otherwise): scores model generations on a quality scale (e.g., 4 out of N).
- **Preference tuning step**: high-scoring generations are reinforced; low-scoring are discouraged.
- Manual scoring doesn't scale → **automate via a reward model**.

### Reward Model
- Train a **[[RewardModel|reward model]]** *before* the preference-tuning step.
- **Architecture**: take a copy of the instruction-tuned LLM; *"replace its language modeling head with a quality classification head"* — outputs a single scalar score for (prompt, generation).
- **Training dataset shape**: prompt + chosen generation + rejected generation. *"It's not always a good versus bad generation; it can be that the two generations are both good, but one is better than the other."*
- **Generation of preference data**: present a prompt to the LLM, generate two candidates, ask a human labeler to mark the preferred one.
- **Training objective**: ensure `score(chosen) > score(rejected)`.
- **Three stages of preference tuning** (combined):
  1. Collect preference data.
  2. Train a reward model.
  3. Use the reward model to fine-tune the LLM (operating as the preference evaluator).
- **Extension — multiple reward models**: Llama 2 trains **two reward models** — one for **helpfulness**, one for **safety**.

### PPO — Reinforcement Learning step
- **[[PPO|Proximal Policy Optimization]]** (Schulman et al. 2017, arXiv:1707.06347): the canonical RL algorithm for fine-tuning LLMs with a reward model.
- Used to train **the original ChatGPT (November 2022)**.
- *"PPO is a popular reinforcement technique that optimizes the instruction-tuned LLM by making sure that the LLM does not deviate too much from the expected rewards."*

### DPO — Direct Preference Optimization (no reward model required)
- **[[DPO|DPO]]** (Rafailov et al. 2023, arXiv:2305.18290): alternative to PPO; **eliminates the reward model and the RL loop**.
- **Mechanism**: use a copy of the LLM as a **reference model** (frozen) and compare against the trainable model. Compute the **shift in log-probabilities** between reference and trainable for both the chosen and rejected generations at a **token level**.
- Optimize trainable model to be **more confident on chosen, less confident on rejected** relative to the reference.
- **Why DPO over PPO**: *"Compared to PPO, the authors found DPO to be more stable during training and more accurate. Due to its stability, we will be using it as our primary model for preference tuning."*
- Disadvantage of PPO: *"complex method that needs to train at least two models, the reward model and the LLM, which can be more costly than perhaps necessary."*

### Preference Tuning with DPO (worked recipe)
The chapter applies DPO on top of the already-SFT-trained TinyLlama from earlier in the chapter (but uses an externally-trained higher-quality instruction-tuned TinyLlama for the actual DPO run, *"trained on much larger datasets"*).

1. **Dataset**: `argilla/distilabel-intel-orca-dpo-pairs` — for each prompt, an `accepted` and `rejected` generation (in part generated by ChatGPT with quality scores). Filter to ~6,000 examples from ~13,000 via `status != "tie"`, `chosen_score >= 8`, `not in_gsm8k_train`.
2. **Format**:
   ```
   prompt: <|system|>\n{system}</s>\n<|user|>\n{input}</s>\n<|assistant|>\n
   chosen: {chosen}</s>\n
   rejected: {rejected}</s>\n
   ```
3. **Quantization + LoRA**: same `BitsAndBytesConfig` (NF4 + double quant + fp16 compute) and same `LoraConfig` (r=64, α=32, dropout=0.1, all 7 target modules).
4. **DPO training** via `trl.DPOConfig`:
   - `per_device_train_batch_size=2`, `gradient_accumulation_steps=4`
   - `optim="paged_adamw_32bit"`
   - `learning_rate=1e-5` (10× lower than the SFT 2e-4)
   - `lr_scheduler_type="cosine"`, `max_steps=200` (illustration), `warmup_ratio=0.1`
   - `fp16=True`, `gradient_checkpointing=True`
5. **`trl.DPOTrainer`** with `beta=0.1`, `max_prompt_length=512`, `max_length=512`.
   - **`beta`**: temperature parameter controlling how strongly to penalize deviation from the reference policy.
6. **Save adapter** via `dpo_trainer.model.save_pretrained("TinyLlama-1.1B-dpo-qlora")`.
7. **Iterative merge**: merge SFT adapter into base, then merge DPO adapter into the SFT-merged model — two adapters stacked.

### ORPO — Odds Ratio Preference Optimization
- **[[ORPO|ORPO]]** (Hong, Lee & Thorne 2024, arXiv:2403.07691) — *"a process that combines SFT and DPO into a single training process. It removes the need to perform two separate training loops, further simplifying the training process while allowing for the use of QLoRA."*
- Forward-look: simplification of the two-pass SFT + DPO pipeline; usable with QLoRA.

## Key Quotes

> "There are three common steps that lead to creating a high-quality LLM: 1. Language modeling [pretraining] ... 2. Fine-tuning 1 (supervised fine-tuning) ... 3. Fine-tuning 2 (preference tuning)." — Ch 12, opening

> "SFT can also be used for other tasks, like classification, but is often used to go from a base generative model to an instruction (or chat) generative model." — Ch 12, defining the role of SFT

> "Adapters add a small number of weights in certain places in the network that can be fine-tuned efficiently while leaving the majority of model weights frozen." — Ch 12, PEFT framing

> "Like adapters, [LoRA's] subset allows for much quicker fine-tuning since we only need to update a small part of the base model. We create this subset of parameters by approximating large matrices that accompany the original LLM with smaller matrices." — Ch 12, LoRA explainer

> "Note that the quantization of LLMs in general is also helpful for inference as quantized LLMs are smaller in size and therefore require less VRAM." — Ch 12, on QLoRA's inference dividend

> "Loading the model now only uses ~1 GB VRAM compared to the ~4 GB of VRAM it would need without quantization. Note that during fine-tuning, more VRAM will be necessary so it does not cap out on the ~1 GB VRAM needed to load the model." — Ch 12, on the practical VRAM win

> "Higher values [num_train_epochs] tend to degrade performance so we generally like to keep this low." — Ch 12, training hyperparameter folklore

> "If you are using the free GPU provided by Google Colab, which is the Tesla T4 at the time of writing, then training might take up to an hour. A good time to take a break!" — Ch 12, on training cost

> "Unlike more specialized models, a generative model's ability to solve mathematical questions does not guarantee success in solving coding questions." — Ch 12, on why eval is hard

> "We want to emphasize the current lack of golden standards. No one metric is perfect for all use cases." — Ch 12, on LLM eval

> "When a measure becomes a target, it ceases to be a good measure." — Goodhart's Law, quoted in Ch 12 in the LLM-eval context

> "But most importantly, we believe that you are the best evaluator. Human evaluation remains the gold standard because it is up to you to decide whether the LLM works for your intended use case." — Ch 12, on evaluation discipline

> "Compared to PPO, the authors found DPO to be more stable during training and more accurate. Due to its stability, we will be using it as our primary model for preference tuning our previously instruction-tuned model." — Ch 12, on why DPO replaces PPO in the worked recipe

> "Since the release of DPO, new methods of aligning preferences have been developed. Of note is Odds Ratio Preference Optimization (ORPO), a process that combines SFT and DPO into a single training process. It removes the need to perform two separate training loops, further simplifying the training process while allowing for the use of QLoRA." — Ch 12, forward-looking note on ORPO

## Connections

### Books and series
- [[HandsOnLLM]] — the parent book.
- [[hands-on-llm-ch01-introduction-to-llms]] — Ch 1's *"Ch 12 forward reference for fine-tuning generative models with RLHF / DPO"* promise; Ch 12 is its fulfillment.
- [[hands-on-llm-ch11-fine-tuning-representation-models]] — sibling Part-III chapter for **representation models**; Ch 11 covered BERT-class encoder fine-tuning, Ch 12 covers decoder-class generative LLM fine-tuning.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — first chapter of Part III (embedding-model training); Ch 12 closes Part III and the book.
- [[hands-on-llm-ch07-advanced-text-generation]] — Ch 7's *"deep treatment of quantization deferred to Ch 12"* promise; Ch 12 delivers the QLoRA quantization recipe.

### Authors and publishers
- [[JayAlammar]] / [[MaartenGrootendorst]] — book co-authors.
- [[OReilly|O'Reilly Media]] — publisher (2024).

### Adjacent fine-tuning sources (cross-source convergence)
- [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] — [[ChipHuyen|Chip Huyen]]'s most thorough fine-tuning treatment; Ch 12 of Hands-On LLMs is the **runnable-code companion** to Huyen Ch 7's frameworks-and-trade-offs framing. Both books cover LoRA / QLoRA / PEFT / preference tuning / RLHF / DPO; Hands-On LLMs Ch 12 walks the actual `bitsandbytes` + `peft` + `trl` code path Huyen frames abstractly.
- [[leh-ch05-supervised-fine-tuning|LEH Ch 5]] — *LLM Engineer's Handbook*'s SFT chapter; Ch 12 is the simpler 1.1B-model worked recipe vs LEH Ch 5's 8B-LLaMA-3 production-pipeline recipe.
- [[leh-ch06-preference-alignment|LEH Ch 6]] — *LEH*'s DPO chapter; Ch 12 walks the same `DPOTrainer` recipe at smaller scale.

### Concepts (this chapter is a primary source for these)

**Pipeline-level**:
- [[SupervisedFinetuning]] / [[PreferenceFinetuning]] — the two-stage post-training pipeline.
- [[InstructionTuning]] — SFT specifically aimed at making a base model follow instructions.
- [[posttraining]] — umbrella for SFT + preference tuning.
- [[rlhf]] / [[DPO]] / [[ORPO]] / [[PPO]] — preference-alignment algorithms.

**PEFT and quantization**:
- [[PEFT]] / [[lora|LoRA]] / [[QLoRA]] / [[adapterlayers|Adapters]] — the parameter-efficient family.
- [[Quantization]] / [[NormalFloat4|NF4]] / [[DoubleQuantization]] / [[PagedOptimizer]] / [[BlockwiseQuantization]] — quantization machinery used by QLoRA.
- [[IntrinsicDimension]] — theoretical justification for low-rank methods.

**Reward modeling**:
- [[RewardModel]] / [[PreferenceData]] / [[ComparisonData]] — the reward-model training stack.

**Tooling**:
- [[trl]] / [[SFTTrainer]] / [[DPOTrainer]] / [[DPOConfig]] — Hugging Face TRL.
- [[bitsandbytes]] / [[BitsAndBytesConfig]] — quantization library.
- [[peft]] / [[LoraConfig]] / [[AutoPeftModelForCausalLM]] / [[PrepareModelForKBitTraining]] — Hugging Face PEFT.
- [[TrainingArguments]] / [[PagedAdamW32bit]] / [[CosineLRSchedule]] / [[Warmup]] / [[GradientCheckpointing]] / [[GradientAccumulation]] — training-loop tactics.

**Models and datasets**:
- [[TinyLlama]] / [[Llama]] — base model family used.
- [[UltraChat]] / [[DistilabelIntelOrcaDPOPairs]] — SFT and DPO datasets.
- [[ChatTemplate]] — UltraChat's `<|user|>...<|assistant|>` format.

**Evaluation**:
- [[Perplexity]] / [[ROUGE]] / [[bleu|BLEU]] / [[BERTScore]] — word-level metrics.
- [[MMLU]] / [[GSM8K]] / [[HellaSwag]] / [[TruthfulQA]] / [[HumanEval]] / [[GLUE]] — public benchmarks.
- [[OpenLLMLeaderboard]] — multi-benchmark aggregator.
- [[LLMAsAJudge]] / [[ChatbotArena]] / [[EloRating]] — judge and crowd-sourced eval.
- [[GoodhartsLaw]] — the evaluation-discipline parable.

### Entities
- [[HuggingFace]] / [[HuggingFaceTRL]] / [[HuggingFacePEFT]] — the stack used by the chapter.
- [[TimDettmers]] — QLoRA first author.
- [[GoogleColab]] — Tesla T4 baseline for the chapter's training cost claim.
- [[Argilla]] / [[Intel]] — Argilla published the orca-dpo-pairs dataset; Intel labeled it.

## Contradictions

**No hard contradictions with prior wiki content.** Ch 12 is the runnable-recipe layer over framings the wiki already had from [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] (Huyen's broader treatment) and [[leh-ch05-supervised-fine-tuning|LEH Ch 5]] / [[leh-ch06-preference-alignment|LEH Ch 6]] (Iusztin/Labonne/Vesa's production-pipeline treatment).

**Soft consistency notes**:
- The `lora_alpha=32 / r=64` ratio in Ch 12's worked recipe is **0.5×**, while the chapter's own rule of thumb says *"choose a value twice the size of r"* (which would be `alpha=128`). The chapter does not flag this discrepancy. [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] reports α:r ratios *"typically 1:8 to 8:1"* — 0.5× falls inside that range, so it is not wrong, just inconsistent with the inline rule.
- **Three reward-model initialization options** in [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]] (from-scratch / on top of pretrained / on top of SFT or strongest available; with SFT-based as best) — Ch 12 only describes the SFT-initialization path, *"we take a copy of the instruction-tuned model and slightly change it so that instead of generating text, it now outputs a single score."* No conflict, just narrower coverage.
- **RLHF as the original-ChatGPT recipe** (Ch 12 attributes ChatGPT-Nov-2022 to PPO) is consistent with [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]'s framing.

## Position in the wiki

**Completes the 12-chapter ingest of *Hands-On Large Language Models***. The book is now fully ingested:
- Part I (Chs 1–3): introduction, tokens / embeddings, transformer internals.
- Part II (Chs 4–9): text classification, clustering, prompt engineering, advanced text generation, semantic search / RAG, multimodal LLMs.
- Part III (Chs 10–12): creating text embedding models, fine-tuning representation models, fine-tuning generation models.

**Ch 12 specifically delivers**:
- The wiki's **first runnable QLoRA SFT recipe** with TinyLlama-1.1B / UltraChat / TRL `SFTTrainer`.
- The wiki's **first runnable DPO recipe** with `argilla/distilabel-intel-orca-dpo-pairs` / TRL `DPOTrainer` / iterative adapter merging.
- A consolidated treatment of the **reward-model + PPO baseline** that DPO is positioned against.
- The wiki's first explicit articulation of **NF4 + blockwise quantization + paged optimizers** as the three QLoRA innovations the chapter spells out (vs prior wiki coverage that named them but did not walk the diagrams).
- A consolidated generative-eval primer (perplexity / ROUGE / BLEU / BERTScore + MMLU / GSM8k / HellaSwag / TruthfulQA / HumanEval / Open LLM Leaderboard + LLM-as-judge + Chatbot Arena + Goodhart's Law).
- A forward-look at **[[ORPO]]** as the SFT + DPO collapse.

The chapter's pedagogy choice — fine-tune a 1.1B model **on a single Colab T4 in roughly an hour** — is the book's deliberate statement that **modern LLM fine-tuning is accessible to anyone with a free Colab account**, the operational corollary of the book's *"intuition-first, runnable-code"* thesis.
