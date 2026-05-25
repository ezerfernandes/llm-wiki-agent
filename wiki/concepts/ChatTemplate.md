---
title: "Chat Template"
type: concept
tags: [llm-engineering, prompt-engineering, tokenization]
sources: [leh-ch05-supervised-fine-tuning, ai-engineering-ch05-prompt-engineering, ai-engineering-ch08-dataset-engineering, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation, hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-24
---

## Definition
Formatting convention that wraps instruction-answer pairs with role markers and special tokens for SFT or inference.

## In LLM Engineer's Handbook
Per [[leh-ch05-supervised-fine-tuning]], base models have no native chat template — you can pick any; instruct models must keep the original. Common templates: [[AlpacaFormat]] (`### Instruction:` / `### Response:`), [[ChatML]] (`<|im_start|>role` ... `<|im_end|>`), Llama 3 (`<|begin_of_text|>`, `<|start_header_id|>role<|end_header_id|>`, `<|eot_id|>`), Phi-3, Gemma. Implementation: Jinja templates in the Transformers library; every whitespace and line break matters.

## From [[ai-engineering-ch05-prompt-engineering|AI Engineering Ch 5]]

[[ChipHuyen|Huyen]] uses the chat template as the **wire-format boundary between [[SystemPrompt|system prompts]] and [[UserPrompt|user prompts]]** — defined by the model developer, distinct from the application-developer-defined [[PromptTemplate|prompt template]].

Two canonical examples (both for Llama):

**Llama 2:**
```
<s>[INST] <<SYS>>
{{ system_prompt }}
<</SYS>>
{{ user_message }} [/INST]
```

**Llama 3** (Meta changed the template between versions):
```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>
{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

Each span between `<|` and `|>` is treated as a single token.

**Silent-failure surface.** Ch 5 explicitly warns:

> "Accidentally using the wrong template can lead to bewildering performance issues. Small mistakes when using a template, such as an extra new line, can also cause the model to significantly change its behaviors."

The failure is silent because output stays *plausible* — only quality degrades. Ch 5's three good practices:

1. Inputs must follow the model's chat template exactly.
2. Third-party prompt-construction tools often use the wrong template — verify it.
3. Print the final prompt before sending it to catch template drift.

**Provider-API mitigation.** Many model APIs (OpenAI, Anthropic) accept `messages=[{"role": ..., "content": ...}]` and apply the chat template server-side, shifting the responsibility to the provider. This is the design reason the same DSPy or LangChain code works across providers without per-template plumbing — but also why a third-party prompt-construction tool that *reconstructs* the template itself is a common bug source.

## Connections

- [[SystemPrompt]] / [[UserPrompt]] — the two halves a chat template wraps.
- [[PromptTemplate]] — the application-side counterpart (parameterized prompt-text, hydrated with data, ≠ chat template).
- [[Llama]] — the model family whose chat-template evolution Ch 5 traces.
- [[Tokenization]] — chat-template special tokens are single tokens to the tokenizer.
- [[meta|Meta]] — defines the Llama chat templates.
- [[ai-engineering-ch05-prompt-engineering]] — prompt-engineering source.
- [[leh-ch05-supervised-fine-tuning]] — SFT-training source.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 surfaces chat templates as the **final step in the data-processing pipeline** before finetuning:

> "Once you've deduplicated and cleaned your data, you need to get it into the right format expected by the model you're finetuning. Each model uses a specific tokenizer and expects data in a specific chat template, as discussed in Chapter 5. **Getting data into the wrong chat template can cause strange bugs in your model**."

### The finetuning-vs-prompting prompt shift

A key Ch 8 framing: at finetuning time, **prompts often get shorter than during prompt engineering** because the model can learn the task from examples rather than from in-prompt task descriptions:

```
# Prompt engineering (3-shot)
Label the following item as either edible or inedible.
Item: burger
Label: edible
Item: car
Label: inedible
Item: mushroom
Label: edible
Item: {INPUT}
Label:

# After finetuning
{INPUT} -->
```

This makes finetuning a **cost-reduction lever** for token-heavy prompt-engineering workloads.

### The silent-failure surface

Per Ch 8 (echoing Ch 5):

> "When you use the finetuned model, make sure that the prompts you use match the format of the finetuning data."

Failure modes from format mismatch:

- `"burger"` — missing end arrow.
- `"Item: burger -->"` — extra prefix.
- `"burger --> "` — extra trailing space.

All produce **silent quality degradation**, not crashes. This is the same silent-failure surface Ch 5 named for inference, applied to finetuning data.

## From [[hands-on-llm-ch06-prompt-engineering|Hands-On LLMs Ch 6]]

Ch 6 surfaces the **`transformers.pipeline` chat-template machinery** directly:

```python
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False)
```

For [[Phi3Mini|Phi-3]], the `messages=[{"role": "user", "content": "Create a funny joke about chickens."}]` renders to:

```
<s><|user|>
Create a funny joke about chickens.<|end|>
<|assistant|>
```

> *"You may recognize the special tokens `<|user|>` and `<|assistant|>` from Chapter 2. This prompt template, further illustrated in Figure 6-2, was used during the training of the model. Not only does it provide information about who said what, but it is also used to indicate when the model should stop generating text (see the `<|end|>` token). This prompt is passed directly to the LLM and processed all at once."* — Ch 6

The Ch 6 framing is the **wiki's most concrete worked example** of chat-template processing — showing exactly the token sequence the model sees. The framing also surfaces a feature [[ai-engineering-ch05-prompt-engineering|Huyen Ch 5]]'s coverage left implicit: the same special tokens that label *who said what* also serve as **stopping tokens** that tell the model when to halt generation.

### Few-shot prompts and role alternation

Ch 6's [[OneShotPrompting|one-shot]] / [[FewShotLearning|few-shot]] examples require properly alternating `user` / `assistant` roles in the `messages` list. Without alternation, the model interprets the prompt as *"talking to itself"*. The `apply_chat_template` machinery handles the rendering automatically; the application developer's responsibility is constructing the correct messages list.

## From [[hands-on-llm-ch07-advanced-text-generation|Hands-On LLMs Ch 7]]

Ch 7 surfaces a structural gotcha [[hands-on-llm-ch06-prompt-engineering|Ch 6]]'s `transformers.pipeline` coverage left implicit: [[LangChainLlamaCpp|`langchain.LlamaCpp`]] does **NOT** auto-apply chat templates. The empty-output demonstration is the chapter's pedagogical hook:

```python
from langchain import LlamaCpp
llm = LlamaCpp(model_path="Phi-3-mini-4k-instruct-fp16.gguf", ...)
llm.invoke("Hi! My name is Maarten. What is 1 + 1?")
# → empty string!
```

The fix is to **explicitly wrap the input in Phi-3's chat template** via a [[PromptTemplate|PromptTemplate]]:

```python
template = """<s><|user|>
{input_prompt}<|end|>
<|assistant|>"""
prompt = PromptTemplate(template=template, input_variables=["input_prompt"])
basic_chain = prompt | llm
basic_chain.invoke({"input_prompt": "Hi! My name is Maarten. What is 1 + 1?"})
# Now produces actual output.
```

The structural lesson: **chat-template application is the responsibility of the application-side code path, not the model loader**. `transformers.pipeline.__call__` happens to apply the template automatically; `langchain.LlamaCpp.invoke` does not. This is a load-bearing operational difference future LangChain receipts should know.

## From [[hands-on-llm-ch12-fine-tuning-generation-models|Hands-On LLMs Ch 12]]

Ch 12 of *Hands-On LLMs* uses the chat template as the **training-side wire format** for the QLoRA-SFT recipe — the wiki's first runnable example of chat-template application as a **dataset-preprocessing step** (vs Chs 6 / 7's inference-side application).

### Ch 12's TinyLlama / UltraChat template

```
<|user|>
{prompt}</s>
<|assistant|>
{response}</s>
```

The chapter calls `tokenizer.apply_chat_template(chat, tokenize=False)` on each [[UltraChat]] example, producing the string above for ingestion by `trl.SFTTrainer` (with `dataset_text_field="text"`).

### The cross-tokenizer trick

Ch 12 loads the chat template from a **different** tokenizer than the base model being trained: the chat-tuned variant `TinyLlama/TinyLlama-1.1BChat-v1.0` defines the template, while the base `TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T` is the model being SFT'd. This is the wiki's first example of cross-tokenizer template borrowing — done because the base model has no native chat template (per LEH Ch 5's framing), so any structurally-compatible template can be borrowed.

### DPO-stage template

The DPO stage uses a slightly different template (with a system-prompt slot):

```
prompt: <|system|>\n{system}</s>\n<|user|>\n{input}</s>\n<|assistant|>\n
chosen: {chosen}</s>\n
rejected: {rejected}</s>\n
```

Ch 12's pedagogical point: chat-template structure is **regime-invariant** (same `<|user|>...<|assistant|>` skeleton across SFT and DPO), but the role-slot inventory expands with the algorithm's needs.
