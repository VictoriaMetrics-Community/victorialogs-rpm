%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    vlagent
Version: 1.25.0
Release: 1
Summary: vlagent is a tiny agent which helps you collect logs from various sources and store them in VictoriaLogs

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaLogs/releases/download/v%{version}/vlutils-linux-%{release_arch}-v%{version}.tar.gz
Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel

%global source_date_epoch_from_changelog 1

Requires: curl

%description
vlagent is a tiny agent which helps you collect logs from various sources and store them in https://docs.victoriametrics.com/victorialogs/. See https://docs.victoriametrics.com/victorialogs/vlagent/#quick-start for details.

%prep
curl -L %{url} > vlutils.tar.gz
tar -zxf vlutils.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp vlagent-prod %{buildroot}%{_bindir}/vlagent-prod

%pre
/usr/bin/getent group victorialogs > /dev/null || /usr/sbin/groupadd -r victorialogs
/usr/bin/getent passwd victorialogs > /dev/null || /usr/sbin/useradd -r -d /var/lib/victorialogs -s /bin/bash -g victorialogs victorialogs

%files
%{_bindir}/vlagent-prod

%changelog