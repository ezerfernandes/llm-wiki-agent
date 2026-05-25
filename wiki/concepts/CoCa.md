---
title: "CoCa"
type: concept
tags: [architecture, contrastive-learning, image-text, vision-language]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# CoCa — Contrastive Captioner

**Yu, Wang, Vasudevan, Yeung, Seyedhosseini & Wu (Google, 2022) — *"CoCa: Contrastive Captioners are Image-Text Foundation Models."*** A dual-objective vision-language pretraining architecture that combines (1) a **contrastive loss** between image and text encoders (CLIP/ALIGN-style) with (2) a **captioning loss** through a multimodal text decoder that cross-attends to the image encoder. The unifying claim is that one architecture can produce both **dual-encoder retrieval embeddings** and **encoder-decoder generation** with a single pretraining run — *"a combination of the two approaches"* (ALBEF + ALIGN + SimVLM).

Architecturally: image encoder → attentional pooling → contrastive head; image encoder → cross-attention → multimodal text decoder → captioning head. The **CLS token** of the text encoder serves as the contrastive embedding; the rest of the text encoder feeds the multimodal decoder.

## Adapted to ECG in [[2408.08849-ecg-chat]]

ECG-Chat directly adopts CoCa's dual-loss structure for ECG-text alignment, swapping the image encoder for a 12-layer **1d-ViT** [[ECGEncoder]] and the text encoder for **[[MedCPT]]**. Loss weights: $\lambda_{con}=1.0$, $\lambda_{cap}=2.0$. Without text-side augmentation, CoCa zero-shot R@1 on [[PTB-XL]] is **2.14**; with [[WaveformDataEnhancement|WDE]] it rises to **64.7** — a 30× jump that demonstrates CoCa generalizes to signal-text when the text side is enriched per-record.

## Connections
- [[2408.08849-ecg-chat]] — ECG-modality extension of CoCa with WDE.
- [[WaveformDataEnhancement]] — the augmentation trick that makes CoCa converge on highly-repetitive ECG report corpora.
- [[ECGEncoder]] — the 1d-ViT image-encoder analogue in ECG-Chat.
- [[ContrastiveLearning]] — the parent paradigm.
- [[MultimodalLLM]] — CoCa-pretrained encoders feed adapters into LLMs in the [[LLaVA15|LLaVA-v1.5]] style.
