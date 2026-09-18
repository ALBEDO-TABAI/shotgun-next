---
type: Framework
title: "合成声音的最小可理解链"
description: "激励／振荡源 → 频谱塑形 → 振幅与音高随时间变化 → 空间与其他处理；先调发音时间形态常比换预设更有效，ADSR 的 sustain 是电平不是时长。"
tags: [practice-m5, 合成, 包络, ADSR, 音色]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#5.3 合成声音的最小可理解链"
---

# 模型
~~~text
激励／振荡源 → 频谱塑形（滤波） → 振幅与音高随时间变化（包络／调制） → 空间和其他处理
~~~
Ableton 乐器手册给出振荡器、噪声、滤波器、放大器、包络及调制等组件的实现示例（来源支持：机制说明）。[2]

# 要点
- **联想不是结论**："正弦波＝纯净""噪声＝空气"只是初始联想，不能跳过试听；同一声源经过不同包络与上下文可被听成不同事件。
- **先调时间形态**：解决"太硬／太黏／拖沓"时，先调发音包络，常比不断换预设有效。
- **ADSR 常见误解**：sustain 通常是**维持电平**而非持续秒数；release 是收到结束后怎样衰减。
- **最终持续时间不只看 MIDI 音长**：采样自带尾部、滤波包络、混响都参与。

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 与三层拆法对应：[起音—主体—尾部](/frameworks/attack-body-tail-three-layers.md)
- 在音色描述上的上游：[04 声音描述语言](/topics/04-sound-description-language.md)
- 应用：[配方 B 水滴到音乐短音](/recipes/water-drop-to-musical-note.md)（合成短音的起音／衰减起点）
- MIDI 音长 ≠ 实际停止时间，同见 [贯穿案例 B 时间结构](/cases/practice-shampoo-time-structure-118bpm.md)

# Citations
[1] [实践知识包 §5.3 合成声音的最小可理解链](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [S19 · Ableton Live Instrument Reference](/references/s19.md)
