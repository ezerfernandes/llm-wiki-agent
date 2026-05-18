---
title: "Amazon SageMaker"
type: entity
tags: [aws, cloud, ml-platform, notebook, gpu]
sources: [d2l-appendix-tools]
last_updated: 2026-05-16
---

# Amazon SageMaker

AWS's fully-managed machine-learning platform; in the [[d2l-appendix-tools|D2L appendix]] context, the relevant surface is **SageMaker notebook instances** — managed GPU-enabled Jupyter environments preconfigured with CUDA + framework wheels, billed by uptime.

## D2L workflow (`d2l-appendix-tools` §`sagemaker`)

1. AWS console → "Amazon SageMaker" → "Notebook instance" → "Create notebook instance".
2. Choose an instance type. D2L's recommended baseline is **`ml.p3.2xlarge`** — one Tesla V100 + 8-core CPU + 61 GB RAM — *"powerful enough for most of the book"*.
3. Specify the framework-specific D2L GitHub repository URL so SageMaker clones the entire book onto the instance at provisioning time: `https://github.com/d2l-ai/d2l-pytorch-sagemaker` / `d2l-en-sagemaker` (MXNet) / `d2l-tensorflow-sagemaker`.
4. Click "Open Jupyter" → edit and run notebooks exactly as in §`jupyter`.
5. **Stop the instance** when finished — *"do not forget to stop the instance to avoid being charged further"*.

To pull upstream updates: open a terminal on the SageMaker instance, `cd SageMaker/d2l-pytorch-sagemaker/`, then `git reset --hard && git pull`.

## Position in the wiki

- The **fastest path to a GPU notebook** in the D2L appendix's three-cloud taxonomy:
  - SageMaker = fastest setup, highest cost (managed instance markup).
  - [[AmazonEC2|EC2]] = cheaper, more setup work (CUDA install, env setup, port forwarding).
  - [[GoogleColab]] = free-tier alternative for readers without an AWS account.
- The D2L appendix explicitly recommends SageMaker over raw EC2 *"if convenience matters more than cost"*.

## Connections

- [[Amazon]] — parent organization (AWS).
- [[AmazonEC2]] — sibling AWS service; cheaper alternative requiring manual setup.
- [[GoogleColab]] — cross-cloud alternative.
- [[Jupyter]] — what SageMaker notebook instances run.
- [[d2l-appendix-tools]] — §`sagemaker` first introduces it in this corpus.
- [[CUDA]] / [[GPU]] — preconfigured on every SageMaker notebook instance with a `p2`/`p3`/`p4`/`g4` instance type.
