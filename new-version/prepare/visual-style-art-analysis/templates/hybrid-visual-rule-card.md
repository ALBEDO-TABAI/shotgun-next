---
type: Template
title: "混合视觉最小规则卡（hybrid_visual_rule）"
description: "scope、source_relations（参照／证据状态／所借关系）、transformation、organizing_rule、preserved、excluded、allowed_variations、exceptions、failure_condition。"
tags: ["part-03", "模板", "规则卡", "YAML"]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/视觉美术分析知识包/三_混合风格与融合规则.md#十一、最小规则卡"
---

# Schema

```yaml
rule_type: hybrid_visual_rule
scope: "一个场景、段落或系列的明确范围"
source_relations:
  - reference: "明确参照或待确认来源"
    evidence_status: "明确引用／形式相似／未知"
    borrowed_relation: "不是只填物件名"
transformation: "被改变的尺寸、材料、角色、维度或顺序"
organizing_rule: "哪些选择共同组织整体"
preserved: []
excluded: []
allowed_variations: []
exceptions: []
failure_condition: "什么变化会使主要机制失效"
```

# 关系

- 所属篇章枢纽：[三 混合风格与融合规则](/topics/03-hybrid-styles-and-fusion-rules.md)
- 参照单元记录：[参照单元记录：来源—所借特征—证据—作用范围—变换—未保留部分](/templates/reference-unit-record.md)
- 第八篇：规则卡句式：[规则卡句式：带条件的提议](/templates/rule-card-sentence.md)

# Citations

[1] [三 混合风格与融合规则 · 十一、最小规则卡](../../../视觉美术分析知识包/三_混合风格与融合规则.md)
