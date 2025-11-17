%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    vlagent
Version: 1.38.0
Release: 1
Summary: vlagent is a tiny agent which helps you collect logs from various sources and store them in VictoriaLogs

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaLogs/releases/download/v%{version}/vlutils-linux-%{release_arch}-v%{version}.tar.gz

Source0: %{name}.service
Source1: %{name}.conf

Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)

%if %{use_systemd}
Requires: systemd curl
BuildRequires: systemd curl
%endif
BuildRequires: curl

%description
vlagent is a tiny agent which helps you collect logs from various sources and store them in https://docs.victoriametrics.com/victorialogs/. See https://docs.victoriametrics.com/victorialogs/vlagent/#quick-start for details.

%prep
curl -L %{url} > vlutils.tar.gz
tar -zxf vlutils.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 -d %{buildroot}/etc/victorialogs/vlagent
cp %{SOURCE1} %{buildroot}/etc/victorialogs/vlagent/
%{__install} -m 0755 -d %{buildroot}/var/lib/vlagent-remotewrite-data
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} %{buildroot}%{_unitdir}/%{name}.service
%endif
cp vlagent-prod %{buildroot}%{_bindir}/vlagent-prod

%pre
/usr/bin/getent group victorialogs > /dev/null || /usr/sbin/groupadd -r victorialogs
/usr/bin/getent passwd victorialogs > /dev/null || /usr/sbin/useradd -r -d /var/lib/vlagent-remotewrite-data -s /bin/bash -g victorialogs victorialogs

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop %{name}
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
%{_bindir}/vlagent-prod
%dir %attr(0775, victorialogs, victorialogs) /etc/victorialogs/vlagent
%dir %attr(0775, victorialogs, victorialogs) /var/lib/vlagent-remotewrite-data
%config /etc/victorialogs/vlagent/vlagent.conf
%if %{use_systemd}
%{_unitdir}/vlagent.service
%endif