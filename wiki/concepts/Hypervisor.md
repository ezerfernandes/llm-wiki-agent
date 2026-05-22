---
title: "Hypervisor"
type: concept
tags: [operating-systems, virtualization, hypervisor]
sources: [dis-13-5-summary-advanced]
last_updated: 2026-05-18
---

# Hypervisor

A **hypervisor** is the layer of software (or firmware) that **virtualizes a machine's hardware so multiple [[OperatingSystem|operating systems]] can run concurrently on it**, each in its own [[VirtualMachine|virtual machine]]. *[[DiveIntoSystems]]* introduces hypervisors in [[dis-13-5-summary-advanced|Ch 13.5]] as one of the OS subsystems Ch 13 deliberately left out of scope — *"a hypervisor virtualizes the system hardware and allows the host OS to run multiple virtual guest operating systems"*.

## Type-1 vs Type-2

- **[[HypervisorType1|Type-1 (bare-metal)]]** — runs directly on hardware; the guest OSes sit on top with no host OS in between (Xen, VMware ESXi, Microsoft Hyper-V root partition, KVM-on-Linux when considered as the host kernel).
- **[[HypervisorType2|Type-2 (hosted)]]** — runs as a process under a conventional host OS (VirtualBox, VMware Workstation, Parallels Desktop, QEMU without KVM).

## Mechanism

The hypervisor exposes a **virtual CPU + virtual memory + virtual devices** interface to each [[GuestOS|guest OS]]. Modern x86 platforms accelerate this with **[[HardwareVirtualization|hardware virtualization extensions]]** — [[IntelVTx|Intel VT-x]] (VMX root/non-root modes) and [[AmdV|AMD-V]] (SVM) — which let guest instructions execute natively on real hardware until they touch a privileged operation that traps into the hypervisor.

## Relation to the OS

A hypervisor is the **OS-of-OSes**: it implements [[Scheduler|scheduling]], [[VirtualMemory|memory management]], and I/O multiplexing analogous to a conventional [[Kernel|kernel]], but its *processes* are entire guest operating systems rather than user programs. The same [[PageTable|page-table]] / [[ContextSwitch|context-switch]] / [[Interrupt|interrupt-handling]] machinery [[dis-13-1-booting-running|Ch 13.1]] / [[dis-13-2-processes|13.2]] / [[dis-13-3-virtual-memory|13.3]] introduced for processes is re-applied one layer up.

## See also

- [[Virtualization]] — the umbrella concept.
- [[GuestOS]] / [[HostOS]] — the host/guest split.
- [[OperatingSystem]] / [[Kernel]] — the substrate the hypervisor virtualizes and itself resembles.
- [[dis-13-5-summary-advanced]] — the source that names this concept in the wiki.
