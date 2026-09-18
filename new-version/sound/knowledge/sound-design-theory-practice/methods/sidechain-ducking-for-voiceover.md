---
type: Method
title: "旁白侧链避让：不把所有音乐压成随字起伏"
description: "先明确避让整组音乐、一层纹理还是一个频段；先手工在整句窗口减约 2 dB，再考虑有限最大削减与平滑恢复的自动避让；导出分轨后回导核对侧链是否仍有效。"
tags: [practice-m6, 侧链, 避让, 旁白, 分轨导出]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#6.6 侧链避让：不是把所有音乐压成随字起伏"
---

# 机制
外部侧链让另一条信号参与检测，从而控制当前轨的处理；**触发信号**与**被处理信号**是两个角色。[2]

# 步骤
1. 明确对象：整组音乐？一层和声／纹理？一个频段？单一装饰引起冲突时，不必让所有音乐下沉。
2. **教学起点**：先手工把整句所在窗口的音乐减小约 **2 dB**，检查最难懂的字。
3. 仍需自动避让：试**有限的最大削减**和**较平滑的恢复**。
4. 数值不适用于所有素材，以**清晰度与音乐连续性**决定。

# 导出陷阱
导出音乐时把人声静音，某些工程会**同时丢失人声触发**。最终导出文件必须**回导核对**，不能只信工程内播放。

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 更好的第一选择常在编配层：[贯穿案例 C（删领奏的减法版）](/cases/practice-shampoo-four-bar-to-draft.md)、[MIDI 四小节对照练习](/exercises/midi-four-bar-motif-comparison.md)
- 广告混音中的具体交接：[12–17 秒旁白交接](/cases/practice-ad-mix-vo-handoff.md)
- 理论层音乐与人声交接：[05 声音时间线](/topics/05-sound-timeline.md)
- 导出核对：[最终导出与交付检查](/checklists/final-export-delivery-check.md)

* 时间线上的交接设计（05）：[音乐与人声的交接](/methods/music-voice-handoff.md)

# Citations
[1] [实践知识包 §6.6](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [S24 · FabFilter Pro-C 3 Side chain](/references/s24.md)
