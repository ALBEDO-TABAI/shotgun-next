---
type: Reference
title: 第一方依据：图像提示与图像编辑
description: 核验当前图像工具的写法与编辑边界，不作模型优劣排名。
tags:
- 官方
- 生图
- 编辑
timestamp: '2026-09-18'
source:
- Midjourney官方文档
- Google官方文档
- OpenAI官方文档
- Runway官方文档
---

# 第一方依据：图像提示与图像编辑

访问与核验日期：2026-09-17。只摘要与本书有关的有限内容，不复制官方长篇示例。链接是动态页面，未来调用需重新核对。

## I01｜Midjourney：Prompt Basics

官方基础指南仍强调简洁清楚的表达，短句通常比很长的指令清单更合适。由此可反对“当代提示必须改成长段自然语言，关键词已全部失效”的泛化。[1]

**在本书中的用途**：提醒创作者把丰富构思与工具输入分开，不把一种写法宣布为所有系统的未来。

**不支持**：任何特定模型在某任务上的优势；删掉某个词必然改善画面。

## I02｜Google：Gemini图像生成指南

官方文档包含风格化图像、文字与图像联合编辑等用法，并通过主体、媒介、细节及修改目标组织描述。[2]

**用途**：图像任务可以用自然说明交代关系与修改，但应按实际任务组织，而非只改变句子长度。

**不支持**：每个接口都能分离身份、风格、布局；一次编辑能绝对锁住全部非目标像素。

## I03｜OpenAI：Image generation

官方图像编辑文档说明蒙版可指导编辑，但其形状不一定被精确遵循；多图输入时也有特定蒙版应用规则。[3]

**用途**：区分视觉打标、原生蒙版与后期精确合成。重要非编辑区域仍需比较。

**不支持**：所有图像生成系统使用相同蒙版机制；写出“绝对不变”就能获得像素级保证。

## I04｜Runway：Gen-4 Image Prompting Guide

该版本图像指南同时讨论描述性句子与关键词组织。[4] 它再次说明，工具、模式和任务比“新派/旧派写法”二分更有实际意义。

**版本边界**：这里明确指Gen-4 Image相关指南，不宣称是该公司的全部最新模型规则。

# Citations

[1] [Midjourney — Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)

[2] [Google — Image generation with Gemini](https://ai.google.dev/gemini-api/docs/image-generation)

[3] [OpenAI — Image generation，Edit an image using a mask](https://developers.openai.com/api/docs/guides/image-generation)

[4] [Runway — Gen-4 Image Prompting Guide](https://help.runwayml.com/hc/en-us/articles/35694045317139-Gen-4-Image-Prompting-Guide)
