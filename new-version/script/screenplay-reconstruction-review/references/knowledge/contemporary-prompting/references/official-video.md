---
type: Reference
title: 视频工具的官方说法
description: 视频工具的官方指南各说了什么，哪些是当前建议、哪些已经归档，这本书主动不推出哪些结论。
tags:
- 官方
- 视频
- 版本
timestamp: '2026-09-18'
source:
- Runway 官方文档
- Google 官方文档
- OpenAI 归档创作指南
---

# 视频工具的官方说法

访问和核验日期：2026-09-17。没有做供应商横向测试，不提供模型排名、价格、生成限额或保证时长。

## Runway：Image to Video Prompting Guide

官方指南把输入图像当作静态视觉条件，提示词主要描述运动、相机变化和时间推进。[1]

**这本书据此区分**：首帧接续 vs 从零生视频。写图生视频时别忽略首帧已经定下的姿势和构图。

**不能推出**：所有多模态身份参考都等于首帧；文字总能覆盖参考图；这本书写的动作一定会执行。

## Runway：Text to Video 与 Introduction to Prompting

官方资料讨论清楚的描述、时间安排和渐进迭代。[2][3]

**这本书据此保留**：简洁起步，按任务加信息。但不把某个提示词长度定为唯一规则。

## Runway：Gen-4 Video Prompting Guide

这版指南偏向**正向表述**，建议从简单动作逐步添加内容。[4]

**重要边界**：这不是"所有视频模型都不支持负向提示"的证据。具体模型和入口要单独核实。

## Google：视频提示指南

官方指南按主体、动作、环境、拍摄方式等维度说明输入，也提醒部分高级镜头和光学效果的可靠性可能变化。[5]

**这本书据此建议**：把镜头移动、旋转、变焦和观看范围分开写；专业术语要服务于看得见的画面。

**不能推出**：在文本里写焦距就一定得到准确透视；每个模型或聚合平台的接口能力相同。

## OpenAI：Sora2 Prompting Guide（已归档）

核验时页面已明确标为归档，可能涉及过时的模型和 API。[6] 这本书只借用其中一个创作层思路："详细控制和创作开放都可以有效，提示是指导不是保证。"

**不作为**：当前产品是否可用、实际模型规格、生成长度、调用方法或价格的依据。

## 这本书主动不推出的结论

没有从这些页面推出"模型按提示词顺序逐句执行摄影机和演员动作"，也不声称知道具体模型内部为什么偏好某个词。**建议、经验和内部机制是三个不同层级。**

# Citations

[1] [Runway — Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide)

[2] [Runway — Text to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/42460036199443-Text-to-Video-Prompting-Guide)

[3] [Runway — Introduction to Prompting](https://help.runwayml.com/hc/en-us/articles/46182941379347-Introduction-to-Prompting)

[4] [Runway — Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)

[5] [Google — Video generation prompt guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)

[6] [OpenAI — Sora2 Prompting Guide，已归档](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
