# 从私有审阅到社区发布

当前阶段只创建私有仓库并上传审阅材料，不启用 GitHub Pages，也不自动修改可见性。

## 当前归档内容

Git 历史只包含教程、版本与来源信息、校验文件、反馈模板及原创页面样式。Release 另附个人私有归档的 GBox 原版 APK、手机离线 HTML 教程、SHA256SUMS 和包信息 JSON。

APK 超过普通 Git 单文件限制，使用 Release 附件而不是提交进 Git。Release 的访问者必须具备当前私有仓库读取权限。[GitHub 官方 Release 说明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

## 公开前需要完成

1. **处理 APK 分发范围。** 未获得 GBox 公开再分发许可时，从每一个 Release 删除 APK 及含 APK 的压缩包，保留官网入口和校验信息。不要只删除最新 Release。若后续获得许可，记录许可的实际范围后再决定是否保留镜像。
2. 尽可能补做一台初始系统 Neo 的纯手机流程复测；若尚未完成，继续保留 README 与实测记录中的明确边界。
3. 确认要为原创教程采用何种公开许可；第三方 APK 不随文本许可改变。
4. 检查全部 Git 历史及 Release 附件，不包含账号、令牌、代理订阅、签名密钥、设备标识、私密截图和原始日志。
5. 修改“私有审阅状态”与下载说明，使社区默认入口清晰；如果不分发 APK，删掉其镜像入口，保留官方链接。重新生成离线教程。
6. 由仓库所有者明确决定何时改为 public。完成后用未登录浏览器核对教程和允许公开的附件，再向社区分享。

将 private 改为 public 会让保留的 Git 历史和 Release 附件进入公开范围。不要把“尚未发社区链接”当作仍然私密。

## 维护约定

离线版由 `tools/build_guide.py` 使用 Python 3 和 Pandoc 生成，输出到不进入 Git 的 `release-assets/`。维护者在仓库目录执行 `python3 tools/build_guide.py` 即可生成 HTML、来源 JSON 和它们的校验值。为个人私有归档增加 `--apk /path/to/official.apk` 时，会先核对 APK 的大小和 SHA-256，再把 APK 校验项加入清单；脚本不复制、不上传 APK。手机读者无需运行此脚本或安装这些工具。

- 新 GBox 版本单独记录文件名、来源、大小、哈希和签名；不要覆写旧版本的校验值。
- 新系统或新机型使用自己的结果，不把作者的一台机器扩大为全型号兼容保证。
- 在 CHANGELOG 中说明实测范围与文档更新；撤回失效下载入口时保留必要解释。
- 不把用户反馈中的原始日志、账号截图或个人配置直接纳入提交。
