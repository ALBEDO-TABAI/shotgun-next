---
type: Skill Interface
title: "初稿写作与设计交接的 agent 执行规格"
description: "输入已选路线与节拍结构，输出同版本的正文、节拍表与设计需求；八条执行指令与五项退出条件，退出不等同最终制作或受众验证通过。"
tags: [topic-05, agent, 执行规格, 退出条件, 交接]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/05_初步剧本写作与设计需求交接.md#20. 练习与 agent 执行规格（agent 指令、退出条件）"
---
# 要点

## 输入与输出

| | 内容 |
|---|---|
| 输入 | 已选表达命题与主机制（第 01、03 篇）、有职责与暂定时间的节拍结构（第 02 篇）、已确认事实与开放项 |
| 核心产物 | 一版可阅读初稿、一张内容节拍表、一份**有消费位置**的设计需求 |
| 何时调用 | 「美术不知道要做什么」、需要把创意写成可交接内容时 |

## 执行指令

1. 将**正文作为内容源**，节拍与需求作为**同版本工作视图**；
2. 对象去重；
3. 由动词补条件；
4. 关系与可见性单独检查；
5. 不把每个需求等同新资产；
6. 显式保留美术与镜头自由；
7. 未经确认的内容变化返回编剧与导演；
8. 不要直接跳成工具提示词。

## 退出条件

- 关键节拍都有必要设计支持；
- 关键需求有使用位置；
- 同一对象没有冲突定义；
- 可设计自由与内容不变量清楚；
- 事实缺口和下一行动明确。

满足后可进入资产与分镜构思——**不等同最终制作或受众验证已经通过**。

# 适用边界

- 本包是可继续用于 skill 开发的知识资料，不是已经安装或跑通的 agent；该规格未经真实 agent 评测。
- 交付格式是面向当前 AI 团队的建议，不是行业统一剧本标准。

# 关系

- 上位主题：[05 初步剧本写作与设计需求交接](/topics/05-script-writing-and-design-handoff.md)
- 指令 1 ↔ [三种文本层级](/frameworks/three-text-levels.md)；指令 2–3 ↔ [八步提取法](/methods/eight-step-design-requirement-extraction.md)、[可写句法](/methods/writable-sentence-syntax.md)；指令 4 ↔ [常漏的可见性与关系需求](/checklists/often-missed-visibility-and-relation-requirements.md)；指令 5 ↔ [V1 设计需求清单](/examples/yiye-lamp-v1-design-requirements.md) 的「数量不是工作量」；指令 7 ↔ [决策归属与内容源](/principles/decision-ownership-and-content-source.md)。
- 退出前的自检：[消费演练](/methods/consumption-rehearsal.md)；输出格式：[初稿与设计需求模板](/templates/draft-and-requirement-template.md)。
- 上游接口：[任务路由与路线生成](/skills/task-routing-and-route-generation.md)、[创意机制生成](/skills/idea-mechanism-generation.md)、[状态—信息—时间编排](/skills/state-info-time-orchestration.md)；下游与总契约：第 06 篇 [skill 执行契约](/skills/skill-execution-contract.md)、[最终完成标准](/checklists/final-completion-criteria.md)。

# Citations

[1] [05 初步剧本写作与设计需求交接 §20（agent 指令与退出条件；输入输出见篇首与 §1）](../../../非人物初步剧本_六专题深化版/05_初步剧本写作与设计需求交接.md)
