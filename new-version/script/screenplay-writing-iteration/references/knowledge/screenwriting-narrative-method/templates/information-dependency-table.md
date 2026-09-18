---
type: Template
title: 信息表：只管理关键依赖，不穷尽世界
description: 为会影响行动、误会、揭示和改编的少数事实建一张状态表（命题、世界状态、呈现位置、各方知识前后、推断依据、未确立项、复查依赖）。
tags: [topic-07, 模板, 信息表, 版本维护]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/07_信息分配留白与揭示设计.md#十一、信息表：只管理关键依赖，不穷尽世界
---

# 模板

```yaml
fact_id: F07
proposition: 父亲没有丢掉旧物
world_status: 本版本确立
presentation: S03开箱后旧物可见
father_state: 知道
daughter_before: 怀疑已丢
daughter_after: 知道未丢
viewer_before: 未明确
viewer_at_S03: 直接看到
inference: 父亲保存并整理
inference_support: 旧标签与已有整理习惯
not_established: 父女所有矛盾已解决
recheck_dependencies: [空桌面, 开箱镜头, 结尾表情与文案]
```

# 字段说明

| 字段 | 含义 |
|---|---|
| `proposition` | 一条会影响行动、误会、揭示或改编的事实命题 |
| `world_status` | 本版本是否确立（也可为"刻意未定"） |
| `presentation` | 观众在哪个位置、通过什么通道实际获得 |
| `<人物>_state` / `_before` / `_after` | 各人物在关键点前后的知识状态 |
| `viewer_before` / `viewer_at_*` | 观众在关键点前后的状态（用五档理解状态） |
| `inference` / `inference_support` | 期望观众形成的推断及其画面内依据 |
| `not_established` | 作品**没有**声称的事，防止过度归因 |
| `recheck_dependencies` | 改动时必须一起复查的镜头、道具、文案 |

# 使用规则

- 看见旧物和确定谁整理是两件事，后者需要归因依据。
- 改开场（例如从顺序 A 换到 B）后，信息表和相关执行要一起更新；B 不能沿用 A 的"观众开场已知"。
- 不为每个生活细节建档。只记录会影响行动、误会、揭示和改编的事项，其他保留在普通文本中。
- 深化应用建议为关键揭示补三项："最早允许明确"、"此前允许哪些线索"、"后续哪些行动依赖已知"。

# 关系

- 上位主题：[本篇枢纽](../topics/07-information-design.md)
- 字段的状态定义：[最小信息模型](../frameworks/minimal-information-model.md)。
- 示例数据来自：[一箱旧物，三种顺序](../cases/box-of-old-things-three-orders.md)。
- 版本变化时的复查：[信息泄露与版本流失检查](../checklists/information-leak-and-version-loss.md)。
- 人物侧对应的最小设定记录：[最小人物与世界模型](../methods/minimal-character-world-model.md)。
- 作为交接物的一部分：[最小交接卡](minimal-handoff-card.md)、[最小协作架构](../frameworks/minimal-collaboration-architecture.md)。

# Citations
[1] 07 信息分配留白与揭示设计 §十一（历史来源定位：`../../../07_信息分配留白与揭示设计.md`；原文件未随上传包提供）
