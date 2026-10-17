#!/usr/bin/env python3
# OpenRTL file declaration
# Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
# Organization introduction: Open hardware, from algorithms to RTL.
# Repository: OpenImage
# Repository introduction: Catalogue of standalone image-codec hardware.
# File: tools/source_headers.py
# Website: https://openrtl.top/
# SPDX-FileCopyrightText: 2026 OpenImage contributors
# SPDX-License-Identifier: MIT
"""Read-only source-notice and inventory checks for this catalogue."""
from pathlib import Path

FILES = {
    '.gitignore', 'LICENSE', 'README.md', 'README.zh-CN.md', 'VERSION',
    'VERSION.license', 'docs/catalogue.md', 'docs/catalogue.zh-CN.md',
    'docs/source-headers.md', 'docs/source-headers.zh-CN.md',
    'tools/source_headers.py', 'tools/test_source_headers.py',
}
IGNORED = {'.git', 'build', '__pycache__'}
OWNER = 'SPDX-FileCopyrightText: 2026 OpenImage contributors'
LICENSE_ID = 'SPDX-License-Identifier: MIT'


def inventory(root):
    return {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
            and not any(part in IGNORED for part in p.relative_to(root).parts)
            and p.suffix != '.pyc'}


def check(root):
    assert inventory(root) == FILES, 'unlisted or missing file'
    assert all(not (root / name).is_symlink() for name in FILES), 'symlink not covered'
    assert (root / 'VERSION').read_bytes() == b'1.0.0\n', 'version data changed'
    license_text = (root / 'LICENSE').read_text()
    assert license_text.startswith('MIT License\n\nCopyright (c) 2026 OpenImage contributors\n')
    assert 'Permission is hereby granted, free of charge' in license_text
    assert 'THE SOFTWARE IS PROVIDED "AS IS"' in license_text
    for name in sorted(FILES - {'LICENSE', 'VERSION'}):
        text = (root / name).read_text()
        if name == 'VERSION.license':
            header = text
            file_name = 'VERSION'
        elif name.endswith('.md'):
            assert text.startswith('<!-- OpenRTL file declaration\n'), name
            header, body = text.split('-->\n', 1)
            assert 'OpenRTL file declaration' not in body, name
            file_name = name
        else:
            lines = text.splitlines()
            if name.endswith('.py'):
                assert lines.pop(0) == '#!/usr/bin/env python3', name
            comments = []
            for line in lines:
                if not line.startswith('# '):
                    break
                comments.append(line[2:])
            header = '\n'.join(comments)
            assert header.startswith('OpenRTL file declaration\n'), name
            assert text.count('# OpenRTL file declaration\n') == 1, name
            file_name = name
        for field in ('Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)',
                      'Organization introduction: Open hardware, from algorithms to RTL.',
                      'Repository: OpenImage',
                      'Repository introduction: Catalogue of standalone image-codec hardware.',
                      'File: ' + file_name, 'Website: https://openrtl.top/', OWNER, LICENSE_ID):
            assert header.splitlines().count(field) == 1, (name, field)
    return len(FILES)


if __name__ == '__main__':
    count = check(Path(__file__).resolve().parents[1])
    print('OPENIMAGE_SOURCE_NOTICES_PASS: ' + str(count) + ' files')
