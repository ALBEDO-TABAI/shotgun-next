---
type: Reference
title: 第一方依据：配音停顿与灯光软硬
description: 只校准容易误传的技术概念，不用软件文档证明艺术效果。
tags:
- 官方
- 配音
- 光线
timestamp: '2026-09-18'
source:
- ElevenLabs官方文档
- Blender 5.2 LTS Manual
---

# 第一方依据：配音停顿与灯光软硬

访问与核验日期：2026-09-17。

## A01｜ElevenLabs：停顿与模型语法

官方说明区分不同模型的停顿控制方式：Eleven v3使用相关音频标签而非相同的SSML break方法；其他适用模型的支持不同，标点形成的停顿也不如专门控制稳定。[1][2]

**本书据此提醒**：别把“……”当成跨工具固定0.3秒；台词与说明应按实际接口分离，时长需要试听确认。

**并未推出**：哪种声线更真实、哪种情绪提示效果最好，也没有提供所有供应商通用的标签表。

## L01｜Blender：Light Objects

本次成功核验的是Blender 5.2 LTS多语言手册页面，其中相关灯光说明为英文。手册将光源功率与半径/尺寸分开说明：尺寸影响阴影软硬；聚光光束边缘与物体投影边缘也不是一回事。[3]

**本书据此校准**：硬光不等于亮，光源方向不等于轮廓效果，百叶窗不是硬光成立的前提。

**并未推出**：AI视频内部按Blender的渲染器计算，或任何提示能获得摄影测量级的精度。涉及材质、拍摄与后期的具体设计，仍是本书的创作建议。

## 核验路径说明

此前复审包保留了旧版Blender英文链接。本次该入口读取未成功，因此没有宣称本次重新读到那个旧页面，改用成功取得的5.2 LTS页面核验稳定概念。不由此推荐特定软件版本。

# Citations

[1] [ElevenLabs — How can I add pauses?](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-can-i-add-pauses)

[2] [ElevenLabs — Do pauses and SSML phoneme tags work with the API?](https://elevenlabs.io/docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api)

[3] [Blender 5.2 LTS Manual — Light Objects](https://docs.blender.org/manual/nl/5.2/render/lights/light_object.html)
