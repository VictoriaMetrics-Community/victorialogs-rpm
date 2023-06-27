# victorialogs-rpm
RPM for victorialogs - [VictoriaLogs](https://docs.victoriametrics.com/VictoriaLogs/) is log management and log analytics system from [VictoriaMetrics](https://docs.victoriametrics.com/).

[![Copr build status](https://copr.fedorainfracloud.org/coprs/antonpatsev/victorialogs/package/victorialogs/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/antonpatsev/victorialogs/package/victorialogs/)

Before install disable [Selinux](https://selinuxproject.org/page/Main_Page). Info https://github.com/patsevanton/victoriametrics-rpm/issues/10

## Installation with yum
Support CentOS 6, CentOS 7, Oraclelinux 7, Rhel 7

```
sudo yum -y install yum-plugin-copr
sudo yum -y copr enable antonpatsev/victorialogs
sudo yum makecache
sudo yum -y install victorialogs
```

## Installation with dnf
Support CentOS-stream 8, CentOS-stream 9, CentOS 8, CentOS 9, Oraclelinux 8, Rhel 8, Rhel 9

```
sudo dnf -y install yum-plugin-copr
sudo dnf -y copr enable antonpatsev/victorialogs
sudo dnf makecache
sudo dnf -y install victorialogs
```
