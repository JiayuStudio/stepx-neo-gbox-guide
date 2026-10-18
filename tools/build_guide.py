#!/usr/bin/env python3
"""Maintainer tool: build the offline guide with Pandoc; phone readers need none of this."""

from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.0.2"


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apk", type=Path, help="Optional official APK for private archive verification")
    args = parser.parse_args()
    output = ROOT / "release-assets"
    output.mkdir(exist_ok=True)
    guide = output / f"STEPX-Neo-GBox-Guide-{VERSION}.html"
    subprocess.run([
        "pandoc", "--standalone", "--toc", "--toc-depth=2", "--embed-resources",
        "--metadata=lang:zh-CN", "--metadata=toc-title:目录",
        "--metadata=title:STEPX Neo · GBox 手机操作手册",
        f"--metadata=subtitle:{VERSION} · 2026-10-18 · 免 ROOT 容器方案",
        "--css=assets/guide.css", "docs/手机安装教程.md", "docs/常见问题.md", "docs/实测记录.md",
        "-o", str(guide),
    ], cwd=ROOT, check=True)
    html = guide.read_text()
    nav_start = html.index('<nav id="TOC"')
    nav_end = html.index("</nav>", nav_start) + len("</nav>")
    nav = html[nav_start:nav_end]
    quick = ('<p class="quick-links"><a href="https://www.gboxlab.com/">打开 GBox 官网</a>'
             ' · <a href="https://github.com/JiayuStudio/stepx-neo-gbox-guide">查看在线教程</a></p>')
    html = (html[:nav_start] + quick + '<details class="guide-toc"><summary>打开目录：安装步骤 / 常见问题 / 实测记录</summary>'
            + nav + '</details>' + html[nav_end:])
    guide.write_text(html)
    manifest = ROOT / "downloads/gbox-1.8.4.02.json"
    package = json.loads(manifest.read_text())
    shutil.copyfile(manifest, output / manifest.name)
    checksums = []
    if args.apk:
        digest = sha256(args.apk)
        if digest != package["sha256"] or args.apk.stat().st_size != package["size_bytes"]:
            raise SystemExit("APK does not match the recorded official version; no checksum manifest written.")
        checksums.append(f'{digest}  {package["archive_filename"]}')
    for path in [guide, output / manifest.name]:
        checksums.append(f"{sha256(path)}  {path.name}")
    (output / "SHA256SUMS").write_text("\n".join(checksums) + "\n")
    print(json.dumps({"guide": guide.name, "bytes": guide.stat().st_size,
                      "apk_verified": bool(args.apk), "checksum_entries": len(checksums)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
