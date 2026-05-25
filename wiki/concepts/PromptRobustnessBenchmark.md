---
title: "PromptRobust"
type: concept
tags: [benchmark, llm-security, adversarial, prompt-robustness]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# PromptRobust

**A benchmark for evaluating LLM robustness against adversarial prompt perturbations**, introduced by Zhu et al. 2023. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] alongside [[AdvBench]] as one of the canonical benchmarks for measuring how robust an LLM-backed system is against [[PromptAttack|prompt attacks]].

> "There are benchmarks that help you evaluate how robust a system is against adversarial attacks, such as AdvBench (Chen et al., 2022) and PromptRobust (Zhu et al., 2023)." — Ch 5

## Relation to PromptRobustness (the property)

PromptRobust (the *benchmark*) is the empirical operationalization of [[PromptRobustness|prompt robustness]] (the *property*) introduced earlier in Ch 5 — the property that a model's outputs do not change dramatically under small semantically-equivalent prompt perturbations. PromptRobust applies adversarial perturbations explicitly designed to elicit such changes.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptRobustness]] — the model-capability property this benchmark measures.
- [[AdvBench]] — sibling adversarial benchmark.
- [[JailbreakBench]] — related jailbreak-evaluation pool.
- [[AttackSuccessRate]] / [[ViolationRate]] — reporting metrics.
- [[PromptAttack]] — the attack class measured.
- [[LLMRedTeaming]] — the discipline this benchmark serves.
