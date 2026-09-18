---
type: Skill Interface
title: "Skill 接口：创意机制生成（03）"
description: "输入任务、产品事实与体验意图，输出可比较的创意路线及可继续写作的片段；给出步骤、退出条件与不应做的事。知识资料，不是已安装或跑通的 agent。"
tags: [topic-03, skill接口, 退出条件, agent]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/script/非人物初步剧本_六专题深化版/03_创意生成与可见过程构造.md#23. 路线比较、模板与退出条件"
---
# 何时调用

需求“只有形容词、想不出内容”，或已有任务定义但缺少具体事件与过程时。需求本身模糊时先用 [任务路由与路线生成（01）](/skills/task-routing-and-route-generation.md)。

# 输入

- 任务（主任务／次任务／本版不做）；
- 产品事实及出处；
- 体验意图（体验词）。

# 步骤

1. 选起笔入口：[五个起笔入口](/methods/five-starting-entries.md)；从形容词出发则做 [体验词转译](/methods/experience-word-translation.md)，每个词至少两种解释并写出相反解读；
2. 按 [意图—关系—可见过程](/frameworks/intent-relation-process-translation.md) 的五步：定义关系 → 选承载对象 → 设计作用或规则 → 安排披露 → 检查相反解读；
3. 按 [机制选择矩阵](/frameworks/mechanism-selection-matrix.md) 选主机制与至多必要的辅助机制，读对应机制卡的“怎么生成”；
4. 用 [六个创意操作](/methods/six-creative-operations.md) 生成机制不同的备选，并过“三问”；
5. 对各路线施加同一限制，看清各自依赖什么（示范：[“一页”灯三次发散](/examples/yiye-lamp-three-divergences.md)）；
6. 填 [路线比较卡](/templates/route-comparison-card.md)，写出选择理由与保留的备选。

# 输出

可比较的创意路线（每条含对象、变化、关系、结束状态、产品联系、核心设计条件、相反解读），以及至少一段可继续写作的片段胚。

# 退出条件

- 至少一条路线已经能写出对象、变化、关系与结束状态；
- 候选之间不是同义改写；
- 产品联系明确；
- 核心设计条件可提出；
- 尚无证据的感受仍标为**意图**。

满足后进入节拍与初稿，**而不是继续无限搜集漂亮参考**。

# 不应自动做什么

- 不把素材词（水、齿轮、漂浮、发光线）当成已完成的创意；
- 不把候选关系表当心理学映射，不宣称固定对应；
- 不为让画面成立而发明产品不存在的结构或功能；
- 不随机穷举组合后直接交付；
- 不照搬参考作品的整套外观，见 [借操作，不借整套外观](/principles/borrow-operations-not-appearance.md)；
- 不直接降成生成提示词。

# 适用边界

本接口整理自知识资料，来源明确声明没有执行实际 agent 评测、视频生成或受众验证，见 [证据分层与使用边界](/principles/evidence-and-use-boundaries.md)。

> 待确认：来源 §23 只给出退出条件与模板；上面的“何时调用”“步骤”“不应自动做什么”由本知识包依据第 03 篇各节与 README 的“给 agent 按问题调用”归纳，转成正式 skill 时需人确认。

# 关系

- 上位主题：[03 创意生成与可见过程构造](/topics/03-idea-generation-and-visible-process.md)
- 上游：[任务路由与路线生成（01）](/skills/task-routing-and-route-generation.md)；下游：[状态／信息／时间编排（02）](/skills/state-info-time-orchestration.md)、[初稿写作与设计交接（05）](/skills/script-writing-and-design-handoff.md)；需要案例支撑时调用 [案例研究与迁移（04）](/skills/case-research-and-transfer.md)；机制本身不成立时，第 02 篇的退出条件要求返回本接口。
- 统一的执行契约见 [skill 执行契约](/skills/skill-execution-contract.md)。

# Citations

[1] [03 创意生成与可见过程构造 §23](../../../非人物初步剧本_六专题深化版/03_创意生成与可见过程构造.md)
