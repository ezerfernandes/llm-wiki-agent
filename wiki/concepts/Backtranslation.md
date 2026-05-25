---
title: "Backtranslation"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

## Definition
Synthetic-data technique that fixes the answer first and asks an LLM to generate the matching instruction.

## In LLM Engineer's Handbook
Backtranslation fixes the answer first (e.g. a raw-text chunk) and asks an LLM to generate the matching instruction — the inverse of the normal direction. Originally from machine-translation. [[leh-ch05-supervised-fine-tuning]] uses backtranslation + rephrasing with GPT-4o-mini to mint the `mlabonne/llmtwin` instruction dataset from Decoding ML articles.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

[[ChipHuyen|Huyen]] in Ch 8 frames back-translation as a **verification mechanism** as well as a synthesis technique:

### Translation verification (the original sense)

> "Let's say the original English sentence is X and the translated Lao sentence is Y. You can use another model to translate the translation back into the original language, X', then compare X' with the original sentence X. If they are very different, the translation Y is likely bad."

The back-translation X → Y → X' lets you score Y without a parallel Y' gold standard — useful when the target language is low-resource.

### [[CodeBackTranslation|Code back-translation]] (Llama 3's clever variant)

Per Dubey et al. 2024:

1. Start with a code snippet.
2. AI generates explanation + documentation from the code.
3. AI regenerates code from the explanation.
4. Compare regenerated to original.
5. Only if faithful, keep the explanation + documentation for SFT.

This generated a large fraction of Llama 3's **2.7M synthetic coding examples**.

### Backtranslation as reverse-instruction (Ch 8)

The [[leh-ch05-supervised-fine-tuning|LEH]] use of "back-translation" — fix the answer, generate the instruction — is what Ch 8 generalizes as [[ReverseInstruction|reverse instruction]] (Köksal et al. 2023; Li et al. 2023; Chen et al. 2023).

So **"backtranslation" in Ch 8 covers three different operations** unified by "translate one direction and verify by going back":

1. Natural-language back-translation (X → Y → X').
2. Code back-translation (code → explanation → regenerated code).
3. Response → instruction reverse synthesis (where the "back-translation" is the response→instruction direction).
