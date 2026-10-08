# oohost: Sovereign DNS Host Resolver

<div align="center">

```
================================================================================
                                 oohost
                Sovereign openOODA DNS Host Resolver
================================================================================
```

**Sovereign DNS Host Resolver**  
*Quick DNS address resolver performing forward and reverse host conversions.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-orange.svg)]()
[![Architecture: x86_64](https://img.shields.io/badge/Arch-x86__64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64)
```bash
curl -fsSL https://openooda-tools.github.io/oohost/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (PKGBUILD)
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oohost/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oohost/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oohost-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oohost/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oohost [options] host [server]

Quick DNS address resolver performing forward and reverse host conversions.

Options:
  -a, -C               equivalent to -t ANY (query all available records)
  -s, --short          terse output: emit only resolved addresses and domain names
  -t, --type <TYPE>    query specified record type (A, AAAA, MX, TXT, CNAME, NS, SOA, ANY)
  -r, --reverse        perform reverse DNS query for IP address
      --server <IP>    specify custom DNS server to query
  -v, --verbose        verbose output with query latency and server statistics
      --no-color       suppress ANSI color sequences
  -j, --json           emit structured RFC 8259 JSON Lines
  -D, --demo           run interactive DNS resolution demonstration showcase
      --test           run internal verification anchor self-test suite
  -h, --help           display this help and exit
      --version        output version information and exit
      --mcp            run as Model Context Protocol stdio server
```

### Examples
```bash
# Forward lookup for IPv4 and IPv6 addresses
oohost example.com

# Reverse lookup for IPv4 address (PTR record)
oohost 93.184.215.14

# Query specific mail exchange (MX) records
oohost -t mx example.com

# Query all available DNS records
oohost -a example.com

# Terse pipeline output (emit only raw resolved addresses)
oohost -s example.com

# Query using custom upstream nameserver
oohost example.com 1.1.1.1

# Verbose query diagnostics with response latency
oohost -v example.com

# Structured JSON Lines telemetry
oohost -j example.com
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oohost` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oohost --mcp
```

### Exposed MCP Tools

1. `host_resolve`: Resolve hostname to IPv4 (A) and IPv6 (AAAA) addresses.
   - Arguments: `target` (String, required)
2. `host_reverse`: Perform reverse DNS lookup for an IPv4 or IPv6 address to retrieve PTR hostname.
   - Arguments: `ip` (String, required)
3. `host_records`: Query specific DNS records for a domain (MX, TXT, NS, SOA, CNAME, ANY).
   - Arguments: `target` (String, required), `type` (String, optional)
4. `host_inspect`: Inspect full DNS diagnostic response including nameserver, TTLs, and query latency.
   - Arguments: `target` (String, required), `server` (String, optional)
5. `host_demo`: Run demonstration showcase of sovereign DNS host resolution.
   - Arguments: none

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient filesystem or socket leakage.
* **Hermetic System Integration:** Inspects upstream nameservers from `systemd-resolved` (`/run/systemd/resolve/resolv.conf`) and `/etc/resolv.conf` with `/etc/hosts` overrides.
* **Negative-Trust Architecture:** Strict input validation and bounded memory buffers.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
