---
name: Dropbox
title: "Dropbox"
type: entity
tags: [company, cloud-storage, infrastructure]
sources: [dmls-ch10-infrastructure-mlops]
last_updated: 2026-05-23
---

# Dropbox

US file-storage and collaboration company. Cited in [[ChipHuyen|Huyen]]'s [[dmls-ch10-infrastructure-mlops|DMLS Ch 10]] as the **flagship [[CloudRepatriation|cloud-repatriation]] case study**: Dropbox migrated the bulk of its storage workload off [[AmazonS3]] onto its own data centers pre-IPO and reported **~$75M saved over the two years preceding the IPO** (S-1 filing, 2017).

## Why it matters in the wiki
[[ChipHuyen]] uses Dropbox as the canonical evidence that the standard "cloud is always cheaper" assumption breaks down at scale. As ML-training and -inference workloads grow, the same trade-off applies — large ML shops should expect repatriation pressure on bulky workloads (training-data storage, inference-cache footprints, archived experiment artifacts) even as elastic / spike workloads stay on cloud.

## Cited alongside
- [[a16z]]'s "The Cost of Cloud, a Trillion Dollar Paradox" (Sarah Wang, Martin Casado; May 2021) — estimated $100B of public market cap lost to cloud markup across 50 top public software companies.
- [[Gartner]] 81% multi-cloud statistic.

## Connections
- [[CloudRepatriation]] — the canonical case study.
- [[MultiCloud]] — related multi-cloud framing.
- [[CloudComputing]] / [[DataCenter]] — the architectural alternatives.
- [[MLPlatform]] — what the infrastructure ultimately hosts.
