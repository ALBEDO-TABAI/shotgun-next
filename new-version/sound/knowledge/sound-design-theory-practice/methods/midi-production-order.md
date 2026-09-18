---
type: Method
title: "MIDI 制作的具体顺序：发音类型→音符连接→句子级表情→发声对齐"
description: "先选对发音采样，再写音符间的间隙/衔接/呼吸，然后做全句目标与回落的表情控制（CC 映射须查所用音源），最后按实际可感起音对齐；随机性只是素材。"
tags: [practice-m4, MIDI, 表情, 人性化, 采样音源]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#4.2 MIDI 制作的具体顺序"
---

# 步骤

1. **先选择发音类型**
   - 长音、短音、连奏采样收到相同音符，也不是相同的演奏动作。
   - 不要先写完一整条机械长音，再期待随机力度修好它。
2. **再写音符连接**
   - 哪些音有间隙、哪些衔接、哪些需要呼吸？
   - 钢琴踏板、弦乐连接、管乐换气不能用同一个"全部拉长 10%"处理。
3. **然后写句子级表情**
   - 先控制全句的目标与回落，再处理单音。
   - 持续音的内部发展可通过音源支持的动态、表情或音色控制实现。
   - **具体 CC 编号与映射必须查所用音源**；不假设 CC1、CC11 对任何音色含义相同。
4. **最后修正发声对齐**
   - MIDI note-on 位置 ≠ 可感知起音。对照实际音频，必要时提前慢起音采样的事件；不为追齐网格切掉自然发音。

# 关于随机性

DeSantis *Humanizing With Automation Envelopes*：包络与细微参数变化可作为电子声音的表达资源。本包建议：**先有意设计句子，再决定是否加入小幅随机性**；随机性是素材，不是表达的替代品（不等同于真人演奏）。

# 关系

- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)（模块 4）
- 应用案例：[持续声部 MIDI 返修例](/cases/sustained-midi-part-revision.md)
- 前置：[节奏设计：先关系后人性化](/methods/rhythm-design-relation-before-humanize.md)、[演奏行为任务](/methods/performer-behavior-task-phrasing.md)
- 符号练习：[MIDI 三版本对照](/exercises/midi-four-bar-motif-comparison.md)（本轮无随机时差与表情控制器）
- 理论对应：[05 声音时间线](/topics/05-sound-timeline.md)（同步不是只有完全卡上或没卡上）

# Citations
[1] [实践知识包 §4.2](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [S15 Dennis DeSantis, Humanizing With Automation Envelopes](/references/s15.md)
