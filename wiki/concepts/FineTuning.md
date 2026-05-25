---
title: "Fine-Tuning"
type: concept
tags: [training, llm, transfer-learning, computer-vision]
sources: [d2l-computer-vision, d2l-nlp-applications, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, ai-engineering-ch07-finetuning, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# Fine-Tuning

Continuing training of a pretrained model on a smaller, task-specific dataset to specialize its behavior. The canonical [[TransferLearning|transfer-learning]] technique — central to applied computer vision (ImageNet → downstream task) and to NLP / LLMs ([[BERT]] / [[GPT]] → task-specific head). Per [[d2l-computer-vision]] §`fine-tuning`: "When target datasets are much smaller than source datasets, fine-tuning helps to improve models' generalization ability."

## Four-step recipe (per [[d2l-computer-vision]])

1. **Pretrain** a neural network ("source model") on a large source dataset (e.g. [[ResNet|ResNet-18]] on [[ImageNet]]).
2. **Copy** all weights from the source model into a target model **except the output layer**. (The output layer's labels are task-specific; the feature-extracting layers learned generic image features that transfer.)
3. **Replace** the output layer with a randomly-initialized head sized to the target task's class count.
4. **Train end-to-end** on the target dataset with:
   - **Smaller LR on copied layers** (preserve learned features).
   - **Larger LR (typically $10\times$) on the new head** (learn from scratch faster).

## D2L's hot-dog example

ResNet-18 pretrained on ImageNet (1000 classes), fine-tuned to a 2-class hot-dog binary classifier on a 2000-image dataset. Backbone LR = $5\times10^{-5}$, head LR = $5\times10^{-4}$. PyTorch parameter-group syntax:

```python
params_1x = [p for n, p in net.named_parameters() if n not in ["fc.weight", "fc.bias"]]
trainer = torch.optim.SGD([
    {'params': params_1x},
    {'params': net.fc.parameters(), 'lr': learning_rate * 10},
], lr=learning_rate, weight_decay=0.001)
```

After 5 epochs, fine-tuned model substantially outperforms a from-scratch ResNet-18 with the same hyperparameters — "its initial parameter values are more effective."

## Variants

- **Full fine-tuning** — update all parameters (D2L's default).
- **Linear probe / feature extraction** — freeze the backbone, train only the head. Faster, more parameter-efficient, but lower ceiling.
- **Parameter-efficient fine-tuning (PEFT):** [[LoRA]] / [[AdapterLayers|adapter layers]] / prefix tuning — add a small number of trainable parameters while keeping the backbone frozen. The de facto standard for LLM fine-tuning.
- **Layer-wise LR decay** — generalization of D2L's "small LR for backbone, big LR for head" to a smooth gradient where lower layers get smaller LR than upper layers. Common in [[BERT]] / [[ViT]] fine-tuning.

## Why it works

The pretrained model has learned generic features (edges, textures, shapes, parts) that are useful across visual tasks. Fine-tuning preserves these and adapts the output layer + slightly perturbs the backbone for the target task. The smaller LR on the backbone is the canonical regularization preventing catastrophic forgetting of useful pretrained features.

## Connections

- [[TransferLearning]] / [[Pretraining]] / [[CNN]] / [[ResNet]] / [[ImageNet]] / [[BERT]] / [[GPT]] / [[LoRA]] / [[AdapterLayers]] / [[LLMFineTuning]].
- [[FCN]] / [[StyleTransfer]] / [[MaskRCNN]] / [[FasterRCNN]] / [[SSD]] — all of these models *begin* with a fine-tuning step from a pretrained classification backbone.
- [[d2l-computer-vision]] §`fine-tuning` — D2L's canonical worked CV example.
- [[d2l-nlp-applications]] §`finetuning-bert` / §`natural-language-inference-bert` — D2L's canonical worked NLP example, formalized as [[FineTuningBert]]: the *pretrained Transformer encoder + task head* template that's the NLP analogue of the CV recipe above.

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] frames finetuning in the [[AIEngineering|AI engineering]] context as **one of two [[ModelAdaptation|model adaptation]] families** — the *weight-update* family. From Ch 1:

> *"Finetuning, on the other hand, requires updating model weights. You adapt a model by making changes to the model itself. In general, finetuning techniques are more complicated and require more data, but they can improve your model's quality, latency, and cost significantly. Many things aren't possible without changing model weights, such as adapting the model to a new task it wasn't exposed to during training."*

Ch 1 also disambiguates:

- **Finetuning ≠ [[posttraining|post-training]] technically.** Conceptually they're the same operation (continue training a previously-trained model), but practitioners use the words to signal **who is doing it**: post-training is done by model developers ([[openai|OpenAI]], [[anthropic|Anthropic]]); finetuning is done by application developers.
- **Finetuning ≠ [[PromptEngineering|prompt engineering]].** Huyen calls out a Business Insider article in which an author claims she "finetuned ChatGPT" by feeding her journal entries into the prompt — that's prompt engineering. Many people use "finetuning" colloquially when they mean prompt engineering.

When to choose finetuning over prompt-based adaptation, per Ch 1:
- Complex tasks where prompt engineering hits a ceiling.
- Strict performance requirements (quality, latency, cost).
- Tasks not seen during pretraining.
- When cheaper inference matters and a smaller finetuned model can replace a larger base model.

Chapter 7 of the book is the deep dive on finetuning techniques including PEFT and [[lora|LoRA]].

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 surfaces finetuning in **three specific roles**:

1. **As [[SupervisedFinetuning|SFT]] inside the post-training pipeline** — the demonstration-data-driven step that turns a pre-trained completion machine into a conversation model. See [[posttraining]], [[SupervisedFinetuning]], [[BehaviorCloning]].
2. **As [[PreferenceFinetuning|preference finetuning]]** — the [[rlhf|RLHF]] / [[DPO]] / [[RLAIF]] stage that aligns the SFT model with human preferences. See [[PreferenceFinetuning]].
3. **As the most-effective layer in the [[StructuredOutputs|structured-outputs]] stack** — when prompting, post-processing, test-time compute, and constrained sampling aren't sufficient, finetuning on examples of the target format produces the most reliable results.

Ch 2 also names **feature-based transfer**: append a task-specific head (e.g., a classifier head with N classes) to a base foundation model before finetuning — guaranteeing the output format by construction. Used for classification tasks; discussed more under transfer learning in Ch 7 of the book.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 frames fine-tuning as the **second half of the LLM two-step training paradigm**:

> "The second step, fine-tuning or sometimes post-training, involves using the previously trained model and further training it on a narrower task. This allows the LLM to adapt to specific tasks or to exhibit desired behavior. For example, we could fine-tune a base model to perform well on a classification task or to follow instructions. It saves massive amounts of resources because the pretraining phase is quite costly and generally requires data and computing resources that are out of the reach of most people and organizations." — Ch 1

The two flavors Ch 1 distinguishes:

1. **Task fine-tuning** — adapt the model to a downstream task (classification, NER, etc.). Most relevant for [[RepresentationModel|representation models]] like [[bert|BERT]].
2. **Instruction / chat fine-tuning** — turn a completion-style base model into an [[InstructModel|instruct model]] that follows directions. *"By fine-tuning these models, we can create instruct or chat models that can follow directions."* Most relevant for [[GenerativeModel|generative models]] like [[GPT]] family / [[Llama]] / [[Phi3Mini|Phi-3]].

The chapter forward-references **Ch 11** for fine-tuning representation models and **Ch 12** for fine-tuning generative models, including additional alignment steps beyond instruction tuning ([[rlhf|RLHF]] / [[DirectPreferenceOptimization|DPO]]).

## From [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]]

Ch 7 is the book's most thorough treatment of finetuning. [[ChipHuyen|Huyen]]'s thesis: **finetuning is the weight-update branch of [[ModelAdaptation|model adaptation]], earned only after prompting and [[rag|RAG]] are exhausted**, because the up-front data + ML-talent + hosting + base-model-churn cost is high. The chapter's most quoted rule: **"finetuning is for form, and RAG is for facts"** — RAG fixes [[InformationBasedFailure|information-based failures]] (factually wrong/outdated outputs), finetuning fixes [[BehaviorBasedFailure|behavior-based failures]] (format, style, domain-specific syntax).

### Reasons to finetune (Ch 7)

- Improve task-specific quality (e.g., less-common SQL dialect, customer-specific queries).
- Structured outputs (JSON, YAML, domain-specific languages).
- [[BiasMitigationFinetuning|Bias mitigation]] — Wang & Russakovsky (2023); Garimella et al. (2022) — finetuning BERT on female-authored / African-authored text reduced gender / racial biases.
- Make a small model competitive with a large model on a narrow task. [[Grammarly]] finetuned [[FlanT5|Flan-T5]] (82,000 (instruction, output) pairs) and beat a GPT-3 variant on text editing at **1/60 the size**.
- Token-usage optimization (pre-prompt-caching era) — finetuned models can use shorter prompts.

### Reasons not to finetune (Ch 7)

- **Cross-task degradation** — finetuning on task A often hurts tasks B, C ("[[AlignmentTax|alignment tax]]" — Bai et al. 2020). Mitigation: finetune on all queries you care about, or use [[ModelMerging|model merging]].
- **High up-front investment**: data acquisition, training expertise, serving infrastructure, monitoring + budget for upkeep as base models improve.
- **Base-model churn risk**: a new base model may outperform your finetuned model on your task before you can iterate.
- **Most "we need to finetune" turns out to be unsystematic prompting.** Huyen notes that many practitioner complaints about prompting are resolved by *better* prompt experiments rather than finetuning.

### Sub-types of finetuning enumerated (Ch 7)

- **[[FullFinetuning|Full finetuning]]** — update all parameters. Indistinguishable from training except for the starting weights.
- **[[PartialFinetuning|Partial finetuning]]** — freeze first N layers, train last layer(s). Memory-cheaper but parameter-inefficient (Houlsby et al. 2019 — needed 25% of BERT-large params to match full FT on GLUE).
- **[[PEFT|Parameter-efficient finetuning]]** — adapter-based ([[lora|LoRA]], [[BitFit]], [[IA3]], [[LongLoRA]]) or soft-prompt-based ([[PrefixTuning]], [[PTuning]], [[PromptTuning]]). The dominant paradigm.
- **[[ContinuedPretraining|Continued pre-training]]** — self-supervised finetuning on cheap task-related raw text before SFT.
- **[[SupervisedFinetuning|SFT]]** — (instruction, response) pairs.
- **[[PreferenceFinetuning|Preference finetuning]]** — (instruction, winning response, losing response) triples.
- **[[InfillingFinetuning|Infilling finetuning]]** — train an autoregressive model to fill blanks; useful for code debug + text editing.
- **[[LongContextFinetuning|Long-context finetuning]]** — modify positional embeddings to handle longer sequences (Code Llama's 4096 → 16384).

### The decision tree (Ch 7, paraphrased)

1. Start with prompting; version your prompts.
2. Add 1–50 in-context examples.
3. If failures are information-based — add [[rag|RAG]] (start with [[BM25]], not vectors).
4. If failures remain behavior-based after RAG — finetune.
5. Combine RAG + finetuning for the last 5–10%.

[[ChipHuyen|Huyen]]'s strict ordering aligns with [[openai|OpenAI]]'s 2023 example workflow but is more opinionated about the prompt-first gate.

## Connections (Ch 7 additions)

- [[MemoryBottleneck]] — Ch 7's core technical framing.
- [[InferenceMemoryFormula]] / [[TrainingMemoryFormula]] — the back-of-the-napkin math.
- [[TrainableParameters]] / [[FrozenParameters]] / [[OptimizerState]] — the memory contributors.
- [[ModelMerging]] / [[CatastrophicForgetting]] / [[TaskVector]] — the multi-task alternative to sequential finetuning.
- [[ContinuedPretraining]] / [[InfillingFinetuning]] / [[LongContextFinetuning]] / [[BiasMitigationFinetuning]] — finetuning subtypes named in Ch 7.
- [[InformationBasedFailure]] / [[BehaviorBasedFailure]] — the failure-mode taxonomy that drives the FT-vs-RAG decision.
- [[OpenAIProgressionPath]] / [[OpenAIDistillationPath]] — base-model selection paths.
- [[GradientAccumulation]] / [[CPUOffloading]] / [[GradientCheckpointing]] — memory-saving training tactics.
- [[PromptLossWeight]] / [[BatchSize]] / [[NumberOfEpochs]] / [[LearningRate]] — the hyperparameter tactics surface.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 is the wiki's **runnable-code recipe** for fine-tuning [[bert|BERT]]-class **representation models** for classification — the task-fine-tuning branch of Ch 1's two-flavors taxonomy. Walks **four regimes** on the same `bert-base-cased` backbone:

1. **Full supervised fine-tuning** via [[HuggingFace|Hugging Face]] [[Trainer|`Trainer`]] + [[TrainingArguments]] (`lr=2e-5`, `batch_size=16`, `weight_decay=0.01`, 1 epoch) + [[DataCollatorWithPadding]] + [[F1Score|F1]] via `compute_metrics` → F1 = **0.85** on [[RottenTomatoes|rotten_tomatoes]] (beats [[hands-on-llm-ch04-text-classification|Ch 4]]'s frozen 0.80).
2. **[[LayerFreezing|Layer freezing]]** via `param.requires_grad = False` — freeze everything except classifier head F1 = 0.63, freeze blocks 0–9 F1 = 0.80. *"Training only the first five encoder blocks is enough to almost reach the performance of training all encoder blocks."*
3. **[[SetFit]]** for few-shot classification (Tunstall et al. 2022, arXiv:2209.11055) — contrastive sentence-pair fine-tuning of a [[SentenceTransformers|SentenceTransformer]] + classification head; 32 labels → F1 = 0.85.
4. **[[ContinuedPretraining|Continued pretraining]] with [[MaskedLanguageModel|MLM]]** via `AutoModelForMaskedLM` + [[DataCollatorForLanguageModeling]] — inserts a domain-adaptation step between generic pretraining and task fine-tuning. *"Like going from a general BERT model to a BioBERT model specialized for the medical domain, to a fine-tuned BioBERT model to classify medication."*

Then pivots to **token-level** fine-tuning ([[NamedEntityRecognition|NER]] on [[CoNLL2003|CoNLL-2003]]) — `AutoModelForTokenClassification` + [[DataCollatorForTokenClassification]] + [[BIOTagging]] + [[LabelAlignment]] + [[seqeval]] for span-level F1.

Ch 11's contribution to the wiki's fine-tuning curriculum is **empirical numbers** for the partial-FT vs full-FT trade-off that [[ai-engineering-ch07-finetuning|AI Engineering Ch 7]] framed in the abstract: freezing 10/12 encoder blocks (well below the Houlsby et al. 2019 *"25%-of-params"* threshold for matching full FT) still reaches 0.80/0.85 of full-FT performance in one epoch on Rotten Tomatoes — confirming the *"upper layers carry most task-specific signal"* intuition.

Forward-references **Ch 12** for fine-tuning **generative** models ([[rlhf|RLHF]] / [[DPO]]) — Ch 11 covers the representation-model half of the fine-tuning curriculum.
