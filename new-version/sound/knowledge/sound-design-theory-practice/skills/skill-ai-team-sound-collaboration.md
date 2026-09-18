---
type: Skill Interface
title: "Skill 接口：AI 声音团队协作与交付"
description: "把已知作品任务转化为可制作、可验证、可交接的声音工作：开始前读权威记录并确认能力，执行时明确阶段与消费者并分离意图/素材/结果，完成时对真实产物验证并输出状态、证据、剩余问题和一个下一动作。"
tags: [topic-10, AI协作, skill, 团队流程]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md#19. 可直接执行的团队 skill"
---

# 目标
把已知作品任务转化为**可制作、可验证、可交接**的声音工作。

# 触发
- 需要在多人／多 agent 间派发、交接、返修或交付声音工作；
- 出现版本变化、素材替换、生成任务或交付验收。

# 最小输入
实际 brief、画面时间线、声音世界规则、当前 cue 状态、可用工具与权限清单（见 [六类权威记录](/frameworks/six-authoritative-sound-records.md)、[声音任务能力矩阵](/templates/sound-task-capability-matrix.md)）。

# 处理
**开始前**
- 读取实际 brief、画面时间线、声音规则与当前状态。
- 确认可用工具、文件、权限及证据范围。
- 未确认内容标为**未知**，不用默认值冒充事实。

**执行时**
- 明确本轮是方向、原型、制作、整合还是验收（[五阶段流程](/methods/sound-production-five-stage-pipeline.md)）。
- 每项任务写清输入、产出、消费者、依赖和批准范围（[最小交接包](/templates/minimum-handoff-package.md)）。
- 分别记录生成意图、实际素材及艺术／技术／权利结果（[三层](/frameworks/plan-observation-decision-layers.md)、[状态链](/frameworks/sound-production-status-chain.md)）。
- 所有声音位置引用共同时间线，变更时检查依赖（[版本变化](/methods/version-change-dependency-update.md)）。
- 外部付费、上传、发布和敏感声音使用按明确授权执行（[权利与批准](/principles/rights-objects-separate-from-approval.md)）。

**完成时**
- 对真实产物做相应验证，不凭请求或自评判定通过（[交付绑定文件](/principles/delivery-claims-bound-to-files.md)）。
- 输出当前状态、证据、剩余问题及**一个明确下一动作**。
- 不把缺输入、失败、待审核或旧版本通过写成最终完成。

# 输出
状态 · 证据 · 剩余问题 · 下一动作。

# 质量门禁
- 下一动作**由当前真实状态推导**：旁白未确认 → 确认旁白（而非生成十个新配乐）；技术验收失败 → 修复对应缺陷（而非重审全部创意方向）。
- 通过 [AI 声音系统故障测试夹具](/checklists/ai-sound-failure-fixtures.md) 八种情形。
- 返修有停止与回退条件（[自动返修](/methods/auto-revision-stop-and-rollback.md)）。

# 核心知识段（精炼）
AI 声音团队按必须完成的职责和真实工具能力分工，而非按职位数量建 agent。各环节共享获批目标、画面时间线、声音规则、cue 记录、素材事实与决策依据；派生摘要须可追溯。生成请求只表达意图，实际素材须另行读取、试听或测量；艺术、技术、权利与发布授权是不同条件。每个字段有消费者、每项产出能进入下一环节；剪辑与声音变化使受影响的旧结论重新接受检查。缺输入、待审核、失败与已完成保持不同状态。模型自评不代替实际听觉证据，创意批准不代替外部操作授权。

# 关系
- 上位主题：[10 AI 影视团队声音协作与交付](/topics/10-ai-team-sound-collaboration.md)
- 调用其他模块的方式：[按问题调用知识包](/principles/invoke-knowledge-by-problem-not-recital.md)

# Citations
[1] [10 AI影视团队声音协作 §19 19. 可直接执行的团队 skill](../../../声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md)
