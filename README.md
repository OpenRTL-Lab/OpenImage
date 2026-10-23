<!-- OpenRTL file declaration
Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
Organization introduction: Open hardware, from algorithms to RTL.
Repository: OpenImage
Repository introduction: Catalogue of standalone image-codec hardware.
File: README.md
Website: https://openrtl.top/
SPDX-FileCopyrightText: 2026 OpenImage contributors
SPDX-License-Identifier: MIT
-->
# OpenImage

OpenImage indexes OpenRTL's standalone, MIT-licensed image-codec hardware for engineers building image acquisition, storage and transmission pipelines. Listed projects provide Chisel sources and generated SystemVerilog for ASIC or FPGA integration. This catalogue provides project links, not codec RTL or a complete imaging system.

[简体中文](README.zh-CN.md)

- **PNG encoding and decoding (1.2.1)**: Converts raw image rows to complete PNG files and back, preserving the selected sample format. Supports static, non-interlaced PNG and all 15 legal colour/bit-depth combinations. Host control, DMA and system buffering are external. [png-codec](https://github.com/OpenRTL-Lab/png-codec)
- **JPEG XL lossless encoding (1.0.0)**: Encodes 8-bit, 1–4-channel images with width and height from 1 to 256 into complete codestreams using a fixed fast-lossless profile. Provides Chisel/SystemVerilog, RTL tests, generic Chipyard adapters and bare-metal software. Not a general JPEG XL decoder or a board project. [jpeg-xl](https://github.com/OpenRTL-Lab/jpeg-xl)

Each project documents its own interfaces, reproduction steps, verification limits, performance and synthesis conditions. This catalogue's original content uses the [MIT License](LICENSE); linked projects and their dependencies retain their own license terms.

For optional codec customization or ASIC/FPGA integration, visit the [OpenRTL website](https://openrtl.top/). Commercial use under MIT does not require purchasing services.
