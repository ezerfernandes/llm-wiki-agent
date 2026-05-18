---
title: "OpenMP Work-Sharing Constructs"
type: concept
tags: [openmp, parallel-computing, pragma, work-sharing]
sources: [parproc-ch04-introduction-to-openmp]
last_updated: 2026-05-17
---

# OpenMP Work-Sharing Constructs

**Work-sharing** is the [[OpenMP]] umbrella term for directives that distribute work units across the threads of an *already-spawned* team. Distinct from [[ParallelPragma|`#pragma omp parallel`]], which **creates** the team; work-sharing constructs **divide** the team's work.

The four canonical work-sharing constructs ([[parproc-ch04-introduction-to-openmp]] §4.3 / §4.5 / §4.7):

| construct | unit of work | distribution |
|---|---|---|
| [[ParallelFor|`for`]] | iterations of a `for` loop | chunked per [[ScheduleClause|schedule]] |
| `sections` / `section` | named code blocks | one section per thread |
| [[OpenMPSingle|`single`]] | one block | exactly one thread |
| [[OpenMPTaskDirective|`task`]] | arbitrary code block | added to a task queue, picked up by any free thread |

All four have an implicit barrier at the closing `}` (which can be overridden with `nowait`).

## Combined work-sharing constructs

Because every work-sharing construct must live inside a `parallel` block, [[OpenMP]] offers convenience forms that merge team-spawning + work-distribution:

- `#pragma omp parallel for` — spawn team **and** distribute the immediately-following loop.
- `#pragma omp parallel sections` — spawn team **and** distribute the immediately-following sections.

[[parproc-ch04-introduction-to-openmp]] §4.7: *"As a shortcut, we can combine the two pragmas."*

## Reduction and schedule interplay

Both `for` and `sections` accept the [[ReductionClause|`reduction`]] clause; `for` additionally accepts the [[ScheduleClause|`schedule`]] clause for iteration-to-thread mapping.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.3 / §4.7 source.
- [[ParallelPragma]] — team-spawner; required outer scope.
- [[ParallelFor]] — the loop work-sharing construct.
- [[OpenMPSingle]] — the one-thread variant.
- [[OpenMPTaskDirective]] — task-queue work-sharing for non-loop, non-section structures.
- [[ScheduleClause]] / [[ReductionClause]] — clauses commonly attached to work-sharing constructs.
- [[Barrier]] — implicit at the end of every work-sharing block.
