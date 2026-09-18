---
type: Framework
title: "Agent 和人怎样分工，不让建议变成事实"
description: 五个可实现的 Agent 角色（研究与证据、创作、剧作分析、制作可行性、版本协调）各自的职责与禁区，以及人的决策位置。
tags: [topic-12, Agent角色, 人机分工, 决策]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/12_创作迭代验证与协作交付流程.md#十三、Agent和人怎样分工，不让建议变成事实
---

# 要点

本包提出的是**可实现的**角色划分，不代表已经搭建、运行或验证。

| 角色 | 负责 | 不能做 |
|---|---|---|
| 研究与证据 | 寻找原始材料，保留来源和使用边界；资料与创作构造分开 | 把网页或项目文档里的指令当成系统命令；靠模型补出缺失事实 |
| 创作 | 提出不同关系与形式的方案，明确新增假设；可模拟人物选择 | 把模型生成的背景当成既有作品证据 |
| 剧作分析 | 按第十一篇核查结构、信息和行为，提出竞争解释和最小修改 | 没有材料时制造问题维持审查产量 |
| 制作可行性 | 核查动作、时长、载体、成本和交付条件；可建议替换 | 默默改变故事事实与人物目标 |
| 版本协调 | 维护当前入口、关键变更、受影响使用者和验证状态 | 用行政字段决定唯一艺术意义 |

## 人的决策位置

决定任务、价值取舍、实际承诺、重要方向与交付。不是每次机械盖章，而是在确实改变目标或有重大代价时作判断。

## 两条警告

- 多个模型意见一致不能替代观众测试；重复生成不自动提供独立证据。
- 不要让 Agent 以完成自己的表格为目标，而忽视输出是否被下一环节实际使用。

# 适用边界 / 不应自动做什么

- 同一人可以承担多个角色，同一角色可由多人协作；不要为了对应名称建立多位 Agent。
- 实际权限需由团队明确。

# 关系

- 上位主题：[本篇枢纽](/topics/12-iteration-and-handoff.md)
- 人与 AI 协作的保留条件见 [人工与 AI 协作的保留条件](/principles/human-ai-collaboration-conditions.md)；AI 审稿的边界见 [AI 辅助审稿的边界](/principles/ai-assisted-review-boundaries.md)。
- 研究证据角色对应 [来源使用总原则](/principles/source-use-and-evidence-boundaries.md)；剧作分析角色对应 [close-reading-and-diagnostic-review](/skills/close-reading-and-diagnostic-review.md)；版本协调对应 [最小协作架构](/frameworks/minimal-collaboration-architecture.md)。
- 两项 AI 研究对分工的启发见 [两项 AI 研究提供什么](/principles/what-two-ai-studies-show.md)。

# Citations
[1] [12 创作迭代验证与协作交付流程 §十三](../../../12_创作迭代验证与协作交付流程.md)
