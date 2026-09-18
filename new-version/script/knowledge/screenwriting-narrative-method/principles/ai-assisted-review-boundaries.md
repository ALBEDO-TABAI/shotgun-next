---
type: Principle
title: "AI 辅助审稿：有条理的意见仍可能漏掉主要问题"
description: "使用模型审稿的五条边界：先取证再评价、多角度优于重复问好不好、人保留问题与方向的决定、生成的内心独白只是解释候选、反馈要进入版本状态。"
tags: [topic-11, AI审稿, 人机协作, 边界]
timestamp: 2026-09-18T00:00:00Z
source: new-version/script/11_作品分析诊断与证据化评价.md#十、AI辅助审稿：有条理的意见仍可能漏掉主要问题
---

# 研究依据与其限度

Rashkin 等人的研究用英语短篇、受控文本扰动和特定模型评估写作反馈：具体、结构良好的建议仍可能漏检更重要的问题，且有过度肯定倾向。本包查阅了作者公开全文；**不能把结果直接外推到中文影视、所有长篇或当前所有模型。**

# 五条边界

| 边界 | 要求 |
|---|---|
| 1. 先取证，再评价 | 要求模型回到具体段落、区分原文与推测，缺材料时标未知。模型编出的台词、场次、创作者访谈不能进入证据 |
| 2. 不同审查角度 | 分别检查事实状态、人物知识、形式约定、替代解释、修改影响。多个模型赞同同一句话，不等于独立观众证据 |
| 3. 人保留决定 | 模型可提出遗漏候选和反事实，不自动把全部反馈应用到作品。建议越具体越要检查它是否建立在真实问题上 |
| 4. 内心独白只是解释候选 | 生成的动机可能帮助想象，也可能让缺乏依据的场景看起来"被解释好了"。仍要回原作品检查；不用模型模拟替代实际角色依据与受众反应 |
| 5. 反馈进入版本状态 | 已修改的问题，旧意见标为过期或重新验证。不因自动审稿清单不断增长，把作品改到只剩最不冒险的表达 |

# 关系
- 上位主题：[本篇枢纽](/topics/11-close-reading-diagnosis.md)
- 与 [测试反馈怎样进入分析](/methods/test-feedback-into-analysis.md) 并列，共同规定外部反馈的证据地位。
- 上位原则见第十二篇 [人与 AI 协作的保留条件](/principles/human-ai-collaboration-conditions.md) 与 [Agent 和人的角色分工](/frameworks/agent-human-role-division.md)；研究本身的可证与不可证见 [两项 AI 研究提供什么](/principles/what-two-ai-studies-show.md)。
- 旧意见随版本过期，对应 [最小协作架构](/frameworks/minimal-collaboration-architecture.md) 中"旧版本可保存，不再自动生效"。
- 研究镜像：[Rashkin 等 2025](/references/rashkin-help-me-write-a-story-2025.md)。

# Citations
[1] [11 作品分析诊断与证据化评价 §十](../../../11_作品分析诊断与证据化评价.md)
[2] [Hannah Rashkin 等：Help Me Write a Story（2025）](/references/rashkin-help-me-write-a-story-2025.md)
