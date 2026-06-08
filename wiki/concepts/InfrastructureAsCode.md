---
title: "Infrastructure as Code"
type: concept
tags: [mlops, infrastructure, automation, operations]
sources: [mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Infrastructure as Code (IaC)

The practice of treating infrastructure configuration as software — version-controlled, reviewed, tested, and automatically executed — rather than manually configured through GUIs or ad hoc CLI commands. IaC brings software-engineering discipline to resource management: changes are tracked, configurations tested before deployment, and environments reproduced reliably.

[[mlsysbook-ch14-ml-operations]] motivates IaC via failures it prevents: a model failing because someone manually provisioned a different GPU type; quotas set via a Slack message six months ago. Tools: [[Terraform]], AWS CloudFormation, Ansible. IaC spans the full ML lifecycle (training compute allocation, distributed storage, container clusters) and integrates with [[CICD]] pipelines, paired with containerization ([[Docker]]) and orchestration ([[Kubernetes]]) plus [[Autoscaling|autoscaling]]. It is a hallmark of the **Scalable** tier of [[OperationalMaturity|operational maturity]].

## Connections
- [[Terraform]] — the most-cited IaC tool in MLOps.
- [[Kubernetes]] / [[Docker]] / [[Autoscaling]] — the orchestration and scaling layer IaC provisions.
- [[CICD]] — IaC integrates into CI/CD for consistent environments.
- [[OperationalMaturity]] — IaC marks the scalable maturity tier.
- [[MLOps]] — resource-management practice.
- [[mlsysbook-ch14-ml-operations]] — source chapter.
