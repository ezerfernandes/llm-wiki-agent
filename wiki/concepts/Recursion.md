---
title: "Recursion"
type: concept
tags: [recursion, function, call-stack, computer-science, assembly]
sources: [dis-7-6-x86-64-recursion, dis-1-4-functions]
last_updated: 2026-05-17
---

# Recursion

**Recursion** is the [[ComputerScience|CS]] pattern in which a [[Function|function]] **invokes itself** — directly or indirectly — as part of computing its result. At the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level, recursion requires **no special instructions**: the [[CallInstruction|`callq`]] / [[RetInstruction|`retq`]] / [[LeaveInstruction|`leaveq`]] apparatus introduced by [[dis-7-5-x86-64-functions|Ch 7.5]] handles a function calling *itself* identically to a function calling *any other function*. What recursion adds is a **dynamic property** of the running [[CallStack|call stack]]: the same function appears on the stack multiple times simultaneously, each invocation with its own [[StackFrame|stack frame]].

## Promoted from Forward Reference

[[Recursion]] was a forward-reference concept implicit across the wiki — referenced by [[dis-1-4-functions|Ch 1.4]] (functions at the [[CLanguage|C]] level) and by [[dis-7-5-x86-64-functions|Ch 7.5]] (the function-call apparatus that makes recursion possible). [[dis-7-6-x86-64-recursion|Ch 7.6]] is the chapter that **operationalizes** recursion at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level via the `sumr` worked example, promoting Recursion to a first-class concept page.

## Two-Case Structure

Every well-formed recursive function decomposes into:

1. **Base case(s)** — input(s) on which the function returns directly **without** a recursive call. In [[dis-7-6-x86-64-recursion|Ch 7.6]]'s `sumr`, the base case is `n <= 0` → return `0`. Without at least one base case the recursion never terminates and the [[CallStack|call stack]] grows until [[StackOverflow|stack overflow]].
2. **Recursive case(s)** — input(s) on which the function calls itself on a **smaller** sub-problem and combines the result. In `sumr` the recursive case is `n > 0` → `return n + sumr(n-1)` — the sub-problem `sumr(n-1)` strictly approaches the base case `n = 0`.

The compiler realizes this two-case structure as a standard [[AsmIfThenElse|Ch 7.4.2 if-pattern]] — [[CmpInstruction|`cmp`]] of `n` against `0`, [[X86JumpInstructions|conditional jump]] on the negated condition, base-case branch falls through, recursive-case branch is jumped to.

## Assembly-Level Realization (per [[dis-7-6-x86-64-recursion|Ch 7.6]])

For `sumr` (sum from `n` down to 1), the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] body is structurally:

```
sumr:
  push %rbp                    # standard Ch 7.5 prologue
  mov %rsp, %rbp
  sub $0x10, %rsp              # 16 bytes of locals
  mov %edi, -0x4(%rbp)         # spill n from %edi to stack slot
  cmp $0x0, -0x4(%rbp)         # base-case test
  jg .Lrec                     # jump to recursive case if n > 0
  mov $0x0, %eax               # base case: return 0
  jmp .Lend
.Lrec:
  mov -0x4(%rbp), %edi         # load n
  sub $0x1, %edi               # decrement: %edi = n - 1
  callq sumr                   # recursive call — %eax := sumr(n-1)
  add -0x4(%rbp), %eax         # %eax := n + sumr(n-1)
.Lend:
  leaveq                       # standard Ch 7.5 epilogue
  retq
```

The recursive [[CallInstruction|`callq sumr`]] is structurally identical to any other `callq` — the [[CallingConvention|calling convention]] (`%edi` = 1st param, `%eax` = return) applies on every invocation, and the [[FramePointer|`%rbp`]]-anchored frame discipline is re-established on every entry.

## Stack-Depth Cost

The headline runtime cost of recursion: **each invocation adds one [[StackFrame|stack frame]] to the [[CallStack|call stack]]**. Calling `sumr(5)` produces 6 stacked `sumr` frames at the deepest point (`n = 5, 4, 3, 2, 1, 0`); calling `sumr(d)` produces `d + 1` frames. This is the **structural memory cost** every recursive algorithm pays — and on bounded stacks (typically 1 MiB to 8 MiB per thread on Linux) the cost becomes a hard depth limit beyond which the program faults with a [[StackOverflow|stack overflow]] (the [[CallStack|stack]] crosses its guard page).

The chain of saved-[[FramePointer|`%rbp`]] values across recursive frames forms a backward singly-linked list along the [[ExecutionStack|execution stack]] — visible in a [[GDB|debugger]] as `backtrace` showing the recursive function repeated $d$ times.

## Tail Recursion (forward reference)

A recursive call is in **tail position** if it is the **last** operation the calling function performs before returning — no work happens after the recursive call returns. [[TailRecursion|Tail-recursive]] functions can be **compiled to iteration** (replacing the `callq` with a `jmp` back to the function's prologue, reusing the current [[StackFrame|frame]] instead of allocating a new one) — eliminating the linear stack-depth cost. This optimization is **not** covered by [[dis-7-6-x86-64-recursion|Ch 7.6]] (and `sumr` is **not** tail-recursive — the `add -0x4(%rbp), %eax` happens *after* the recursive call returns, so the call is not in tail position).

## Connections

- [[dis-7-6-x86-64-recursion]] — the source that operationalizes Recursion at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level.
- [[dis-1-4-functions]] — the [[CLanguage|C]]-level introduction of [[Function|functions]] and the [[ExecutionStack|execution stack]]; Recursion is a special case of the function-call pattern Ch 1.4 introduces.
- [[CallStack]] / [[ExecutionStack]] — the LIFO of [[StackFrame|frames]] Recursion grows linearly with depth.
- [[StackFrame]] — one is allocated per recursive invocation, each with its own copies of parameters and locals.
- [[CallInstruction]] / [[RetInstruction]] / [[LeaveInstruction]] — the [[X86_64|x86-64]] instructions that implement the call/return discipline Recursion reuses unchanged.
- [[CallingConvention]] — the [[CallingConvention|System V AMD64 convention]] governing argument-passing and return-value flow at every recursive call boundary.
- [[FramePointer]] / [[StackPointer]] — `%rbp` is re-anchored on every recursive entry; the chain of saved-`%rbp` values across frames is the structure debuggers walk for `backtrace`.
- [[AsmIfThenElse]] — the [[X86_64|x86-64]] compilation pattern Ch 7.6 uses for the base-case vs recursive-case dispatch.
- [[Function]] — the higher-level abstraction Recursion is a runtime pattern of.
- [[TailRecursion]] — the optimization-eligible sub-case (forward reference; not covered by Ch 7.6).
- [[StackOverflow]] — the failure mode when recursion depth exceeds the available [[CallStack|call stack]] (forward reference; not named by Ch 7.6).
