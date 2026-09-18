---
type: Reference
title: 配音和灯光的官方说法
description: 两个容易被误传的技术点：省略号不等于固定停顿秒数；硬光不等于亮。只校准概念，不用软件文档证明艺术效果。
tags:
- 官方
- 配音
- 光线
timestamp: '2026-09-18'
source:
- ElevenLabs 官方文档
- Blender 5.2 LTS Manual
---

# 配音和灯光的官方说法

访问和核验日期：2026-09-17。

## ElevenLabs：停顿和模型语法

官方说明区分了不同模型的停顿控制方式：Eleven v3 用相关音频标签，而不是相同的 SSML break 方法；其他模型的支持各不相同；**标点形成的停顿也不如专门的控制稳定。**[1][2]

**这本书据此提醒**：别把"……"当成跨工具固定的 0.3 秒。台词和说明要按实际接口分开，时长要试听确认。

**没有推出**：哪种声线更真实、哪种情绪提示效果最好。也没有一张所有供应商通用的标签表。

## Blender：Light Objects

这次成功核验的是 Blender 5.2 LTS 多语言手册页面，相关灯光说明为英文。手册把光源的**功率**和**半径 / 尺寸**分开说明：尺寸影响阴影软硬；聚光光束的边缘和物体投影的边缘也不是一回事。[3]

**这本书据此校准**：硬光不等于亮；光源方向不等于轮廓效果；百叶窗不是硬光成立的前提。

**没有推出**：AI 视频内部按 Blender 的渲染器计算；任何提示词能获得摄影测量级的精度。材质、拍摄和后期的具体设计仍然是这本书的创作建议。

## 核验路径说明

之前的复审包保留了旧版 Blender 英文链接。这次那个入口读取不成功，所以不宣称重新读到了那个旧页面，改用成功取得的 5.2 LTS 页面核验稳定概念。不由此推荐特定软件版本。

# Citations

[1] [ElevenLabs — How can I add pauses?](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-can-i-add-pauses)

[2] [ElevenLabs — Do pauses and SSML phoneme tags work with the API?](https://elevenlabs.io/docs/help-center/technical/do-pauses-and-ssml-phoneme-tags-work-with-the-api)

[3] [Blender 5.2 LTS Manual — Light Objects](https://docs.blender.org/manual/nl/5.2/render/lights/light_object.html)
