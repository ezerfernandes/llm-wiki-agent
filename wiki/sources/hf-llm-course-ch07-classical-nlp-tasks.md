---
title: "HuggingFace LLM Course — Ch 7: Classical NLP tasks"
type: source
tags: [hf-llm-course, course, nlp, ner, mlm, translation, summarization, qa, causal-lm]
date: 2026-05-23
source_file: raw/hf-llm-course/ch07-classical-nlp-tasks.md
---

## Summary

Chapter 7 of the HuggingFace LLM Course is the "everything comes together" chapter: it walks through six end-to-end NLP task recipes — **token classification (NER)**, **masked language modeling**, **translation**, **summarization**, **training a causal LM from scratch**, and **extractive question answering** — each with both a `Trainer`/`Seq2SeqTrainer` path and a manual [[Accelerate]] training loop. Every recipe culminates in a model pushed to the [[HuggingFaceHub]] with an inference widget. The chapter introduces task-specific data collators ([[DataCollatorForTokenClassification]], [[DataCollatorForLanguageModeling]], [[DataCollatorForSeq2Seq]]) that handle the per-task subtleties around label padding (`-100` to ignore in loss), random masking, and seq2seq label shifting / `decoder_input_ids`. It introduces the right metric per task — **seqeval** for NER, **perplexity** for MLM, **SacreBLEU** for translation, **ROUGE** for summarization, and **SQuAD exact-match + F1** for QA — and shows the full data-processing tricks each task needs: word-id-aware label alignment for subword tokens in NER, concat-then-chunk for MLM, `text_target` for seq2seq labels, sliding-window chunking with `return_overflowing_tokens` for both code-CLM training and long-context QA, and span-extraction post-processing for QA. Section 8 closes with a short bridge from classical NLP to LLMs.

## Key Claims

- Token classification covers **NER**, **POS tagging**, and **chunking**, all formulated as one-label-per-token; CoNLL-2003 uses the BIO scheme with 9 classes (`O`, `B-/I-PER`, `B-/I-ORG`, `B-/I-LOC`, `B-/I-MISC`).
- Subword tokenization of pre-tokenized inputs creates a label-token mismatch; use `tokenizer(..., is_split_into_words=True)` plus `inputs.word_ids()` (fast-tokenizer feature) to align labels, with special tokens labeled `-100` (the default ignored index for cross-entropy).
- For continuation subtokens of a `B-XXX` entity, flip the label to `I-XXX` (i.e., `label += 1` if `label % 2 == 1`).
- `DataCollatorForTokenClassification` pads **labels** (not just inputs) with `-100` so the loss ignores padding positions.
- NER evaluation uses the **seqeval** library loaded via `evaluate.load("seqeval")`; it expects string labels per token and returns per-entity P/R/F1 plus overall scores.
- Setting a wrong `num_labels` causes obscure "CUDA error: device-side assert triggered" failures at `Trainer.train()` time — verify `model.config.num_labels` matches the dataset.
- Fine-tuning a language model on in-domain data before fine-tuning a task head is **domain adaptation**; popularized by [[ULMFiT]] (2018, LSTM-based).
- [[DistilBERT]] (~67M params) is roughly 2× smaller and 2× faster than [[BERT]] base (~110M) with similar downstream quality, trained via [[KnowledgeDistillation]].
- For both masked and causal LM, the standard preprocessing is to **concatenate all tokenized examples** and split into equal `chunk_size` chunks (drop or pad the tail) — preserving information from documents longer than the context window.
- `DataCollatorForLanguageModeling(mlm_probability=0.15)` performs the canonical BERT-style random masking on the fly per batch; `mlm=False` switches the same collator to causal-LM mode where labels equal `input_ids`.
- **Whole-word masking** masks all subtokens of a randomly-selected word together; requires a custom collator that uses precomputed `word_ids`.
- **Perplexity** is defined as `exp(cross_entropy_loss)`; lower is better; reported here as 21.75 → 11.32 after domain adaptation on IMDb.
- For reproducible eval perplexity, apply masking **once** to the test set instead of via the on-the-fly collator (eliminates per-run noise).
- Translation is a sequence-to-sequence task; Marian `Helsinki-NLP/opus-mt-en-fr` was pretrained on the [[Opus]] corpus and is fine-tuned on the [[KDE4]] dataset (210k EN/FR pairs).
- The tokenizer's `text_target=` argument tokenizes labels with the **target-language vocabulary**; forgetting it produces gibberish over-tokenization of foreign words.
- [[DataCollatorForSeq2Seq]] is special: it needs the `model` argument because it builds `decoder_input_ids` by **right-shifting labels** with a model-specific start token; padded label positions use `-100` for loss masking.
- **BLEU** (Papineni 2002) measures n-gram overlap with reference translations, with brevity and repetition penalties; weakness: expects pre-tokenized text. **[[SacreBLEU]]** standardizes tokenization for cross-model comparability.
- `predict_with_generate=True` in `Seq2SeqTrainingArguments` makes evaluation use autoregressive `generate()` instead of teacher-forced argmax — critical for honest BLEU/ROUGE.
- Marian baseline BLEU on KDE4 EN→FR: 39.27 → 52.94 after 3 epochs (14-point improvement); Accelerate variant reaches BLEU 54.44.
- Summarization with **[[mT5]]-small** (multilingual T5) on the Multilingual Amazon Reviews corpus: use review titles as targets, filter titles > 2 words to avoid degenerate single-word labels.
- For summarization, beats a **lead-3 baseline** (first three sentences via `nltk.sent_tokenize`) — baseline ROUGE-1/2/L/Lsum = 16.74 / 8.83 / 15.6 / 15.96 on validation.
- **ROUGE** variants: `rouge1` (unigram overlap), `rouge2` (bigram), `rougeL` (longest common subsequence per sentence), `rougeLsum` (LCS over the whole summary); the metric returns confidence intervals (`low`/`mid`/`high`) for P/R/F1.
- ROUGE expects each generated/reference summary to have sentence boundaries marked by **newlines**; use `nltk.sent_tokenize` on decoded predictions before computing.
- Encoder-decoder models (T5, mT5, BART, mBART-50, PEGASUS) dominate summarization; GPT-2 can do few-shot summarization by appending "TL;DR".
- Training a causal LM **from scratch** (GPT-2 architecture, randomly initialized) makes sense when training data differs strongly from existing pretrained corpora — e.g., DNA, musical notes, or programming languages.
- The [[CodeParrot]] dataset (180 GB of Python from GitHub) is filtered for `pandas`/`sklearn`/`matplotlib`/`seaborn` via streaming, yielding ~3% (~6 GB, 600k scripts).
- Use `return_overflowing_tokens=True` + `return_length=True` to chunk long source files into fixed-context-length training examples (here 128); drop chunks smaller than `context_length`.
- A scaled-down GPT-2 with 124.2M parameters trained on ~2.1B tokens (vs GPT-3 300B, Codex 100B) is sufficient for simple Python autocomplete.
- A **custom keytoken-weighted loss** can bias training toward samples containing target API tokens (`plt`, `pd`, `sk`, `fit`, `predict`) without throwing away the rest.
- Extractive QA frames the task as predicting `start_position` and `end_position` token indices within a `[CLS] question [SEP] context [SEP]` input; labels `(0, 0)` mean "answer not in this chunk."
- Long [[SQuAD]] contexts are handled via a sliding window (`max_length=384`, `stride=128`, `truncation="only_second"`, `return_overflowing_tokens=True`), turning 87,599 examples into ~88,729 features.
- QA post-processing scores `(start, end)` pairs by `start_logit + end_logit` (sum, not product — equivalent to logarithms of probabilities and skips the softmax), filtering to top-`n_best=20` indices and `max_answer_length=30`.
- For QA validation features, **null out offsets for question tokens** (`offset_mapping[k] = None where sequence_ids[k] != 1`) so post-processing can't accidentally pick spans from the question.
- BERT fine-tuned on SQuAD reaches exact_match 81.18 / F1 88.67, matching the BERT paper's reported 80.8 / 88.5.
- Across all six tasks, the recipe ends the same way: `push_to_hub` (with `tags=` to pick the right widget on the Hub), then re-use via `pipeline(<task>, model=<checkpoint>)`.

## Key Quotes

> "The first rule we'll apply is that special tokens get a label of `-100`. This is because by default `-100` is an index that is ignored in the loss function we will use (cross entropy). Then, each token gets the same label as the token that started the word it's inside … For tokens inside a word but not at the beginning, we replace the `B-` with `I-`." — Section 2

> "By fine-tuning the language model on in-domain data you can boost the performance of many downstream tasks, which means you usually only have to do this step once! This process of fine-tuning a pretrained language model on in-domain data is usually called *domain adaptation*." — Section 3

> "There are various mathematical definitions of perplexity, but the one we'll use defines it as the exponential of the cross-entropy loss." — Section 3

> "If you forget to indicate that you are tokenizing labels, they will be tokenized by the input tokenizer, which in the case of a Marian model is not going to go well at all." — Section 4

> "The traditional metric used for translation is the BLEU score … One weakness with BLEU is that it expects the text to already be tokenized, which makes it difficult to compare scores between models that use different tokenizers. So instead, the most commonly used metric for benchmarking translation models today is SacreBLEU, which addresses this weakness (and others) by standardizing the tokenization step." — Section 4

> "For ROUGE, recall measures how much of the reference summary is captured by the generated one. … `rougeL` and `rougeLsum` measure the longest matching sequences of words by looking for the longest common substrings in the generated and reference summaries." — Section 5

> "Examples where it can make sense to train a new model include for datasets consisting of musical notes, molecular sequences such as DNA, or programming languages." — Section 6

> "Note that `DataCollatorForLanguageModeling` supports both masked language modeling (MLM) and causal language modeling (CLM). By default it prepares data for MLM, but we can switch to CLM by setting the argument `mlm=False`." — Section 6

> "Encoder-only models like BERT tend to be great at extracting answers to factoid questions … but fare poorly when given open-ended questions … In these more challenging cases, encoder-decoder models like T5 and BART are typically used to synthesize the information." — Section 7

> "Here we will change this process slightly because we don't need to compute actual scores (just the predicted answer). This means we can skip the softmax step. To go faster, we also won't score all the possible `(start_token, end_token)` pairs, but only the ones corresponding to the highest `n_best` logits … with `start_logit + end_logit` (instead of the product, because of the rule `log(ab) = log(a) + log(b)`)." — Section 7

## Code & Patterns

### NER label alignment for subword tokens

```python
def align_labels_with_tokens(labels, word_ids):
    new_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            current_word = word_id
            label = -100 if word_id is None else labels[word_id]
            new_labels.append(label)
        elif word_id is None:
            new_labels.append(-100)
        else:
            label = labels[word_id]
            if label % 2 == 1:  # B-XXX -> I-XXX
                label += 1
            new_labels.append(label)
    return new_labels
```

### MLM concat-and-chunk

```python
def group_texts(examples):
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    total_length = (total_length // chunk_size) * chunk_size
    result = {
        k: [t[i : i + chunk_size] for i in range(0, total_length, chunk_size)]
        for k, t in concatenated_examples.items()
    }
    result["labels"] = result["input_ids"].copy()
    return result

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm_probability=0.15)
```

### Whole-word masking collator

```python
mask = np.random.binomial(1, wwm_probability, (len(mapping),))
for word_id in np.where(mask)[0]:
    for idx in mapping[word_id]:
        new_labels[idx] = labels[idx]
        input_ids[idx] = tokenizer.mask_token_id
```

### Seq2seq tokenization with text_target

```python
def preprocess_function(examples):
    inputs = [ex["en"] for ex in examples["translation"]]
    targets = [ex["fr"] for ex in examples["translation"]]
    return tokenizer(inputs, text_target=targets,
                     max_length=128, truncation=True)

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
# batch keys: input_ids, attention_mask, labels (-100 padded), decoder_input_ids (right-shifted)
```

### SacreBLEU / ROUGE compute pattern

```python
# SacreBLEU expects references as list-of-lists
metric = evaluate.load("sacrebleu")
metric.compute(predictions=[pred], references=[[ref1, ref2]])

# ROUGE expects newline-separated sentences
decoded_preds  = ["\n".join(sent_tokenize(p.strip())) for p in decoded_preds]
decoded_labels = ["\n".join(sent_tokenize(l.strip())) for l in decoded_labels]
result = rouge_score.compute(predictions=decoded_preds,
                             references=decoded_labels, use_stemmer=True)
result = {k: v.mid.fmeasure * 100 for k, v in result.items()}
```

### Causal LM: chunk-by-overflow + init-from-config

```python
outputs = tokenizer(element["content"], truncation=True,
                    max_length=context_length,
                    return_overflowing_tokens=True,
                    return_length=True)
# Keep only chunks of full context_length

config = AutoConfig.from_pretrained("gpt2",
    vocab_size=len(tokenizer), n_ctx=context_length,
    bos_token_id=tokenizer.bos_token_id, eos_token_id=tokenizer.eos_token_id)
model = GPT2LMHeadModel(config)  # 124.2M params, random init

tokenizer.pad_token = tokenizer.eos_token
data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)
```

### Keytoken-weighted loss

```python
def keytoken_weighted_loss(inputs, logits, keytoken_ids, alpha=1.0):
    shift_labels = inputs[..., 1:].contiguous()
    shift_logits = logits[..., :-1, :].contiguous()
    loss_per_sample = CrossEntropyLoss(reduction="none")(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1)
    ).view(shift_logits.size(0), shift_logits.size(1)).mean(axis=1)
    weights = torch.stack([(inputs == kt).float() for kt in keytoken_ids]).sum((0, 2))
    weights = alpha * (1.0 + weights)
    return (loss_per_sample * weights).mean()
```

### QA sliding-window training labels

```python
inputs = tokenizer(
    questions, examples["context"],
    max_length=384, truncation="only_second",
    stride=128,
    return_overflowing_tokens=True,
    return_offsets_mapping=True,
    padding="max_length",
)
# Use sequence_ids() to find context boundaries, offset_mapping to map answer
# characters -> token indices; (0,0) if answer not in chunk.
```

### QA span extraction post-processing

```python
n_best = 20
max_answer_length = 30

start_indexes = np.argsort(start_logit)[-1 : -n_best - 1 : -1].tolist()
end_indexes   = np.argsort(end_logit)[-1 : -n_best - 1 : -1].tolist()
for s in start_indexes:
    for e in end_indexes:
        if offsets[s] is None or offsets[e] is None: continue
        if e < s or e - s + 1 > max_answer_length: continue
        answers.append({
            "text": context[offsets[s][0] : offsets[e][1]],
            "logit_score": start_logit[s] + end_logit[e],
        })
best = max(answers, key=lambda x: x["logit_score"])
```

### Accelerate evaluation gather pattern (recurring across sections)

```python
predictions = accelerator.pad_across_processes(predictions, dim=1, pad_index=-100)
labels      = accelerator.pad_across_processes(labels, dim=1, pad_index=-100)
predictions_gathered = accelerator.gather(predictions)
labels_gathered      = accelerator.gather(labels)
```

## Connections

- [[HuggingFaceTransformers]] — provides the `Trainer`/`Seq2SeqTrainer`, all `AutoModelFor*` heads, `pipeline`, and the per-task data collators used throughout.
- [[Accelerate]] — `Accelerator.prepare`, `accelerator.gather`, `pad_across_processes`, `unwrap_model().generate()`; the alternative path to `Trainer` shown in every section.
- [[Datasets]] / [[HuggingFaceHub]] — `load_dataset`, `Dataset.map`, `train_test_split`, `push_to_hub`; foundation built in Chapter 5.
- [[FastTokenizers]] — `word_ids()`, `sequence_ids()`, `offset_mapping`, `return_overflowing_tokens` — all rely on the Rust-backed fast tokenizers from Chapter 6.
- [[FineTuning]] / [[FineTuningBert]] — extends Chapter 3 by adding task-specific heads and metrics.
- [[NER]] — section 2 is the canonical NER recipe.
- [[POSTagging]] / [[Chunking]] — also covered conceptually as token-classification variants.
- [[BIO]] / [[IOBTagging]] — the BIO label scheme used by CoNLL-2003.
- [[CoNLL2003]] — dataset for NER.
- [[seqeval]] — evaluation library for sequence labeling.
- [[MaskedLanguageModeling]] — section 3 is the canonical MLM recipe.
- [[DistilBERT]] — student model used in section 3.
- [[KnowledgeDistillation]] — training procedure behind DistilBERT.
- [[ULMFiT]] — historical precedent for domain adaptation.
- [[DomainAdaptation]] — central concept of section 3.
- [[Perplexity]] — evaluation metric for language models.
- [[WholeWordMasking]] — variant masking strategy.
- [[IMDb]] — dataset used for MLM domain adaptation.
- [[Seq2Seq]] / [[EncoderDecoder]] — architecture family covering translation and summarization.
- [[Translation]] — section 4 is the canonical translation recipe.
- [[Marian]] / [[OpusMT]] — pretrained models used in section 4.
- [[KDE4]] — dataset for fine-tuning EN→FR.
- [[Opus]] — multilingual corpus underlying Marian/OpusMT pretraining.
- [[mBART]] / [[M2M100]] — multilingual seq2seq alternatives mentioned.
- [[BLEU]] — n-gram overlap metric for translation.
- [[SacreBLEU]] — standardized BLEU implementation.
- [[Summarization]] — section 5 is the canonical summarization recipe.
- [[T5]] / [[mT5]] — text-to-text Transformer used in section 5.
- [[BART]] / [[mBART50]] / [[PEGASUS]] — alternative summarization models.
- [[SentencePiece]] / [[Unigram]] — tokenization scheme used by mT5.
- [[ROUGE]] — overlap metric family for summarization.
- [[AmazonReviewsMulti]] — bilingual dataset used in section 5.
- [[NLTK]] — provides `sent_tokenize` for ROUGE-friendly post-processing.
- [[CausalLanguageModeling]] / [[GPT2]] — section 6 trains a from-scratch GPT-2.
- [[CodeParrot]] — Python source code dataset filtered in section 6.
- [[CodeGeneration]] / [[Codex]] / [[GitHubCopilot]] — application context for section 6.
- [[GradientAccumulation]] — used to reach effective batch size 256 in section 6.
- [[CosineLRSchedule]] — learning rate schedule used in section 6.
- [[GradientClipping]] — used in the Accelerate loop.
- [[QuestionAnswering]] / [[ExtractiveQA]] / [[SpanExtraction]] — section 7 is the canonical extractive QA recipe.
- [[SQuAD]] — dataset for QA fine-tuning.
- [[ELI5]] — generative-QA contrast mentioned in the tip box.
- [[ExactMatch]] / [[F1Score]] — metrics for QA evaluation.
- [[SlidingWindow]] — chunking strategy shared by section 6 (long Python files) and section 7 (long contexts).
- [[LargeLanguageModel]] — section 8 explicitly bridges the chapter's classical-NLP foundations to modern LLMs.
- [[ChainOfThought]] — referenced in section 8 as an LLM capability that builds on these foundations.
- [[ModelHub]] / [[PushToHubCallback]] — every section ends with a push-to-Hub step.
- [[Pipeline]] — used to demo each fine-tuned model.

## Contradictions

- No direct contradictions with existing wiki pages identified. One subtle nuance worth flagging: section 7 shows that scoring `(start, end)` spans via `start_logit + end_logit` (a **sum**) is equivalent to the product of softmax probabilities only because softmax is monotonic across a fixed denominator — earlier Chapter 6 prose described the QA pipeline as "taking the product of the corresponding two probabilities," which is true after softmax but the implementation here skips softmax entirely. Not a contradiction, but the log-sum trick is a useful clarification when comparing QA recipes across sources.
- Whole-word-masking improvement is left as an exercise — the chapter never asserts it definitively beats vanilla MLM, only that it's "one technique that can be used"; existing wiki pages that claim WWM is unambiguously better should be checked against this hedge.
