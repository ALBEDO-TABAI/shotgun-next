---
type: Reference
title: 图像工具的官方说法
description: 四家图像工具的官方文档各说了什么，这本书用了哪一句，没有推出哪些结论。
tags:
- 官方
- 生图
- 编辑
timestamp: '2026-09-18'
source:
- Midjourney 官方文档
- Google 官方文档
- OpenAI 官方文档
- Runway 官方文档
---

# 图像工具的官方说法

访问和核验日期：2026-09-17。只摘和这本书有关的内容，不复制官方长篇示例。链接是动态页面，以后用需要重新核对。

**这不是模型排名。** 只说每家文档写了什么，以及这本书据此提醒了什么。

## Midjourney：Prompt Basics

官方基础指南仍然强调简洁清楚，短句往往比长指令清单更合适。[1]

**这本书用它来反对一种说法**："当代提示词必须全部改成长段自然语言，关键词已经完全失效。" 不是这样。丰富的构思和给工具的输入是两回事。

**不能推出**：某个模型在某任务上更强；删掉某个词一定会改善画面。

## Google：Gemini 图像生成指南

官方文档包含风格化图像、文字与图像联合编辑等用法，用主体、媒介、细节和修改目标来组织描述。[2]

**这本书用它来说明**：图像任务可以用自然说明交代关系和修改，但要按实际任务组织，不是只把句子变长。

**不能推出**：每个接口都能分离身份、风格、布局；一次编辑能绝对锁住全部非目标像素。

## OpenAI：Image generation

官方图像编辑文档说明蒙版可以指导编辑，但其形状**不一定被精确遵循**；多图输入时也有特定的蒙版应用规则。[3]

**这本书用它来区分**：视觉打标、原生蒙版、后期精确合成是三种不同的东西。重要的非编辑区域仍需要对比检查。

**不能推出**：所有图像系统用相同的蒙版机制；写"绝对不变"就能得到像素级保证。

## Runway：Gen-4 Image Prompting Guide

这版图像指南同时讨论描述性句子和关键词组织。[4] 再次说明：工具、模式和任务比"新派 / 旧派写法"的二分更有实际意义。

**版本边界**：这里明确指 Gen-4 Image 相关指南，不代表该公司全部最新模型的规则。

# Citations

[1] [Midjourney — Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)

[2] [Google — Image generation with Gemini](https://ai.google.dev/gemini-api/docs/image-generation)

[3] [OpenAI — Image generation，Edit an image using a mask](https://developers.openai.com/api/docs/guides/image-generation)

[4] [Runway — Gen-4 Image Prompting Guide](https://help.runwayml.com/hc/en-us/articles/35694045317139-Gen-4-Image-Prompting-Guide)
