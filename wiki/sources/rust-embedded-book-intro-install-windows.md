---
title: "The Embedded Rust Book — Installation (Windows)"
type: source
tags: [rust, embedded, book-chapter, installation, windows]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/intro/install/windows.md
---

# The Embedded Rust Book — Installation (Windows)

## Summary

File 8 of 44 of *[[TheEmbeddedRustBook|The Embedded Rust Book]]* — the **Windows-specific** install sub-page, the third OS branch off the OS-agnostic [[rust-embedded-book-intro-install|install manifest]] alongside [[rust-embedded-book-intro-install-linux|Linux]] and [[rust-embedded-book-intro-install-macos|macOS]]. No package manager is assumed (no Chocolatey / scoop mention): each tool ships as a vendor binary. [[GDB|`arm-none-eabi-gdb`]] comes from ARM's official Windows `.exe` installer (Arm GNU Toolchain), [[OpenOCD]] from the third-party xPack binary distribution (no official Windows release), [[QEMU]] from the QEMU project's own Windows builds, plus a mandatory [[STLink|ST-LINK]] **USB driver** (STMicroelectronics' `stsw-link009`) without which [[OpenOCD]] can't drive the probe. Common thread: every installer must add itself to `%PATH%` (or be added manually) and the user verifies with `-v`.

## Key Claims

- **`arm-none-eabi-gdb` ships as an ARM-signed `.exe`.** Source is ARM's "Arm GNU Toolchain Downloads" page — *not* a package manager. The installer offers an **"Add path to environment variable"** checkbox that must be ticked, else `%PATH%` won't pick up the tools.
- **No official OpenOCD Windows binary.** The recommended path is the third-party **[[xPackProject|xPack project]]** binary distribution. Users either compile from source or grab the xPack build; in the latter case `%PATH%` must be manually extended to the xPack install bin directory (default path: `C:\Users\USERNAME\AppData\Roaming\xPacks\@xpack-dev-tools\openocd\0.10.0-13.1\.content\bin\`).
- **QEMU has first-party Windows builds.** Linked straight off `qemu.org/download/#windows`; no third-party intermediary.
- **ST-LINK USB driver is mandatory, separate from OpenOCD.** Without [[STMicroelectronics]]'s `stsw-link009` driver installed, [[OpenOCD]] **won't work** on Windows. User must pick the correct 32-bit / 64-bit variant matching the OS bitness.
- **No Zadig / WinUSB swap mentioned.** The chapter sticks with the vendor [[STLink|ST-LINK]] driver — it does not route the user through Zadig's generic WinUSB substitution that some Windows libusb tooling needs. (The udev-equivalent step on Linux was a `70-st-link.rules` ACL; on Windows it is simply installing the ST driver.)
- **Verification pattern identical to Linux/macOS.** Each tool is verified with `<tool> -v` printing a banner — e.g. `arm-none-eabi-gdb -v` → "GNU gdb (GNU Tools for Arm Embedded Processors 7-2018-q2-update) 8.1.0.20180315-git", `openocd -v` → "Open On-Chip Debugger 0.10.0".

## Key Quotes

> "ARM provides `.exe` installers for Windows. Grab one from [here], and follow the instructions. Just before the installation process finishes tick/select the 'Add path to environment variable' option."

> "There's no official binary release of OpenOCD for Windows but if you're not in the mood to compile it yourself, the xPack project provides a binary distribution."

> "You'll also need to install [this USB driver] or OpenOCD won't work. Follow the installer instructions and make sure you install the right version (32-bit or 64-bit) of the driver."

## Connections

- [[TheEmbeddedRustBook]] — file 8/44; the Windows branch of the OS-specific install split, closing the three-OS trio.
- [[rust-embedded-book-intro-install]] — the OS-agnostic parent install chapter that branches here.
- [[rust-embedded-book-intro-install-linux]] — sibling OS branch; on Linux the ST-LINK seat-user access is granted via a [[UdevRules|udev rule]], not a driver install.
- [[rust-embedded-book-intro-install-macos]] — sibling OS branch; macOS needs no driver step at all (USB exposed to the seat user by default).
- [[GDB]] — installed via ARM's official Windows `.exe` (Arm GNU Toolchain) with the "Add path to environment variable" tick-box.
- [[OpenOCD]] — installed via the [[xPackProject|xPack project]] binary distribution; `%PATH%` extension required.
- [[QEMU]] — installed via the QEMU project's own Windows builds.
- [[STLink]] — requires [[STMicroelectronics]]'s `stsw-link009` USB driver on Windows for [[OpenOCD]] to see the probe.
- [[STMicroelectronics]] — vendor of the `stsw-link009` Windows USB driver.
- [[xPackProject]] — third-party project providing the only practical Windows binary distribution of [[OpenOCD]] for this chapter.

## Contradictions

- None. Strictly additive — Windows-side operationalization of the OS-agnostic [[rust-embedded-book-intro-install]] manifest. Tool list matches [[rust-embedded-book-intro-tooling]]. Where [[rust-embedded-book-intro-install-linux|Linux]] needs a udev rule for [[STLink|ST-LINK]] ACLs and [[rust-embedded-book-intro-install-macos|macOS]] needs nothing, Windows needs a vendor USB driver — the equivalence point across the three OS branches.
