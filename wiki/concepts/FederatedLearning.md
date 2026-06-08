---
title: "Federated Learning"
type: concept
tags: [distributed-training, privacy, model-merging]
sources: [ai-engineering-ch07-finetuning, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch14-ml-operations, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Federated Learning

A distributed-training paradigm where **multiple devices train the same model on their local data without centralizing the data**, then merge their model updates centrally. Originally introduced by [[McMahan2016FederatedAveraging|McMahan et al. (2016)]] for Google's mobile-Gboard work.

Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], federated learning is naturally framed as a **[[ModelMerging|model-merging]] operation**:

> "Model merging is one way to do federated learning (McMahan et al., 2016), in which multiple devices train the same model using separate data. For example, if you deploy model X to multiple devices, each copy of X can continue learning separately from the on-device data. After a while, you have multiple copies of X, all trained on different data. You can merge these copies together into one new base model that contains the learning of all constituent models."

## Why it matters

- **Privacy**: raw data never leaves the device. Required for HIPAA / GDPR / privacy-sensitive workloads.
- **Bandwidth**: ship model deltas, not training data — much smaller.
- **Personalization**: each device's model can adapt to its user's behavior.
- **Compute distribution**: training cost spreads across many edge devices.

## The base operation: [[LinearCombinationMerging|FedAvg]]

Federated Averaging — the canonical algorithm from McMahan et al. — is just **[[LinearCombinationMerging|linear combination merging]]** of the per-device model updates, weighted by the number of training examples per device. The whole framework Ch 7 builds around model merging applies directly.

## On-device finetuning fits federated learning

Per Ch 7: on-device deployment + multi-LoRA adapters + occasional merging back to a central base = the canonical modern federated-learning pipeline. [[Apple]]'s on-device AI work (2024) is the closest mainstream instance.

## Limitations

- **Aggregation can be slow** if devices are unreliable / sporadically online.
- **Adversarial devices** can poison the aggregate model.
- **Heterogeneous data distributions** across devices can make naive averaging unstable.

## Connections

- [[ModelMerging]] — federated learning is the multi-device application of merging.
- [[LinearCombinationMerging]] — the core operation (FedAvg).
- [[McMahan2016FederatedAveraging]] — the foundational paper.
- [[Apple]] — on-device finetuning + federated workflows.
- [[HybridML]] / [[EdgeML]] — [[mlsysbook-ch02-ml-systems|mlsysbook Ch 2]] lists federated/collaborative learning as a privacy-preserving extension of the hybrid integration menu, keeping data local to the edge.
- [[DiabeticRetinopathyScreening]] — [[mlsysbook-ch03-ml-workflow|Ch 3]] presents federated learning as a *constraint-driven* architectural choice forced by patient-privacy regulation (not a universal improvement): its trade-off is per-round communication cost plus non-IID convergence issues across clinic sites.
- [[ai-engineering-ch07-finetuning]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] — sources.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 cites federated learning as letting edge devices improve models without transmitting raw data (edge-cloud coordination).
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 frames FedAvg as "data minimization by architecture," but stresses it must be combined with [[DifferentialPrivacy|differential privacy]] because gradients still leak training data via reconstruction attacks (validated with [[MembershipInferenceAttack|membership inference]]).

