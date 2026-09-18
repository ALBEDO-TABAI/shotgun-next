---
type: Template
title: "事件表 + 关系表（阶段 C）"
description: "只有事件表容易变成音效采购单；关系表记录每个声音与谁融合、与谁分离、接替谁、遮蔽谁、揭示什么、维持什么未知。"
tags: [topic-01, 事件表, 关系表, 阶段C, 模板]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/一.md#阶段 C：同时建立“事件表”和“关系表”"
---

# Schema
**事件表**
| 声音 | 位置（时间码／文字边界） | 怎样出现 | 怎样变化 |
|---|---|---|---|

**关系表**
| 声音 | 与谁融合 | 与谁分离 | 接替谁 | 遮蔽谁 | 揭示什么 | 维持什么未知 |
|---|---|---|---|---|---|---|

# Examples
| 只是事件 | 是关系 |
|---|---|
| 瓶盖声在产品开启时出现。 | 瓶盖声完成后，音乐中原本紧密的纹理开始展开；不再额外增加转场冲击。 |

# 关系
- 流程位置：[五阶段](/methods/auditory-world-design-five-stages.md) 阶段 C；上位 [01 枢纽](/topics/01-auditory-world.md)
- 关系列的理论依据：[听觉场景分析](/frameworks/auditory-scene-analysis-tracks-vs-streams.md)、[前景交接](/principles/foreground-handoff-over-occupation.md)
- 生产化：[05 声音时间线](/topics/05-sound-timeline.md)（点位表到生产表）、[07 案例](/topics/07-shampoo-ad-case.md)（音效资产蓝图：事件、关系与来源分开）

# Citations
[1] [一.md 阶段 C：同时建立“事件表”和“关系表”](../../../声音设计理论与方法_二至十/一.md)
