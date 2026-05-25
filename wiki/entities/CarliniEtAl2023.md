---
title: "Carlini et al. 2023 — Extracting Training Data from Diffusion Models"
type: entity
tags: [paper, privacy, training-data, diffusion-models, copyright, llm-security]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Carlini et al. 2023 — Extracting Training Data from Diffusion Models

The paper that extended [[TrainingDataExtraction|training-data extraction]] from text models to **diffusion models**. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] for the result that >1,000 near-duplicate images can be extracted from [[StableDiffusion|Stable Diffusion]], many containing trademarked company logos.

## Headline result

The author concluded:

> "Diffusion models are much less private than prior generative models such as GANs, and... mitigating these vulnerabilities may require new advances in privacy-preserving training." — paraphrased in Ch 5

This extended the extraction-attack family to a new modality and made [[CopyrightRegurgitation|copyright regurgitation]] a documented (rather than theoretical) risk for image-generation models.

## Implication for [[StableDiffusion|Stable Diffusion]] (and similar models)

If commercial logos can be near-duplicated by an open-source diffusion model, the model is **leaking trademarked imagery** by construction — independent of any adversarial intent on the user's side. This is the same problem class as text [[CopyrightRegurgitation|copyright regurgitation]], with the same legal exposure for downstream applications.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[TrainingDataExtraction]] — the parent attack.
- [[CopyrightRegurgitation]] — what the extracted images often contain.
- [[StableDiffusion]] — the model studied.
- [[CarliniEtAl2020]] — same first author's earlier text-model work.
- [[InformationExtraction]] / [[PromptAttack]] — broader families.
