---
title: "Loadable Kernel Module"
type: concept
tags: [operating-systems, kernel, drivers, extensibility]
sources: [dis-13-5-summary-advanced]
last_updated: 2026-05-18
---

# Loadable Kernel Module

A **loadable kernel module (LKM)** is *"executable code that can be loaded into the kernel and run in kernel mode"* — *[[DiveIntoSystems]]* [[dis-13-5-summary-advanced|Ch 13.5]]'s definition. LKMs let an [[OperatingSystem|OS]] **extend a running [[Kernel|kernel]] without rebooting** — the kernel-extensibility mechanism that supports modern device-driver model, filesystem-driver, and networking-stack pluggability.

## Mechanism

- The module is compiled against the running kernel's headers, producing an object file (`.ko` on Linux, `.kext` directory bundle on macOS, `.sys` on Windows).
- `insmod` / `modprobe` (Linux) / `kextload` (legacy macOS) / driver-install APIs (Windows) inject the object into the running kernel address space.
- The module runs in [[KernelMode|kernel mode]] — full privileges, full access to kernel data structures — same trust level as the rest of the [[Kernel|kernel]].
- `rmmod` removes it (when refcount allows).

## What lives as a module

- Device drivers (most of them — graphics, network, storage, USB).
- Filesystem implementations (ext4, xfs, btrfs, fuse on Linux; many third-party Windows filesystems).
- Network protocol modules.
- Hardware-specific tuning.

## Trade-offs

- **Pro**: Add hardware support, filesystem, or feature **without a reboot**; ship kernel features outside the monolithic kernel build.
- **Con**: Modules run with **full kernel privileges** — a buggy or malicious module can crash or compromise the entire system. Modern Linux signs modules and enforces [[Kconfig|`CONFIG_MODULE_SIG`]] to mitigate.

## See also

- [[Kernel]] / [[KernelMode]] — the substrate modules attach to.
- [[OperatingSystem]] — the umbrella.
- [[DeviceDriver]] — the most common LKM use case.
- [[Microkernel]] — an alternative kernel architecture where these capabilities live as user-space processes instead.
- [[dis-13-5-summary-advanced]] — the source for this page.
