---
type: Principle
title: "内容 ID、版本与检查结果不要互相冒充"
description: "同一个引用必须能确定其内容与版本；自检通过、导演认可、用户确认、资产可用、生成成功各是不同状态，都不能替代传播效果已验证；变更后只复核受影响的检查。"
tags: [topic-06, 版本, 内容 ID, 检查状态, 复核]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md#19. 内容 ID、版本与检查结果不要互相冒充"
---
# 要点

## 1. 引用必须同时确定内容与版本

B02 可以作为 V1 的内容编号；V2 改为 R02 是本篇的教学展示，实际系统也可以保持稳定语义 ID 并更新版本。**选择哪种命名不是核心**，核心是同一个引用能确定其内容与版本，不能只凭「B02」猜当前是哪一稿。

## 2. 五种状态互不替代

| 状态 | 它表示什么 |
|---|---|
| 自检通过 | 检查范围内未发现问题 |
| 导演认可 | 当前表达选择可接受 |
| 用户确认 | 获得相应授权 |
| 资产可用 | 能支撑某项实现 |
| 实际生成成功 | 某个结果被产出 |

它们**都不能替代「传播效果已验证」**。

## 3. 变更后的复核范围

- 未受变更影响的检查，可以保留记录。
- 受影响的项，应重新检查或标记需要复核。
- 不要让旧回执因为文件名没变就继续为新内容背书。
- 也不要因为局部变更把所有已完成工作无差别作废。

# 适用边界

- 这是交接与记录层面的原则，不规定具体的版本号方案或工具。
- 本包自身的检查同样遵守此原则：包内结构检查通过，不等于创意效果或 agent 实测通过，见 [知识包结构检查](/checklists/package-structure-checks.md)。

# 关系
- 上位主题：[06 创意优化、验证与多 Agent 回修](/topics/06-optimization-validation-and-multi-agent-revision.md)
- 第 05 篇的 [设计状态与交付状态](/frameworks/design-status-vs-delivery-status.md) 处理需求侧的同类问题（「已列出」不冒充「已可用」）；本原则处理版本与检查侧。
- 受影响范围怎么确定，见 [变更消费与更新回执](/methods/change-consumption-and-update-receipt.md) 与 [V1→V2 消费表](/examples/yiye-lamp-v1-to-v2-consumption-table.md)。
- 「传播效果已验证」需要什么证据，见 [不同问题需要不同证据](/frameworks/validation-by-question-type.md)；测试记录中的版本行见 [一轮测试的记录格式](/templates/test-round-record.md)。
- 对应评估情境「脚本已改但旧 QC 仍通过」，见 [十四项待运行评估情境](/checklists/agent-evaluation-scenarios.md)。

# Citations

[1] [06 创意优化、验证与多 Agent 回修 §19](../../../非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md)
