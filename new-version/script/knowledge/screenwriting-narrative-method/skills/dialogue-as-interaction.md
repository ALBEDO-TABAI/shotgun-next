---
type: Skill Interface
title: "skill：dialogue-as-interaction"
description: 对白模块的输入（前后文、人物知识、关系与任务、必要信息、语言风格、目标媒介）、八步操作与关键轮次 YAML 输出模板；只标对理解和执行有影响的轮次。
tags: [topic-06, skill, 对白, 接口]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/06_对白潜台词与话语行动.md#十二、skill：dialogue-as-interaction
---

# 启动条件

语言与互动不成立：人物没有理由此刻这样说、上一句没改变下一句、人物替作者交代材料、风格与作品约定不符。

# 输入

- 场景前后文
- 人物当前知识
- 关系与任务
- 必须传递的信息
- 语言风格
- 目标媒介

孤立台词只允许局部判断，不足以确认全片人物一致性。

# 操作

1. 写不含对白的行动简述
2. 列双方需要与共同知识
3. 拟互动流
4. 检查回应是否改变策略
5. 明确必要信息载体
6. 润色声音
7. 放回动作与时间
8. 试读或简易表演

# 输出模板

```yaml
scene_id: UMBRELLA-01
utterance: 这个别换
referent: 原木柄
speaker_action: 指定不可替换的部件
uptake: 修理者追问其他部分是否可换
viewer_requirement: 木柄对顾客重要
not_established: 木柄的完整家族来历
alternative_reading: 也可能只是使用偏好
protected: 指称可见、许可获得确认
validation_status: 自拟稿，未试读
```

- 不为每个语气词建记录，只标对理解和执行有影响的关键轮次。
- 交付应包含：可读场景稿、关键互动说明、必要替代方案、试读问题；不把心理解释全部塞进正文。

# 不应自动做什么

- 不把每句都改成潜台词或金句。
- 不自行更改人物已知信息或场景目标（属第 04、05、07 篇）。

# 关系

- 上位主题：[本篇枢纽](/topics/06-dialogue-as-interaction.md)
- 八步操作的顺序对应 [对白改写三轮](/methods/dialogue-rewrite-three-rounds.md)；步骤 4 依据 [对话作为随反馈变化的策略](/frameworks/dialogue-as-strategy-under-feedback.md)；步骤 5 依据 [说明性对白的三个决定](/methods/exposition-dialogue-decisions.md)。
- 输出模板中的 `utterance` 取自 [修伞店协商案例](/cases/umbrella-repair-shop-negotiation.md)。
- `validation_status` 与统一状态含义（proposal/current/consumed/checked）见 [统一 skill 接口](/skills/unified-skill-interface.md)；本模块在总表中的启动条件与"不应自动做什么"见 [按问题调用模块](/methods/call-modules-by-problem.md)。
- 输入依赖：人物知识与策略来自 [character-relation-world-model](/skills/character-relation-world-model.md)，场景任务来自 [scene-plot-and-rhythm-design](/skills/scene-plot-and-rhythm-design.md)，信息安排来自 [information-design-and-reveal](/skills/information-design-and-reveal.md)。
- 交付后的执行约束见 [对白交接给执行](/templates/dialogue-handoff-to-execution.md)。

# Citations
[1] [06 对白潜台词与话语行动 §十二](../../../06_对白潜台词与话语行动.md)
