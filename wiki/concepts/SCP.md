---
title: "SCP"
type: concept
tags: [unix, networking, security, file-transfer]
sources: [dis-app2-3-remote-access]
last_updated: 2026-05-18
---

# SCP (Secure Copy)

**SCP** is the encrypted analog of `cp` — it transfers files between machines over an [[SSH]] session, using the same authentication + encryption.

Per [[dis-app2-3-remote-access|DIS Appendix 2.3]], the syntax mirrors [[UnixCommandLine|`cp`]] but each side may be a remote path of the form `user@host:path`:

```bash
scp prog.c       user@host:~/         # local -> remote
scp user@host:./file ./               # remote -> local
scp -r mydir/    user@host:~/         # recursive (directory)
```

## Performance note
For many small files, DIS recommends archive-then-transfer: [[Tar|`tar -czvf bundle.tar.gz mydir/`]] first, then `scp bundle.tar.gz user@host:~/`. Compression reduces wire bytes and a single SSH session avoids per-file handshake overhead.

## Related
- [[SSH]] — the underlying transport.
- [[Tar]] — the canonical pre-`scp` packaging step.
- [[DiveIntoSystems]] — Appendix 2.3.

## Sources
- [[dis-app2-3-remote-access]] — DIS Appendix 2.3 *Remote Access*.
