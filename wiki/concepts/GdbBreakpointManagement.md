---
title: "GDB Breakpoint Management (`enable` / `disable` / `delete` / `clear` / `ignore` / `condition`)"
type: concept
tags: [debugging, gdb, breakpoint, debugging-primitive]
sources: [dis-3-2-gdb-commands]
last_updated: 2026-05-17
---

# GDB Breakpoint Management

After [[Breakpoint|`break <loc>`]] creates a numbered breakpoint, [[GDB]] supplies a small command family that **manipulates** the resulting breakpoint without re-setting it. [[dis-3-2-gdb-commands|DIS Ch 3.2]] codifies six commands plus the [[GdbInfo|`info breakpoints`]] query.

## The command family

| Command | Effect |
|---|---|
| `enable N` | Re-arm previously disabled breakpoint `N`. |
| `disable N` | **Temporarily silence** breakpoint `N` — it stays in the table, but execution flies through. |
| `delete N` | Permanently remove breakpoint `N`. |
| `delete` (no arg) | Remove **all** breakpoints. |
| `clear N` | Remove the breakpoint at source-line `N` (located by source position rather than breakpoint ID). |
| `ignore N M` | Skip breakpoint `N` the next `M` times it would fire, then start halting normally. |
| `condition N (expr)` | Attach a **[[ConditionalBreakpoint|conditional]]** — breakpoint `N` halts only when `expr` evaluates to true. |
| [[GdbInfo|`info breakpoints`]] | List all breakpoints with state, location, hit count, condition. |

Each operation references the **breakpoint ID** that `break` printed at creation time — except `clear`, which looks up by source location.

## The disable/enable vs delete distinction

- **`disable`** is the right answer when you'll likely want the breakpoint back. Use it to silence breakpoints while debugging an unrelated path, then `enable` them again later. Disabled breakpoints remain numbered and visible in `info breakpoints`.
- **`delete`** is permanent — the ID is freed, the location forgotten. Use only when the breakpoint has served its purpose. `delete` (no arg) wipes the whole table.

## `ignore N M` — the hit-count suppressor

`ignore 2 1000` means "skip breakpoint 2 the next 1000 times, then start halting." Used to **bypass loop body iterations** that aren't interesting — e.g., a bug that only manifests at iteration 1001:

```text
(gdb) break inner_body
(gdb) ignore 1 1000
(gdb) run
... runs through 1000 iterations silently ...
... halts at iteration 1001 ...
```

The [[ConditionalBreakpoint|conditional-breakpoint]] equivalent is `condition 1 (iter == 1000)` — same effect, expression-driven instead of counter-driven.

## `condition N (expr)` — the conditional breakpoint

The headline workflow [[dis-3-2-gdb-commands|Ch 3.2]] singles out: *"pause at a breakpoint inside a loop only after some number of iterations or pause the program at a breakpoint only when the value of a variable has an interesting value."* The full mechanism lives on [[ConditionalBreakpoint]].

## `clear` vs `delete` — by location vs by ID

- `delete 1` removes breakpoint **#1** regardless of where it lives.
- `clear 124` removes whatever breakpoint sits at **line 124** of the current file.

`clear` is what you want after typing `break 124` — `clear 124` is the inverse without having to remember the ID.

## Connections

- [[dis-3-2-gdb-commands]] — introducing source.
- [[GDB]] / [[Debugger]] — the host tool.
- [[Breakpoint]] — what these commands manage.
- [[ConditionalBreakpoint]] — the most powerful variant, surfaced by `condition N (expr)`.
- [[GdbInfo]] — `info breakpoints` enumerates the current breakpoint table.
- [[Watchpoint]] — sibling primitive (pauses on memory writes, not PC reach); same `enable` / `disable` / `delete` lifecycle.
