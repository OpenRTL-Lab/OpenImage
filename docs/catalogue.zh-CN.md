<!-- OpenRTL file declaration
Organization: OpenRTL Lab (GitHub: OpenRTL-Lab)
Organization introduction: Open hardware, from algorithms to RTL.
Repository: OpenImage
Repository introduction: Catalogue of standalone image-codec hardware.
File: docs/catalogue.zh-CN.md
Website: https://openrtl.top/
SPDX-FileCopyrightText: 2026 OpenImage contributors
SPDX-License-Identifier: MIT
-->
# 目录使用说明

本目录帮助工程师选择独立的图像编解码硬件项目，不打包硬件源码、共用生成器或系统集成工程。

[English](catalogue.md)

## 项目选择

[项目索引](../README.zh-CN.md)列出 PNG 编码器与解码器版本 1.2.1，以及 JPEG XL 无损编码器版本 1.0.0。项目版本独立于本目录的 VERSION，后者标识索引本身而非编解码器发行版。

沿项目链接查阅支持的图像范围、原生流接口、Chisel 源码、生成的 SystemVerilog、参考比较和复现说明。集成前应核对所选版本的限制；协议理论能力不等于某个加速器已经实现的能力。

## 证据与集成边界

测量结果与综合条件只适用于所链项目文档对应的版本及工作负载。本目录不提供共用性能数字或系统级验证结论。ASIC/FPGA 集成是用途定位，不代表已上板、已流片或适用于所有应用。主机控制、数据搬运及系统存储集成仍由集成方负责。

## 许可与检查

本目录包含原创文档、小型声明检查工具和 [MIT 许可证](../LICENSE)，不包含第三方编解码实现。所链项目与依赖保留自己的许可条款。文件归属及本地检查命令见[来源声明](source-headers.zh-CN.md)。这些检查不生成或仿真硬件。
