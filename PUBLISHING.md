# 离线教程构建

需要 Python 3 与 Pandoc。在仓库目录运行：

```sh
python3 tools/build_guide.py
```

生成文件位于 `release-assets/`：

- `STEPX-Neo-GBox-Guide-v1.0.2.html`：离线教程。
- `gbox-1.8.4.02.json`：实测安装包的版本与来源信息。
- `SHA256SUMS`：前两个文件的校验值。

GBox 安装包使用 [官网下载入口](https://www.gboxlab.com/)。可选参数 `--apk /path/to/GBox.apk` 用于本地核对安装包大小与哈希。
