---
title: "Rule-Based Data Synthesis"
type: concept
tags: [dataset-engineering, synthetic-data, templates]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Rule-Based Data Synthesis

**The traditional approach to [[DataSynthesis|data synthesis]]: predefined rules and templates with values populated by random generators.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], rule-based synthesis predates AI-powered synthesis by decades — it's been used in software testing (the [[Faker]] / Chance libraries) and gaming (procedural generation) long before deep-learning training data became a use case.

## How it works

Start with a template; fill its fields with a generator:

```
Transaction ID: [Unique Identifier]
Date: [MM/DD/YYYY]
Time: [HH:MM:SS]
Amount: [Transaction Amount]
Merchant Name: [Merchant/Store Name]
Merchant Category: [Category Code]
Location: [City, State, Country]
Payment Method: [Credit Card/Debit Card/Cash/Online Payment]
Transaction Status: [Completed/Pending/Failed]
Description: [Transaction Description]
```

A random generator (e.g., [[Faker]]) populates each field. Output: a synthetic transaction usable for training a fraud detector.

## Common use cases

- **Document structures with fixed format** — invoices, resumes, tax forms, bank statements, contracts, configuration files.
- **Grammar / syntax-driven content** — regular expressions, math equations.
- **Image augmentation** — random rotation, crop, scale, erase. [[AlexNet]] (Krizhevsky et al. 2012) credited this technique for its [[ImageNet]] win.
- **Text augmentation** — synonym replacement, gender-token swaps (bias mitigation).

## The most impressive rule-based-synthesis result

[[DeepMind|DeepMind]]'s [[AlphaGeometry]] (Trinh et al. 2024) trained on **100 million synthetic Olympiad-level geometry examples**, generated entirely procedurally from a small set of axioms. The result was Olympiad-level performance — without any human-annotated geometry data.

## Bias-mitigation augmentation (Ch 8 Table 8-2)

Procedural rewriting to balance gender / racial / family-role distributions:

| Original | Augmented |
|---|---|
| She's a fantastic nurse. | He's a fantastic nurse. |
| She's a fantastic nurse. | She's a fantastic doctor. |
| The CEO of the firm, Mr. Alex Wang, … | The CEO of the firm, Ms. Alexa Wang, … |
| Today, my mom made a casserole for dinner. | Today, my dad made a casserole for dinner. |
| Emily has always loved the violin. | Mohammed has always loved the violin. |

Replacement candidates come from a synonym dictionary or from embedding-space nearest neighbors.

## Limitations

- Templates can't express complex semantic dependencies.
- Coverage is limited to what the templates explicitly enumerate.
- Quality depends on the rule designer's domain expertise — exactly what [[AIPoweredDataSynthesis|AI-powered synthesis]] was invented to bypass.

## Connections

- [[DataSynthesis]] — parent concept.
- [[Simulation]] / [[AIPoweredDataSynthesis]] — the other two synthesis approaches.
- [[DataAugmentation]] — adjacent CV/NLP technique.
- [[Faker]] — the canonical Python rule-based generator.
- [[AlphaGeometry]] — the headline rule-based synthesis success.
- [[Perturbation]] — a sub-technique (rule-based noise injection).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
