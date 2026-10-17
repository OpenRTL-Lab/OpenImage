<!-- OpenRTL file declaration
Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
Organization introduction: Open hardware, from algorithms to RTL.
Repository: OpenImage
Repository introduction: Catalogue of standalone image-codec hardware.
File: docs/source-headers.md
Website: https://openrtl.top/
SPDX-FileCopyrightText: 2026 OpenImage contributors
SPDX-License-Identifier: MIT
-->
# Source notices

This document identifies the catalogue's file origins and license notices, including the files that cannot safely contain comments.

[简体中文](source-headers.zh-CN.md)

## File coverage

| Files | Origin and notice |
| --- | --- |
| Both README files and the four Markdown files in `docs/` | Original catalogue documentation, MIT; HTML-comment declaration |
| `tools/source_headers.py`, `tools/test_source_headers.py`, `.gitignore` | Original catalogue tools/configuration, MIT; native comment declaration |
| `VERSION` | Original catalogue version data; declaration in `VERSION.license` |
| `VERSION.license` | Companion identifying VERSION, its copyright and MIT license |
| `LICENSE` | Standard MIT legal wording with the original project's copyright notice; not claimed as newly authored legal text |

OpenZK supplies the catalogue-structure reference; the OpenImage descriptions and tools are written for this repository. No OpenZK code or hardware implementation is bundled. Links do not relicense the linked files or dependencies. Organization branding does not transfer copyright.

## Local checks

From the repository root, using Python 3.9 or newer and only its standard library:

```sh
python3 tools/source_headers.py
python3 tools/test_source_headers.py
```

Expected markers are `OPENIMAGE_SOURCE_NOTICES_PASS` and `OPENIMAGE_SOURCE_NOTICE_TESTS_PASS`. The checker rejects missing, duplicate or wrong-file declarations, missing VERSION companions and unlisted files outside ignored Git/build/cache directories. Tests run in temporary copies, include deliberately damaged notices and check that repeated checking leaves every file unchanged. No network access, credential, EDA tool or hardware simulation is required.
