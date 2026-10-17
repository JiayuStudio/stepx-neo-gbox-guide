# 下载与核验

## 官网下载

- [GBox 官网与稳定版入口](https://www.gboxlab.com/)
- [本次实测 GBox 1.8.4.02 官方原始链接](https://agile-files.gboxlab.com/GBox-1.8.4.02-1080402-7899902-website.apk)

查询日期为 2026-10-18；当时官网稳定版为 1.8.4.02，标注更新日期 2026-09-22。后续新版本需单独核验，不能用本文的校验值判断另一版本。

## 私有归档

作者个人私有归档位于 [v1.0.0 Release](https://github.com/JiayuStudio/stepx-neo-gbox-guide/releases/tag/v1.0.0)，需要仓库读取权限。APK 不存入 Git 历史。公开再分发未获授权，见 [第三方声明](../THIRD_PARTY_NOTICES.md)。

| 字段 | 值 |
| --- | --- |
| 归档文件 | `GBox-1.8.4.02-official.apk` |
| 包名 | `com.gbox.android` |
| versionName / versionCode | `1.8.4.02` / `1080402` |
| 大小 | `124361684` 字节 |
| APK SHA-256 | `e19f71b249ae190067c52de84c586696315b8e305192c56710961fa72334f5ad` |
| 签名证书 SHA-256 | `2f1a26c7225d085cde5267dc91556dd2c7d19bdc8cffee58e95bbfd39ac697ae` |
| 签名校验 | APK v1、v2 通过 |
| ABI | `arm64-v8a`、`armeabi-v7a` |

机器可读信息在 [gbox-1.8.4.02.json](gbox-1.8.4.02.json)，校验文件在 [SHA256SUMS](SHA256SUMS)。改文件名未改变 APK 内容，没有改包名、修改代码或重签名。

APK 校验是来源和完整性检查，不是软件安全审计。本仓库没有将 Google 原生三个 APK、失败改包、用户代理工具或个人配置打包成所谓“一键套件”。
