---
title: "The Embedded Rust Book — Installation (Linux)"
type: source
tags: [rust, embedded, book-chapter, installation, linux]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/install/linux.md
---

# The Embedded Rust Book — Installation (Linux)

## Summary

File 6 of 44 of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — the **Linux-specific** install sub-page that branches off the OS-agnostic [[rust-embedded-book-intro-install|install manifest]]. Two operational halves: (1) distro-specific package install for the three native binaries — [[GDB]] (as `gdb-multiarch` on modern Debian / Ubuntu, `gdb-arm-none-eabi` on older Ubuntu and Arch, plain `gdb` on Fedora), [[OpenOCD]], and [[QEMU|`qemu-system-arm`]] — across Ubuntu / Debian, Fedora, and Arch; (2) a [[UdevRules|udev rule]] (`/etc/udev/rules.d/70-st-link.rules`) that grants the logged-in user `uaccess` to the [[STLink|ST-LINK]] USB device on the [[STM32F3DISCOVERY]] board, so [[OpenOCD]] can talk to the probe **without `sudo`**. The chapter closes with `udevadm control --reload-rules` and a `lsusb` + `getfacl` verification flow.

## Key Claims

- **Three native binaries are required, distro-named differently.** [[GDB]] for ARM Cortex-M, [[OpenOCD]], [[QEMU|`qemu-system-arm`]]. Per-distro install:
  - Ubuntu 18.04+ / Debian stretch+ → `sudo apt install gdb-multiarch openocd qemu-system-arm` (debug with `gdb-multiarch`).
  - Ubuntu 14.04 / 16.04 → `sudo apt install gdb-arm-none-eabi openocd qemu-system-arm` (debug with `arm-none-eabi-gdb`).
  - Fedora 27+ → `sudo dnf install gdb openocd qemu-system-arm`.
  - Arch → `sudo pacman -S arm-none-eabi-gdb qemu-system-arm openocd`.
- **GDB command name varies.** `gdb-multiarch` (modern Debian/Ubuntu) vs `arm-none-eabi-gdb` (older Ubuntu, Arch) vs plain `gdb` (Fedora) — the chapter is explicit that the binary invoked when debugging Cortex-M programs depends on distro.
- **Udev rule grants non-root USB access to the ST-LINK.** Create `/etc/udev/rules.d/70-st-link.rules` matching the two [[STLink|ST-LINK]] revisions on the F3 board (`idVendor==0483, idProduct==3748` for V2; `idProduct==374b` for V2-1) and apply `TAG+="uaccess"` so the seat-owning user gets ACL-based access without [[Sudo|`sudo`]].
- **Reload + replug.** After writing the rule, `sudo udevadm control --reload-rules`, then unplug + replug the board so udev applies the new rule on enumeration.
- **Verification flow.** `lsusb` to confirm the device shows up as `ID 0483:374b STMicroelectronics ST-LINK/V2.1`, take note of bus/device numbers, then `ls -l /dev/bus/usb/<bus>/<device>` should show a `+` in the permission column (ACL present); `getfacl ...| grep user` should list `user:<you>:rw-`.
- **No mention of `plugdev` group.** This chapter deliberately uses the modern *uaccess* / `logind` ACL mechanism rather than the older `GROUP="plugdev"` pattern — the same rule works on any logind-using distro without managing group membership.

## Key Quotes

> "This rule lets you use OpenOCD with the Discovery board without root privilege."

> "Create the file `/etc/udev/rules.d/70-st-link.rules` with the contents shown below."

> "The `+` appended to permissions indicates the existence of an extended permission. The `getfacl` command tells the user `you` can make use of this device."

## Connections

- [[TheEmbeddedRustBook]] — file 6/44; the Linux branch of the OS-specific install split.
- [[rust-embedded-book-intro-install]] — the OS-agnostic parent install chapter that branches here.
- [[GDB]] — installed per-distro; binary name varies (`gdb-multiarch` / `arm-none-eabi-gdb` / `gdb`).
- [[OpenOCD]] — installed per-distro; the udev rule exists specifically so it can drive [[STLink|ST-LINK]] without root.
- [[QEMU|`qemu-system-arm`]] — installed per-distro; the host emulator from the [[rust-embedded-book-intro-tooling|tooling chapter]].
- [[UdevRules]] — the Linux subsystem this chapter uses to assign USB-device ACLs.
- [[STLink|ST-LINK]] — the USB device the udev rule targets (`0483:3748` for V2, `0483:374b` for V2-1).
- [[STM32F3DISCOVERY]] — the board carrying the on-board ST-LINK; the reference platform for the rule.
- [[STMicroelectronics]] — vendor of the F3 board and ST-LINK.

## Contradictions

- None. Strictly additive — this chapter is the Linux-side operationalization of the OS-agnostic [[rust-embedded-book-intro-install]] manifest; toolchain versions and tool list match [[rust-embedded-book-intro-tooling]]. Note the version vintage of the chapter (Ubuntu 14.04 / 16.04 / 18.04, Fedora 27, Debian stretch) — the *commands* are still correct on current LTS releases, only the version anchors are dated.
