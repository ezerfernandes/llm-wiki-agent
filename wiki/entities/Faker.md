---
title: "Faker"
type: entity
tags: [library, python, data-synthesis]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Faker

**Python library that generates fake data — names, addresses, phone numbers, email addresses — for testing and template-based synthesis.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], Faker is the canonical example of a **rule-based random generator** that powers [[RuleBasedDataSynthesis|template-driven data synthesis]].

## Original use

> "Libraries like Faker and Chance let you generate data in simple formats such as names, addresses, phone numbers, and email addresses for testing."

## Ch 8 application

Faker (or similar) populates fields in a template like:

```
Transaction ID: [Unique Identifier]
Date: [MM/DD/YYYY]
Amount: [Transaction Amount]
Merchant Name: [Merchant/Store Name]
…
```

To generate synthetic transactions — used to bootstrap fraud-detection models when real transaction data is too sensitive for early development.

## Connections

- [[RuleBasedDataSynthesis]] — the technique Faker enables.
- [[DataSynthesis]] — parent category.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
