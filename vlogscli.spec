%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    vlogscli
Version: 0.37.0
Release: 1
Summary: vlogsqcli is an interactive command-line tool for querying VictoriaLogs

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v%{version}-victorialogs/vlogscli-linux-%{release_arch}-v%{version}-victorialogs.tar.gz

Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel

%global source_date_epoch_from_changelog 1

%if %{use_systemd}
Requires: curl
%endif

%description
vlogsqcli is an interactive command-line tool for querying VictoriaLogs

%prep
curl -L %{url} > vlogscli.tar.gz
tar -zxf vlogscli.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp vlogscli-prod %{buildroot}%{_bindir}/vlogscli-prod

%pre
/usr/bin/getent group victorialogs > /dev/null || /usr/sbin/groupadd -r victorialogs
/usr/bin/getent passwd victorialogs > /dev/null || /usr/sbin/useradd -r -d /var/lib/victorialogs -s /bin/bash -g victorialogs victorialogs

%changelog
* Mon Oct 21 2024 Denys Holius <rpm@victoriametrics.com>
- Updated to version v0.37.0-victorialogs
  See Full Changelog at https://docs.victoriametrics.com/victorialogs/changelog/#v0370
