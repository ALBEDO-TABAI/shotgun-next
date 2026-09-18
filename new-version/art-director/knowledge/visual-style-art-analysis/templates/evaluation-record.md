---
type: Template
title: "最小评价记录（虚构模板）"
description: "work_version、scope、purpose、criterion（name/reason）、observation（statement/source）、judgment（status/statement/limitation）、preserve、candidate_change、verification、approval_scope。"
tags: ["part-07", "模板", "评价记录", "YAML"]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/art-director/视觉美术分析知识包/七_作品评价与反馈验证.md#十一、最小记录示例"
---

# Schema（虚构示例，不是真实项目记录）

```yaml
example_status: fictional_template
work_version: concept_B_v1
scope: single_still_concept
purpose: brand_image
criterion:
  name: spatial_scale_relationship
  reason: 让植物从陪衬转变为产品所处的环境
observation:
  statement: 方案描述中叶片与产品交叠，叶片尺度被放大
  source: supplied_concept_description
judgment:
  status: needs_visual_test
  statement: 这一关系具有概念潜力，尚不能确认成图效果
  limitation: 尚未提供可检查的渲染图或受众材料
preserve: 放大植物构成环境的关系
candidate_change: 仅在包装必要信息处调整遮挡
verification:
  question: 尺度关系与必要产品信息能否同时保留
  evidence_required: 同条件方案图与实际输出检查
approval_scope: null
```

# 用法

不要把示例中的状态转换成真实项目已完成的记录。结构服务于判断，不要求所有日常讨论都先填表。

# 关系

- 所属篇章枢纽：[七 作品评价与反馈验证](/topics/07-evaluation-feedback-and-validation.md)
- judgment.status：[证据＋状态，而不是单一分数：成立、存在风险、未成立、证据不足、不适用](/frameworks/evidence-status-not-score.md)
- approval_scope：[从评审意见走向修改与验收：三类事项与批准范围](/methods/review-to-revision-acceptance.md)

# Citations

[1] [七 作品评价与反馈验证 · 十一、最小记录示例](../../../视觉美术分析知识包/七_作品评价与反馈验证.md)
