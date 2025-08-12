%define release_arch amd64
%ifarch aarch64
%define release_arch arm64
%endif

Name:    vlogscli
Version: 1.27.0
Release: 1
Summary: vlogsqcli is an interactive command-line tool for querying VictoriaLogs

Group:   Development Tools
License: ASL 2.0
URL: https://github.com/VictoriaMetrics/VictoriaLogs/releases/download/v%{version}/vlutils-linux-%{release_arch}-v%{version}.tar.gz

Requires(pre): /usr/sbin/useradd, /usr/bin/getent, /usr/bin/echo, /usr/bin/chown
Requires(postun): /usr/sbin/userdel
Requires: curl

%description
vlogsqcli is an interactive command-line tool for querying VictoriaLogs, see https://docs.victoriametrics.com/victorialogs/querying/vlogscli/

%prep
curl -L %{url} > vlutils.tar.gz
tar -zxf vlutils.tar.gz

%install
%{__install} -m 0755 -d %{buildroot}%{_bindir}
cp vlogscli-prod %{buildroot}%{_bindir}/vlogscli-prod

%pre
/usr/bin/getent group victorialogs > /dev/null || /usr/sbin/groupadd -r victorialogs
/usr/bin/getent passwd victorialogs > /dev/null || /usr/sbin/useradd -r -d /var/lib/victorialogs -s /bin/bash -g victorialogs victorialogs

%files
%{_bindir}/vlogscli-prod