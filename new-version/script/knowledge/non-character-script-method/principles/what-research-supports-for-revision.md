---
type: Principle
title: "调研为回修提供了什么，而不是保证了什么"
description: "并行原型、迭代框架、配置管理与 AI 创意实验只为回修提供工作入口；本篇把它们转成三个工作习惯，而不把它们当作效果保证。"
tags: [topic-06, 证据边界, 并行原型, 配置管理, AI 同质化]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md#2. 调研提供了什么，而不是保证了什么"
---
# 要点

| 来源 | 可以据此说什么 | 不能据此说什么 |
|---|---|---|
| Dow 等人的并行原型实验 [2] | 为「在相近投入下比较不同方案」提供实践相关证据 | 不能保证任意三条 AI 路线都能改善创意 |
| Design Council 的过程框架 [3] | 方法强调迭代与检验，不要求一次线性锁死 | 不证明本包的 agent 分工或项目耗时 |
| NASA 配置管理 [4] | 为基线、提案与已落实变更的区分提供工程入口 | 本包采用的是轻量化对应，不是完整机构制度 |
| Doshi 与 Hauser 的短故事在线实验 [5] | 同时观察到个体作品评价改善与组内作品相似性增加 | 是特定模型、样本与任务的结果，不是关于当前视频 agent 的普遍定律 |

Doshi 与 Hauser 的结果给出的提示是：评价单条方案「不错」之外，还可检查候选之间是否真的有机制差异。

**本篇据此形成的三个工作习惯（本包综合）：**

1. 把评估意见变成可验证的改动假设。
2. 在有限范围内保留不同机制。
3. 确保每项被采纳的内容变化真正进入下游使用的当前版本。

# 适用边界

- 改稿、测试方案、评估题库与 agent 协议均为原创综合；本篇没有实际投放、受众实验或 agent 运行成绩。
- 不要由此推出：所有 AI 创作必然同质化、多 agent 同时调用等于并行原型实验、或某个流程已被验证为最优。

# 关系
- 上位主题：[06 创意优化、验证与多 Agent 回修](/topics/06-optimization-validation-and-multi-agent-revision.md)
- 全包的证据分层见 [证据分层与使用边界](/principles/evidence-and-use-boundaries.md)。
- 习惯一落到 [从反馈到改稿](/methods/feedback-to-revision.md) 与 [一轮测试的记录格式](/templates/test-round-record.md)；习惯二落到 [十二种提升操作](/methods/twelve-uplift-operations.md) 的「保留替代方案」和 [V2 改动说明与两条提升分支](/examples/yiye-lamp-v2-changes-and-branches.md)；习惯三落到 [变更消费与更新回执](/methods/change-consumption-and-update-receipt.md)。
- 第 01 篇同样用并行原型支持 [机制路线的发散与选择](/methods/mechanism-route-divergence-and-selection.md)，且同样不规定通用最佳路线数量。

# Citations

[1] [06 创意优化、验证与多 Agent 回修 §2](../../../非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md)
[2] [S09｜Dow 等：Parallel prototyping](/references/s09-dow-parallel-prototyping.md)
[3] [S01｜Design Council：The Double Diamond](/references/s01-design-council-double-diamond.md)
[4] [S11｜NASA：6.5 Configuration Management](/references/s11-nasa-configuration-management.md)
[5] [S13｜Doshi & Hauser：Generative AI 与创意多样性](/references/s13-doshi-hauser-generative-ai-creativity.md)
