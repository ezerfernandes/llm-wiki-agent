---
title: "Dive into Systems — Ch 2.1 Parts of Program Memory and Scope"
type: source
tags: [book, dive-into-systems, c-language, memory, scope]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C2-C_depth/scope_memory.html
---

## Summary

Section 2.1 of [[DiveIntoSystems]] **opens Ch 2 *A Deeper Dive Into C*** by upgrading [[dis-1-4-functions|Ch 1.4]]'s "[[ExecutionStack|execution stack]] of [[StackFrame|frames]]" cartoon into the **full four-region [[ProcessMemory|program memory]] model**: a running [[CLanguage|C]] program's [[AddressSpace|address space]] partitions into a **[[CodeSection|code section]]** (instructions), a **[[DataSection|data section]]** ([[GlobalVariable|globals]]), a **[[HeapSection|heap]]** ([[DynamicMemoryAllocation|dynamically allocated]] storage — *forward-referenced* to Ch 2.4), and a **[[StackSection|stack]]** ([[LocalVariable|locals]] and [[FunctionParameter|parameters]]). The section pairs this with the **first formal definition of [[VariableScope|scope]]** the corpus has had (Ch 1.4's [[FunctionScope|function scope]] was operational): *"a variable's scope defines when its name has meaning … the set of program code blocks in which a variable is bound to a program memory location."* Two scope classes get formal treatment: **[[GlobalVariable|global variables]]** (declared *outside* any function body, *"remain permanently in scope and can be used by any code in the program"*, live in the [[DataSection|data section]]) and **local variables + parameters** (declared *inside* a function, scoped to that function, allocated on the [[StackSection|stack]] on call / deallocated on return — [[dis-1-4-functions|Ch 1.4]]'s rule, now re-stated with the memory-region geography in place). The worked example uses a single global `int g_x` updated by `main` and read by `max`, alongside local `int val` declared independently in `main`, `change_global`, and `max` — making concrete the *"identical names in different functions are different variables"* rule. Style coda: *"avoid programming with global variables whenever possible"* — code that uses only locals is *"more modular, more general-purpose, and easier to debug."* This section does **not yet** discuss `static` variables, block scope, or file scope — leaving those for later chapters.

## Key Claims

- **A program's [[AddressSpace|address space]] is partitioned into four regions.** Per the chapter: *"The program's instructions are stored in the [[CodeSection|code]] section of the memory"*; *"[[GlobalVariable|Global variables]] are stored in the [[DataSection|data]] section"*; *"The [[HeapSection|heap]] portion of memory is the part of a program's address space associated with [[DynamicMemoryAllocation|dynamic memory allocation]]"*; *"[[LocalVariable|Local variables]] and [[FunctionParameter|parameters]] reside in the portion of memory for the [[StackSection|stack]]."* This is the chapter's headline picture — the upgrade from [[dis-1-4-functions|Ch 1.4]]'s "stack of frames" to **stack-plus-three-more-regions**.
- **Formal definition of [[VariableScope|scope]] arrives here for the first time.** Per the chapter: *"A variable's **scope** defines when its name has meaning. In other words, scope defines the set of program code blocks in which a variable is bound to (associated with) a program memory location."* [[dis-1-4-functions|Ch 1.4]] used [[FunctionScope|function scope]] *operationally* (top frame is in scope); Ch 2.1 supplies the underlying *language* definition that [[FunctionScope]] and [[GlobalScope]] are both instances of.
- **[[GlobalVariable|Global variables]] are *outside any function body*; live in the [[DataSection|data section]]; permanent for the program's life.** Per the chapter: *"Declaring a variable outside of any function body creates a global variable. Global variables remain permanently in scope and can be used by any code in the program."* The data-section storage is what makes "permanent" load-bearing — unlike [[LocalVariable|locals]], globals do not vanish on function return, because no [[StackFrame|frame]] pops them.
- **[[LocalVariable|Local variables]] + [[FunctionParameter|parameters]] are *inside a function body*; live on the [[StackSection|stack]]; scoped to that function.** Per the chapter: *"Local variables and parameters are only in scope inside the function in which they are defined."* This is [[dis-1-4-functions|Ch 1.4]]'s rule re-issued with the [[StackSection|stack-region]] geography — the same [[FunctionScope|function-scope]] rule, now connected to *where in memory* the storage lives.
- **The `g_x` worked example makes the scope geography concrete.** A single `int g_x = 0;` outside `main` is *read* in `max` and *written* in `change_global`, demonstrating cross-function reachability without parameter passing. The same program declares an `int val` in **three** different functions (`main`, `change_global`, `max`) — different variables despite the shared name, because each lives in a different [[FunctionScope|function scope]] / [[StackFrame|stack frame]].
- **Avoid globals as a style rule.** Per the chapter: programs that rely on globals to communicate are *harder to debug and less modular*; code that uses only [[LocalVariable|locals]] (with values passed via [[FunctionParameter|parameters]] and [[ReturnStatement|return]] values) is *"more modular, more general-purpose, and easier to debug."* This restates a discipline familiar from any introductory programming course and frames the rest of Ch 2's [[Pointer|pointer]] / [[DynamicMemoryAllocation|dynamic-allocation]] material as the *alternative* to globals for cross-function communication.
- **Three of the four regions are *known territory*; the [[HeapSection|heap]] is foreshadowed.** [[StackSection|Stack]] = [[dis-1-4-functions|Ch 1.4]]'s [[ExecutionStack|execution stack]] of [[StackFrame|frames]], now placed inside the broader [[AddressSpace|address space]]; [[CodeSection|code section]] holds the [[CompilationProcess|compiled]] [[BinaryExecutable|binary]] instructions (the runtime side of [[dis-1-1-getting-started|Ch 1.1]]'s compile-then-run model); [[DataSection|data section]] is the new region introduced for [[GlobalVariable|globals]]; [[HeapSection|heap]] is *named* but its mechanism ([[Malloc|`malloc`]] / [[Free|`free`]]) is **deferred to Ch 2.4**.
- **`static` / block scope / file scope are *not* covered here.** Ch 2.1 introduces only the **global-vs-local** scope split. The four C scope classes proper ([[BlockScope|block]] / [[FunctionScope|function]] / [[FileScope|file]] / [[FunctionPrototypeScope|function-prototype]]) and the [[StaticVariable|`static`]] storage class are left to later sections — a *deferred-deliberately* gap the wiki should not patch in advance.

## Key Quotes

> "A variable's **scope** defines when its name has meaning. In other words, scope defines the set of program code blocks in which a variable is bound to (associated with) a program memory location." — the chapter's headline definition of [[VariableScope|scope]]; the corpus's first formal one.

> "Declaring a variable outside of any function body creates a **global variable**. Global variables remain permanently in scope and can be used by any code in the program." — the *outside-any-function* placement rule for [[GlobalVariable|globals]] plus the *permanent-scope* lifetime guarantee, the two load-bearing claims of the section.

> "**Local variables and parameters** are only in scope inside the function in which they are defined." — [[dis-1-4-functions|Ch 1.4]]'s [[FunctionScope|function-scope]] rule, restated as Ch 2.1's second scope class.

> "The program's instructions are stored in the *code* section of the memory." — names the [[CodeSection|code section]] as the first of the four [[ProcessMemory|program-memory]] regions.

> "Global variables are stored in the *data* section." — names the [[DataSection|data section]] as the storage region for [[GlobalVariable|globals]].

> "The *heap* portion of memory is the part of a program's address space associated with dynamic memory allocation." — names the [[HeapSection|heap]] and forward-references [[DynamicMemoryAllocation|dynamic allocation]] (Ch 2.4).

> "Local variables and parameters reside in the portion of memory for the *stack*." — names the [[StackSection|stack]] as the storage region for [[LocalVariable|locals]] + [[FunctionParameter|parameters]], connecting [[dis-1-4-functions|Ch 1.4]]'s [[ExecutionStack|execution-stack]] story to the wider [[AddressSpace|address space]].

> "Code that uses only local variables tends to be more modular, more general-purpose, and easier to debug." — the chapter's style rule against [[GlobalVariable|globals]]; the *why* behind preferring [[FunctionParameter|parameter]] / [[ReturnStatement|return]] communication.

## Connections

- [[DiveIntoSystems]] — the book; this is **Ch 2.1**, the first section of Ch 2 *A Deeper Dive Into C*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-1-4-functions]] — Ch 1.4; supplies the [[ExecutionStack|execution stack]] / [[StackFrame|stack frame]] / [[FunctionScope|function scope]] vocabulary that Ch 2.1 generalizes. Ch 1.4's "stack of frames" is now the [[StackSection|stack section]] of the four-region address-space picture.
- [[dis-1-1-getting-started]] — Ch 1.1; the [[CompilationProcess|compile-then-run]] model produces the [[BinaryExecutable|binary]] whose instructions live in the [[CodeSection|code section]] Ch 2.1 names.
- [[dis-1-7-summary]] — Ch 1.7; explicitly forward-referenced **pointer variables** and **dynamic memory allocation** as the two big Ch 2 deferrals; Ch 2.1 introduces the [[HeapSection|heap]] region in preparation for both.
- [[CLanguage]] — the language whose memory model the chapter formalizes.
- [[ProcessMemory]] — the new umbrella concept: the four-region picture itself.
- [[AddressSpace]] — the abstract container the four regions partition.
- [[CodeSection]] / [[DataSection]] / [[HeapSection]] / [[StackSection]] — the four regions.
- [[VariableScope]] — the new umbrella scope concept (Ch 1.4 only had [[FunctionScope]] operationally).
- [[GlobalScope]] — the new scope class (alongside [[FunctionScope]]) introduced here.
- [[GlobalVariable]] — declared outside any function; lives in [[DataSection]]; [[GlobalScope]]; permanent.
- [[LocalVariable]] — pre-existing page; Ch 2.1 augments it with the *lives on the [[StackSection|stack]]* geography.
- [[FunctionScope]] — pre-existing; Ch 2.1 re-issues it as one of two scope classes.
- [[StackFrame]] / [[ExecutionStack]] — pre-existing; Ch 2.1 places them inside the [[StackSection|stack section]].
- [[CMemoryAddress]] — pre-existing; every variable's address now sits in one of four named regions.
- [[DynamicMemoryAllocation]] — named here; mechanism deferred to Ch 2.4.

## Contradictions

- **No contradictions.** Ch 2.1 *extends* and *re-states* [[dis-1-4-functions|Ch 1.4]]'s [[ExecutionStack|stack-of-frames]] / [[FunctionScope|function-scope]] story by placing it inside the broader four-region [[ProcessMemory|program-memory]] picture and adding the [[GlobalVariable|global-variable]] / [[DataSection|data-section]] case. No claim from Ch 1 is overturned; the [[StackSection|stack]] of Ch 2.1 is *the same stack* as the [[ExecutionStack]] of [[dis-1-4-functions|Ch 1.4]], now named as a region of the address space.
