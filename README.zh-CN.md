<!-- OpenRTL file declaration
Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
Organization introduction: Open hardware, from algorithms to RTL.
Repository: OpenImage
Repository introduction: Catalogue of standalone image-codec hardware.
File: README.zh-CN.md
Website: https://openrtl.top/
SPDX-FileCopyrightText: 2026 OpenImage contributors
SPDX-License-Identifier: MIT
-->
# OpenImage

OpenImage 索引 OpenRTL 的独立 MIT 许可图像编解码硬件，面向构建图像采集、存储与传输流水线的工程师。所列项目提供 Chisel 源码与生成的 SystemVerilog，供 ASIC 或 FPGA 集成。本目录提供项目链接，不包含编解码 RTL，也不是完整成像系统。

[English](README.md)

- **PNG 编码与解码（1.2.1）**：在原始图像行与完整 PNG 文件之间转换，保留所选采样格式。支持静态、非交错 PNG 及全部 15 种合法颜色类型与位深组合。主机控制、DMA 和系统缓冲需外部集成。[png-codec](https://github.com/OpenRTL-Lab/png-codec/blob/main/README.zh-CN.md)

各项目分别说明自己的接口、复现步骤、验证限制、性能与综合条件。本目录原创内容采用 [MIT 许可证](LICENSE)；所链项目及其依赖保留各自的许可条款。

如需可选的编解码器定制或 ASIC/FPGA 集成服务，请访问 [OpenRTL 官网](https://openrtl.top/)。MIT 许可的商业使用不以购买服务为条件。
