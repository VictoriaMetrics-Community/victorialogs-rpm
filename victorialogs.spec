%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    victorialogs
Version: 1.8.0
Release: 1
Summary: Log management and log analytics system from VictoriaMetrics team.

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v%{version}-victorialogs/victoria-logs-linux-%{release_arch}-v%{version}-victorialogs.tar.gz

Source0: %{name}.service
Source1: victorialogs.conf
Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel

%global source_date_epoch_from_changelog 1

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)

%if %{use_systemd}
Requires: systemd curl
BuildRequires: systemd
%endif

%description
VictoriaLogs is log management and log analytics system from VictoriaMetrics.

%prep
curl -L %{url} > victorialogs.tar.gz
tar -zxf victorialogs.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 -d %{buildroot}/etc/victorialogs
cp %{SOURCE1} %{buildroot}/etc/victorialogs
cp victoria-logs-prod %{buildroot}%{_bindir}/victoria-logs-prod
%{__install} -m 0755 -d %{buildroot}/var/lib/victorialogs
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} \
    %{buildroot}%{_unitdir}/%{name}.service
%endif

%pre
/usr/bin/getent group victorialogs > /dev/null || /usr/sbin/groupadd -r victorialogs
/usr/bin/getent passwd victorialogs > /dev/null || /usr/sbin/useradd -r -d /var/lib/victorialogs -s /bin/bash -g victorialogs victorialogs
%{__mkdir} -p /var/lib/victorialogs
/usr/bin/echo "WARINING: chown -R victorialogs:victorialogs /var/lib/victorialogs"
/usr/bin/echo "THIS MAY TAKE SOME TIME"
/usr/bin/chown -R victorialogs:victorialogs /var/lib/victorialogs

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
%config /etc/victorialogs/victorialogs.conf
%{_bindir}/victoria-logs-prod
%dir %attr(0775, victorialogs, victorialogs) /var/lib/victorialogs
%if %{use_systemd}
%{_unitdir}/%{name}.service
%endif

%changelog
* Mon Jan 29 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v v1.8.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v180

* Mon Dec 09 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v v1.3.2-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v132

* Fri Dec 06 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v v1.2.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v120

* Sat Nov 09 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v v0.42.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v0420

* Mon Oct 21 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.37.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v0370

* Mon Sep 09 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.29.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v0290

* Tue Jul 18 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.28.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v0280

* Tue Jun 26 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.23.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v0230

* Fri May 24 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.10.0-victorialogs
  See Full Changelog at https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v0.10.0-victorialogs

* Mon May 13 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.6.0-victorialogs
  See Full Changelog at https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v0.6.0-victorialogs
