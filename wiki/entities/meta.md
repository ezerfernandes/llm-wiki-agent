---
title: "Meta"
type: entity
tags: [organization, ai-lab]
sources: [2601.21343-self-improving-pretraining, 2603.19247-prompt-optimization-jailbreaking, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, ai-engineering-ch04-evaluate-ai-systems, ai-engineering-ch05-prompt-engineering, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch09-multimodal-llms]
last_updated: 2024-12-04
---

# Meta

Parent of FAIR (Fundamental AI Research). The Self-Improving Pretraining work originates from FAIR at Meta — uses an existing post-trained model as both rewriter and judge during RL pretraining to instill safety / factuality / quality earlier in the pipeline.

Also publishes the open-weights **LLaMA** family. [[LLaMA4Maverick|LLaMA-4 Maverick]] (a 17B-active / 128-expert MoE; `meta-llama/Llama-4-Maverick-17B-128E-Instruct`) is one of four target models in the [[2603.19247-prompt-optimization-jailbreaking|Algoverse adaptive red-teaming paper]] — baseline danger 0.215 rises to 0.623 under [[SIMBA]] and 0.581 under [[MIPROv2]].

## Connections
- [[fair|FAIR]]
- [[2601.21343-self-improving-pretraining]]
- [[reinforcementlearning|ReinforcementLearning]]
- [[LLaMA4Maverick]] — MoE open-weights model probed in adaptive red-teaming.
- [[Llama2_7BChat]] / [[Llama3_8BInstruct]] — earlier LLaMA generations.
- [[2603.19247-prompt-optimization-jailbreaking]] — adaptive red-teaming paper.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] cites Meta in *AI Engineering* Ch 1 as **one of the big-corporation foundation-model developers** alongside [[google|Google]], [[microsoft|Microsoft]], Baidu, and Tencent — the resource tier that can afford to develop FMs from scratch. Meta is also named as the developer of **[[PyTorch]]**, one of the canonical modeling/training frameworks named in the [[ModelingAndTraining|modeling-and-training]] section of the [[AIEngineeringStack|AI engineering stack]] discussion (alongside [[google|Google's]] [[TensorFlow]] and [[HuggingFace|Hugging Face's]] Transformers).

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 supplies the **Llama scale evolution** that anchors the chapter's training-token-budgeting discussion:

| Llama | Training tokens |
|---|---|
| Llama 1 | **1.4 trillion** |
| Llama 2 | **2 trillion** |
| Llama 3 | **15 trillion** |

Three additional Meta-specific Ch-2 data points:

1. **Switched from [[rlhf|RLHF]] (Llama 2) to [[DPO|DPO]] (Llama 3)** to reduce complexity. Llama 2 authors had argued *"the superior writing abilities of LLMs ... are fundamentally driven by RLHF"* (Touvron et al. 2023, quoted in Ch 2).
2. **Compute-suboptimal-by-choice.** Llama deliberately trained smaller-than-[[ChinchillaScalingLaw|Chinchilla]]-optimal models to favor inference economics — Sardana et al. (2023) formalized this as *inference-aware scaling*.
3. **Llama 2 / Llama 3 model dimensions** (Ch 2 Table 2-4). Llama 2-7B: 32 transformer blocks, 4096 hidden dim, 32 attention heads (128/head), 32K vocab, 4K context. Llama 3 family: 128K vocab, 128K context. Llama 3-405B has 126 transformer blocks.

Plus the *"Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning"* paper Ch 2 cites: a model with a 2% error rate may need an order of magnitude more data, compute, or energy than one with a 3% error rate. This is the [[LastMileChallenge|last-mile challenge]] expressed in scaling-law terms.

[[ThomasScialom]] (Llama 2 author) is cited for the **$3.50/comparison vs $25/written-response** cost data point — quantifying why [[ComparisonData|comparison data]] scales better than [[DemonstrationData|demonstration data]].

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 anchors **the LLM training-cost-anchor** to Meta's [[Llama|Llama 2]]:

> "Llama 2 has been trained on a dataset containing 2 trillion tokens. Imagine the compute necessary to create that model! ... To create the Llama 2 family of models, for example, Meta used A100-80 GB GPUs. Assuming renting such a GPU would cost $1.50/hr, the total costs of creating these models would exceed $5,000,000! ... The models were trained for 3,311,616 GPU hours." — Ch 1

This is the chapter's canonical citation for the **asymmetry between pretraining and inference compute**: training Llama 2 is out of reach of most teams; running quantized Llama 2 / Llama 3 inference on a consumer GPU is tractable. Ch 1 also names Meta's Llama models as one of four representative [[OpenSourceLLM|open-weights LLM]] families (alongside [[Cohere]] Command R, [[Mistral]], and [[microsoft|Microsoft's]] Phi).

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 surveys Meta's **[[Galactica]]** (Taylor et al. 2022) in its comparative tokenizer tour — the scientific-knowledge LLM with `[START_REF]` / `[END_REF]` citation tokens, the `<work>` chain-of-thought-reasoning token, and tokens for mathematics, amino acid sequences, and DNA sequences. Galactica's tokenizer also uses per-digit and whitespace-run tokens (matching [[StarCoder2]]) plus the unique single-token encoding for `\t\t` (two tabs).

Ch 2 also implicitly engages **Llama 2's BPE tokenizer** as the parent of the [[Phi3Mini|Phi-3]] tokenizer (Phi-3 reuses Llama 2's 32,000-vocab BPE plus chat-role tokens). See [[Llama]].

## From [[ai-engineering-ch04-evaluate-ai-systems|AI Engineering Ch 4]]

Ch 4 surfaces Meta in four specific roles:

1. **[[LlamaLicense|Llama Community Licenses]]** — Llama 2 and Llama 3 ship under custom community licenses with two material restrictions: (a) **700M MAU cap** triggers a special-license requirement; (b) **no output-based training** — Llama outputs cannot be used to train other models. Ch 4 contrasts this with [[Mistral]]'s license, which originally banned distillation but was later relaxed.
2. **[[LlamaGuard|Llama Guard]] paper** (Inan et al. 2023) — defines a [[Safety|safety]] taxonomy that Ch 4 names alongside [[OpenAIModeration|OpenAI's content moderation endpoint]] as the canonical harm-taxonomy reference.
3. **[[FacebookHateSpeech|Facebook hate-speech detection model]]** — Meta's specialized hate-speech classifier; one of three named cheap specialized safety classifiers (with [[PerspectiveAPI]] and [[SkolkovoToxicityClassifier]]).
4. **Political-leaning skew** — Feng et al. 2023 finding that Meta's Llama is *"more authoritarian"* than OpenAI's GPT-4 (which leans left/libertarian).

Ch 4 also positions Meta as the strongest argument that the **strongest open-source model will lag commercial models** structurally — *"It might be argued that Meta supports open source models only to keep their competitors (Google, Microsoft/OpenAI) in check."*

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

Meta appears in Ch 5 in **three roles**:

1. **[[Llama]] [[ChatTemplate|chat templates]]** — Ch 5's worked examples of chat-template format use the **Llama 2** (`<s>[INST] <<SYS>> ... <</SYS>> ... [/INST]`) and **Llama 3** (`<|begin_of_text|><|start_header_id|>system<|end_header_id|>` ...) templates. Meta changed the template between major versions; Ch 5 uses this as a case study for why third-party tools using stale templates cause silent quality regressions.
2. **Llama 3 prompt-position preference.** *"Some models, including Llama 3, seem to perform better when the task description is at the end of the prompt"* — the canonical contrast with GPT-4's beginning-bias.
3. **[[LAMABenchmark|LAMA]] (Language Model Analysis)** ([[PetroniEtAl2019|Petroni et al. 2019]]) — the 2019 [[FactualProbing|factual-probing]] benchmark introduced by Meta's AI lab. Founding work of the research area whose techniques later got repurposed as [[TrainingDataExtraction|training-data extraction]] attacks.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 is the wiki's most extensive coverage of **Meta's [[Llama|Llama 3]] data pipeline** — the chapter's single most-cited model:

### Headline claims (Dubey et al. 2024)

- **Llama 3's gains over Llama 2 are "primarily driven by improvements in data quality and diversity"** — not architecture.
- **Per-phase data mix** (the full [[DataMix]] table in Llama / DataMix pages).
- **Annealing on small amounts of high-quality code+math data** during pre-training boosts reasoning benchmarks.
- **Human annotations are more error-prone than AI-assisted annotation tools** for nuanced safety policies.
- **Multi-message chat format** designed by Llama 3 authors for tool-use data (message headers specifying source/destination; special termination tokens).
- **2.7M synthetic coding examples** generated via the [[CodeBackTranslation|code back-translation]] + code translation + scratch generation pipeline.

### Llama 3 paper as the chapter's case study

[[ChipHuyen|Huyen]] explicitly names the Llama 3 paper as "an excellent case study for instruction data synthesis." The chapter's three Llama-3-data-techniques (code translation, code back-translation, scratch synthesis with verifier loop) get a multi-page treatment that effectively serves as a worked example of Ch 8's full synthesis-and-verification pipeline.

### Scaling-law experiments for data mix

Meta's approach for choosing Llama 3's data mix (per Ch 8):

1. For each candidate data mix, train several **small models**.
2. Use those small-model results to **predict large-model performance** on that mix.
3. Pick the best-guess mix derived from the experiments.

This is one of the chapter's few concrete recommendations for **how to choose a data mix** rather than just describing existing mixes.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 surfaces Meta as the author of **OPT-2.7b** — the LLM backbone inside the [[BLIP2|BLIP-2]] checkpoint (`Salesforce/blip2-opt-2.7b`) Ch 9 loads for its [[ImageCaptioning|image-captioning]] and [[VisualQuestionAnswering|VQA]] worked examples. OPT-2.7b is what `model.language_model` returns when introspecting the BLIP-2 wrapper; its tokenizer is `GPT2TokenizerFast` (GPT-2-family [[BPE]] byte-level encoder) with 50,265-token vocabulary and `</s>` BOS/EOS/UNK. Meta's contribution here is the **open-weights generative LLM substrate** that adapter-style multimodal LLMs like BLIP-2 bridge a frozen [[VisionTransformer|ViT]] to — without Meta's OPT release, Salesforce Research could not have bridged BLIP-2 to a non-Meta open LLM with comparable ergonomics. The chapter also references [[ImageBind]] (Girdhar et al. 2023 — Meta) indirectly via prior wiki coverage as the six-modality successor to CLIP in the [[MultimodalEmbeddingSpace|multimodal-embedding-space]] lineage.
