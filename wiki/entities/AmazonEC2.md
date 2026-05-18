---
title: "Amazon EC2"
type: entity
tags: [aws, cloud, compute, gpu, infrastructure]
sources: [d2l-appendix-tools]
last_updated: 2026-05-16
---

# Amazon EC2 (Elastic Compute Cloud)

AWS's foundational on-demand virtual-machine service. In the [[d2l-appendix-tools|D2L appendix]] context, EC2 is the cheaper-but-more-work alternative to [[AmazonSageMaker]] for running the D2L book on cloud GPUs.

## GPU instance types covered in `d2l-appendix-tools` §`aws`

| Name | GPU | Notes |
|------|-----|-------|
| `g2` | Grid K520 | ancient |
| `p2` | Kepler K80 | old but often cheap as spot |
| `g3` | Maxwell M60 | good trade-off |
| `p3` | Volta V100 | high performance for FP16 |
| `p4` | Ampere A100 | high performance for large-scale training |
| `g4` | Turing T4 | inference optimized FP16 / INT8 |

`p2.xlarge` = 1 GPU; `p2.16xlarge` = 16 GPUs. Higher-GPU SKUs cost more both in $/hr and quota-request friction. D2L recommends `p2.xlarge` for the book's content.

## EC2-on-D2L runbook (`d2l-appendix-tools` §`aws`)

1. **Region selection** — choose a region near you (Oregon is the US default) that has the GPU instance type you want.
2. **Quota request** — by default new accounts cannot launch `p2`+ instances; submit "Request limit increase" and wait ~one business day.
3. **Launch instance** — pick an Ubuntu AMI, the GPU instance type, an SSH key pair (download `.pem` immediately — only chance), and bump default disk from 8 GB to **64 GB** (CUDA alone takes 4 GB).
4. **SSH in** — `chmod 400 D2L_key.pem && ssh -i "D2L_key.pem" ubuntu@ec2-xx-xxx-xxx-xxx.y.compute.amazonaws.com`.
5. **Install CUDA 12.1** — `apt-get update && apt-get install build-essential git libgfortran3` → fetch NVIDIA's `.deb` repo package → `dpkg -i` → `apt-get install cuda` → append `/usr/local/cuda-12.1/bin` to `PATH` + `lib64` to `LD_LIBRARY_PATH` in `~/.bashrc` → verify with `nvidia-smi`.
6. **Install D2L** — follow [[d2l-installation]]'s Linux runbook: [[Miniconda]] → `conda activate d2l` → `pip install` the framework wheel → `pip install d2l==1.0.3`.
7. **Run Jupyter remotely** — locally: `ssh -i "D2L_key.pem" ubuntu@... -L 8889:localhost:8888`; on the instance: `jupyter notebook`; open `http://localhost:8889/?token=...` in your local browser.

## Billing semantics

- **Stopping** an instance preserves disk + state and can be restarted later (billed for retained EBS storage only).
- **Terminating** an instance deletes everything; not recoverable.
- Best practice: take an **AMI snapshot** before terminating ("Image → Create" in the EC2 console) so a new instance can be launched from "My AMIs" with CUDA + Miniconda + `d2l` pre-installed.
- Spot instances exist as a cheaper alternative for fault-tolerant workloads.

## Position in the wiki

The on-prem-build-guide alternative is in §`selecting-servers-gpus` of the same chapter. EC2's role is the cloud counterpart: "launch and stop instances on demand without having to buy and build our own computer" ([[d2l-appendix-tools]] §`aws` summary).

## Connections

- [[Amazon]] — parent (AWS).
- [[AmazonSageMaker]] — sibling AWS service; managed-Jupyter alternative.
- [[GoogleColab]] — cross-cloud free-tier alternative.
- [[CUDA]] — installed manually on EC2 (preinstalled on SageMaker notebooks).
- [[Miniconda]] / [[D2LPackage]] — D2L install chain on the instance.
- [[NVIDIA]] — every supported GPU; CUDA is the API.
- [[GPU]] — what the `p2`/`p3`/`p4`/`g4` instance types deliver.
- [[d2l-appendix-tools]] — §`aws` runbook.
- [[d2l-installation]] — the install steps that run *inside* the EC2 instance after CUDA is set up.
