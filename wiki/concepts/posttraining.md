---
title: "Post Training"
type: concept
tags: [training, post-training, foundation-models]
sources: [ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

# Post Training

The process of **training a model after the pre-training phase** to specialize its behavior — instruction-following, safety, format adherence, conversation skills. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]:

> *"Many people use post-training to refer to the process of training a model after the pre-training phase. Conceptually, post-training and finetuning are the same and can be used interchangeably. However, sometimes, people might use them differently to signify the different goals."*

## Post-training vs. finetuning — who does it

The practical distinction Ch 1 draws is **who does the work**:

| Phase | Who | Goal |
|---|---|---|
| **Post-training** | Model developers (e.g., [[openai\|OpenAI]], [[anthropic\|Anthropic]]) | Improve a base model before release — instruction following, safety alignment, format consistency. |
| **[[FineTuning\|Finetuning]]** | Application developers | Adapt a (possibly already-post-trained) model to a specific task or domain. |

> *"It's usually post-training when it's done by model developers. For example, OpenAI might post-train a model to make it better at following instructions before releasing it. It's finetuning when it's done by application developers."*

## Why the names exist

Ch 1's footnote: *"If you find the terms 'pre-training' and 'post-training' lacking in imagination, you're not alone. The AI research community is great at many things, but naming isn't one of them."*

Conceptually post-training and finetuning are the same operation (continue training a previously-trained model). The two-word taxonomy exists to signal **intent and ownership** — who is doing the training and for what audience.

## Compute proportions

Per Ch 1's InstructGPT data point: **pre-training uses ~98% of total compute**; post-training fits into the remaining ~2%. This proportion is roughly stable across frontier models — pre-training is the resource-intensive step; post-training is comparatively cheap.

## Connections

- [[Pretraining]] — the prior phase.
- [[FineTuning]] — conceptually equivalent; different audience.
- [[ModelingAndTraining]] — parent training-phase taxonomy.
- [[ai-engineering-ch01-intro]] — primary source.
- [[FoundationModel]] — what gets post-trained.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 supplies the **detailed two-stage decomposition** of post-training:

1. **[[SupervisedFinetuning|Supervised finetuning (SFT)]]** — finetune the pre-trained model on (prompt, response) [[DemonstrationData|demonstration data]] to optimize for conversation rather than completion. Also called [[BehaviorCloning|behavior cloning]].
2. **[[PreferenceFinetuning|Preference finetuning]]** — further finetune the SFT model to align with human preferences via [[rlhf|RLHF]], [[DPO]], or [[RLAIF]].

The chapter's framing: pre-training is *"reading to acquire knowledge"* while post-training is *"learning how to use that knowledge."*

### Compute proportion (concretized)

Ch 2 reiterates the InstructGPT data point from Ch 1 with a sharper interpretation:

> "As post-training consumes a small portion of resources compared to pre-training (InstructGPT used only 2% of compute for post-training and 98% for pre-training), you can think of post-training as **unlocking the capabilities that the pre-trained model already has but are hard for users to access via prompting alone**."

### "Both stages are bandages on bad pre-training data"

Ch 2's blunt assessment:

> "Both SFT and preference finetuning are steps taken to address the problem created by the low quality of data used for pre-training. If one day we have better pre-training data or better ways to train foundation models, we might not need SFT and preference at all."

### The Shoggoth meme

Ch 2 maps the three training stages onto the *Shoggoth with a smiley face* meme: pre-trained model (untamed monster on indiscriminate data) → SFT (socially acceptable via demonstration data) → preference finetuning (customer-appropriate via comparison data).

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* is the wiki's **first chapter to walk all three stages of the post-training pipeline end-to-end with runnable code**. The chapter's framing of the **three-step LLM training pipeline**:

> *"These three steps demonstrate the process of starting from an untrained architecture and ending with a preference-tuned LLM."* — Ch 12

| Stage | Method (Ch 12) | Output |
|---|---|---|
| 1. Language modeling (pretraining) | Self-supervised next-token prediction on massive text | Base / pretrained / foundation model |
| 2. **[[SupervisedFinetuning|SFT]]** | Next-token prediction on labeled `(instruction, response)` pairs ([[QLoRA]] + [[SFTTrainer]]) | Instruction / chat model |
| 3. **[[PreferenceFinetuning|Preference tuning]]** | Alignment via reward signal ([[DPO]] in Ch 12's recipe; [[PPO]] as the canonical RL baseline) | Aligned / preference-tuned model |

### The contrast with Ch 12's other framing

Ch 12 implicitly **collapses Huyen's "post-training" vs "finetuning" who-does-it distinction** by walking a *full* application-engineer-feasible post-training pipeline on a free Google Colab T4. The chapter's pedagogical statement: post-training is no longer model-developer-only territory; modern QLoRA + TRL puts the full pipeline within reach of anyone with a free Colab account.
