---
title: "Virtualization"
type: concept
tags: [operating-systems, virtualization, hypervisor]
sources: [dis-13-5-summary-advanced]
last_updated: 2026-05-18
---

# Virtualization

**Virtualization** is the OS / systems technique of presenting a **virtual interface** that abstracts away the underlying physical resource. *[[DiveIntoSystems]]* names virtualization in [[dis-13-5-summary-advanced|Ch 13.5]] as one of the OS subsystems beyond Ch 13's core (processes + VM + IPC) — *"a hypervisor virtualizes the system hardware and allows the host OS to run multiple virtual guest operating systems"*.

## Forms

- **Hardware virtualization** — a [[Hypervisor|hypervisor]] virtualizes the whole machine, letting multiple [[GuestOS|guest operating systems]] share one physical host (the [[dis-13-5-summary-advanced|Ch 13.5]] sense).
- **OS-level virtualization / containers** — a single kernel hosts isolated user-space environments ([[LinuxContainers|Linux containers]], LXC, Docker, FreeBSD jails, Solaris zones). No guest kernel; isolation via [[Namespace|namespaces]] + [[Cgroup|cgroups]].
- **[[VirtualMemory|Virtual memory]]** — *"an abstraction that gives each [[Process|process]] its own private, logical [[AddressSpace|address space]]"* — the [[dis-13-3-virtual-memory|Ch 13.3]] sense. Each process *thinks* it owns the entire memory; the [[PageTable|page table]] + [[MMU]] virtualize the [[PhysicalAddress|physical memory]].
- **Process abstraction** — *"the [[Process|process]] is the OS's virtualization of the [[CPU]]"* — the [[dis-13-2-processes|Ch 13.2]] mechanism-vs-policy framing; every process sees a private virtual CPU.

## Headline claim

Virtualization is **the OS's defining technique** — the entire `[[OperatingSystem|operating system]]` chapter of *[[DiveIntoSystems]]* (Ch 13) is implicitly *"how the OS virtualizes the [[CPU]] (Ch 13.2) and the memory (Ch 13.3) for user processes"*. Ch 13.5 just names the **next layer up** — virtualizing the entire machine via a [[Hypervisor|hypervisor]].

## See also

- [[Hypervisor]] / [[HypervisorType1]] / [[HypervisorType2]] — the hardware-virtualization mechanism.
- [[VirtualMemory]] — per-process memory virtualization.
- [[Process]] — per-process CPU virtualization.
- [[OperatingSystem]] / [[Kernel]] — the substrate that implements virtualization.
- [[dis-13-5-summary-advanced]] — the source for the hardware-virtualization sense.
