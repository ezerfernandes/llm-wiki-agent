---
title: "AutoPeftModelForCausalLM"
type: concept
tags: [peft, lora, hugging-face, model-loading, hands-on-llm]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# AutoPeftModelForCausalLM

**`peft.AutoPeftModelForCausalLM`** is the [[peft|PEFT]] library's auto-loader for **PEFT-wrapped causal LMs** — give it a folder containing a saved adapter + the path to the base model it was trained on, and it reconstructs the wrapped model ready to merge or to continue training.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses `AutoPeftModelForCausalLM` to **load the QLoRA SFT adapter** before the merge step:

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained(
    "TinyLlama-1.1B-qlora",     # folder containing the saved LoRA adapter
    low_cpu_mem_usage=True,
    device_map="auto",
)

merged_model = model.merge_and_unload()
```

For DPO, the same loader is used **with quantization** to reload the SFT adapter onto a 4-bit base for the DPO training pass:

```python
model = AutoPeftModelForCausalLM.from_pretrained(
    "TinyLlama-1.1B-qlora",
    low_cpu_mem_usage=True,
    device_map="auto",
    quantization_config=bnb_config,   # 4-bit NF4 with double quant
)
```

## `merge_and_unload()`

The chapter's central PEFT operation: takes a model with a frozen base + trainable LoRA adapter and **fuses the adapter back into the base weights** in one shot. Returns a regular `transformers` model that can be used for inference with no PEFT-specific runtime. The chapter reloads the base in 16-bit (not 4-bit) specifically to do the merge cleanly.

## Iterative merging in Ch 12's two-adapter case

Ch 12 stacks two adapters (SFT then DPO) by **merging sequentially**:

```python
# Step 1: merge SFT adapter into base
model = AutoPeftModelForCausalLM.from_pretrained("TinyLlama-1.1B-qlora", ...)
sft_model = model.merge_and_unload()

# Step 2: load DPO adapter on top of SFT-merged model
dpo_model = PeftModel.from_pretrained(
    sft_model,
    "TinyLlama-1.1B-dpo-qlora",
    device_map="auto",
)
dpo_model = dpo_model.merge_and_unload()
```

## Connections

- [[peft|PEFT]] — the library.
- [[lora|LoRA]] / [[QLoRA]] — the techniques whose adapters this loader handles.
- [[PrepareModelForKBitTraining]] — the function called before training a 4-bit base.
- [[BitsAndBytesConfig]] — the quantization passed when reloading for further training.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
