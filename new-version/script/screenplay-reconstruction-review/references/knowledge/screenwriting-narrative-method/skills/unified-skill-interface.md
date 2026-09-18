---
type: Skill Interface
title: "统一 skill 接口：iterative-screenwriting-workflow 与全包统一输入／输出"
description: 本包各模块共用的输入结构（material/request/context）、输出结构（result 十二字段）、状态词含义（proposal/current/consumed/checked）与限制声明；是知识接口示例，不是可安装的 skill 包。
tags: [topic-12, skill接口, 统一输入输出, 状态]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/12_创作迭代验证与协作交付流程.md#十六、统一skill接口建议
---

# 定位

本包提供理论与知识、操作方法和接口范例，**不是可直接安装执行的技能实现**。实际系统需要实现读取、版本、权限和工具调用，并由真实执行结果确认状态。

# 统一输入（全包共用）

```yaml
material:
  artifact: 当前作品或创作材料
  version: 当前版本
  scope: 全片、序列、场景或单图
  completeness: 完整或明确缺失项
request:
  mode: analyze
  question: 当前要解决的具体问题
context:
  purpose: 已知或明确未知
  form_profile: 现有或待建立
  facts: 有来源的事实
  assumptions: 明确标记的创作假设
  constraints: 实际要求与资源条件
```

输入不完整时，先判断缺失是否影响当前问题：能局部回答就限定范围，不能回答就给出需要获取的材料，不擅自补全。

# 统一输出（全包共用）

```yaml
result:
  scope: 结论适用范围
  observation: 实际材料
  interpretation: 机制假设与竞争解释
  intention_evidence: 来源或未知
  reception_evidence: 实测或未测
  decision: 当前选择及理由
  protected_relations: 不能无说明破坏的关系
  flexible_execution: 可替换的具体方式
  tradeoffs: 获得与损失
  next_validation: 对象、方法与条件
  consumers: 谁需要实际使用
  status: proposal
```

# 状态词的含义（必须来自实际工作）

| 状态 | 含义 |
|---|---|
| proposal | 提议，不用于执行 |
| current | 已选为当前执行，带适用范围 |
| consumed | 相关使用者已理解并使用 |
| checked | 实际成果已经检查 |

字段写了不等于状态发生；原型检查通过不等于受众效果普遍成立。

# 第十二篇的创作模式接口：iterative-screenwriting-workflow

```yaml
skill_name: iterative-screenwriting-workflow
mode: create
inputs:
  material_version: required
  purpose: known_or_explicitly_unknown
  form_profile: provisional
  facts_and_constraints: sourced
  current_question: required
outputs:
  current_artifact: script_or_relevant_prototype
  decision_record: essential_only
  uncertainties: explicit
  affected_consumers: identified
  next_validation: actionable
states:
  proposal: not_for_execution
  current: selected_with_scope
  consumed: understood_and_used
  checked: actual_result_reviewed
limits:
  audience_simulation_is_not_audience_data: true
  invented_motive_is_not_source_fact: true
  completion_does_not_mean_universal_effectiveness: true
```

# 适用边界 / 不应自动做什么

- 不为了对应模块名称建立十一位 Agent，也不要求每个物料经过全部流程。
- 输出中的 `intention_evidence` 与 `reception_evidence` 必须写"来源／未知""实测／未测"，不能空缺或猜测。

# 关系

- 上位主题：[本篇枢纽](../topics/12-iteration-and-handoff.md)
- 各篇专属 skill 的输入／输出在此结构上细化，路由见 [按问题调用模块](../methods/call-modules-by-problem.md)。
- `status` 四态对应 [最小协作架构](../frameworks/minimal-collaboration-architecture.md) 的"一项决定需要四个状态"。
- 输入中的 facts/assumptions 区分依据 [四类输入与不确定性](../frameworks/four-input-types-and-uncertainty.md)；`protected_relations` 的示范见 [护肤片五个关键关系](../cases/skincare-film-five-protected-relations.md)。
- limits 三条对应 [人工与 AI 协作的保留条件](../principles/human-ai-collaboration-conditions.md)。

# Citations
[1] 12 创作迭代验证与协作交付流程 §十六（历史来源定位：`../../../12_创作迭代验证与协作交付流程.md`；原文件未随上传包提供）
[2] skill 接口与调用总表：定位、统一输入、统一输出（历史来源定位：`../../../00_skill接口与调用总表.md`；原文件未随上传包提供）
