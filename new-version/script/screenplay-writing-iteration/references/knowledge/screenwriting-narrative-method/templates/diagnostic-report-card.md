---
type: Template
title: "诊断报告卡（issue card）"
description: "单个问题的 YAML 报告卡：范围、观察、假设、替代解释、需保护机制、候选修改、代价、验证方式与状态，使每条诊断意见可回看、可替换、可验证。"
tags: [topic-11, 模板, 报告卡, 诊断]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/11_作品分析诊断与证据化评价.md#八、完整诊断练习：门口的箱子（示例报告卡）
---

# Schema

| 字段 | 含义 |
|---|---|
| issue_id | 问题编号 |
| scope | 结论适用的材料范围 |
| observed | 实际观察到的材料事实 |
| hypothesis | 对问题机制的假设 |
| alternative | 竞争解释，或"现状可能足够"的条件 |
| protected | 修改时不能破坏的有效机制 |
| candidate_fix | 候选最小修改 |
| cost | 修改的代价 |
| verification | 怎样验证 |
| status | 当前状态（例如：教学诊断、非真实看片结果） |

# Examples

```yaml
issue_id: DOOR-R01
scope: 上述自拟片段
observed: 邀请主要通过"往里放"，未显示实际进入
hypothesis: 关系许可可能缺少动作确认
alternative: 若目标只到发出邀请，现状可能足够
protected: 日常事务承载关系的表达方向
candidate_fix: 呈现腾出位置与箱子进入
cost: 增加动作时间或改变镜头范围
verification: 简易走位与无主题提示首看
status: 教学诊断，非真实看片结果
```

# 使用规则
- status 必须来自实际工作：教学诊断、未测试、已测试等，不把"写了字段"当作状态已发生。
- alternative 不是可选项，它防止把单一解释当成事实。
- protected 来自第一遍记录中的有效部分。

# 关系
- 上位主题：[本篇枢纽](../topics/11-close-reading-diagnosis.md)
- 示范来自 [门口的箱子诊断练习](../cases/box-at-the-door-diagnosis.md)；字段生成过程见 [症状—原因—方案诊断](../methods/symptom-cause-solution-diagnosis.md)。
- 多张报告卡汇总进入 [分析报告结构](analysis-report-structure.md)。
- 字段与第十二篇 [统一 skill 接口](../skills/unified-skill-interface.md) 的统一输出（protected_relations / tradeoffs / next_validation / status）对齐；与第八篇 [决策记录](decision-record.md) 互补。

# Citations
[1] 11 作品分析诊断与证据化评价 §八 示例报告卡（历史来源定位：`../../../11_作品分析诊断与证据化评价.md`；原文件未随上传包提供）
