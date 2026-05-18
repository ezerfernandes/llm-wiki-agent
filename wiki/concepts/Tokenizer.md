---
title: "Tokenizer"
type: concept
tags: [nlp, preprocessing]
sources: [madewithml-transformers]
last_updated: 2026-05-15
---

# Tokenizer

The component that implements [[Tokenization]] — mapping strings to integer IDs and back. Must be versioned with the model to avoid [[TrainingServingSkew]]; common implementations include [[sentencepiece]] and [[wordpiece]].
