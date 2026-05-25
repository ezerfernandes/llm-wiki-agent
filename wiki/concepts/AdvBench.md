---
title: "AdvBench"
type: concept
tags: [benchmark, llm-security, adversarial, jailbreak]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# AdvBench

**A benchmark for evaluating LLM robustness against adversarial attacks**, introduced by Chen et al. 2022. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as one of the canonical benchmarks for measuring how robust an LLM-backed system is against [[PromptAttack|prompt attacks]].

> "There are benchmarks that help you evaluate how robust a system is against adversarial attacks, such as AdvBench (Chen et al., 2022) and PromptRobust (Zhu et al., 2023)." — Ch 5

## Role in the defense ecosystem

AdvBench is part of the **reporting layer** of [[LLMRedTeaming|LLM red teaming]] — alongside its sibling [[PromptRobustnessBenchmark|PromptRobust]], it provides a standardized adversarial-prompt pool so different models and different defense configurations can be compared on a common axis. Reported scores typically use the [[AttackSuccessRate|ASR]] / [[ViolationRate|violation rate]] metric family.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[PromptRobustnessBenchmark]] — sibling benchmark (Zhu et al. 2023).
- [[JailbreakBench]] — related jailbreak-evaluation pool.
- [[AttackSuccessRate]] / [[ViolationRate]] — reporting metrics.
- [[Jailbreak]] / [[PromptAttack]] — the attack class measured.
- [[LLMRedTeaming]] — the discipline this benchmark serves.
