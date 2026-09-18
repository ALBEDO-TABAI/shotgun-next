---
type: Skill Interface
title: "把本知识转成 skill 时的执行契约"
description: "非人物初步剧本能力转成 skill 的契约：触发范围、输入最小集、输出最小集、六篇按问题加载、停止规则与明确不做的事。"
tags: [topic-06, skill, 执行契约, agent, 停止规则]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md#22. 把本知识转成 skill 时的执行契约"
---
# 要点

| 契约项 | 内容 |
|---|---|
| **触发范围** | 产品 TVC、非人物品牌片、材料体验、抽象系统、系列陈列、形式循环，以及剧情片中的非人物段落。角色存在不自动排除使用 |
| **输入最小集** | 当前需求、已有稿件或参考、产品事实与授权内容、交付条件、用户当前选择。已有稿件任务先读取并定位，不默认从头发明 |
| **输出最小集** | 本轮任务判断、当前表达命题、初稿／修订稿、设计需求、变更说明与下一行动。用户只要局部润色时，不强行输出完整理论报告 |
| **内部工作** | 六篇按问题加载（见下表）；不要每次把所有机制和来源全部输出给用户 |
| **停止规则** | 当前请求已完成、关键未知已标、下一行动清楚，即可交付；不为追求「完美」无限追加路线。真正阻塞的事实问题只暂停依赖它的任务，其他工作可继续 |
| **明确不做** | 未授权生成或消费；虚构产品功效；把内部创作假设当论文结论；让下游以实现便利更改内容；把用户未确认的候选标为最终 |

## 按问题加载

| 卡在哪里 | 加载 |
|---|---|
| 路线 | [01 能力定位与连续创作路径](/topics/01-capability-and-creative-path.md)、[03 创意生成与可见过程构造](/topics/03-idea-generation-and-visible-process.md) |
| 时间 | [02 对象、信息与时间体验编排](/topics/02-object-information-time-orchestration.md) |
| 参考迁移 | [04 一手案例研究与方法迁移](/topics/04-primary-case-research-and-transfer.md) |
| 交接 | [05 初步剧本写作与设计需求交接](/topics/05-script-writing-and-design-handoff.md) |
| 优化 | [06 创意优化、验证与多 Agent 回修](/topics/06-optimization-validation-and-multi-agent-revision.md) |

# 适用边界

- 本包是可继续用于 skill 开发的知识资料，**不是已经安装或跑通的 agent**；本契约没有运行记录。
- 契约不规定 agent 数量：并行比较可以由同一编剧在不同机制下完成，不需要额外永久 agent。

> 待确认：「未授权生成或消费」中的授权入口、以及谁有权把候选标为最终，需要团队结合真实系统权限确定。

# 关系
- 上位主题：[06 创意优化、验证与多 Agent 回修](/topics/06-optimization-validation-and-multi-agent-revision.md)
- 各篇自己的执行接口：[任务路由与路线生成](/skills/task-routing-and-route-generation.md)、[状态、信息与时间编排](/skills/state-info-time-orchestration.md)、[创意机制生成](/skills/idea-mechanism-generation.md)、[案例研究与迁移](/skills/case-research-and-transfer.md)、[初步剧本写作与设计需求交接](/skills/script-writing-and-design-handoff.md)；本契约是它们的总装。
- 验收用 [十四项待运行评估情境](/checklists/agent-evaluation-scenarios.md)；交付口径见 [最终完成标准](/checklists/final-completion-criteria.md)。
- 输入形态不同（只有一句需求、已有初稿、参考片反推）时的入口见第 01 篇 [三种输入入口](/methods/entry-modes-by-input.md)；工作深度见 [项目规模与工作模式](/frameworks/project-scale-work-modes.md)。
- 角色与变更权限见 [多 agent 回修：一个现行内容源](/frameworks/multi-agent-revision-single-content-source.md) 与 [三类变更](/frameworks/three-change-classes.md)。

# Citations

[1] [06 创意优化、验证与多 Agent 回修 §22](../../../非人物初步剧本_六专题深化版/06_创意优化验证与多Agent回修.md)
