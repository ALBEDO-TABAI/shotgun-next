---
type: Skill Interface
title: "任务路由与路线生成：给 agent 的执行指令与停止条件"
description: "第 01 篇面向 agent 的接口：输入一条 brief，输出一页任务定义、可写的表达命题、机制不同的候选路线、选定路线的内容骨架及设计问题；含六条执行指令与四条停止条件。"
tags: [topic-01, skill 接口, 执行指令, 停止条件]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/01_能力定位与连续创作路径.md#13. 给 agent 的执行指令与停止条件"
---
# 要点

## 定位

给 agent 一份「精密、舒展、有产品感、不要人物故事」的需求，它不应只回一篇非叙事理论，也不应马上输出十条生成提示词；它需要完成一次**可交接的创作**：决定本片让人接触什么关系，构思承载该关系的具体过程，写成连续内容，并指出下游需要设计什么。

## 输入

- 用户 brief（可能只有一句需求、已有创意或初稿、或一条参考片）；
- 已有产品事实及其出处、交付条件。

## 输出（本篇完成后的产物）

1. 一页任务定义；
2. 一个可写的表达命题；
3. 机制不同的候选路线；
4. 选定路线的内容骨架；
5. 设计问题。

完整正文与设计清单在第 05 篇展开；本接口不替它重复生成另一份「最终稿」。

## 执行指令

1. 先路由任务，不以「广告」推断结构；
2. 先生成内容机制，不以「高级」直接推断材质；
3. 只追问会改变核心内容的缺口；
4. 让每条候选路线有明确对象、变化与设计条件；
5. 选定后写出牺牲和开放项；
6. 再进入第 02、03、05 篇的具体编排与写作。

## 停止条件

- 能用普通语言说明本片为什么这样展开；
- 能指出产品与表达的联系；
- 重要事实没有被默默补造；
- 下一环节知道具体要设计或验证什么。

停止并不意味着所有细节锁死，而意味着本阶段已经产生足够明确的工作依据。

# 适用边界

- 本包是可继续用于 skill 开发的知识资料，**不是已经安装或跑通的 agent**；上述指令未经真实 agent 评测。
- 未完成的生成测试不能写成「已证实可生成」，也不能因此否认文本阶段已经完成。
- 不按片型再建角色：这是在现有编剧 agent 中补能力的接口。

# 关系

- 上位主题：[01 能力定位与连续创作路径](/topics/01-capability-and-creative-path.md)
- 指令 1 的工具见 [四层 brief 路由](/frameworks/four-layer-brief-routing.md)；指令 3 见 [brief 解包](/methods/brief-unpacking.md)；指令 2、4、5 见 [机制路线的发散与选择](/methods/mechanism-route-divergence-and-selection.md)；整体流程见 [七步连续创作法](/methods/seven-step-creative-path.md)。
- 按输入形态与规模裁剪执行深度，见 [三种输入入口](/methods/entry-modes-by-input.md) 与 [项目规模与三种工作模式](/frameworks/project-scale-work-modes.md)。
- 输出的填写格式见 [任务与路线卡模板](/templates/task-and-route-card.md)。
- 下游接口：[创意机制生成](/skills/idea-mechanism-generation.md)、[状态、信息与时间编排](/skills/state-info-time-orchestration.md)、[初步剧本写作与设计需求交接](/skills/script-writing-and-design-handoff.md)；整包的执行契约见 [Skill 执行契约](/skills/skill-execution-contract.md)，待运行的评估情境见 [agent 评估情境](/checklists/agent-evaluation-scenarios.md)。
- 决定交给谁，见 [主责与协作](/principles/decision-ownership-and-content-source.md)。
- 配套练习见 [香氛三种任务定义练习](/exercises/fragrance-three-task-definitions.md)。

# Citations

[1] [01 能力定位与连续创作路径 §13](../../../非人物初步剧本_六专题深化版/01_能力定位与连续创作路径.md)
