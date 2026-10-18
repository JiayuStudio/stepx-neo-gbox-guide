# STEPX Neo 免 ROOT 使用 Google Play：GBox 手机操作教程

适用于希望在 STEPX Neo 上登录 Google 账号、通过 Play 商店安装应用的用户。使用 **GBox 容器**，操作步骤在手机上完成，不要求电脑、USB 调试、ROOT、Bootloader 解锁或刷机。

**这不是全系统原生 GMS 安装方案。** Google 账号与应用主要运行在 GBox 中，手机外部的应用不会因此自动获得完整 Google 服务。

归属：[StepX Neo 研究所](https://github.com/JiayuStudio/stepx-neo-lab)。

教程版本：**v1.0.1 · 2026-10-18**。实测设备：STEPX Neo（系统型号 StepX PZ261A），Android 16 / StepAOS 1.0.0.2，GBox 1.8.4.02。

> **验证范围：** 一台实机已完成 Google 登录和应用安装，删除先前失败的宿主 Google 组件后仍可打开容器内 Play。初次安装由电脑 ADB 辅助，之后使用手机自身网络；下面的纯手机安装入口依据 Android 安装流程与同版本向导整理，**尚未在恢复出厂的 Neo 上独立走完整轮**。其他系统版本请按实际结果反馈。

## 从这里开始

- [详细手机安装教程](docs/手机安装教程.md)：下载、安装权限、初始化、登录、安装应用、验收。
- [常见问题](docs/常见问题.md)：连接 Google 卡住、黑白屏、下载等待、通知、卸载失败组件。
- [实测记录与边界](docs/实测记录.md)：哪些通过、哪些没有测过，以及历史试验对复现的影响。
- [下载与安装包核验](downloads/README.md)：官网入口、版本、大小、SHA-256、签名指纹。
- [手机离线阅读版](https://github.com/JiayuStudio/stepx-neo-gbox-guide/releases/download/v1.0.1/STEPX-Neo-GBox-Guide-v1.0.1.html)：下载后用支持本地 HTML 的浏览器打开；阅读不用联网，下载和登录仍需联网。

## 最短操作路线

1. 先让**手机本身**能够访问 Google；在手机浏览器打开 [Google 登录页](https://accounts.google.com/)，确认能加载。
2. 手机浏览器进入 [GBox 官网](https://www.gboxlab.com/)，下载稳定版。本次通过的是 **1.8.4.02**。
3. 打开下载的 APK，按手机提示仅为当前浏览器或文件管理器允许“安装未知应用”，安装 GBox。
4. 打开 GBox，阅读协议，完成媒体/文件权限和后台运行设置。本次没有安装可选 HMS Core。
5. 在 **GBox 首页**打开 Google Play 商店，输入自己的 Google 账号并完成验证。
6. 在该商店搜索一个应用并安装，从 GBox“已安装应用”打开；退出重开后再检查一次。

初次配置只需要 **一个 GBox APK**。无需按顺序在手机系统里安装 Google 服务框架、Google Play 服务、Play 商店三个独立 APK，也不用安装本项目早期的改包实验。

## 社区下载与归属

本教程属于 [StepX Neo 研究所](https://github.com/JiayuStudio/stepx-neo-lab)，可公开阅读。安装 GBox 请使用官网入口；本仓库不公开镜像第三方 APK。Release 提供离线教程、来源信息与校验值。

旧私有审阅版的 APK 镜像已撤下；公开附件不包含个人账号、代理配置、设备标识或原始日志。第三方软件范围见 [第三方声明](THIRD_PARTY_NOTICES.md)。

本仓库提供独立社区实践记录，与 STEPX、Google、GBox 没有官方合作关系。安装包没有修改、重签名或植入个人配置；本仓库不提供 Google 账号或代理订阅。

## 反馈

请记录设备型号、Android/StepAOS 版本、GBox 版本、失败步骤及可见错误文字。公开反馈不要包含账号、验证码、代理订阅、设备序列号或未处理的系统日志。模板见 [反馈模板](docs/反馈模板.md)。
