---
title: "Made With ML — Setup"
type: source
tags: [mlops, made-with-ml, setup, ray, anyscale]
date: 2026-05-15
source_file: raw/madewithml/mlops-setup.md
---

## Summary
The opening lesson of the Made With ML MLOps course sets up the development environment used throughout the curriculum, supporting both a local laptop workflow and a remote, autoscaling [[Anyscale]] cluster powered by [[Ray]]. It defines the cluster (environment + compute) via `cluster_env.yaml` and `cluster_compute.yaml`, launches an Anyscale Workspace with VSCode/JupyterLab, clones the [[MadeWithML]] GitHub repository, and initializes Ray inside a notebook to discover available CPU/GPU resources for downstream workloads.

## Key Claims
- A cluster is a group of servers consisting of one head node plus worker nodes that can be fixed-size or autoscale based on application demand.
- The course standardizes on Python 3.10 (via pyenv) and a `requirements.txt` for dependency installation, mirrored in Anyscale's `post_build_cmds`.
- Anyscale Workspaces provide an "infinite laptop" experience on top of cluster compute, environment, and persistent storage.
- Worker nodes can be configured with `min_workers=0` so GPUs only spin up when needed, sharply reducing compute costs without manual infra management.
- [[Ray]] is chosen as the distributed runtime because it is used by [[OpenAI]], Spotify, Netflix, Instacart, and Doordash for production ML workloads.
- Resource budgeting uses `ray.cluster_resources()`: locally, set `num_workers` a few less than total CPUs; on Anyscale, allocate per worker `{"CPU": 3, "GPU": 1}` for a g4dn.xlarge.
- New packages on Anyscale must be installed with `pip install --user` so head and worker nodes all receive them, then added to `requirements.txt` for future builds.

## Key Quotes
> "Workspaces allow us to use development tools such as VSCode, Jupyter notebooks, web terminal, etc. on top of our cluster compute, environment and storage. This create an 'infinite laptop' experience that feels like a local laptop experience but on a powerful, scalable cluster."

> "We'll be using Ray to scale and productionize our ML application. Ray consists of a core distributed runtime along with libraries for scaling ML workloads."

## Connections
- [[MadeWithML]] — the course/repo this lesson belongs to.
- [[GokuMohandas]] — author and instructor.
- [[Anyscale]] — managed Ray platform hosting the course's remote cluster.
- [[Ray]] — distributed runtime initialized in the notebook.
- [[MLOps]] — overarching discipline of the course.
- [[PythonLanguage]] — base language (3.10).
- [[Jupyter]] — interactive notebook environment used for development.
- [[VSCode]] — IDE used in Workspaces and locally.
- [[GitHub]] — repository host for the Made-With-ML codebase.
- [[ClusterAutoscaling]] — pattern for `min_workers=0` to `max_workers`.
- [[VirtualEnvironment]] — Python venv isolation pattern.
- [[GPUCompute]] — g4dn.xlarge worker provisioning.
- [[AWS]] — underlying cloud provider in the example cluster compute config.
- [[DistributedComputing]] — the broader paradigm Ray implements.

## Contradictions
- None identified; this is a tooling/setup lesson with no claims that conflict with existing wiki content.
