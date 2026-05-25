---
title: "Visual Question Answering"
type: concept
tags: [multimodal, vision-language, task, vqa, chat]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Visual Question Answering (VQA)

The task of **answering a natural-language question about a specific image**. Framed in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] as the extension of [[ImageCaptioning|image captioning]] that requires the model to *"process both the image as well as the question at once."*

*"Instead of following this linear structure, we can try to present both modalities simultaneously by performing what is called visual question answering. In this particular use case, we give the model an image along with a question about that specific image for it to answer."*

## Mechanism via [[BLIP2|BLIP-2]] (Ch 9)

The interface trick: pass **both** `image` **and** `text` to the BLIP-2 processor. Without text the model captions; with text it answers.

```python
prompt = "Question: Write down what you see in this picture. Answer:"
inputs = blip_processor(image, text=prompt, return_tensors="pt").to(device, torch.float16)
generated_ids = model.generate(**inputs, max_new_tokens=30)
generated_text = blip_processor.batch_decode(generated_ids, skip_special_tokens=True)
```

The image becomes a [[SoftVisualPrompt|soft visual prompt]]; the question becomes a textual prompt; the LLM decodes an answer conditioned on both.

## Multi-turn chat as concatenated VQA (Ch 9)

*"To do so, we can give the model our previous conversation, including its answer to our question. We then ask it a follow-up question."* The chat history is folded into the prompt:

```python
prompt = (
    "Question: Write down what you see in this picture. "
    "Answer: A sports car driving on the road at sunset. "
    "Question: What would it cost me to drive that car? Answer:"
)
```

This second turn produces *"$1,000,000"* — *"highly specific! This shows more chat-like behavior from BLIP-2, which allows for some interesting conversations."*

## Worked examples (Ch 9)

| Turn | Prompt | Answer |
|---|---|---|
| 1 | *"Question: Write down what you see in this picture. Answer:"* | *"A sports car driving on the road at sunset"* |
| 2 | *"... Question: What would it cost me to drive that car? Answer:"* | *"$1,000,000"* |

Ch 9 closes with an `ipywidgets`-based interactive notebook chatbot over a single fixed image that re-renders BLIP-2's response on every text-widget input change.

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[BLIP2]] — Ch 9's worked VQA model.
- [[ImageCaptioning]] — the simpler one-modality-in, one-modality-out predecessor.
- [[SoftVisualPrompt]] — the image-side conditioning mechanism.
- [[MultimodalLLM]] — the architectural pattern that supports VQA.
- [[PromptEngineering]] — VQA uses prompt engineering over the textual side; the *"Question: ... Answer:"* template is the simplest VQA prompt.
