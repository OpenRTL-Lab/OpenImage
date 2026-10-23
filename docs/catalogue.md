<!-- OpenRTL file declaration
Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
Organization introduction: Open hardware, from algorithms to RTL.
Repository: OpenImage
Repository introduction: Catalogue of standalone image-codec hardware.
File: docs/catalogue.md
Website: https://openrtl.top/
SPDX-FileCopyrightText: 2026 OpenImage contributors
SPDX-License-Identifier: MIT
-->
# Using the catalogue

This catalogue helps engineers select a standalone image-codec hardware project. It does not bundle hardware sources, a shared generator or a system integration project.

[简体中文](catalogue.zh-CN.md)

## Project selection

The [Project index](../README.md) lists PNG encoder/decoder version 1.2.1 and JPEG XL lossless encoder version 1.0.0. Project versions are independent of this catalogue's VERSION, which identifies the index rather than a codec release.

Follow the project link for its supported image profile, native streaming interface, Chisel source, generated SystemVerilog, reference comparisons and reproduction instructions. Check the selected version's limits before integration; a protocol's theoretical capabilities are not necessarily implemented by a particular accelerator.

## Evidence and integration boundaries

Measurements and synthesis conditions belong to the linked project's documented version and workload. This catalogue supplies no shared performance number or system-level validation. ASIC/FPGA integration describes the intended use, not board testing, fabrication or qualification for every application. Host control, data movement and system memory integration remain the integrator's responsibility.

## Licensing and checks

The catalogue contains original documentation, small notice-checking tools and the [MIT License](../LICENSE), not third-party codec implementations. Linked projects and their dependencies keep their own license terms. File attribution and local checking commands are described in [Source notices](source-headers.md). These checks do not generate or simulate hardware.
