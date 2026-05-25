---
title: "LLM Engineer's Handbook — Ch 5: Supervised Fine-Tuning"
type: source
tags: [book, llm-engineering, llm-engineers-handbook, fine-tuning, sft, lora, qlora, instruction-dataset, unsloth, trl, chat-template]
date: 2024-10-22
source_file: raw/books/llm-engineers-handbook/ch05-supervised-fine-tuning.md
---

## Summary
Chapter 5 of the *LLM Engineer's Handbook* (Iusztin, Labonne, Vesa — Packt 2024) is an end-to-end practitioner's guide to Supervised Fine-Tuning (SFT). It covers (1) building instruction datasets — quantity heuristics, curation, rule-based filtering, exact / fuzzy / semantic deduplication, decontamination, quality evaluation (LLM-as-a-judge, reward models, classifier filters), exploration, generation (Evol-Instruct, UltraFeedback) and augmentation — (2) the three SFT techniques (full fine-tuning, [[lora|LoRA]], [[QLoRA]]) with their memory math, (3) chat templates (Alpaca, ShareGPT, OpenAI, ChatML, Llama 3, Phi-3, Gemma) and training hyperparameters (LR schedule, batch size, packing, epochs, optimizers, weight decay, gradient checkpointing), and (4) a hands-on Llama-3.1-8B fine-tune on the authors' `mlabonne/llmtwin` dataset (3,335 pairs) using [[Unsloth]] + [[TRL]] SFTTrainer, producing the `mlabonne/TwinLlama-3.1-8B` model. The pipeline is concretely demonstrated: backtranslation + rephrasing of scraped articles via GPT-4o mini in JSON mode, regex-chunked into 1,000–2,000-character extracts, parallelized through `ThreadPoolExecutor(max_workers=4)` at < $0.50 total cost.

## Key Claims
- The hardest part of fine-tuning is dataset construction, not training; raw text rarely contains natural instruction/answer pairs, so you must transform it.
- Three dimensions define a high-quality instruction dataset: **accuracy**, **diversity**, **complexity**.
- Data-quantity heuristics: ~1,000 high-quality samples can suffice for a 70B model (LIMA), but 7B-class models need many more just to learn the chat template. General-purpose fine-tunes recommend ≥ 1M samples (Yi uses < 10K; Meta used ~10M for Llama 3 including preference alignment; OpenHermes/Dolphin use ~1M). Task-specific models need 100–100,000.
- Rule-based filtering uses length thresholds, keyword exclusion, and format checking; fast and transparent but binary and rule-brittle.
- **Exact deduplication** via MD5/SHA-256 hashing; **fuzzy deduplication** via MinHash signatures + Jaccard similarity; **semantic similarity** via Word2Vec/GloVe/FastText, BERT or sentence-transformer embeddings + cosine/Euclidean, with K-means/DBSCAN/hierarchical clustering for scale.
- Data decontamination: add the evaluation set into the deduplication pass and remove only the training-side duplicates; track provenance.
- LLM-as-a-judge biases: **position bias** (favors first answer), **length bias** (favors longer answers), **intra-model favoritism** (GPT-4o prefers GPT-4 family). Mitigations: randomize order, length-normalize, use a **jury of multiple LLMs**, aim for ~80% agreement with human evaluators.
- **Reward models** (e.g. RLHFlow/ArmoRM-Llama3-8B-v0.1) add regression + gating heads to a decoder-only base to output multi-dimensional quality scores (helpfulness, correctness, coherence, complexity, verbosity); compare on Allen Institute's RewardBench leaderboard.
- **Classifier quality filters** (e.g. HuggingFaceFW/fineweb-edu-classifier) add a classification head onto Snowflake/snowflake-arctic-embed-m and train it for 20 epochs on 450K samples annotated by Llama 3 70B Instruct.
- **Evol-Instruct** evolves instructions via in-depth methods (constraints, deepening, concretizing, more reasoning steps, complicating input) and in-breadth methods (new instructions in same domain); AutoEvol gives the canonical 4-step rewriter prompt.
- **UltraFeedback** evolves *answer quality* by sampling diverse responses and scoring them with GPT-4 across instruction-following / truthfulness / honesty / helpfulness.
- Standard instruction storage formats: **Alpaca**, **ShareGPT**, **OpenAI**, **OASST**, **raw text** (raw-text fine-tuning is "continual pre-training").
- Standard chat templates: **ChatML** (`<|im_start|>` / `<|im_end|>`), **Alpaca**, **Llama 3** (`<|begin_of_text|>`, `<|start_header_id|>`, `<|eot_id|>`), **Phi-3**, **Gemma** (`<start_of_turn>` / `<end_of_turn>`); whitespace/line-breaks matter for tokenization — use Jinja templates (Transformers).
- Full fine-tuning memory math (single GPU, fp32): **16 bytes/parameter baseline** = 4 (params) + 4 (gradients) + 8 (Adam optimizer states) = **~112 GB for 7B, ~1,120 GB for 70B**. Memory-reduction techniques: model parallelism, gradient accumulation, 8-bit Adam, activation checkpointing — drop to ~14–15 bytes/param in mixed precision.
- Full FT is destructive (catastrophic forgetting); SFT on new knowledge can increase hallucination frequency.
- **LoRA**: trainable low-rank matrices A, B s.t. $\Delta W = BA$, $W' = W + BA$; original $W$ frozen. Rank $r$ typically 8–256; alpha heuristic α = 2r; optional dropout 0–0.1. Target modules: Q, K, V, O attention projections + FFN/MLP blocks + linear output. For Llama 3 8B with rank 16 on every module, **42M trainable params (0.5196% of 8B)**. Lets a 7B model fine-tune in 14–18 GB VRAM. Multi-LoRA serving via LoRAX, [[HuggingFace]] TGI, NVIDIA NIM.
- **QLoRA** (Dettmers et al.): NF4 4-bit quantization of the base model + LoRA adapters + double quantization + paged optimizers (uses NVIDIA unified memory). Reduces peak GPU memory ~75% vs LoRA — e.g. 7B drops from 14 → 9.1 GB at init, 15.6 → 9.3 GB during fine-tune. Cost: ~30% slower than LoRA, with minor performance difference.
- **Learning rate** typical range 1e-6 to 1e-3 (start 1e-5 for transformers); use **linear or cosine scheduler** with **5% warmup** to peak (e.g. 3e-4) then decay (e.g. to 1e-7). Linear and cosine perform comparably.
- **Batch size** typically 1–32; **gradient accumulation** lets you achieve larger effective batch (effective = per-device × num GPUs × accumulation steps).
- **Maximum sequence length** 512–4,096 typical, up to 128K+ for long-context. Truncation (left/right) trims excess.
- **Packing** combines multiple short samples into one slot up to max-seq-length; requires attention masks to prevent cross-sample attention.
- **Number of epochs** typically 1–10; 2–5 most common; monitor validation loss for early stopping.
- **Optimizers**: AdamW recommended (especially **adamw_8bit**); AdaFactor for severe memory constraints; **paged AdamW 8-bit** offloads to CPU RAM; `adamw_torch` if memory and max performance both available.
- **Weight decay** 0.01–0.1 typical; 0.01 standard.
- **Gradient checkpointing** trades compute for memory by recomputing some activations on the backward pass.
- **Three monitored training metrics**: training loss, validation loss, gradient norm. Watch for: spikes / continual loss increase (failed run), validation loss rising while training falls (overfitting), large gradient norm (instability — apply gradient clipping).
- Three primary fine-tuning libraries recommended: **TRL** (Hugging Face — single & multi-GPU, FSDP & DeepSpeed, most up-to-date algorithms), **Axolotl** (Wing Lian — YAML configs, multi-format datasets, also TRL-based, FSDP/DeepSpeed), **Unsloth** (Daniel & Michael Han — custom kernels, 2–5× speedup, up to 80% less memory, single-GPU only at writing time, auto-converts to GGUF).
- Model-selection criteria for fine-tune target: **license**, **budget** (< 10B easier), **performance** (Open LLM Leaderboard + domain benchmarks).

## Key Quotes
> "Creating an instruction dataset is the most difficult part of the fine-tuning process."

> "For large models (around 70 billion parameters, for example), this number can be as low as 1,000 high-quality samples (see the LIMA paper)."

> "If you choose to re-train a model on raw text, this is a type of fine-tuning generally called 'continual pre-training.'"

> "A study showed that fine-tuning a model on new knowledge could result in more frequent hallucinations."

> "This gives us a baseline of 16 bytes per parameter. This translates into 112 GB of VRAM for a 7B model and 1,120 GB for a 70B model."

> "Even when targeting every module with a rank of 16, a Llama 3 8B model only has 42 million trainable LoRA parameters out of 8 billion parameters, which is 0.5196% of the model's parameters."

> "QLoRA provides significant memory savings compared to LoRA, reducing peak GPU memory usage by up to 75%. … However, this memory efficiency comes at the cost of increased training time, with QLoRA being about 30% slower than LoRA."

> "A common issue with chat templates is that every single whitespace and line break is extremely important. Adding or removing any character would result in a wrong tokenization."

## SFT Techniques Covered
- **Full fine-tuning** — every parameter trained; best accuracy ceiling but 16 bytes/param memory cost and risk of catastrophic forgetting; pre-training-style next-token loss.
- **[[lora|LoRA]]** — freeze $W_0$, train low-rank $\Delta W = BA$; hyperparams rank $r$, alpha ($\alpha = 2r$ heuristic), dropout (0–0.1), target modules (Q/K/V/O, MLP up/down/gate). Non-destructive, swappable adapters, 14–18 GB VRAM for a 7B fine-tune.
- **[[QLoRA]]** — NF4 quantization of the frozen base + LoRA on top + double-quantization + paged optimizers; ~75% less peak GPU memory than LoRA but ~30% slower.
- **Continual pre-training** — fine-tuning on raw text (no instruction pairs); same machinery, "raw text" data format.
- **Instruction dataset construction** — Alpaca / ShareGPT / OpenAI / OASST / raw text formats; chat templates (ChatML, Llama 3, Phi-3, Gemma, Alpaca) via Jinja.
- **Synthetic data generation** — Alpaca-style seed prompts, [[Outlines]]/JSON-mode structured generation; Evol-Instruct (in-depth + in-breadth), UltraFeedback (answer-quality evolution); backtranslation + rephrasing of raw text.
- **Quality filters** — rule-based (length, keyword, format), MinHash fuzzy dedup, semantic-similarity dedup, LLM-as-judge, reward models (ArmoRM), encoder-only classifier filters (fineweb-edu-classifier).
- **Libraries**: [[HuggingFace]] **TRL** (`SFTTrainer`), **Axolotl** (YAML configs), **Unsloth** (`FastLanguageModel`).

## Code & Concrete Examples

### Instruction-dataset pipeline (Chapter 3 → Chapter 5)
- `load_articles_from_json` → 76-row HF `Dataset` with fields `id, content, platform, author_id, author_full_name, link`.
- `clean_text` regex: `[^\w\s.,!?']` and `\s+` collapse.
- `extract_substrings`: regex sentence split, build 1,000–2,000-char chunks (`sentence_pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"`).
- `generate_instruction_answer_pairs`: OpenAI `gpt-4o-mini`, `response_format={"type": "json_object"}`, `max_tokens=1200`, `temperature=0.7`, prompt asks for **5 instruction-answer pairs per extract** in the author's writing style.
- `InstructionAnswerSet.from_json` parses the JSON response into `List[Tuple[str, str]]`.
- `ThreadPoolExecutor(max_workers=4)` (higher hits OpenAI rate limits).
- 90/10 train/test split via `dataset.train_test_split(test_size=0.1)`; pushed to `mlabonne/llmtwin` (3,335 pairs, < $0.50).
- Library pins: `openai==1.37.1`, `datasets==2.20.0`, `tqdm==4.66.4`.

### Fine-tuning code (Unsloth + TRL)
- Base: **`meta-llama/Meta-Llama-3.1-8B`** with `max_seq_length=2048`, `load_in_4bit=False` (LoRA, not QLoRA).
- LoRA config: `r=32`, `lora_alpha=32`, `lora_dropout=0`, `target_modules=["q_proj", "k_proj", "v_proj", "up_proj", "down_proj", "o_proj", "gate_proj"]`.
- Dataset mix: `mlabonne/llmtwin` (3K samples) concatenated with **`mlabonne/FineTome-Alpaca-100k`** `train[:10000]` (FineTome = arcee-ai/The-Tome filtered by fineweb-edu-classifier). 95/5 train/test split.
- Chat template: **Alpaca** (`### Instruction:` / `### Response:`) with manual `EOS_TOKEN` append.
- `SFTTrainer` args: `learning_rate=3e-4`, `lr_scheduler_type="linear"`, `per_device_train_batch_size=2`, `gradient_accumulation_steps=8` (effective batch 16), `num_train_epochs=3`, `warmup_steps=10`, `optim="adamw_8bit"`, `weight_decay=0.01`, `packing=True`, `report_to="comet_ml"`, fp16/bf16 auto-detected via `is_bfloat16_supported()`.
- Trained on A40 / A100 / L4 GPUs; **50 minutes on an A100**.
- Inference: `FastLanguageModel.for_inference(model)` + `TextStreamer`; sample prompt "Write a paragraph to introduce supervised fine-tuning."
- Export: `model.save_pretrained_merged("model", tokenizer, save_method="merged_16bit")` and `push_to_hub_merged("mlabonne/TwinLlama-3.1-8B", ...)`.
- Experiment tracking via **[[CometML|Comet ML]]** — monitors training loss, eval loss, gradient norm.

### Reference datasets & models cited
- **LIMA** (Zhou et al. 2023, arXiv 2305.11206) — < 1,000 high-quality samples.
- **Alpaca** (Tahori, Gulrajani, Zhang, Dubois et al. 2023, Stanford CRFM).
- **SlimOrca / OpenOrca** (Lian et al. 2023, Open-Orca/SlimOrca).
- **Orca** (Mukherjee et al. 2023, arXiv 2306.02707) — progressive learning from GPT-4 explanation traces.
- **AutoEvol / Evol-Instruct** (Zeng et al. 2024, arXiv 2406.00770).
- **Yi** (01.AI 2024, arXiv 2403.04652).
- **QLoRA** (Dettmers et al. 2023, arXiv 2305.14314).
- **LoRA** (Hu et al. 2021, arXiv 2106.09685).
- **ArmoRM-Llama3-8B-v0.1** (RLHFlow, arXiv 2406.12845).
- **fineweb-edu-classifier** (HuggingFaceFW).
- **RewardBench** (Allen Institute for AI, allenai/reward-bench).
- Tools: **Argilla** (manual annotation), **Nomic Atlas / BunkaTopics / Lilac** (topic-clustering visualization), HF text-clustering pipeline (sentence-transformers + UMAP + DBSCAN).

## Connections
- [[FineTuning]] — parent transfer-learning concept; SFT is the LLM specialization.
- [[LLMFineTuning]] — sibling concept.
- [[lora|LoRA]] — central PEFT method; chapter formalizes rank/alpha/target-module recipe.
- [[QLoRA]] — quantized LoRA variant; chapter explains NF4 + double quantization + paged optimizers and gives memory numbers.
- [[adapterlayers]] — broader PEFT family.
- [[PrefixTuning]] — alternative PEFT technique mentioned in parent literature.
- [[InstructionTuning]] — what SFT is in the LLM context.
- [[knowledgedistillation]] — related when smaller models learn from larger-LLM outputs (UltraFeedback, GPT-4 judges, fineweb-edu Llama 3 70B annotations).
- [[Hallucination]] — chapter cites the result that SFT on new knowledge increases hallucinations.
- [[continuallearning]] / catastrophic forgetting — risk of full fine-tuning.
- [[LLMAsAJudge]] — quality-evaluation strategy with documented biases.
- [[RewardFunction]] / [[rlhf]] — reward models reused for data quality scoring.
- [[CosineLRSchedule]] / [[Warmup]] — recommended LR schedule components.
- [[Adam]] / AdamW — recommended optimizer (8-bit variant for memory).
- [[GradientClipping]] — mitigation for large gradient norms.
- [[Dropout]] — optional LoRA regularizer.
- [[Word2Vec]] / [[GloVe]] / [[FastText]] / [[bert]] — semantic-similarity dedup embeddings.
- [[BERTScore]] / cosine-similarity — semantic similarity measure family.
- [[HuggingFace]] — datasets, hub, TRL, TGI, ArmoRM hosting, fineweb-edu-classifier.
- [[meta]] / [[Llama3_8BInstruct]] / Llama 3.1 8B — base model for the chapter's worked example.
- [[openai]] / GPT-4o-mini / GPT-4 — used for synthetic-data generation, LLM-as-judge, UltraFeedback critiques.
- [[CometML]] — experiment tracker for the training run.
- [[NVIDIA]] — A40 / A100 / L4 / A6000 GPUs referenced; NF4 / paged optimizers leverage CUDA unified memory; NIM serves multiple LoRA adapters.
- [[2407.10930-better-together]] / [[BootstrapFinetune]] — DSPy-side counterpart using rank 32 / alpha 64 LoRA on Q/K only.
- [[2507.03152-medval]] — QLoRA-in-DSPy precedent.
- [[BootstrapFinetune]] — BFT optimizer that wraps LoRA / QLoRA inside DSPy.
- New entities introduced: **Unsloth**, **TRL** (HF), **Axolotl**, **PaulIusztin**, **MaximeLabonne** (mlabonne), **AlexVesa**, **PacktPublishing**, **Argilla**, **NomicAtlas**, **WingLian**, **TimDettmers**, **HuggingFaceTGI**, **LoRAX**, **NvidiaNIM**, **ArmoRM**, **RewardBench**.
- New concepts introduced: **SupervisedFineTuning** (canonical SFT page), **InstructionDataset**, **ChatTemplate**, **ChatML**, **AlpacaFormat**, **ShareGPTFormat**, **GGUF**, **EvolInstruct**, **UltraFeedback**, **MinHashDeduplication**, **DataDecontamination**, **DataDeduplication**, **RuleBasedFiltering**, **SemanticSimilarityDedup**, **TopicClustering**, **Backtranslation**, **NF4Quantization**, **DoubleQuantization**, **PagedOptimizer**, **GradientAccumulation**, **GradientCheckpointing**, **Packing**, **AdamW**, **AdamW8bit**, **AdaFactor**, **CatastrophicForgetting**, **ContinualPretraining**, **FullFineTuning**, **ParameterEfficientFineTuning**, **MaxSequenceLength**, **EffectiveBatchSize**, **RewardModel**, **JuryOfLLMs**, **LIMA**, **Alpaca**, **Orca**, **SlimOrca**, **OpenHermes**, **Dolphin**, **FineTomeDataset**, **LLMTwinDataset**, **TwinLlama**, **FinewebEduClassifier**.

## Contradictions
- None observed within the chapter; consistent with [[lora|LoRA]] / [[QLoRA]] / [[FineTuning]] pages already in the wiki (the wiki's existing LoRA page cites Hu et al. and BetterTogether's rank 32 / alpha 64 / Q+K-only setting — the chapter recommends rank 32 / alpha 32 across Q/K/V/O+MLP, a different but compatible operating point; the wiki's QLoRA page covers the same NF4+double-quant+paged-optimizer recipe).
