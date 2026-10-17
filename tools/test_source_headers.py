#!/usr/bin/env python3
# OpenRTL file declaration
# Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
# Organization introduction: Open hardware, from algorithms to RTL.
# Repository: OpenImage
# Repository introduction: Catalogue of standalone image-codec hardware.
# File: tools/test_source_headers.py
# Website: https://openrtl.top/
# SPDX-FileCopyrightText: 2026 OpenImage contributors
# SPDX-License-Identifier: MIT
"""Exercise notice rejection and read-only checking in disposable copies."""
import hashlib
import shutil
import tempfile
from pathlib import Path

import source_headers as notices


def snapshot(root):
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
            for name in notices.FILES}


def rejected(root):
    try:
        notices.check(root)
    except (AssertionError, ValueError):
        return
    raise AssertionError('damaged notice was accepted')


def main():
    source = Path(__file__).resolve().parents[1]
    notices.check(source)
    mutations = (
        ('missing', 'README.md', lambda t: t.replace('SPDX-License-Identifier: MIT\n', '', 1)),
        ('duplicate', 'README.md', lambda t: t.replace('File: README.md\n', 'File: README.md\n' * 2, 1)),
        ('wrong-file', 'README.md', lambda t: t.replace('File: README.md\n', 'File: other.md\n', 1)),
        ('tamper', 'tools/source_headers.py', lambda t: t.replace('# Repository: OpenImage\n', '# Repository: other\n', 1)),
    )
    for label, name, mutation in mutations:
        with tempfile.TemporaryDirectory(prefix='openimage-notice-') as tmp:
            root = Path(tmp)
            for file in notices.FILES:
                destination = root / file
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source / file, destination)
            before = snapshot(root)
            notices.check(root)
            notices.check(root)
            assert snapshot(root) == before, 'checking changed files'
            target = root / name
            target.write_text(mutation(target.read_text()))
            rejected(root)
    for name in ('VERSION.license', 'extra.txt'):
        with tempfile.TemporaryDirectory(prefix='openimage-inventory-') as tmp:
            root = Path(tmp)
            for file in notices.FILES:
                destination = root / file
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source / file, destination)
            if name == 'VERSION.license':
                (root / name).unlink()
            else:
                (root / name).write_text('unlisted\n')
            rejected(root)
    print('OPENIMAGE_SOURCE_NOTICE_TESTS_PASS: missing/duplicate/wrong-file/tamper/companion/inventory/read-only')


if __name__ == '__main__':
    main()
