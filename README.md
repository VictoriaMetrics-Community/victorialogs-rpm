# victorialogs-rpm
RPM for victorialogs - VictoriaLogs is log management and log analytics system from VictoriaMetrics.

[![Copr build status](https://copr.fedorainfracloud.org/coprs/antonpatsev/VictoriaMetrics/package/victoriametrics/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/antonpatsev/VictoriaMetrics/package/victoriametrics/)

Before install disable Selinux. Info https://github.com/patsevanton/victoriametrics-rpm/issues/10

## Installation with yum
Support CentOS 6, CentOS 7, Oraclelinux 7

```
sudo yum -y install yum-plugin-copr
sudo yum -y copr enable antonpatsev/victorialogs
sudo yum makecache
sudo yum -y install victorialogs
```

## Installation with dnf
Support CentOS 8, CentOS-stream 8, CentOS-stream 9, Oraclelinux 8, Fedora 33,34,35

```
sudo dnf -y install yum-plugin-copr
sudo dnf -y copr enable antonpatsev/victorialogs
sudo dnf makecache
sudo dnf -y install victorialogs
```
