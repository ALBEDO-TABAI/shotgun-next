---
type: Template
title: "最小结构化知识记录（虚构教学模板）"
description: "record_id/version/kind、source（asset_id/version/available_material/locator）、scope、observation、interpretations（含 author 与 alternatives）、production_fact、transfer_rule、validation、active_project_decision；未知保持 null。"
tags: ["part-08", "模板", "知识记录", "YAML"]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/视觉美术分析知识包/八_分析沉淀与知识复用.md#十一、一份最小的结构化示例"
---

# Schema（虚构教学模板：无真实图像资源，资源标识与定位保持空值）

```yaml
record_id: example_scale_environment_001
record_version: 1
record_kind: teaching_example
source:
  asset_id: null
  asset_version: null
  available_material: fictional_text_description
  locator: null
scope: single_concept_description
observation:
  statement: 描述设定中，叶片大于产品并形成前后遮挡
  evidence_kind: supplied_description
interpretations:
  - statement: 植物可能从成分陪衬转变为主体所处的环境
    kind: analytical_hypothesis
    author: knowledge_pack_example
    support: observation
    alternatives:
      - 仍可能只被理解为巨型道具展示
production_fact:
  actual_material: null
  actual_method: null
transfer_rule:
  problem: 小型象征元素没有参与空间表达
  operation: 将元素转化为可组织前后关系的空间结构
  preserve:
    - 能够辨认的尺度关系
    - 与新任务相关的主体和环境关系
  may_change:
    - 具体元素
    - 配色
    - 物理或数字实现方式
  failure_conditions:
    - 裁切删除了关键尺度线索
    - 元素仅被放大但没有构成空间关系
validation:
  performed: false
  required: 实际图像检查与符合任务的观看反馈
active_project_decision: null
```

# 用法

- 不要求采用 YAML，更不要求照搬字段；关键是保留来源、身份、范围和使用条件。
- 真实项目至少要补齐：替换为实际可访问材料；记录真实版本和定位；区分可见事实与文本转述；确定当前任务；说明谁作判断及哪些检查已完成；只有实际确认发生后才写入批准范围。
- 如果某个值仍然未知，**保持未知比填一个看起来合理的猜测更有用**。

# 关系

- 所属篇章枢纽：[八 分析沉淀与知识复用](/topics/08-knowledge-capture-and-reuse.md)
- 第二篇：观察记录：[单条观察记录（visual_observation）](/templates/visual-observation-record.md)
- 解释是有人提出的主张：[解释是有人提出的主张：写清谁、基于什么材料；允许多重解释并存但不等量齐观](/principles/interpretation-is-an-authored-claim.md)
- 对应的迁移案例：[虚构案例：从植物庭院决策卡到新任务的迁移链](/cases/fictional-plant-courtyard-transfer-chain.md)

# Citations

[1] [八 分析沉淀与知识复用 · 十一、一份最小的结构化示例](../../../视觉美术分析知识包/八_分析沉淀与知识复用.md)
