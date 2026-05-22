---
title: "SSH"
type: concept
tags: [unix, networking, security, remote-access]
sources: [dis-app2-3-remote-access]
last_updated: 2026-05-18
---

# SSH (Secure Shell)

**SSH** is the standard Unix tool for encrypted remote login. Per [[dis-app2-3-remote-access|DIS Appendix 2.3]], `ssh username@hostname` *"starts a unix shell on the remote machine through which the user can access files and run applications."*

## Usage
```bash
ssh sarita@cs87.cs.college.edu        # password (or key) prompt
ssh -p 2222 user@host                  # non-default port
ssh user@host 'ls -la ~/'              # one-shot remote command
```

## Cross-platform
- **Unix / macOS** — `ssh` ships in the base system.
- **Windows** — native in modern PowerShell; legacy: PuTTY.

## Key-based authentication
Generate a keypair with `ssh-keygen -t rsa`:

| File | Role |
|---|---|
| `~/.ssh/id_rsa` | private key — **keep secret** |
| `~/.ssh/id_rsa.pub` | public key — copy to remote's `~/.ssh/authorized_keys` |

Public-key auth is asymmetric: the server proves identity by encrypting a challenge with the public key that only the private-key holder can decrypt. The same mechanism underlies GitHub / GitLab / Bitbucket SSH-based Git access.

## Related
- [[SCP]] — file copy *over* SSH (same encryption + auth).
- [[UnixCommandLine]] — local shell context.
- [[DiveIntoSystems]] — Appendix 2.3.

## Sources
- [[dis-app2-3-remote-access]] — DIS Appendix 2.3 *Remote Access*.
