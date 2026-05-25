---
name: MLDeploymentMyths
title: "Four Myths of ML Deployment"
type: concept
tags: [deployment, mlops, common-mistakes]
sources: [dmls-ch07-model-deployment]
last_updated: 2026-05-23
---

# Four Myths of ML Deployment

The opening framing of [[ChipHuyen|Huyen]]'s [[dmls-ch07-model-deployment|DMLS Ch 7]] — four common misconceptions among teams approaching ML deployment for the first time.

## Myth 1: "You only deploy one or two ML models at a time."
Reality: production organizations run **hundreds** of models simultaneously. Per Algorithmia's 2021 enterprise ML survey, 41% of organizations with >25,000 employees run **more than 100** models. [[BookingCom|Booking.com]] had 150+ models in production (Bernardi et al. KDD 2019). [[Uber]] runs thousands. Build infrastructure for many models, not for one.

## Myth 2: "Model performance is stable after deployment."
Reality: ML systems decay over time due to [[DistributionShift|data distribution shift]] and [[SoftwareRot|software rot]]. Static post-deployment metrics are not the steady state — they're a snapshot of pre-decay. Per [[dmls-ch08-distribution-shifts-monitoring|DMLS Ch 8]], even without changes the data the model sees will drift.

## Myth 3: "You don't need to update your models that often."
Reality: high-cadence updates are standard. [[Weibo]] reports a 10-minute ML iteration cycle. [[AlibabaDAMOAcademy|Alibaba]] / [[ByteDance]] run continuous-learning loops. Industrial DevOps cadences are extreme: [[Etsy]] (50 deploys/day, 2015), [[Netflix]] (thousands/day), [[Amazon]] (every 11.7 seconds via SageMaker).

## Myth 4: "Most ML engineers don't need to worry about scale."
Reality: even research models in production routinely hit scale issues. [[Roblox]] runs [[bert|BERT]] on CPU for 1B+ daily inferences at <20ms latency. The scale-doesn't-matter assumption only holds for prototype-stage projects.

## Connections
- [[dmls-ch07-model-deployment]] — source chapter.
- [[BatchInference]] / [[OnlineInference]] / [[StreamingPrediction]] — the three prediction modes Ch 7 enumerates.
- [[ModelCompression]] / [[Quantization]] / [[KnowledgeDistillation]] — the production-scale fixes.
- [[ContinualLearning]] — the discipline response to Myth 3.
- [[DistributionShift]] / [[Monitoring]] — the discipline response to Myth 2.
- [[MLOps]] — the umbrella response to all four myths.
