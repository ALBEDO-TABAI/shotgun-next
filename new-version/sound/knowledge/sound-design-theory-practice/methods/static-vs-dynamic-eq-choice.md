---
type: Method
title: "静态 EQ 与动态 EQ 怎样选"
description: "频率持续过多用静态 EQ，只在部分音节／重击出现时试动态 EQ；先考虑移开冲突音，再在相关时刻压低频带，并检查削减的代价。"
tags: [practice-m6, EQ, 动态EQ, 旁白清晰度]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音创作与制作_实践知识包/声音创作与制作_实践知识包.md#6.4 静态 EQ 与动态 EQ 怎样选"
---

# 判断
| 情况 | 先试 |
|---|---|
| 某段频率**持续**过多 | 静态 EQ |
| 只在部分音节、重击或某些音符出现 | 动态 EQ（频段增益随检测信号变化，可内部或外部触发）[2] |

# Examples
教学例：音乐中某个明亮短音只在旁白关键字上冲出来。
1. 先比较**移开这个短音**；
2. 必须保留时，再试**只在相关时刻**压低对应频带；
3. 不要在没有冲突频率证据时，预先给全曲中频挖固定坑。

# 代价检查
- 主旋律是否失去身份？
- 旁白是否变薄？
- 人声结束后音乐是否自然恢复？

效果器的好处必须与失去的内容一起评估。

# 关系
- 上位主题：[实践包主枢纽](/topics/p-sound-creation-production.md)
- 前一步：[频率冲突的排查顺序](/checklists/frequency-conflict-triage-order.md)
- 另一种按触发避让：[侧链避让](/methods/sidechain-ducking-for-voiceover.md)

# Citations
[1] [实践知识包 §6.4](../../../声音创作与制作_实践知识包/声音创作与制作_实践知识包.md)
[2] [S21 · FabFilter Pro-Q 4 Dynamic EQ](/references/s21.md)
