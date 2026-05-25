---
title: "Banking77"
type: entity
tags: [dataset, classification, intent-classification, banking, polyai, benchmark]
sources: [dspy-optimizers, dspy-tutorial-classification-finetuning]
last_updated: 2026-05-24
---

# Banking77

**Banking77** is a **fine-grained intent-classification dataset** of customer service queries from a banking domain, published by [[PolyAI]] on [[HuggingFace]] as `PolyAI/banking77`. The dataset's defining property is **77 distinct intent categories** in a single closed-set classification task — significantly more granular than the typical 5-10 intent slots in earlier conversational AI benchmarks.

The dataset is the **canonical fine-grained intent-classification benchmark in the DSPy tutorial corpus** — the only dataset on which the wiki has two independent end-to-end `dspy.BootstrapFinetune` receipts.

## Intent Categories

The 77 labels span the operational breadth of retail banking customer service. The first ten classes (in `features['label'].names` order) are:

```
activate_my_card
age_limit
apple_pay_or_google_pay
atm_support
automatic_top_up
balance_not_updated_after_bank_transfer
balance_not_updated_after_cheque_or_cash_deposit
beneficiary_not_allowed
cancel_transfer
card_about_to_expire
```

The label space includes routine product questions (`apple_pay_or_google_pay`, `visa_or_mastercard`, `fiat_currency_support`), state queries (`pending_card_payment`, `pending_cash_withdrawal`, `pending_top_up`, `pending_transfer`), failure-mode reports (`card_not_working`, `contactless_not_working`, `top_up_failed`, `declined_card_payment`, `declined_cash_withdrawal`, `declined_transfer`, `failed_transfer`), identity/verification flows (`verify_my_identity`, `verify_source_of_funds`, `verify_top_up`, `why_verify_identity`, `unable_to_verify_identity`), and edge cases (`lost_or_stolen_card`, `lost_or_stolen_phone`, `card_swallowed`, `compromised_card`, `wrong_amount_of_cash_received`, `wrong_exchange_rate_for_cash_withdrawal`). The closed set is large enough that **a 77-way `Literal[...]`-typed [[DSPySignatures|DSPy Signature]] output** is the standard wiki shape.

## Wiki Receipts

| Source | Task shape | Substrate | Result |
|---|---|---|---|
| [[dspy-optimizers]] (page 13 receipt) | `text, hint -> label` with `Literal[tuple(CLASSES)]` + `with_updated_fields` (2000 examples, hint-as-input training trick) | API self-distillation: GPT-4o-mini → fine-tuned GPT-4o-mini via OpenAI fine-tuning API | **66% → 87%** (+21 pts) |
| [[dspy-tutorial-classification-finetuning]] | `f"text -> label: Literal{CLASSES}"` inline string-form (500 examples per stage, no hint) | Cross-model open-weights distillation: GPT-4o-mini teacher → fine-tuned local Llama-3.2-1B student via [[HuggingFaceTRL|TRL]]+[[HuggingFacePEFT|PEFT]]; inference via [[SGLang]] `LocalProvider` | **51.5% no-metric / 55% teacher → 86.7%** (+31.7 pts vs teacher) |

**Both receipts converge on ~87% post-BFT within 0.3 points** despite radically different inference and fine-tuning substrates — concrete evidence that [[BootstrapFinetune]]'s metric-filter mechanism dominates the substrate choice on closed-set classification.

## Loading

```python
from datasets import load_dataset
from dspy.datasets import DataLoader
import dspy

CLASSES = load_dataset("PolyAI/banking77", split="train",
                       trust_remote_code=True).features['label'].names
kwargs = dict(fields=("text", "label"), input_keys=("text",),
              split="train", trust_remote_code=True)
raw_data = [
    dspy.Example(x, label=CLASSES[x.label]).with_inputs("text")
    for x in DataLoader().from_huggingface(dataset_name="PolyAI/banking77",
                                           **kwargs)[:1000]
]
```

The `trust_remote_code=True` flag is required because Banking77 ships dataset-specific loading logic on the [[HuggingFace]] Hub.

## Connections

- [[PolyAI]] — publisher.
- [[HuggingFace]] — hosting platform (`PolyAI/banking77`).
- [[Classification]] — task family.
- [[IntentClassifier]] — task type (intent classification is the discriminative-NLP task family Banking77 belongs to).
- [[BootstrapFinetune]] — the only DSPy optimizer with worked Banking77 receipts in the wiki; both receipts converge on ~87%.
- [[DSPySignatures]] — the canonical Banking77 Signature uses `Literal[CLASSES]` typed-output to constrain the model to the 77-way closed set.
- [[chainofthought|`dspy.ChainOfThought`]] — the canonical module wrapper for Banking77 in DSPy (both wiki receipts use CoT).
- [[dspy-optimizers]] / [[dspy-tutorial-classification-finetuning]] — the two wiki source pages with end-to-end Banking77 receipts.
- [[FineTuning]] — Banking77 is the wiki's canonical *closed-set classification* fine-tuning target.
- [[KnowledgeDistillation]] — the [[dspy-tutorial-classification-finetuning|classification fine-tuning tutorial]] uses Banking77 to demonstrate inverted distillation (student strictly outperforms teacher).
- [[Llama|Llama-3.2-1B-Instruct]] — the open-weights student model in [[dspy-tutorial-classification-finetuning]].
- [[GPT|GPT-4o-mini]] — the teacher in [[dspy-tutorial-classification-finetuning]]; both teacher and student in [[dspy-optimizers]]'s self-distillation receipt.
