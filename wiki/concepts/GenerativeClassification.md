---
title: "Generative Classification"
type: concept
tags: [llm, classification, generative-model, prompt-engineering]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Generative Classification

Using a [[GenerativeModel|generative LLM]] — decoder-only ([[ChatGPT|ChatGPT]] / [[GPT|GPT]]) or encoder-decoder ([[t5|T5]] / [[FLANT5|Flan-T5]]) — as a **classifier** by (1) prompting the model with an instruction that asks it to emit a class label, then (2) **parsing the free-text output back to a class assignment**.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

The chapter's second half (*"Text Classification with Generative Models"*) is the wiki's first end-to-end treatment of this regime. The framing:

> "Classification with generative language models, such as OpenAI's GPT models, works a bit differently from what we have done thus far. These models take as input some text and generative text and are thereby aptly named sequence-to-sequence models. This is in stark contrast to our task-specific model, which outputs a class instead." — Ch 4

The asymmetry: a [[TaskSpecificModel|task-specific representation model]] **outputs a class directly** (via a softmax head); a generative model **outputs text** that must be parsed.

## Two recipes from Ch 4

### Recipe 1: Flan-T5 (encoder-decoder, open source)

```python
pipe = pipeline("text2text-generation",
                model="google/flan-t5-small", device="cuda:0")

prompt = "Is the following sentence positive or negative? "
data = data.map(lambda example: {"t5": prompt + example["text"]})

y_pred = []
for output in pipe(KeyDataset(data["test"], "t5")):
    text = output[0]["generated_text"]
    y_pred.append(0 if text == "negative" else 1)
```

[[RottenTomatoes|Rotten Tomatoes]] F1: **0.84**.

### Recipe 2: ChatGPT (decoder-only, closed source via API)

```python
prompt = """Predict whether the following document is a positive or negative
movie review:

[DOCUMENT]

If it is positive return 1 and if it is negative return 0. Do not give any
other answers."""

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.replace("[DOCUMENT]", document)}
    ],
    model="gpt-3.5-turbo-0125",
    temperature=0
)
```

[[RottenTomatoes|Rotten Tomatoes]] F1: **0.91** — the chapter's best result across all four regimes.

## Three load-bearing prompt-engineering rules

1. **State the task explicitly.** Generative models *"have no idea what to do with"* a bare input — *"we need to help it understand the context and guide it toward the answers."*
2. **Constrain the output schema.** Ch 4's ChatGPT prompt says *"Do not give any other answers"* — output parsing fails on free-form responses.
3. **Set `temperature=0`** for deterministic classification — otherwise the same input can produce different labels on different runs.

## Comparison to other classification regimes

| Regime | Output | Requires labels? | Requires GPU? |
|---|---|---|---|
| Task-specific | Class logits | Pretrained, no | Inference only |
| Embedding + classifier | Embedding → logits | Yes (labeled train set) | Embedding only |
| Zero-shot embedding | Cosine to label embedding | No | Embedding only |
| **Generative classification** | **Free text → parse** | **No** | **Generation (or API)** |

## Failure modes

- **Output parsing brittleness.** If the model says *"Positive (this is clearly a happy movie)"* instead of *"positive"*, the simple `text == "negative"` check fails. Robust parsers (regex / JSON-mode / [[Outlines|constrained decoding]]) are needed at scale.
- **[[DataContamination|Benchmark contamination]].** Ch 4 explicitly flags: *"since we do not know what data the model was trained on, we cannot easily use these kinds of metrics for evaluating the model. For all we know, it might have actually been trained on our dataset!"* — closed-source LLM F1 numbers on public datasets are epistemologically suspect.
- **Cost.** Ch 4's full 1,066-row test sweep on `gpt-3.5-turbo-0125` cost ~3 cents in 2024; scaling to millions of records makes API costs the dominant deployment concern.
- **Rate limits.** Production deployments require **[[ExponentialBackoff|exponential backoff]]** on API errors.

## Connections

- [[GenerativeModel]] — the parent model category.
- [[PromptEngineering]] — the discipline for designing the instruction.
- [[FLANT5]] / [[ChatGPT]] / [[t5]] — the worked example models.
- [[InstructionTuning]] / [[PreferenceFinetuning]] — the post-training stages that make generative classification work out of the box.
- [[TaskSpecificModel]] / [[EmbeddingModel]] / [[ZeroShotClassification]] — the alternative classification regimes Ch 4 compares against.
- [[ExponentialBackoff]] — required for API-based generative classification at scale.
- [[DataContamination]] — the epistemological limit.
- [[hands-on-llm-ch04-text-classification]] — primary source.
