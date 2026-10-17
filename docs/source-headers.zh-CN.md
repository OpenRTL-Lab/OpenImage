<!-- OpenRTL file declaration
Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
Organization introduction: Open hardware, from algorithms to RTL.
Repository: OpenImage
Repository introduction: Catalogue of standalone image-codec hardware.
File: docs/source-headers.zh-CN.md
Website: https://openrtl.top/
SPDX-FileCopyrightText: 2026 OpenImage contributors
SPDX-License-Identifier: MIT
-->
# 来源声明

本文说明本目录各类文件的来源和许可声明，包括不能安全插入注释的文件。

[English](source-headers.md)

## 文件覆盖

| 文件 | 来源与声明 |
| --- | --- |
| 两份 README 及 `docs/` 内四份 Markdown | 原创目录文档，MIT；采用 HTML 注释声明 |
| `tools/source_headers.py`、`tools/test_source_headers.py`、`.gitignore` | 原创目录工具与配置，MIT；采用原生注释声明 |
| `VERSION` | 原创目录版本数据；声明位于 `VERSION.license` |
| `VERSION.license` | 标识 VERSION、其版权及 MIT 许可的伴随文件 |
| `LICENSE` | 标准 MIT 法律措辞及本项目原有版权声明；不对法律原文主张新创作 |

OpenZK 是目录结构参考；OpenImage 的介绍与工具针对本仓库撰写，不打包 OpenZK 代码或硬件实现。链接不会变更所链文件或依赖的许可。组织品牌展示不代表版权转让。

## 本地检查

在仓库根目录使用 Python 3.9 或更新版本，只需其标准库：

```sh
python3 tools/source_headers.py
python3 tools/test_source_headers.py
```

预期标记为 `OPENIMAGE_SOURCE_NOTICES_PASS` 和 `OPENIMAGE_SOURCE_NOTICE_TESTS_PASS`。检查器拒绝缺失、重复或文件身份不符的声明、缺失的 VERSION 伴随文件，以及未列入清单且不在忽略的 Git、构建或缓存目录内的文件。测试在临时副本中执行，包含故意损坏声明的反例，并核重复检查不改变任何文件。不需要网络、凭证、EDA 工具或硬件仿真。
