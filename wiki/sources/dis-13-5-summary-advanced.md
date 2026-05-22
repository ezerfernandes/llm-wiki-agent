---
title: "Dive into Systems — Ch 13.5 Summary and Other OS Functionality"
type: source
tags: [book-chapter, dive-into-systems, operating-systems, summary, virtualization, filesystem, kernel-modules]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C13-OS/advanced.html
---

## Summary

**Ch 13.5 *Summary and Other OS Functionality*** is the **closing-prose leaf** of Ch 13 *The Operating System* of *[[DiveIntoSystems]]*. It recaps the chapter's core arc — [[Process|processes]] + [[Multiprogramming|multiprogramming]] + [[VirtualMemory|virtual memory]] + [[ContextSwitch|context switching]] + [[InterprocessCommunication|IPC]] — and **names the OS subsystems Ch 13 deliberately left out**: [[FileSystem|filesystems]], protection / [[OperatingSystemSecurity|security]], [[SchedulingPolicy|scheduling policies]], [[Networking|networking]], [[Virtualization|virtualization]] / [[Hypervisor|hypervisors]], and [[LoadableKernelModule|loadable kernel modules]]. The headline take-away: *Dive into Systems* covers the [[Kernel|kernel]] **mechanism** layer in depth but defers full **policy** / **service** coverage to a dedicated OS course; the section recommends [[OperatingSystemsThreeEasyPieces|*Operating Systems: Three Easy Pieces*]] (Arpaci-Dusseau & Arpaci-Dusseau, 2018) as the canonical next-step textbook.

## Key Claims

- The Ch 13 arc unifies as: **the OS = the body of software that manages [[ComputerHardware|hardware]] resources and abstracts them for user programs** — concretized by Ch 13.1 ([[Booting|boot]] + [[KernelMode|dual-mode]] + [[SystemCall|syscall]] trap), Ch 13.2 ([[Process|processes]] + [[ContextSwitch|context switch]] + [[ProcessScheduling|scheduling]] mechanism), Ch 13.3 ([[VirtualMemory|virtual memory]] + [[PageTable|page tables]] + [[TLB]]), Ch 13.4 ([[InterprocessCommunication|IPC]] = [[Signal|signals]] + [[MessagePassing|message passing]] + [[SharedMemoryIPC|shared memory]]).
- **Filesystem abstractions** are an entire OS subsystem Ch 13 did not cover — the [[FileSystem]] manages on-disk layout, naming, metadata, permissions, and the [[OpenSyscall|`open`]] / [[ReadSyscall|`read`]] / [[WriteSyscall|`write`]] / [[CloseSyscall|`close`]] syscall surface that turns raw block devices into the *file* abstraction.
- **Security and protection** is similarly its own subsystem — user authentication, [[AccessControl|access control]], capability and permission models, kernel hardening (e.g., the post-Meltdown [[KernelPageTableIsolation|KPTI]] response Ch 13.1 foreshadowed).
- **[[SchedulingPolicy|Scheduling policies]]** (CFS / O(1) / EEVDF / real-time) sit *on top* of Ch 13.2's [[ContextSwitch|context-switch]] mechanism — the **mechanism vs policy split** is the deliberate Ch 13 framing and the policy half is deferred.
- **[[InterprocessCommunication|Interprocess communication]]** beyond Ch 13.4's three canonical families also includes higher-level constructs (D-Bus, RPC, [[Mailbox|mailboxes]], shared message queues) layered on the primitives.
- **[[Networking]]** is treated as an OS subsystem with its own protocol-stack implementation ([[TCP|TCP]] / [[UDP]] / [[IP]] / device drivers / [[Socket|socket]] API), forwarded to Ch 14 / external resources.
- **[[Virtualization]] / [[Hypervisor|hypervisors]]** — *"virtualizes the system hardware and allows the host OS to run multiple virtual guest operating systems"* — named as a distinct OS-implementation discipline; covers Type-1 ([[HypervisorType1|bare-metal]]) vs Type-2 ([[HypervisorType2|hosted]]) hypervisors, [[HardwareVirtualization|hardware virtualization extensions]] ([[IntelVTx|Intel VT-x]] / [[AmdV|AMD-V]]), and the [[GuestOS|guest OS]] / [[HostOS|host OS]] distinction.
- **[[LoadableKernelModule|Loadable kernel modules]]** — *"executable code that can be loaded into the kernel and run in kernel mode"* — the kernel-extensibility mechanism (Linux `.ko`, macOS kexts, Windows drivers) that lets device drivers and filesystem implementations attach to a running kernel without reboot.
- **OS extensibility / tuning** — system administrators tune OS [[KernelBuffer|buffers]], [[OSCache|caches]], and [[SwapPartition|swap partitions]] via runtime knobs (`sysctl`, `/proc/sys`) — *the kernel exposes a configuration surface*.
- **Pedagogical close**: pointer to [[OperatingSystemsThreeEasyPieces|*Operating Systems: Three Easy Pieces*]] (Arpaci-Dusseau & Arpaci-Dusseau, 2018) as the canonical follow-on for full-scope OS coverage.

## Key Quotes

> "A hypervisor virtualizes the system hardware and allows the host OS to run multiple virtual guest operating systems."

> "A loadable kernel module is executable code that can be loaded into the kernel and run in kernel mode."

> *(recap framing)* Operating systems also implement filesystem abstractions, security and protection policies, scheduling policies, interprocess communication mechanisms, networking, virtualization, and loadable kernel modules — surfaced here as the **deferred-subsystems checklist** beyond Ch 13's process / VM / IPC core.

## Connections

- [[DiveIntoSystems]] — **second-to-last leaf of Ch 13** and the **prose-close** of the OS chapter; pairs with [[dis-13-6-exercises|Ch 13.6 *Exercises*]] which closes Ch 13 entirely.
- [[dis-13-1-booting-running]] / [[dis-13-2-processes]] / [[dis-13-3-virtual-memory]] / [[dis-13-4-ipc]] / [[dis-13-4-1-signals]] / [[dis-13-4-2-message-passing]] / [[dis-13-4-3-shared-memory]] — the six Ch 13 leaves this summary recaps.
- [[OperatingSystem]] — Ch 13's umbrella concept; this leaf names the **remaining subsystems** Ch 13 did not cover.
- [[FileSystem]] — newly minted from this section as the canonical name for the file-abstraction subsystem.
- [[Virtualization]] / [[Hypervisor]] — newly minted from this section as the umbrella for hardware-multiplexing OSes.
- [[LoadableKernelModule]] — newly minted from this section as the kernel-extensibility mechanism.
- [[OperatingSystemsThreeEasyPieces]] — newly minted as the recommended follow-on textbook (Arpaci-Dusseau & Arpaci-Dusseau, 2018).
- [[Kernel]] / [[KernelMode]] / [[UserMode]] — reused unchanged from [[dis-13-1-booting-running|Ch 13.1]].
- [[SchedulingPolicy]] — mechanism-vs-policy split from [[dis-13-2-processes|Ch 13.2]]; this section names the policy half as the deferred subsystem.
- [[InterprocessCommunication]] / [[Networking]] — reused from [[dis-13-4-ipc|Ch 13.4]]; networking specifically called out as a separate OS subsystem.

## Contradictions

None — pure recap + forward-reference to deferred OS subsystems.
