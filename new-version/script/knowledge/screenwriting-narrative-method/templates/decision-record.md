---
type: Template
title: 评审决策记录
description: 把评审意见列表转成决策记录的最小字段：采用的修改、解决的问题、依据、接受的损失、验证方式，以及未采用的重要意见及原因。
tags: [topic-08, 模板, 决策记录, 评审]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/08_表达精准度有效性与审美判断.md#深化应用：评审分歧怎样形成可推进的讨论
---

# 用途

避免下次会议同一问题重新启动却失去历史。只有改变任务、理解或执行的决定才需要记录；普通形容词式意见不入记录。

# Schema

| 字段 | 内容 |
|---|---|
| 采用的修改 | 具体改动与位置 |
| 解决的问题 | 该修改针对哪个已确认的问题（事实 / 机制 / 标准 / 执行） |
| 依据 | 可回看的材料、试演或测试结果 |
| 接受的损失 | 明确放弃什么（余味、共同发现、动作留白……） |
| 验证方式 | 对象、方法、条件 |
| 未采用的重要意见 | 意见内容 + 未采用原因（偏好、超出任务、证据不足……） |

# Examples

```yaml
decision: D08-03
version: roughcut_v03
change: 女儿先提出"来之前发消息"的条件，父亲接受
problem: 机制分歧——推回钥匙可读为许可也可读为控制
basis: 试演两版；内部三人首看中两人读成控制
loss: 增加两句对白，减少动作留白
validation: 不提示主题的首看，问"钥匙谁决定怎么用"
rejected:
  - opinion: 加童年回忆闪回
    reason: 属于方案而非问题；更小线索已能解决
```

# 关系

- 上位主题：[本篇枢纽](/topics/08-expression-evaluation.md)
- 产生此记录的流程见 [评审分歧形成可推进讨论](/methods/review-disagreement-to-decision.md)。
- 与第 12 篇 [最小协作架构](/frameworks/minimal-collaboration-architecture.md) 中“一项决定需要四个状态”配合使用；与第 02 篇 [修改记录：旧决定为什么不再有效](/checklists/deliverable-completion-criteria.md) 同属版本历史。
- 字段与 [J08 判断记录](/skills/evidence-based-expression-review.md) 互补：J08 记判断，本记录记决定。

# Citations
[1] [08 表达精准度有效性与审美判断 深化应用](../../../08_表达精准度有效性与审美判断.md)
