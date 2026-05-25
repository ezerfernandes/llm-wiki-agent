---
title: "BLIP-2"
type: entity
tags: [model, multimodal, vision-language, mllm, salesforce]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# BLIP-2

**BLIP-2: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation 2** — [[Salesforce|Salesforce Research]]'s 2023 multimodal text-generation model that bridges a **frozen pretrained image encoder** ([[VisionTransformer|ViT]]) and a **frozen pretrained LLM** via a small trainable **[[QFormer|Querying Transformer (Q-Former)]]** + a linear projection layer. Introduced in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] as the canonical worked example of an **adapter-on-frozen-encoder multimodal LLM**.

Cited as **Li et al. 2023** *"BLIP-2: Bootstrapping language-image pretraining with frozen image encoders and large language models"* (ICML 2023, PMLR).

## Why BLIP-2 matters

*"Creating a multimodal language model from scratch requires significant computing power and data. We would have to use billions of images, text, and image-text pairs to create such a model. As you can imagine, this is not easily feasible! Instead of building the architecture from scratch, BLIP-2 bridges the vision-language gap by building a bridge, named the Querying Transformer (Q-Former), that connects a pretrained image encoder and a pretrained LLM."*

The architectural punchline: **only the Q-Former is trained**. The image encoder ([[VisionTransformer|ViT]]) and the LLM are both frozen — so adding vision to an existing text LLM no longer costs full-pretraining compute, only Q-Former-training compute.

## Architecture (two stages)

**Stage 1 — Q-Former representation learning** on (image, caption) pairs. The frozen ViT produces image features → fed into the Q-Former's Image Transformer; captions → fed into the Q-Former's Text Transformer (the two modules **share attention layers**). Trained jointly on three objectives:

1. **[[ImageTextContrastive|Image-text contrastive learning]]** — maximize mutual information between paired (image, text) embeddings.
2. **[[ImageTextMatching|Image-text matching]]** — binary classification of (image, text) pairs as matched / unmatched.
3. **[[ImageGroundedTextGeneration|Image-grounded text generation]]** — train the model to generate text from visual features.

**Stage 2 — LLM soft-prompting.** The Q-Former's learnable embeddings (now visually-conditioned in text-compatible space) are passed through a fully-connected linear projection to match the LLM's expected shape, then **fed to the LLM as a [[SoftVisualPrompt|soft visual prompt]]**. *"The LLM will be given information about the image in a similar manner to the context you would provide an LLM when prompting."*

## Worked checkpoint — `Salesforce/blip2-opt-2.7b`

[[hands-on-llm-ch09-multimodal-llms|Ch 9]]'s runnable example uses [[Salesforce]]'s `Salesforce/blip2-opt-2.7b` via Hugging Face `transformers`:

```python
from transformers import AutoProcessor, Blip2ForConditionalGeneration
blip_processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16
)
```

- **Image encoder**: a [[VisionTransformer|ViT]] (introspectable via `model.vision_model`).
- **LLM backbone**: OPT-2.7b from [[meta]] (introspectable via `model.language_model`); uses a `GPT2TokenizerFast`.
- **Image preprocessing**: resizes any input to **224 × 224** (`torch.Size([1, 3, 224, 224])`).

## Use cases demonstrated in Ch 9

1. **[[ImageCaptioning|Image captioning]]** — supercar image → *"an orange supercar driving on the road at sunset."* Rorschach inkblot → *"a black and white ink drawing of a bat."*
2. **[[VisualQuestionAnswering|Visual question answering]] / multimodal chat** — supercar + *"Question: Write down what you see in this picture. Answer:"* → *"A sports car driving on the road at sunset."* Follow-up *"What would it cost me to drive that car?"* → *"$1,000,000"* (highly specific). Chat is implemented by concatenating prior `Question: ... Answer: ...` turns into the prompt.

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[QFormer]] — the trainable bridge.
- [[VisionTransformer]] — the frozen image encoder.
- [[SoftVisualPrompt]] — the mechanism by which Q-Former outputs condition the LLM.
- [[ImageTextContrastive]] / [[ImageTextMatching]] / [[ImageGroundedTextGeneration]] — the three Q-Former training objectives.
- [[MultimodalLLM]] — the architectural family BLIP-2 anchors.
- [[LLaVA15]] — the successor / simplification ([[QFormer|Q-Former]] → 2-layer MLP projector).
- [[Idefics2]] — the [[Mistral|Mistral-7B]]-based descendant cited alongside BLIP-2 in Ch 9.
- [[Salesforce]] — author lab.
- [[ImageCaptioning]] / [[VisualQuestionAnswering]] — Ch 9's two BLIP-2 use cases.
