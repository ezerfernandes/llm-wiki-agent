---
title: "AI Engineering Ch 7 — Finetuning"
type: source
tags: [book, finetuning, peft, lora, ai-engineering, oreilly, ai-engineering-book]
date: 2024-12-04
source_file: raw/papers/ai-engineering/ch07-finetuning.md
parent_source: ai-engineering-chip-huyen
---

# AI Engineering Ch 7 — Finetuning

## Summary

Chapter 7 of [[ChipHuyen|Chip Huyen]]'s *AI Engineering* ([[OReilly|O'Reilly Media]], December 2024) is the book's deep dive on **adapting foundation models by updating their weights**. Huyen positions finetuning as the *weight-update* branch of [[ModelAdaptation|model adaptation]] (vs. the prompt-based branch from Ch 5–6), with a strict "earn it" gate: finetune only after prompting and [[rag|RAG]] have been exhausted, because finetuning carries up-front data costs, ML talent costs, hosting costs, and a brittle commitment problem ("new base models may improve faster than you can enhance your finetuned model"). She crystalizes the most-quoted rule of the chapter: **"finetuning is for form, and RAG is for facts"** — RAG repairs *information-based* failures, finetuning repairs *behavior-based* failures (format, tone, structured output, domain-specific syntax).

The technical core of the chapter is **memory** — finetuning's #1 bottleneck. Huyen derives back-of-the-napkin formulas: inference needs roughly `N × M × 1.2` bytes (weights + 20% for activations and KV cache); training needs `weights + activations + gradients + optimizer states`, and with Adam (which stores two states per trainable parameter) a 7B model in FP16 needs ~56 GB just for weights+optimizer — already past most consumer GPUs. This motivates the cascade of memory-saving techniques the chapter then surveys: **[[Quantization|quantization]]** (FP32 → FP16 → BF16 → FP8 → INT8 → INT4 → 1.58-bit [[BitNetB158|BitNet b1.58]]), [[PEFT|parameter-efficient finetuning]] (cuts *trainable* parameters), [[GradientCheckpointing|gradient checkpointing]] (recompute activations instead of storing them), and [[CPUOffloading|CPU offloading]] via [[DeepSpeed]].

The **numerical-representations** section (FP32 / FP16 / BF16 / TF32 / FP8 / FP4 / INT8 / INT4 / NF4) is unusually thorough for an application-engineering book — Huyen notes that **[[BF16]] has more range bits but less precision than [[FP16]]** (1234.56789 → 1235.0 in FP16 vs 1232.0 in BF16), which is why Llama 2 (released in BF16) produced "much worse than advertised" quality for teams who loaded it in FP16 by mistake. She also distinguishes [[PostTrainingQuantization|PTQ]] from [[QuantizationAwareTraining|QAT]] and from training directly in lower precision ([[CharacterAI|Character.AI]] trained entirely in INT8).

The **PEFT** section opens with [[Houlsby2019AdapterModules|Houlsby et al. (2019)]] — inserting two adapter modules per transformer block on a frozen BERT achieves within-0.4% of full finetuning using 3% of the parameters — but adapters add inference latency. Huyen then divides PEFT into **adapter-based methods** ([[AdapterLayers|adapters]], [[lora|LoRA]], [[BitFit]], [[IA3]], [[LongLoRA]]) and **soft-prompt-based methods** ([[PrefixTuning|prefix tuning]], [[PTuning|P-Tuning]], [[PromptTuning|prompt tuning]]). The chapter analyzes 1,000+ issues on `huggingface/peft` and concludes LoRA dominates.

The **[[lora|LoRA]] deep-dive** is the longest single section of the chapter. Huyen explains: (1) the **low-rank factorization** math (W' = W + α/r · W_AB, with A: n×r and B: r×m); (2) the **[[IntrinsicDimension|intrinsic-dimension]] hypothesis** ([[ArmenAghajanyan|Aghajanyan]] et al. 2020) — pre-training implicitly compresses a model's intrinsic dimension, which is *why* PEFT works at all; (3) **LoRA configurations** — usually applied to attention's Wq, Wk, Wv, Wo; rank between 4–64; α:r ratios between 1:8 and 8:1; (4) **multi-LoRA serving** — keeping A, B separate enables 100 finetuned customer models to share one base; (5) **[[QLoRA|QLoRA]]** ([[TimDettmers|Dettmers]] et al., NeurIPS 2023) — NF4 quantization + paged optimizers let a 65B model finetune on a single 48 GB GPU, producing the [[Guanaco]] family.

The **[[ModelMerging|model-merging]]** section is the chapter's most experimental and most fun. Huyen frames merging as the *combination* counterpart to finetuning's *adaptation* — particularly attractive for multi-task finetuning (avoiding [[CatastrophicForgetting|catastrophic forgetting]]) and on-device deployment (one merged model instead of N task-specific models). She names three merging primitives: **[[Summing|summing]]** ([[LinearCombinationMerging|linear combination]], [[SLERP]]; uses [[TaskVector|task vectors]] = finetuned − base for [[TaskArithmetic|task arithmetic]]); **[[LayerStacking|layer stacking]]** ("frankenmerging" — [[Goliath120B|Goliath-120B]] took 72 of 80 layers from each of two Llama-2-70Bs; [[SparseUpcycling|sparse upcycling]] turns dense checkpoints into MoEs; [[DepthwiseScaling|depthwise scaling]] built [[SOLAR107B|SOLAR 10.7B]] from a 32-layer 7B); and **[[ConcatenationMerging|concatenation]]** (rarely worth it). She also covers **[[TIESMerging|TIES]]** and **[[DAREMerging|DARE]]** — both prune redundant task-vector parameters (keeping the top ~20% suffices) before merging. The section ends with [[FederatedLearning|federated learning]] framed as a model-merging use case.

The **finetuning-tactics** section gives practical advice on base-model choice ([[OpenAIProgressionPath|progression]] vs [[OpenAIDistillationPath|distillation]] paths), framework choice ([[LLaMAFactory|LLaMA-Factory]], [[Unsloth]], [[HuggingFacePEFT|HF PEFT]], [[Axolotl]], [[LitGPT]] for single-machine; [[DeepSpeed]] / [[PyTorchDistributed|PyTorch Distributed]] / [[ColossalAI]] for multi-machine), and **hyperparameters**: [[LearningRate|learning rate]] (1e-7 to 1e-3; start from pre-training LR × 0.1–1), [[BatchSize|batch size]] (≥8 to avoid instability; use [[GradientAccumulation|gradient accumulation]] when memory-bound), [[NumberOfEpochs|epochs]] (1–2 for millions of examples, 4–10 for thousands), and [[PromptLossWeight|prompt loss weight]] (default 10%, so the model learns mostly from responses, not prompts).

## Key Claims

- **"Finetuning is for form, and RAG is for facts."** [[rag|RAG]] repairs information-based failures (factually wrong / outdated outputs); finetuning repairs behavior-based failures (format, tone, structured outputs, domain-specific syntax like a less-popular SQL dialect). Both can be combined — but if a model has both kinds of failure, start with RAG.
- **General-purpose models can outperform domain-specific models.** [[BloombergGPT]] (50B params, $1.3M–$2.6M training compute, March 2023) was outperformed by GPT-4-0314 the same month: FiQA sentiment 87.15 (zero-shot) vs 75.07; ConvFinQA 76.48 vs 43.41. "Beware of the argument that general-purpose models don't work well for domain-specific tasks."
- **[[Ovadia2024FineTuningOrRetrieval|Ovadia et al. (2024)]] empirically established the RAG-vs-finetuning hierarchy on MMLU**: base model + RAG > finetuned model + RAG > finetuned model alone > base model alone, across Mistral-7B, Llama-2-7B, Orca-2-7B for current-events QA. "RAG on top of a finetuned model can boost its performance on MMLU 43% of the time" — meaning 57% of the time the finetune actively hurts.
- **Memory bottleneck math**: Adam optimizer stores 2 values per trainable parameter (gradient + momentum + variance = 3 values total at FP16 × 2 bytes = 6 bytes per trainable param). A 13B model fully-finetuned with Adam = 13B × 3 × 2 bytes = **78 GB just for gradients+optimizer states**. PEFT collapses this by reducing trainable parameters.
- **The intrinsic-dimension hypothesis explains PEFT.** [[Aghajanyan2020IntrinsicDimension|Aghajanyan et al. (2020)]]: "pre-training implicitly minimizes the model's intrinsic dimension. Surprisingly, larger models tend to have lower intrinsic dimensions after pre-training." This is the theoretical reason a 175B model's behavior can be meaningfully modified by ~4.7M LoRA parameters (0.0027% of full).
- **LoRA rank is surprisingly insensitive.** The [[lora|LoRA paper]] showed rank=2 across all four attention matrices outperformed rank=8 on one matrix, given the same 18M-parameter budget. [[Databricks]] (Sooriyarachchi 2023) and the LoRA authors both observed that "increasing r beyond a certain value may not yield any discernible increase in quality of model output." Some argue higher r causes overfitting. [[SebastianRaschka|Raschka]] (2023) saw r=256 win on his tasks — so the rule isn't universal.
- **Multi-LoRA serving is the under-discussed win.** For 100 customer models (each Llama-2-13B), option-1 (pre-merged) needs 100 × 26 GB = 2.6 TB; option-2 (shared W + per-customer A, B) needs 26 GB + 100 × 6.55 MB ≈ 26.66 GB. The 100× storage win is what makes per-tenant LoRA economical.
- **QLoRA's NF4 was designed for the empirical normal distribution of pretrained weights.** [[NormalFloat4|NF4]] (NormalFloat-4) quantizes around the insight that pre-trained weights are approximately N(0, σ²); combined with paged optimizers it lets a 65B model finetune on a single 48 GB GPU. [[Guanaco]] 65B was preferred to ChatGPT by GPT-4 judges (Elo 1022 vs 966) in May 2023, though it didn't beat GPT-4 itself (Elo 1348).
- **Model merging is one of the few finetuning-adjacent operations that doesn't need a GPU.** Linear-combination and SLERP merges of weights can run on CPU. Together with [[FederatedLearning|federated learning]], this is the path for "indie" model developers without compute access.
- **TIES and DARE prune up to 80% of task-vector parameters before merging with no degradation.** [[Yadav2023TIES|Yadav et al. (2023)]] showed keeping the top 20% of task-vector parameters matches keeping 100%. The more constituent models, the more important pruning becomes ("more opportunities for redundant parameters in one task to interfere with other tasks").
- **Training in lower precision is harder than inference in lower precision.** Backpropagation is more sensitive to rounding error (small changes compound across update steps; loss values need precise computation). The common pattern is **mixed precision**: keep a master FP32 copy of weights, run forward/backward in FP16/BF16/FP8, accumulate gradients in FP32 — managed via [[AutomaticMixedPrecision|AMP]].
- **The principal limitations of LoRA**: doesn't match full-finetuning quality on every task; harder to implement than full FT (needs model-architecture knowledge); but PEFT frameworks ([[HuggingFacePEFT|HF PEFT]], [[Axolotl]], [[Unsloth]], [[LitGPT]]) make this a non-issue for popular base models.
- **Prompt loss weight (default 10%) is the under-mentioned SFT hyperparameter.** During instruction finetuning, both prompts and responses contribute to the loss; setting prompt-loss-weight to 10% (the default) makes the model learn mostly from responses, which matches inference (where only the response is generated). 100% means equal weighting; 0% means response-only.

## Key Quotes

> "Finetuning is for form, and RAG is for facts. A RAG system gives your model external knowledge to construct more accurate and informative answers. A RAG system can help mitigate your model's hallucinations. Finetuning, on the other hand, helps your model understand and follow syntaxes and styles. While finetuning can potentially reduce hallucinations if done with enough high-quality data, it can also worsen hallucinations if the data quality is low." — Ch 7

> "Some might say that you're not doing AI until you've seen a 'RuntimeError: CUDA out of memory' error." — Ch 7, footnote on memory pressure

> "The principle that post-training should align the model to 'know what it knows' rather than add knowledge." — quoted from [[Llama31Paper|Llama 3.1 paper]] (Dubey et al. 2024)

> "Larger models tend to have lower intrinsic dimensions after pre-training. This suggests that pre-training acts as a compression framework for downstream tasks. In other words, the better trained an LLM is, the easier it is to finetune the model using a small number of trainable parameters and a small amount of data." — Ch 7, paraphrasing [[Aghajanyan2020IntrinsicDimension|Aghajanyan et al. (2020)]]

> "AI engineering experiments should start with prompting, following the best practices discussed in Chapter 6. Explore more advanced solutions only if prompting alone proves inadequate. Ensure you have thoroughly tested various prompts, as a model's performance can vary greatly with different prompts." — Ch 7

> "Beware of the argument that general-purpose models don't work well for domain-specific tasks, and, therefore, you must finetune or train models for your specific tasks. As general-purpose models become more capable, they also become better at domain-specific tasks and can outperform the domain-specific models." — Ch 7, on the BloombergGPT vs GPT-4 example

> "Imagine one model that can answer the first 60% of the questions and another model that can answer the last 60% of the questions. Combined, perhaps they can answer 80% of the questions." — Ch 7, on the value proposition of model merging

> "I've never met a single person who could explain to me, on the spot, the differences between [prefix-tuning, P-Tuning, prompt tuning]." — Ch 7, footnote

## Concepts

### New (minted by this chapter)

- [[PEFT]] — parameter-efficient finetuning (the umbrella term, with the canonical Houlsby 2019 reference)
- [[FullFinetuning]] — the all-weights baseline PEFT measures itself against
- [[PartialFinetuning]] — freeze first-N-layers, train last layer(s) — the inefficient predecessor of PEFT
- [[TrainableParameters]] — the memory-defining quantity in finetuning
- [[FrozenParameters]] — the unchanged-during-finetuning counterpart
- [[ModelMerging]] — combining multiple models' weights into one
- [[TaskVector]] — finetuned model minus base model; the operand of task arithmetic
- [[TaskArithmetic]] — adding/subtracting task vectors to compose / remove capabilities
- [[LinearCombinationMerging]] — weighted-average merging (incl. [[ModelSoup|model soups]])
- [[SLERP]] — Spherical Linear Interpolation for merging two task vectors
- [[TIESMerging]] — TrIm, Elect Sign, and Merge; prune redundant params before merging
- [[DAREMerging]] — Drop And REscale; sibling-pruning merge method
- [[LayerStacking]] — passthrough / "frankenmerging"; take layers from multiple models
- [[Frankenmerging]] — alternate name for layer stacking
- [[ConcatenationMerging]] — sum-of-ranks merge (rarely recommended)
- [[SparseUpcycling]] — turn a dense checkpoint into an MoE via layer copies + router
- [[DepthwiseScaling]] — layer-stacking technique to grow a model (SOLAR 10.7B)
- [[ModelUpscaling]] — broader category: create a bigger model from a smaller one without training from scratch
- [[CatastrophicForgetting]] — neural-net failure mode in sequential multi-task finetuning
- [[FederatedLearning]] — multi-device training + merging without centralizing data
- [[ContinuedPretraining]] — self-supervised finetuning on cheap task-related data, before SFT
- [[InfillingFinetuning]] — finetune an autoregressive model to fill blanks
- [[LongContextFinetuning]] — modify positional embeddings to extend max context
- [[BiasMitigationFinetuning]] — counteract pre-training biases by curated finetuning data
- [[InformationBasedFailure]] — model failure due to missing/outdated facts (use RAG)
- [[BehaviorBasedFailure]] — model failure due to wrong format/style (use finetuning)
- [[AlignmentTax]] — performance loss on tasks A,B from finetuning on task C
- [[MemoryBottleneck]] — finetuning's #1 cost driver
- [[InferenceMemoryFormula]] — `N × M × 1.2`
- [[TrainingMemoryFormula]] — `weights + activations + gradients + optimizer states`
- [[OptimizerState]] — Adam: 2 values/param; momentum SGD: 1; vanilla SGD: 0
- [[ActivationMemory]] — can dwarf weight memory at scale; addressed by gradient checkpointing
- [[GradientCheckpointing]] — recompute activations instead of caching
- [[ActivationRecomputation]] — alternate name for gradient checkpointing
- [[CPUOffloading]] — move excess tensors from GPU to CPU during training ([[DeepSpeed]])
- [[NumericalRepresentation]] — the bit-allocation between sign / range / precision
- [[FP32]] / [[FP64]] / [[FP16]] / [[BF16]] / [[TF32]] / [[FP8]] / [[FP4]] / [[INT8]] / [[INT4]] — specific numerical formats
- [[NormalFloat4]] — NF4, QLoRA's 4-bit format designed for pretrained-weight distributions
- [[BitNetB158]] — 1.58-bit transformer (Microsoft, 2024)
- [[BinaryConnect]] / [[XnorNet]] / [[BitNet]] — earlier 1-bit-LLM lineage
- [[PostTrainingQuantization]] — PTQ (the common case)
- [[QuantizationAwareTraining]] — QAT (simulate low precision during training)
- [[MixedPrecisionTraining]] — keep some ops in higher precision
- [[AutomaticMixedPrecision]] — AMP (auto-select precision per op)
- [[Minifloat]] — float formats with <8 bits
- [[GradientAccumulation]] — accumulate gradients across batches before updating
- [[PromptLossWeight]] — fraction of loss attributed to prompt tokens vs response tokens
- [[NumberOfEpochs]] — passes through training data; 1–2 for millions, 4–10 for thousands
- [[BatchSize]] — examples per gradient update; ≥8 to avoid instability
- [[LowRankFactorization]] — the math underneath LoRA: decompose W ≈ A·B with rank ≪ min(d,k)
- [[IntrinsicDimension]] — the minimal-parameter manifold pretrained models live on
- [[HardPrompt]] — discrete-token human-readable prompt (standard prompting)
- [[SoftPrompt]] — continuous-vector learned prompt (PEFT)
- [[PromptTuning]] — Lester et al. 2021; soft prompt at embedded input only
- [[PTuning]] — Liu et al. 2021; soft prompt at input layer
- [[IA3]] — Liu et al. 2022; per-activation scaling vectors; strong for multi-task
- [[BitFit]] — Zaken et al. 2021; finetune only bias parameters
- [[LongLoRA]] — Chen et al. 2023; LoRA variant for context extension
- [[ReLoRA]] — Lialin et al. 2023; low-rank pretraining
- [[GaLore]] — Zhao et al. 2024; low-rank pretraining at 7B scale
- [[MultiLoraServing]] — serving N customer LoRAs sharing one base model
- [[AdapterHub]] — community registry of finetuned adapters
- [[OpenAIProgressionPath]] — base-model selection: cheap → middling → best
- [[OpenAIDistillationPath]] — best teacher → small dataset → cheaper student
- [[ModelEnsemble]] — combine outputs (vs. merging which combines weights)
- [[MixtureOfAgents]] — TogetherAI 2024; six weak open-source models combined to GPT-4o-level

### Updated (already existed, now augmented)

- [[FineTuning]] — anchor for the chapter's full-finetuning vs PEFT contrast
- [[lora|LoRA]] — deep-dive section in this chapter
- [[QLoRA]] — Dettmers et al. (NeurIPS 2023), introduced in this chapter
- [[Quantization]] — Ch 7 is the book's most thorough quantization treatment
- [[knowledgedistillation|Knowledge Distillation]] — Huyen's "distill the larger model's knowledge into the smaller model" framing, used in the OpenAI distillation path
- [[PrefixTuning]] — Li & Liang 2021; one of the three soft-prompt PEFT siblings
- [[adapterlayers|Adapter Layers]] — Houlsby et al. 2019 — the original PEFT paper
- [[SupervisedFinetuning]] — SFT framing carries forward from Ch 2
- [[PreferenceFinetuning]] — preference data framing carries forward from Ch 2
- [[TransferLearning]] — Ch 7 opens with the InstructGPT framing: finetuning as "unlocking the capabilities a model already has but that are difficult for users to access via prompting alone"
- [[ModelAdaptation]] — Ch 7 is the weight-update half of the model-adaptation dichotomy
- [[Backpropagation]] — Ch 7 reviews the forward/backward decomposition for the memory math
- [[forwardpass|Forward Pass]] / [[Gradient]] / [[Adam]] / [[GradientDescent]] / [[Momentum]] — referenced in the optimizer-state discussion
- [[FloatingPoint]] / [[FloatingPointPrecision]] — Ch 7 covers the IEEE-754 family + AI-specific formats (BF16, TF32, FP8, FP4)
- [[MixtureOfExperts]] — sparse upcycling produces MoEs from dense checkpoints
- [[LearningRate]] / [[LearningRateScheduler]] / [[HyperparameterTuning]] — the hyperparameter tactics section
- [[ZeRO]] — DeepSpeed framing for CPU offloading
- [[StructuredOutputs]] — Ch 7 names structured outputs as a canonical finetuning use case (vs. Ch 2's prompt-based treatment)
- [[Hallucination]] — finetuning can both reduce and worsen hallucination depending on data quality
- [[rag|RAG]] — the "form vs facts" framing positions RAG against finetuning

## Entities

### New

- [[BloombergGPT]] — Bloomberg's $1.3–2.6M 50B-param finance model (2023); the chapter's domain-finetuning cautionary tale
- [[TimDettmers]] — author of LLM.int8(), QLoRA, NF4 quantization
- [[ArmenAghajanyan]] — intrinsic-dimension theory of pretrained models
- [[EdwardHu]] — first author on the LoRA paper
- [[NeilHoulsby]] — first author on the canonical adapter-PEFT paper (2019)
- [[SebastianRaschka]] — practitioner-author cited on LoRA hyperparameters (r=256 win)
- [[LLaMAFactory]] — finetuning framework
- [[LitGPT]] — finetuning framework (Lightning AI)
- [[ColossalAI]] — distributed training framework
- [[Goliath120B]] — early frankenmerge from two Llama-2-70Bs
- [[SOLAR107B]] — depthwise-scaled 10.7B model from a 7B
- [[Guanaco]] — Llama-7B-to-65B family produced by QLoRA
- [[Vicuna]] — referenced as a QLoRA benchmark comparator
- [[Orca2]] — referenced in the Ovadia RAG-vs-FT study
- [[CodeLlama]] — long-context finetuning case study (Llama 2 → 16,384 tokens)
- [[InstructGPT]] — the canonical "finetuning unlocks existing capabilities" framing
- [[CharacterAI]] — trained entirely in INT8
- [[XnorAI]] — Xnor-Net spinoff, acquired by [[Apple]] for $200M
- [[AdapterHub]] — community adapter registry

### Updated (already existed)

- [[ChipHuyen]] — Ch 7 author voice
- [[NVIDIA]] — TF32, Blackwell 4-bit, mixed-precision-training tooling
- [[Apple]] — on-device LoRA + quantization (3.5 bits-per-weight), Xnor.ai acquisition
- [[HuggingFace]] — `huggingface/peft`, transformers PTQ, AdapterHub neighbor
- [[meta|Meta]] — Llama 2/3/3.1 / Code Llama as base models
- [[google|Google]] — BFloat16 design, TPU optimization
- [[microsoft|Microsoft]] — BitNet b1.58, DeepSpeed
- [[DeepSpeed]] — CPU offloading
- [[Databricks]] — empirical LoRA-rank insensitivity finding
- [[Grammarly]] — Flan-T5 finetune beating GPT-3 at 1/60 the size
- [[openai|OpenAI]] — InstructGPT framing, progression/distillation finetuning paths
- [[TogetherAI]] — Mixture-of-Agents (six open models merged to GPT-4o-level)
- [[PyTorch]] — built-in PTQ, AMP support
- [[TensorFlow]] — PTQ, TensorFlow Lite (on-device quantized inference)
- [[Unsloth]] / [[Axolotl]] — PEFT frameworks
- [[Bitsandbytes]] — the library implementing NF4 / 4-bit / 8-bit quantization

## Connections

- **Ch 1 → Ch 7**: [[ModelAdaptation]] dichotomy (prompt-based vs finetuning) — Ch 7 is the deep dive on the second branch.
- **Ch 2 → Ch 7**: [[SupervisedFinetuning|SFT]] / [[PreferenceFinetuning]] / feature-based transfer — Ch 7 expands these into a memory + PEFT theory.
- **Ch 5 → Ch 7**: prompting precedes finetuning; finetuning is "earned" only after prompts are exhausted.
- **Ch 6 → Ch 7**: [[rag|RAG]] vs finetuning decision tree — the "form vs facts" rule.
- **Ch 8 (next chapter) ← Ch 7**: dataset engineering — the chapter ends pointing forward to data curation, which is "the hardest part of finetuning."
- **Ch 9 (forthcoming) ← Ch 7**: inference optimization — quantization, PTQ, KV-cache compression, prompt caching all get fuller treatment.
- **External**: [[Aghajanyan2020IntrinsicDimension]] / [[Houlsby2019AdapterModules]] / [[Hu2021LoRA]] / [[Dettmers2023QLoRA]] / [[Ovadia2024FineTuningOrRetrieval]] / [[Yadav2023TIES]] / [[Wortsman2022ModelSoups]] / [[Kim2023SOLAR]] / [[Komatsuzaki2022SparseUpcycling]] / [[Ilharco2022TaskArithmetic]].

## Contradictions

- **LoRA-rank sweet spot is contested.** The LoRA paper, [[Databricks]] (Sooriyarachchi 2023), and most practitioners report r=4–64 is sufficient and higher r doesn't help; [[SebastianRaschka|Raschka]] (2023) reports r=256 won on his tasks. Both are cited inside the same section without resolution — the chapter's stance is "experimentation is needed."
- **"Finetuning vs RAG" hierarchy from [[Ovadia2024FineTuningOrRetrieval|Ovadia et al. (2024)]] partially conflicts with practitioner reports** in other parts of the wiki where domain finetuning meaningfully improves over RAG (e.g., [[2507.03152-medval|MedVAL]] clinical validators). The reconciliation: Ovadia's benchmark is current-events QA (information-heavy); MedVAL is style-and-rubric scoring (behavior-heavy). Consistent with the chapter's "form vs facts" rule.
- **Domain-specific models vs general-purpose models.** Ch 7 uses [[BloombergGPT]] (lost to GPT-4-0314) as evidence that domain-specific pretraining isn't worth it. This contradicts the "specialization wins" framing in some papers and tutorials (and partially in [[2605.12966-agentic-ai-to-agi]] §3.2). The synthesis: at scale, general-purpose models with strong post-training tend to win; specialization is most valuable as a *finetune on top of* a strong general-purpose base, not as a from-scratch pre-train.
- **"Finetuning is for form" vs. the bias-mitigation use case.** Huyen names bias mitigation (e.g., finetuning on female-CEO data to mitigate gender bias) as a finetuning use case — but bias mitigation involves changing the model's *content distribution*, not its *form*. The rule "finetuning is for form, RAG is for facts" is therefore approximate, not absolute.

## Notable Omissions

- **No coverage of [[DPO]] / [[RLHF]] / [[RLAIF]]** — those are deferred to Ch 2 (already done) and the post-training literature; Ch 7 focuses on SFT-style finetuning + PEFT.
- **No detailed RLVR/GRPO treatment** — preference finetuning at the technique level is only touched on; the [[grpo]] / [[rlvr]] family is not discussed.
- **No detailed coverage of [[FlashAttention]] or [[PagedAttention]]** — both are mentioned only obliquely as "memory-saving" techniques.
- **No explicit coverage of LoRA's interaction with quantized KV-cache** — though both topics are introduced, the combination is left for Ch 9.
- **Light treatment of multi-machine / distributed finetuning** — only a sentence pointing at [[DeepSpeed]] / [[PyTorchDistributed]] / [[ColossalAI]].
