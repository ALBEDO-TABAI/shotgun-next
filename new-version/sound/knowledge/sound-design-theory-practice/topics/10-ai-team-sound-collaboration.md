---
type: Topic Guide
title: "10 AI 影视团队：声音职责、协作合同与可验证交付"
description: "把前九篇转成可分工、可消费、可返修的工作体系：按职责与真实能力分工，共享权威记录，分离意图/素材/批准，显式状态，依赖驱动的版本更新，绑定文件的验收。"
tags: [topic-10, AI协作, 团队, 交付, 主题枢纽]
timestamp: 2026-09-18T00:00:00Z
source: "new-version/sound/声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md#全篇（原体系第十点）"
---

# 本篇核心问题
放进 AI 影视团队后，声音工作应**交付什么**？关键不是虚构一支职位齐全的 agent 团队，而是明确每个声音决策**由谁提出、依据什么、由谁批准**，以及产物怎样进入下一环节。

> 证据身份：角色划分、状态模型、字段和验收流程均为本包**综合方案**；不表示已安装或运行任何 agent、生成服务、混音系统或发布工具。能力与权限须在具体环境中验证。

# 核心知识段
AI 声音团队以必须完成的职责和真实工具能力划分工作；共享获批目标、画面时间线、声音规则、cue 记录、素材事实和决策依据；生成请求只表达意图，实际素材另行读取、试听或测量；艺术、技术、权利与发布授权是不同条件；每个字段有消费者，每项产出能进入下一环节；变化使受影响的旧结论重新接受检查；缺输入、待审核、失败与已完成保持不同状态；模型自评不代替听觉证据，创意批准不代替外部操作授权。

# 原则 · Principles
* [保留专业职责，而非职位名称与 agent 数量](/principles/responsibilities-not-agent-count.md) - 先定必须负责的判断与所需证据（§1）
* [字段必须被消费](/principles/fields-must-be-consumed.md) - 谁读、何时读、影响何动作、缺值怎么办（§8）
* [知识来源、项目数据与操作指令保持边界](/principles/knowledge-data-instruction-boundary.md) - 资料不带来操作权限；声称要保留不确定性（§14）
* [权利对象与批准分离](/principles/rights-objects-separate-from-approval.md) - 作品 vs 录音；方向批准 ≠ 外部授权（§15）
* [交付结论绑定实际文件](/principles/delivery-claims-bound-to-files.md) - 测量真实导出，校验值不等于质量（§16）
* [最小版本与扩展版本](/principles/minimal-vs-extended-sound-team.md) - 不为团队感制造冗余（§18）
* [按问题调用知识包，避免复述理论](/principles/invoke-knowledge-by-problem-not-recital.md) - 模块路由与 skill 评价标准（§23）

# 框架 · Frameworks
* [固定工作流与 agent 的任务区分](/frameworks/workflow-vs-agent-task-types.md) - 确定性／解释取舍／实际感知／外部后果（§2）
* [声音团队核心职责与直接消费者](/frameworks/sound-team-role-responsibilities.md) - 八种职责与越界边界（§5）
* [六类权威记录](/frameworks/six-authoritative-sound-records.md) - 避免多个"最终版本"（§6）
* [计划—观测—决策三层](/frameworks/plan-observation-decision-layers.md) - 意图、素材、批准分开；借 PROV 思路（§7）
* [声音工作状态链](/frameworks/sound-production-status-chain.md) - 七个状态，艺术／技术／权利分列（§9）
* [分轨、混音组、M&E 与伪分轨](/frameworks/stems-mixgroups-me-distinctions.md) - 四种不同交付对象（§12）

# 方法 · Methods
* [声音制作五阶段流程](/methods/sound-production-five-stage-pipeline.md) - 以关系原型连接上下游（§10）
* [生成式工具的工作合同](/methods/generative-tool-task-contract.md) - 给任务而非情绪词（§11）
* [版本变化按依赖更新](/methods/version-change-dependency-update.md) - 五步变更顺序（§13）
* [自动返修的停止与回退条件](/methods/auto-revision-stop-and-rollback.md) - 按失败类别行动（§22）

# 模板 · Templates
* [声音任务能力矩阵](/templates/sound-task-capability-matrix.md) - 七类能力的验证项（§3）
* [可传递的声音 brief](/templates/transferable-sound-brief.md) - 六字段 brief（§4）
* [cue 计划记录](/templates/cue-plan-record.md) - 只记录计划的 JSON 示例（§7）
* [一次交接的最小信息包](/templates/minimum-handoff-package.md) - 六项交接结构（§20）
* [交付验收记录](/templates/delivery-acceptance-record.md) - 结论绑定文件（§16）

# 检查清单 · Checklists
* [AI 声音系统故障测试夹具](/checklists/ai-sound-failure-fixtures.md) - 八种失败情形的预期与禁止（§17）

# 案例 · Case Studies
* [音乐素材替换的完整传播](/cases/music-asset-replacement-propagation.md) - 依赖包括被批准的声音关系（§21）

# Skill 接口
* [Skill 接口：AI 声音团队协作与交付](/skills/skill-ai-team-sound-collaboration.md) - 开始前／执行时／完成时（§19）

# 跨模块关系
- 本篇是全体系的**落地层**：调用 [02 功能](/topics/02-music-sound-functions.md)、[03 适配](/topics/03-music-fit-judgment.md)、[04 描述](/topics/04-sound-description-language.md)、[05 时间线](/topics/05-sound-timeline.md)、[06 非常规声音](/topics/06-unconventional-sound.md) 做创作判断，以 [07 洗发水广告案例](/topics/07-shampoo-ad-case.md) 的 C04 为示例，借 [08 分析](/topics/08-work-sound-analysis.md) 的证据分层与 [09 评价验收](/topics/09-sound-evaluation-acceptance.md) 的验收方法。
- 整体听觉世界规则来自 [01 整个听觉世界](/topics/01-auditory-world.md)；实际制作层见 [声音创作与制作实践](/topics/p-sound-creation-production.md)。
- 全包证据约定：[00 研究方法与证据边界](/topics/00-research-method-evidence.md)。

# 本篇文献
[EDIT](/references/edit.md) · [THOM](/references/thom.md) · [AGENT](/references/agent.md) · [PROV](/references/prov.md) · [NIST](/references/nist.md) · [COPY](/references/copy.md) · [BS.1770](/references/itu-bs-1770.md) · [EBU R128](/references/ebu.md) · [WAI](/references/wai.md)

* 案例交付计划（07）：[shampoo-ad 交付计划](/cases/shampoo-ad-delivery-plan.md)；[蓝图不是已验证结果](/principles/blueprint-not-verified-result.md)

# Citations
[1] [10 AI影视团队声音协作 全篇（原体系第十点）](../../../声音设计理论与方法_二至十/10_AI影视团队_声音协作与交付.md)
[2] [EDIT](/references/edit.md)
[3] [THOM](/references/thom.md)
[4] [AGENT](/references/agent.md)
[5] [PROV](/references/prov.md)
[6] [NIST](/references/nist.md)
[7] [COPY](/references/copy.md)
[8] [ITU-R BS.1770](/references/itu-bs-1770.md)
[9] [EBU R 128](/references/ebu.md)
[10] [W3C WAI](/references/wai.md)
