---
title: "Image Captioning"
type: concept
tags: [multimodal, vision-language, task]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Image Captioning

The task of **producing a natural-language description of an image**. Framed in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] as *"the most straightforward usage of a model like [[BLIP2|BLIP-2]]"* — the simplest application of an adapter-style [[MultimodalLLM|multimodal LLM]] that accepts images and emits text.

## Motivating use cases (Ch 9)

*"You might be a store that wants to create descriptions of its clothing or perhaps you are a photographer that does not have the time to manually label the 1,000+ pictures of a wedding."*

## Mechanism via [[BLIP2|BLIP-2]] (Ch 9)

*"An image is converted to pixel values that the model can read. These pixel values are passed to BLIP-2 to be converted into [[SoftVisualPrompt|soft visual prompts]] that the LLM can use to decide on a proper caption."* — the LLM **decodes a caption** conditioned on the soft visual prompt the same way it would decode a continuation conditioned on a textual prompt.

```python
inputs = blip_processor(image, return_tensors="pt").to(device, torch.float16)
generated_ids = model.generate(**inputs, max_new_tokens=20)
generated_text = blip_processor.batch_decode(generated_ids, skip_special_tokens=True)
```

## Worked examples (Ch 9)

- **Supercar image** → *"an orange supercar driving on the road at sunset."*
- **Rorschach inkblot** → *"a black and white ink drawing of a bat."*

## Limits

*"Domain-specific images, like pictures of specific cartoon characters or imaginary creations, may fail as the model was trained on largely public data."* — the same training-data-distribution-as-coverage caveat that limits dense retrieval ([[hands-on-llm-ch08-semantic-search-and-rag|Ch 8]]) limits multimodal models. Captioning is intuitive but not magic.

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[BLIP2]] — Ch 9's worked image-captioning model.
- [[SoftVisualPrompt]] — the mechanism by which the image conditions the LLM.
- [[VisualQuestionAnswering]] — the natural extension of captioning to **image + question → answer**.
- [[MultimodalLLM]] — the broader pattern category.
- [[CLIP]] — captioning's contrastive predecessor (the encoder-only counterpart).
