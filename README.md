# victorialogs-rpm

<p align="center">
   <img src="logo.png" width="300" alt="Home Assistant Add-on VictoriaLogs Database for logs">
</p>

[![GitHub license](https://img.shields.io/github/license/VictoriaMetrics/VictoriaMetrics.svg)](https://github.com/VictoriaMetrics-Community/homeassistant-addon-victoriametrics/blob/main/LICENSE) [![Slack](https://img.shields.io/badge/join%20slack-%23victoriametrics-brightgreen.svg)](https://slack.victoriametrics.com/) [![Twitter Follow](https://img.shields.io/twitter/follow/VictoriaMetrics?style=social)](https://x.com/VictoriaMetrics) [![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/VictoriaMetrics?style=social)](https://www.reddit.com/r/VictoriaMetrics/) [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white)](https://t.me/VictoriaMetrics_en)

RPM for victorialogs - [VictoriaLogs](https://docs.victoriametrics.com/VictoriaLogs/) is log management and log analytics system from [VictoriaMetrics](https://docs.victoriametrics.com/).

| Package | Status |
| ------- | ------ |
| victorialogs| [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaLogs/package/victorialogs/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaLogs/package/victorialogs/) |
| vlogscli | [![Copr build status](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaLogs/package/vlogscli/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/victoriametrics/VictoriaLogs/package/vlogscli/) |

Before install disable [Selinux](https://selinuxproject.org/page/Main_Page).

## Installation with yum
Support CentOS 6, CentOS 7, Oraclelinux 7, Rhel 7

```
sudo yum -y install yum-plugin-copr
sudo yum -y copr enable victoriametrics/VictoriaLogs
sudo yum makecache
sudo yum -y install victorialogs
```

## Installation with dnf
Support CentOS-stream 8, CentOS-stream 9, CentOS 8, CentOS 9, Oraclelinux 8, Rhel 8, Rhel 9

```
sudo dnf -y install yum-plugin-copr
sudo dnf -y copr enable victoriametrics/VictoriaLogs
sudo dnf makecache
sudo dnf -y install victorialogs
```

# Data ingestion [#](https://docs.victoriametrics.com/victorialogs/data-ingestion/#)

[](https://github.com/VictoriaMetrics/Victoriametrics/edit/master/docs/VictoriaLogs/data-ingestion/README.md)

[VictoriaLogs](https://docs.victoriametrics.com/victorialogs/) can accept logs from the following log collectors:

-   Syslog, Rsyslog and Syslog-ng - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/syslog/).
-   Filebeat - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/filebeat/).
-   Fluentbit - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/fluentbit/).
-   Logstash - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/logstash/).
-   Vector - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/vector/).
-   Promtail (aka Grafana Loki) - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/promtail/).
-   Telegraf - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/telegraf/).
-   OpenTelemetry Collector - see [these docs](https://docs.victoriametrics.com/victorialogs/data-ingestion/opentelemetry/).

The ingested logs can be queried according to [these docs](https://docs.victoriametrics.com/victorialogs/querying/).


## [VictoriaLogs datasource for Grafana](https://github.com/VictoriaMetrics/victorialogs-datasource)

The VictoriaLogs datasource plugin allows you to query and visualize [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/) data in [Grafana](https://grafana.com).

- [Installation](https://github.com/VictoriaMetrics/victorialogs-datasource#installation)
- [Notes](https://github.com/VictoriaMetrics/victorialogs-datasource#notes)
- [License](https://github.com/VictoriaMetrics/victorialogs-datasource#license)

### Looking for a Demo without installation?

Just visit [https://play-grafana.victoriametrics.com/...](https://play-grafana.victoriametrics.com/explore?schemaVersion=1&panes=%7B%22pd1%22:%7B%22datasource%22:%22P566C6523BE02F42C%22,%22queries%22:%5B%7B%22refId%22:%22A%22,%22datasource%22:%7B%22type%22:%22victorialogs-datasource%22,%22uid%22:%22P566C6523BE02F42C%22%7D,%22expr%22:%22%2A%22,%22queryType%22:%22range%22%7D%5D,%22range%22:%7B%22from%22:%22now-1h%22,%22to%22:%22now%22%7D%7D%7D&orgId=1)

<p>
    <a href="#"><img src="Grafana-datasource-for-VictoriaLogs-demo.png" alt="Victoriametrics Grafana playground of a datasource for VictoriaLogs demo" style="width:100%;height:auto;"></a>
</p>