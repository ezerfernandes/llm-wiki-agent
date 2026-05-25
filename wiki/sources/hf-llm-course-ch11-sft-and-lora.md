---
title: "HuggingFace LLM Course — Ch 11: Fine-tune LLMs with SFT and LoRA"
type: source
tags: [hf-llm-course, course, sft, lora, peft, fine-tuning, llm, evaluation]
date: 2026-05-23
source_file: raw/hf-llm-course/ch11-sft-and-lora.md
---

## Summary

Chapter 11 of the HuggingFace LLM Course is a practical guide to instruction-tuning open LLMs end-to-end: structuring conversations with chat templates, running Supervised Fine-Tuning (SFT) with the TRL `SFTTrainer`, reducing memory cost via Low-Rank Adaptation (LoRA) through the PEFT library, and measuring the result with automatic benchmarks (MMLU, BBH, GSM8K, MATH, HumanEval, Alpaca Eval) and `lighteval`. The chapter argues SFT is the lever that converts a next-token base model into an assistant-like instruct model — but warns the cost only pays off when prompting an existing instruct model is genuinely insufficient. LoRA is presented as the default memory-efficient path: freeze base weights, inject trainable rank-decomposition matrices into attention layers, optionally merge adapters back via `merge_and_unload` for zero-latency inference. The closing evaluation section reframes benchmarks as a starting point — domain-specific custom evals, LLM-as-Judge, and arenas like Chatbot Arena are needed to capture real-world quality.

## Key Claims

- SFT is now the dominant adaptation method for LLMs; nearly all consumer-facing chat models (e.g., ChatGPT) have undergone SFT to become helpful and aligned.
- A *base* model predicts next tokens on raw text; an *instruct* model is SFT-tuned on conversational data — making a base model behave like an instruct model requires formatting prompts via a chat template.
- ChatML (system/user/assistant roles with explicit start/end markers) is used by SmolLM2 and Qwen 2; Mistral wraps turns in `[INST] ... [/INST]`; Llama 2/3 use family-specific tags — using the wrong template silently degrades performance.
- `tokenizer.apply_chat_template(messages, tokenize=False)` lets one code path serve many model families by deferring formatting to the tokenizer config pulled from the Hub.
- Chat templates extend beyond text turns: they encode tool calls, multimodal image/audio content, and function calls via structured `content` lists and `tool_calls` fields.
- SFT should only be pursued when prompting an existing instruct model is insufficient; the two strongest justifications are *template control* (strict output schemas/styles) and *domain adaptation* (specialised terminology, professional standards).
- The `SFTTrainer` from TRL (built on `transformers`) auto-applies the model's chat template when the dataset has a `messages` field — no manual formatting code needed.
- Key SFT hyperparameters cluster into duration (`num_train_epochs`, `max_steps`), batch (`per_device_train_batch_size`, `gradient_accumulation_steps`), learning rate (`learning_rate`, `warmup_ratio`), and monitoring (`logging_steps`, `eval_steps`, `save_steps`).
- Healthy training loss has three phases — sharp initial drop, gradual stabilization, convergence — and a small train/val gap is the canonical indicator of generalization vs. memorization.
- `packing=True` in `SFTConfig` concatenates multiple short examples into one sequence to maximize GPU utilization; with `max_steps` set this can silently train for more effective epochs than expected. A `formatting_func` enables custom QA-pair packing.
- LoRA freezes pretrained weights and injects trainable rank-decomposition matrices into transformer layers (typically attention projections), cutting trainable parameters by ~90%.
- When applied to GPT-3 175B, LoRA reduced trainable parameters by 10,000x and GPU memory by 3x versus full fine-tuning, with no inference-time latency overhead once adapters are merged.
- Core LoRA config knobs: `r` (rank, typically 4-32), `lora_alpha` (scaling, usually 2x rank), `lora_dropout` (0.05-0.1), `bias` ("none"/"all"/"lora_only"), `target_modules` (e.g. `"all-linear"` or `"q_proj,v_proj"`), and `task_type` (e.g. `"CAUSAL_LM"`).
- TRL's `SFTTrainer` accepts a `peft_config` argument, so LoRA training is a one-line addition to the existing SFT pipeline.
- After training, `PeftModel.merge_and_unload()` fuses adapter weights back into the base model, producing a single deployable checkpoint with no adapter-loading overhead at inference.
- QLoRA (Quantized LoRA) is supported natively for further memory reduction by combining LoRA with quantized base weights.
- General-knowledge benchmarks like MMLU (57 subjects) and TruthfulQA test breadth and misinformation susceptibility; BBH and GSM8K target reasoning and math; HumanEval (164 problems) tests functional code correctness; MATH covers 12,500 competition-level math problems; Alpaca Eval uses GPT-4 as judge on 805 prompts.
- Benchmark scores do not reliably predict deployed performance — a comprehensive evaluation strategy combines standard benchmarks, LLM-as-Judge, crowdsourced arenas (Chatbot Arena), and custom domain datasets.
- `lighteval` exposes tasks via the format `{suite}|{task}|{num_few_shot}|{auto_reduce}` (e.g. `"mmlu|abstract_algebra|0|0"`), runnable from the CLI with an `accelerate` or `vllm` backend.

## Key Quotes

> "Most LLMs that people interact with on platforms like ChatGPT have undergone SFT to make them more helpful and aligned with human preferences." — Section 1, framing SFT as the dominant post-training step.

> "Using the wrong template can result in poor model performance or unexpected behavior. The easiest way to ensure this is to check the model tokenizer configuration on the Hub." — Section 2, on the silent-failure mode of chat templates.

> "When using a dataset with a 'messages' field, the SFTTrainer automatically applies the model's chat template, which it retrieves from the hub." — Section 3, on TRL's convention-over-configuration design.

> "When applied to GPT-3 175B, LoRA reduced trainable parameters by 10,000x and GPU memory requirements by 3x compared to full fine-tuning." — Section 4, the headline efficiency claim.

> "During inference, these adapter weights can be merged with the base model, resulting in no additional latency overhead." — Section 4, on LoRA's deployment story.

> "Benchmark performance doesn't always translate directly to real-world effectiveness." — Section 5, the central caveat behind custom evals.

## Code & Patterns

### Chat template application (model-agnostic)

```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-135M-Instruct")
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
]
prompt = tok.apply_chat_template(messages, tokenize=False)
```

The same call works for Mistral, Qwen, Llama — each tokenizer's Jinja template handles the family-specific markers.

### Template families seen in the chapter

- **ChatML** (SmolLM2, Qwen 2): role tokens `system` / `user` / `assistant` with explicit boundary markers.
- **Mistral**: `[INST] ... [/INST]` wrapping each user turn; system message folded into the first instruction.
- **Llama 2**: `[INST]` blocks plus `<<SYS>>` system wrapping and `<s>`/`</s>` boundaries.
- **Llama 3**: role-specific header tokens with per-message end-of-turn markers.

### Tool-use message shape

```python
{"role": "assistant", "content": "...", "tool_calls": [
    {"tool": "calculator", "parameters": {"operation": "multiply", "x": 123, "y": 456}}
]}
{"role": "tool", "tool_name": "calculator", "content": "56088"}
```

### Multimodal message shape

`content` becomes a list of typed parts: `{"type": "text", ...}` and `{"type": "image", "image_url": ...}`.

### Minimal SFT pipeline (TRL)

```python
from trl import SFTConfig, SFTTrainer
training_args = SFTConfig(
    output_dir="./sft_output",
    max_steps=1000,
    per_device_train_batch_size=4,
    learning_rate=5e-5,
    logging_steps=10, save_steps=100,
    eval_strategy="steps", eval_steps=50,
)
trainer = SFTTrainer(model=model, args=training_args,
                     train_dataset=ds["train"], eval_dataset=ds["test"],
                     processing_class=tokenizer)
trainer.train()
```

### Packing + custom formatting

```python
def formatting_func(ex):
    return f"### Question: {ex['question']}\n ### Answer: {ex['answer']}"
training_args = SFTConfig(packing=True)
trainer = SFTTrainer("facebook/opt-350m", train_dataset=ds, args=training_args,
                     formatting_func=formatting_func)
```

### LoRA configuration

```python
from peft import LoraConfig
peft_config = LoraConfig(
    r=6, lora_alpha=8, lora_dropout=0.05,
    bias="none", target_modules="all-linear",
    task_type="CAUSAL_LM",
)
trainer = SFTTrainer(model=model, args=args, train_dataset=ds["train"],
                     peft_config=peft_config, processing_class=tokenizer)
```

Rules of thumb stated: start small (`r=4-8`), set `lora_alpha = 2 * r`, dropout 0.05-0.1.

### Loading and switching adapters

```python
from peft import PeftModel, PeftConfig
config = PeftConfig.from_pretrained("ybelkada/opt-350m-lora")
base = AutoModelForCausalLM.from_pretrained(config.base_model_name_or_path)
lora_model = PeftModel.from_pretrained(base, "ybelkada/opt-350m-lora")
# also: load_adapter(), set_adapter(), unload()
```

### Merging adapters for deployment

```python
base_model = AutoModelForCausalLM.from_pretrained(name, torch_dtype=torch.float16, device_map="auto")
peft_model = PeftModel.from_pretrained(base_model, "path/to/adapter", torch_dtype=torch.float16)
merged_model = peft_model.merge_and_unload()
merged_model.save_pretrained(out); tokenizer.save_pretrained(out)
```

Precision must match training precision throughout; always save the tokenizer alongside the merged model.

### Evaluation with lighteval

Task spec: `{suite}|{task}|{num_few_shot}|{auto_reduce}`, e.g. `"mmlu|abstract_algebra|0|0"`.

```bash
lighteval accelerate "pretrained=your-model-name" \
    "mmlu|anatomy|0|0" "mmlu|professional_medicine|0|0" \
    --max_samples 40 --batch_size 1 \
    --output_path "./results" --save_generations true
```

Benchmarks discussed: [[MMLU]], TruthfulQA, [[BBH]], [[GSM8K]], MATH, HumanEval, Alpaca Eval, HELM. Alternative methods: [[LLMAsJudge]], Chatbot Arena, custom domain suites.

### Warning patterns surfaced
- Validation loss rising while training loss falls → overfitting.
- Loss too low / outputs too similar to training → memorization.
- Loss flat → underfitting or LR too low.
- `packing=True` with `max_steps` can over-train.

## Connections

- [[HuggingFace]] — publisher of the course, TRL, PEFT, lighteval, SmolLM2.
- [[TRL]] — provides the `SFTTrainer` and `SFTConfig` used throughout Sections 3-4.
- [[PEFT]] — library implementing `LoraConfig`, `PeftModel`, `merge_and_unload`.
- [[LightEval]] — evaluation harness with `{suite}|{task}|{shots}|{reduce}` task spec.
- [[SmolLM2]] — recurring base model (135M and Instruct variants) used in examples.
- [[DeepSeekR1DistillQwen1.5B]] — target model for the SFT and LoRA walkthroughs.
- [[Mistral]] / [[Qwen]] / [[Llama2]] / [[Llama3]] — template families contrasted in Section 2.
- [[SupervisedFineTuning]] — the chapter's central concept, refining [[FineTuning]] practice for chat-style data.
- [[LoRA]] — parameter-efficient fine-tuning method introduced as a SFT add-on.
- [[ParameterEfficientFineTuning]] — broader family that includes LoRA and QLoRA.
- [[QLoRA]] — quantized LoRA, named as a memory-efficiency extension.
- [[ChatTemplate]] / [[ChatML]] — message-formatting conventions enabling cross-model training.
- [[ApplyChatTemplate]] — the `tokenizer.apply_chat_template` API.
- [[InstructTuning]] — synonym used throughout to describe what SFT produces.
- [[ToolUse]] / [[FunctionCalling]] / [[MultimodalInputs]] — advanced template scenarios.
- [[GradientAccumulation]] — referenced as `gradient_accumulation_steps` for effective-batch scaling.
- [[Packing]] — `SFTTrainer` packing for GPU utilization.
- [[MergeAndUnload]] — the adapter-fusion step before deployment.
- [[MMLU]], [[BBH]], [[GSM8K]], [[MATH]], [[HumanEval]], [[AlpacaEval]], [[HELM]], [[TruthfulQA]] — benchmarks named in Section 5.
- [[ChatbotArena]] / [[LLMAsJudge]] — alternative evaluation modalities.
- [[smoltalk]] — `HuggingFaceTB/smoltalk` dataset used in exercises.
- [[bitsandbytes]] — implied dependency behind QLoRA's quantization (named in conventional HF tutorials).
- [[HuggingFaceLLMCourse]] — parent course this chapter belongs to.
- [[DirectPreferenceOptimization]] — referenced as a related post-SFT alignment method.

## Contradictions

- None identified within Chapter 11 itself.
- Cross-wiki: the chapter's framing of SFT as a small, well-bounded engineering step may sit in tension with sources that emphasize the data-curation and alignment effort as the dominant cost; reviewers should reconcile with any [[Alignment]] or [[RLHF]] pages once consolidated.
- The chapter's heuristic `lora_alpha = 2 * r` is presented as a rule of thumb; some practitioner sources prefer `alpha = r` or treat alpha as decoupled — flag if a [[LoRA]] concept page already states a different convention.
