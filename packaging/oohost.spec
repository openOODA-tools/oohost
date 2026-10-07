Name:           oohost
Version:        0.1.0
Release:        1%{?dist}
Summary:        Quick DNS address resolver performing forward and reverse host conversions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oohost
Source0:        oohost-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oohost is a sovereign, capability-bounded HOST RESOLVER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oohost
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oohost-uninstall

%files
/usr/bin/oohost
/usr/bin/oohost-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
