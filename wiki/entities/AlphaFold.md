---
title: "AlphaFold"
type: entity
tags: [model, biology, drug-discovery, googledeepmind]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# AlphaFold

[[googledeepmind|DeepMind]]'s protein-structure-prediction model — **one of the most famous [[DomainSpecificModel|domain-specific foundation models]] in existence**. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]]:

> "One of the most famous domain-specific models is perhaps DeepMind's AlphaFold, trained on the sequences and 3D structures of around 100,000 known proteins."

## Why it matters in the Ch 2 framing

AlphaFold is Huyen's anchor example of the **"domain data is unlikely to be on the public internet"** category. Protein sequence/structure data follows specific formats, is expensive to acquire (X-ray crystallography is hard), and is largely confined to scientific consortia — exactly the conditions where a general-purpose FM like [[gemini|Gemini]] or [[GPT4|GPT-4]] won't have meaningful coverage.

## What it does

AlphaFold predicts the **3D folded structure of a protein from its amino-acid sequence** — a problem of immense biological importance that was largely unsolved before 2020. AlphaFold 2 (CASP 2020) effectively closed the long-standing "protein folding problem" for the bulk of known protein structures.

## Position in the wiki

This wiki page is intentionally brief — AlphaFold is named in Ch 2 as an example, not analyzed in depth. Other AI-for-biology models named alongside it:
- [[BioNeMo]] ([[NVIDIA]]) — biomolecular data for drug discovery.
- [[MedPaLM2]] ([[google|Google]]) — medical QA.

## Connections
- [[DomainSpecificModel]] — the concept AlphaFold exemplifies.
- [[googledeepmind|Google DeepMind]] — the builder.
- [[BioNeMo]] / [[MedPaLM2]] — peer biomedical FMs named in Ch 2.
- [[FoundationModel]] — the broader category.
- [[ai-engineering-ch02-foundation-models]] — primary source.
