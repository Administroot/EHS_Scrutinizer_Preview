# EHS_Scrutinizer (Preview) / EHS莫哭泣（预览版）

<p align=center>
    <img src="./logo.jpg" alt="logo" title="logo" />
</p>

<p align="center">
  <a href="#">
      <img src="https://img.shields.io/badge/give%20me-a%20star-green.svg" alt="give me a star">
    </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-EPL2.0-brightgreen.svg" alt="License-EPL2.0">
  </a>
</p>

[English](README_en.md) | 简体中文

本项目与2024年大年初一诞生`:fireworks:``:fireworks:``:fireworks:`

名字来源：EHS_Scrutinizer（意译：EHS检查器， 音译：EHS莫哭泣）。本软件愿景为杜绝由于粗心大意、概念不清、自以为是等所导致的受到批评、克扣工资乃至提包走人现象的发生，节省泪水，赠你笑容。

一个EHS生产力工具!

支持通过GUI界面一键生成各种EXCEL表格，也可以通过内置工具来检查你的表格！

完整详细的使用指引，上手无难度！

[帮助文档](https://administroot-blog.netlify.app/zh-cn/posts/ehs_scrutinizer_helper)

## 内容列表

- [功能](#功能)
- [安装](#安装)
- [使用](#使用)
- [预览](#预览)
- [原理图](#原理图)
- [参与开发](#参与开发)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

## 功能

Use EHS Scrutinizer to automate your workflow, so you can focus on work that matters most.

EHS Scrutinizer 用于:

- 一键生成各种EXCEL表格
- 一键检查你的表格
- 针对分析结论，提供专业的建议

具体功能见[**帮助文档**](https://administroot-blog.netlify.app/zh-cn/posts/ehs_scrutinizer_helper)

## 安装

[EHS Scrutinizer正式版]() 在Microsoft Store搜索EHS Scrutinizer正式版（未上线`:sleepy:`）

[EHS Scrutinizer试用版]() 在Microsoft Store搜索EHS Scrutinizer试用版（未上线`:sleepy:`）

（开发者）拉取本仓库master分支源代码自行编译构建。
环境要求：Python3.8+，Windows10+

``` shell
git clone https://github.com/Administroot/EHS_Scrutinizer_Preview.git
pip install -r requirements.txt
foo bar
```

## 使用

双击运行程序

## 预览

![预览]()

## 原理图

流程如下：

[流程图](./flowchart.png)

1. 从用户填写的EXCEL表格（模板.xlsx）中获取信息。
2. 通过预处理过滤器清洗数据，出现概念问题（如同一操作位接害时间不同）提醒用户，并决定是否继续流程。并进行专门化的数据处理。
3. 通过通用预处理过滤器清洗数据，确保数据原子性。
4. 数据入Sqlite数据库。
5. Sql查询，通过后处理过滤器清洗数据，并进行专门化的数据处理。
6. 通过通用后处理过滤器清洗数据。
7. 数据写入EXCEL表格。

## 参与开发

详见[EHS Scrutinizer开发者文档](https://administroot-blog.netlify.app/zh-cn/posts/ehs_scrutinizer_developer_doc/)

## 如何贡献

非常欢迎你的加入!

[提一个Issue](https://github.com/Administroot/EHS_Scrutinizer_Preview/issues/new)

## 使用许可

[EPL2.0](https://github.com/Administroot/EHS_Scrutinizer_Preview/blob/main/LICENSE) © Administroot
