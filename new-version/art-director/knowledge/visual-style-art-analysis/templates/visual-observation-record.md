---
type: Template
title: "单条观察记录（visual_observation）"
description: "asset_version、scope、locator、observation、relation、interpretation、alternatives、not_observable、next_check；字段是表达约定，删字段不等于删证据边界。"
tags: ["part-02", "模板", "观察记录", "YAML"]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/视觉美术分析知识包/二_视觉观察与形式证据.md#十一、推荐的单条观察记录"
---

# Schema

```yaml
record_type: visual_observation
asset_version: "实际材料的明确版本；未知则记录未知"
scope: "整图／局部／镜头／段落"
locator: "图号、区域或已核实的时间区间"
observation: "可回到材料检查的描述"
relation: "对象之间的关系；无足够依据时留空"
interpretation: "与观察分开记录的候选解释"
alternatives: []
not_observable: []
next_check: "只有会改变判断时才填写补证动作"
```

# 用法

这些字段是表达约定，不是必须上数据库的技术要求。没有下游需要的字段可以删除，**但不能把删除字段变成删除证据边界**。

# 关系

- 所属篇章枢纽：[二 视觉观察与形式证据](/topics/02-visual-observation-and-formal-evidence.md)
- locator 的原则：[定位是证据的一部分：陈述必须绑定到对象](/principles/locator-is-part-of-evidence.md)
- 第八篇：结构化知识记录：[最小结构化知识记录（虚构教学模板）](/templates/structured-knowledge-record.md)

# Citations

[1] [二 视觉观察与形式证据 · 十一、推荐的单条观察记录](../../../视觉美术分析知识包/二_视觉观察与形式证据.md)
