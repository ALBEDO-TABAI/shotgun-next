---
type: Method
title: "变更如何真正被消费：从提案到更新回执"
description: "一项被采纳的内容变更要经过：指出原版本与受影响位置、编剧与导演决定、生成新版本、更新时间与需求用途、下游确认转向新版本、旧任务停止或标记失效；附最小提案格式。"
tags: [topic-06, 变更管理, 更新回执, 版本, 交接]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md#18. 变更如何真正被消费：从提案到更新回执"
---
# 要点

## 流程（以美术提出「将 V1 的 B04/B05 合并，让纸面局部自然回到整体」为例）

1. 指出原版本和受影响位置。
2. 编剧与导演选择是否采用。
3. 若采用，生成 V2 对应内容。
4. 更新相关时间与 D09 的使用位置。
5. 镜头端确认转向消费 V2。
6. 旧 B05 的单独制作任务停止或标记失效。

## 两种常见失败

- 只把 V2 放进文件夹，却继续让镜头端读取 V1。
- 只改最终状态，让旧需求与新下一行动互相冲突。

**回执应说明**：读了哪个版本、哪些引用已更新、仍有哪些任务受影响。

# Schema

最小提案格式：

```text
基于版本／受影响内容 ID：
当前问题与依据：
提议的新表达或实现：
保持不变的内容：
改变的关系、事实或任务：
受影响的需求／时序／版本：
处理结论及新版本：
消费者确认采用的版本：
仍需做的下一行动：
```

这是交接约定，不是要求建一个巨型数据库。五行说明能解决时，不再加十个无人使用字段。

# 适用边界

- 借用的是 NASA 配置管理中「现行基线、变更提案、已实施变更」的区分（来源与限度见 [调研为回修提供了什么](/principles/what-research-supports-for-revision.md)），只取最小思想；不要求短片团队建立配置委员会，字段必须有实际消费者。
- 「消费者确认采用的版本」只能由真实消费者填写；本包的示范不代填「已确认」。

# 关系
- 上位主题：[06 创意优化、验证与多 Agent 回修](/topics/06-optimization-validation-and-multi-agent-revision.md)
- 完整落实示范见 [V1→V2 消费表](/examples/yiye-lamp-v1-to-v2-consumption-table.md)。
- 何种改动需要走本流程，见 [三类变更](/frameworks/three-change-classes.md)；各角色职责见 [多 agent 回修：一个现行内容源](/frameworks/multi-agent-revision-single-content-source.md)。
- 与第 05 篇的需求双向追溯是一对：[八步设计需求提取](/methods/eight-step-design-requirement-extraction.md) 建立「节拍↔需求」对应，本方法保证改稿后这份对应被同步更新；受影响检查是否需复核见 [内容 ID、版本与检查结果不要互相冒充](/principles/content-id-version-check-separation.md)。
- 对应评估情境「美术合并段落」「脚本已改但旧 QC 仍通过」，见 [十四项待运行评估情境](/checklists/agent-evaluation-scenarios.md)。

# Citations

[1] [06 创意优化、验证与多 Agent 回修 §18](../../../非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md)
