---
title: "Soft Visual Prompt"
type: concept
tags: [multimodal, soft-prompt, vision-language, mllm]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Soft Visual Prompt

A **continuous, trainable embedding derived from a non-text encoder (typically a [[VisionTransformer|ViT]])** that is **passed into an LLM in the same architectural role a text prompt would occupy**. Introduced operationally in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] as the stage-2 output of [[BLIP2|BLIP-2]]'s [[QFormer|Q-Former]]:

> *"The learnable embeddings derived from step 1 now contain visual information in the same dimensional space as the corresponding textual information. The learnable embeddings are then passed to the LLM. In a way, these embeddings serve as soft visual prompts that condition the LLM on the visual representations that were extracted by the Q-Former."*

A soft visual prompt is the **vision-modality specialization of [[SoftPrompt|soft prompts]]** — and the substrate the entire adapter-style [[MultimodalLLM|multimodal LLM]] family rests on.

## Why "soft" + "visual"

| | [[HardPrompt\|Hard prompt]] | [[SoftPrompt\|Soft prompt]] | **Soft visual prompt** |
|---|---|---|---|
| **Form** | Discrete tokens | Continuous trainable vectors | Continuous vectors **derived from a non-text encoder** |
| **Origin** | Author types it | Trained as PEFT layer | **Forward pass over an image through ViT + bridge** |
| **Role at the LLM** | Textual input | Pseudo-textual input | Pseudo-textual input |

The wiki's first instance of a soft prompt whose values come from a non-text modality's encoder rather than from PEFT training.

## Pipeline (Ch 9 / BLIP-2)

```
image
  → frozen ViT             (feature extraction)
  → Q-Former               (stage-1 trained to be image-text bilingual)
  → linear projection      (shape-match to LLM expected embedding dim)
  → LLM                    (decodes a caption / answer conditioned on the soft visual prompt)
```

*"There is also a fully connected linear layer in between them to make sure that the learnable embeddings have the same shape as the LLM expects."*

The result: *"the LLM will be given information about the image in a similar manner to the context you would provide an LLM when prompting."*

## Generalization beyond BLIP-2

The soft-visual-prompt pattern generalizes across the adapter-style [[MultimodalLLM|MLLM]] family:

- **[[BLIP2|BLIP-2]]** — bridge is the [[QFormer|Q-Former]] + linear projection.
- **[[LLaVA15|LLaVA-v1.5]]** — bridge is a **2-layer MLP** (simpler than Q-Former).
- **[[Idefics2|Idefics 2]]** — yet another bridge ([[Mistral|Mistral 7B]] backbone, Laurençon et al. 2024).
- **[[2408.08849-ecg-chat|ECG-Chat]]** — extends the pattern to a **physiological-signal modality** (`ECG → 1d-ViT → MLP projector → Vicuna-13B`).

In every case, the bridge's output occupies the *"soft visual prompt"* slot.

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[SoftPrompt]] — the parent concept.
- [[QFormer]] — the Ch 9 bridge that produces the soft visual prompt.
- [[BLIP2]] — Ch 9's worked model.
- [[LLaVA15]] — sibling architecture; bridge is 2-layer MLP.
- [[Idefics2]] — sibling architecture.
- [[2408.08849-ecg-chat]] — the soft-modality-prompt pattern beyond images.
- [[VisionTransformer]] — the frozen feature-extractor side.
- [[MultimodalLLM]] — the architectural pattern the soft visual prompt underlies.
- [[PrefixTuning]] — gradient-based soft-prompting predecessor.
