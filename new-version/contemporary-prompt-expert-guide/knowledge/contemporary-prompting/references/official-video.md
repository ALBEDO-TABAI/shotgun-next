---
type: Reference
title: 第一方依据：视频提示、运动与任务适配
description: 记录当前指导和历史参考的区别，避免把供应商建议提升为通用机制。
tags:
- 官方
- 视频
- 版本
timestamp: '2026-09-18'
source:
- Runway官方文档
- Google官方文档
- OpenAI归档创作指南
---

# 第一方依据：视频提示、运动与任务适配

访问与核验日期：2026-09-17。没有做供应商横向性能测试，不提供当前模型排名、价格、生成限额或保证时长。

## V01｜Runway：Image to Video Prompting Guide

官方指南把输入图像作为静态视觉条件，提示主要描述运动、相机变化与时间推进。[1]

**用途**：本书区分首帧接续与从零生视频，提醒不要忽略首帧的姿势和构图。

**不支持**：所有多模态身份参考都等于首帧；文字总能覆盖参考图；本书所写动作必然执行。

## V02｜Runway：Text to Video与Introduction to Prompting

官方资料讨论清楚的描述、时间安排与渐进迭代。[2][3] 本书据此保留简洁起步和按任务增加信息，但不将某一提示长度设为唯一规则。

## V03｜Runway：Gen-4 Video Prompting Guide

这一版本的指南偏向正向表述，并建议从简单动作逐步添加内容。[4]

**重要边界**：这不是“所有视频模型不支持负向提示”的证据。具体模型与入口应单独核实。

## V04｜Google：视频提示指南

官方指南按主体、动作、环境和拍摄方式等维度说明输入，也提醒部分高级镜头与光学效果的可靠性可能变化。[5]

**用途**：把镜头移动、旋转、变焦与观看范围分开描述；专业术语应服务可观察的画面。

**不支持**：在文本里写焦距就一定获得准确透视；每个模型或聚合平台接口有相同能力。

## V05｜OpenAI：Sora2 Prompting Guide，历史创作参考

核验时页面已明确标为归档，可能涉及过时模型与API。[6] 本书仅借用其中“详细控制与创作开放均可有效，提示是指导而非保证”的创作层思路。

**不作为**当前产品是否可用、实际模型规格、生成长度、调用方法或价格的依据。

## 本书主动不采用的推论

未从这些页面推出“模型按提示词顺序逐句执行摄影机与演员动作”，也不声称知道具体模型内部为何偏好某个词。建议、经验与内部机制是不同层级。

# Citations

[1] [Runway — Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide)

[2] [Runway — Text to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/42460036199443-Text-to-Video-Prompting-Guide)

[3] [Runway — Introduction to Prompting](https://help.runwayml.com/hc/en-us/articles/46182941379347-Introduction-to-Prompting)

[4] [Runway — Gen-4 Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)

[5] [Google — Video generation prompt guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)

[6] [OpenAI — Sora2 Prompting Guide，已归档](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)
